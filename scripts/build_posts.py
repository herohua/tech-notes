#!/usr/bin/env python3
"""Transform notes/*.md into Jekyll posts under build/_posts and build/assets/notes."""

from __future__ import annotations

import os
import re
import shutil
import sys
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
NOTES_DIR = ROOT / "notes"
IMAGES_DIR = ROOT / "images"
BUILD_DIR = ROOT / "build"
POSTS_OUT = BUILD_DIR / "_posts"
ASSETS_OUT = BUILD_DIR / "assets" / "notes"

FRONT_MATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)$", re.DOTALL)
IMAGE_PATH_RE = re.compile(r"(!\[[^\]]*\]\()(?:\.\./)?images/([^)]+)(\))")
NOTE_LINK_RE = re.compile(r"(?<!!)(\[[^\]]+\]\()(?:\.\/)?([A-Za-z0-9_-]+)\.md(#[^)\s]*)?(\))")
SLUG_RE = re.compile(r"[^a-z0-9]+")

SOURCE_REPO = os.environ.get("SOURCE_REPO", "herohua/tech-notes")
SOURCE_SHA = os.environ.get("GITHUB_SHA", "")
SOURCE_REF = SOURCE_SHA or os.environ.get("SOURCE_REF", "main")


def slugify(text: str) -> str:
    return SLUG_RE.sub("-", text.lower()).strip("-")


def parse_note(path: Path) -> tuple[dict, str] | None:
    raw = path.read_text(encoding="utf-8")
    match = FRONT_MATTER_RE.match(raw)
    if not match:
        print(f"  skip (no front matter): {path.name}", file=sys.stderr)
        return None
    fm = yaml.safe_load(match.group(1)) or {}
    body = match.group(2)
    return fm, body


def build() -> list[Path]:
    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)
    POSTS_OUT.mkdir(parents=True)
    ASSETS_OUT.mkdir(parents=True)

    notes: list[tuple[Path, dict, str]] = []
    publishable_stems: set[str] = set()
    for note_path in sorted(NOTES_DIR.glob("*.md")):
        parsed = parse_note(note_path)
        if parsed is None:
            continue
        fm, body = parsed
        notes.append((note_path, fm, body))
        if fm.get("publish"):
            publishable_stems.add(note_path.stem)

    published: list[Path] = []
    used_images: set[str] = set()

    for note_path, fm, body in notes:
        if not fm.get("publish"):
            print(f"  draft: {note_path.name}")
            continue

        title = fm.get("title")
        post_date = fm.get("date")
        if not title or not post_date:
            print(f"  skip (missing title/date): {note_path.name}", file=sys.stderr)
            continue

        if isinstance(post_date, str):
            post_date = date.fromisoformat(post_date)

        slug = slugify(note_path.stem)
        post_name = f"{post_date.isoformat()}-{slug}.md"

        for _, img, _ in IMAGE_PATH_RE.findall(body):
            used_images.add(img)
        body = IMAGE_PATH_RE.sub(r"\1/assets/notes/\2\3", body)

        def rewrite_note_link(match: re.Match) -> str:
            label_open, target_stem, anchor, close = match.groups()
            if target_stem not in publishable_stems:
                print(
                    f"  WARN: {note_path.name} links to unpublished/missing note '{target_stem}.md'",
                    file=sys.stderr,
                )
                return match.group(0)
            return f"{label_open}/{target_stem}{anchor or ''}{close}"

        body = NOTE_LINK_RE.sub(rewrite_note_link, body)

        new_fm = {"layout": "post", "title": str(title), "date": post_date.isoformat()}
        if fm.get("tags"):
            new_fm["tags"] = fm["tags"]
        new_fm["source_url"] = f"https://github.com/{SOURCE_REPO}/blob/{SOURCE_REF}/notes/{note_path.name}"
        if SOURCE_SHA:
            new_fm["source_commit"] = SOURCE_SHA

        out = POSTS_OUT / post_name
        fm_yaml = yaml.safe_dump(new_fm, sort_keys=False, allow_unicode=True).strip()
        out.write_text(f"---\n{fm_yaml}\n---\n\n{body.lstrip()}", encoding="utf-8")
        published.append(out)
        print(f"  published: {note_path.name} -> {post_name}")

    for img in used_images:
        src = IMAGES_DIR / img
        if not src.exists():
            print(f"  WARN: missing image referenced by a note: {img}", file=sys.stderr)
            continue
        dest = ASSETS_OUT / img
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)

    return published


if __name__ == "__main__":
    posts = build()
    print(f"\nBuilt {len(posts)} post(s) into {BUILD_DIR}")
