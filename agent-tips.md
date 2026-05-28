# Agent Tips & Tricks

Personal reference for working with coding agents effectively.

## General

- **Always use worktrees when parallel agents touch the same repo** — baked into `AGENTS.md`. Without it, agents stomp each other's files.
- **Spawn agent teams** to parallelize independent work.
- **Use absolute paths** in prompts — relative paths cause file ambiguity across worktrees.
- **Gate destructive actions explicitly** — *"don't run until I give permission"*, *"don't update the PR yet"*.
- **"Don't fallback"** — tell the agent to surface failures instead of silently swapping to a backup path.

## Skills

- **`superpowers`** plugin is the most useful pack — provides core workflow skills (brainstorming, plan/execute, worktrees, parallel subagents, systematic debugging, TDD, code review, verification).
- Personal skills are hosted at [github.com/herohua/skills](https://github.com/herohua/skills) — refresh with **`/sync-skills`**.
- Pattern: complete a task, then ask the agent to **distill it into a skill** and PR to the skills repo.

## MCP

- **Prefer MCP tools over raw CLI/API** (Playwright MCP for browser automation, ADO MCP over `az` CLI).
- **Pick the right scope and stick with it** — user-scope for general-purpose MCPs you want everywhere (ADO, Playwright); project-scope (`~/.mcp.json` in repo) only for MCPs specific to that project (same idea as project-local skills); local rarely useful. If the same MCP shows up in multiple scopes, Claude Code warns because OAuth tokens are stored per-endpoint — remove the duplicates rather than living with the conflict.
- **MCP commands need `cmd /c` wrapper** around `npx` on Windows.
- **User-scope MCP install works; project-scope `/mcp add` just opens the dialog.** Use:
  ```
  claude mcp add <name> --scope user -- npx -y --registry https://registry.npmjs.org <pkg>
  ```
- **Restart the session** after installing an MCP for it to load.
- `~/.mcp.json` is the shared project MCP config.
- **Playwright MCP disconnects** → fix with `npx playwright install`.

### Useful MCPs

| MCP | Install in Claude Code |
|---|---|
| `azure-devops` | `claude mcp add azure-devops --scope user -- cmd /c npx -y @azure-devops/mcp ceapex` |
| `drawio` | `claude mcp add drawio --scope user -- cmd /c npx -y @next-ai-drawio/mcp-server@latest` |
| `playwright` | `/plugin install playwright@claude-plugins-official` |
| `microsoft-docs` | `/plugin install microsoft-docs@claude-plugins-official` |

