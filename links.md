# Curated tech links

External references I find useful. Maintained alongside my own notes in [notes/](notes/).

Last bulk verified: 2026-05-19 · 152 entries

## Contents

- [AI / LLM / Agents](#ai-llm-agents) — 49
- [Azure](#azure) — 15
- [.NET](#net) — 23
- [Web / API / Protocols](#web-api-protocols) — 13
- [Developer tools](#developer-tools) — 9
- [Architecture](#architecture) — 9
- [Security](#security) — 6
- [Auth / OAuth](#auth-oauth) — 4
- [PowerShell](#powershell) — 6
- [Frontend / JS](#frontend-js) — 3
- [Docs & Markdown](#docs-markdown) — 7
- [Personal blogs](#personal-blogs) — 3
- [Misc](#misc) — 5

---

## AI / LLM / Agents

### Foundations & design patterns

- [Introduction to Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/agent-framework-overview) — learn.microsoft.com
- [Overview - Agent Skills](https://agentskills.io/home) — agentskills.io
- [《Agentic Design Patterns》分享](https://www.cnblogs.com/wintersun/p/19072835) — cnblogs.com — Chinese-language summary of the Agentic Design Patterns book.
- [Agentic AI - DeepLearning.AI - Agentic Design Patterns](https://learn.deeplearning.ai/courses/agentic-ai/lesson/rm9bg7/agentic-design-patterns) — learn.deeplearning.ai — Andrew Ng's Agentic AI course — design patterns lesson.
- [Equipping agents for the real world with Agent Skills \ Anthropic](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) — anthropic.com — The Agent Skills primitive explained by the team that shipped it.
- [Demystifying evals for AI agents \ Anthropic](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) — anthropic.com — How to actually measure agent quality.
- [Building Effective AI Agents \ Anthropic](https://www.anthropic.com/engineering/building-effective-agents) — anthropic.com — Anthropic's canonical framing of agent loops; start here.

### Prompt & context engineering

- [Prompt Engineering | Kaggle](https://www.kaggle.com/whitepaper-prompt-engineering) — kaggle.com — Google's prompt engineering whitepaper (Kaggle mirror).
- [Google 官方提示工程 (Prompt Engineering)白皮书 | 宝玉的分享](https://baoyu.io/blog/google-prompt-engineering-whitepaper#google_vignette) — baoyu.io — Chinese translation of Google's prompt engineering whitepaper.
- [GPT-4.1 Prompting Guide | OpenAI Cookbook](https://cookbook.openai.com/examples/gpt4-1_prompting_guide) — cookbook.openai.com — Official OpenAI prompting guide for GPT-4.1.
- [Context Engineering for AI Agents: Lessons from Building Manus](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus) — manus.im — Manus team's lessons on context engineering.

### Agent frameworks & MCP

- [What we saw in the past three months. And what we see in the future.](https://manus.im/blog/what-we-saw-in-the-past-three-months-and-what-we-see-in-the-future) — manus.im
- [Code Mode: the better way to use MCP](https://blog.cloudflare.com/code-mode/) — blog.cloudflare.com — Cloudflare's case for code-mode over plain MCP tool calls.
- [10 Microsoft MCP Servers to Accelerate Your Development Workflow](https://devblogs.microsoft.com/blog/10-microsoft-mcp-servers-to-accelerate-your-development-workflow) — devblogs.microsoft.com

### Coding agents & tools

- [GitHub Copilot: The agent awakens](https://github.blog/news-insights/product-news/github-copilot-the-agent-awakens/) — github.blog
- [GitHub Copilot Testing for .NET Brings AI-powered Unit Tests to Visual Studio 2026](https://devblogs.microsoft.com/dotnet/github-copilot-testing-for-dotnet-available-in-visual-studio/) — devblogs.microsoft.com
- [Power agentic workflows in your terminal with GitHub Copilot CLI](https://github.blog/ai-and-ml/github-copilot/power-agentic-workflows-in-your-terminal-with-github-copilot-cli/) — github.blog
- [Unrolling the Codex agent loop | OpenAI](https://openai.com/index/unrolling-the-codex-agent-loop/) — openai.com
- [GitHub Copilot Archives](https://github.blog/tag/github-copilot/) — github.blog
- [Claude Code: An analysis](https://southbridge-research.notion.site/claude-code-an-agentic-cleanroom-analysis) — southbridge-research.notion.site — Deep reverse-engineering of Claude Code's architecture.
- [AI coding tools are shifting to a surprising place: The terminal | TechCrunch](https://techcrunch.com/2025/07/15/ai-coding-tools-are-shifting-to-a-surprising-place-the-terminal/) — techcrunch.com

### Platforms & APIs

- [JSON-LD Articles and Presentations](https://json-ld.org/learn.html) — json-ld.org
- [RDFa](https://rdfa.info/) — rdfa.info
- [Direct preference optimization - Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/fine-tuning-direct-preference-optimization?context=%2Fazure%2Fai-foundry%2Fcontext%2Fcontext) — learn.microsoft.com
- [AI - Azure AI services Blog](https://techcommunity.microsoft.com/category/ai/blog/azure-ai-services-blog) — techcommunity.microsoft.com
- [OpenRouter](https://openrouter.ai/) — openrouter.ai — Unified API across LLM providers.
- [How to use predicted outputs with Azure OpenAI in Azure AI Foundry Models - Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/predicted-outputs?tabs=python-secure) — learn.microsoft.com
- [Reinforcement fine-tuning - Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reinforcement-fine-tuning?toc=%2Fazure%2Fai-foundry%2Ftoc.json&bc=%2Fazure%2Fai-foundry%2Fbreadcrumb%2Ftoc.json&view=foundry-classic&preserve-view=true) — learn.microsoft.com

### Learning & analysis

- [How fast is AI improving? - AI Digest](https://theaidigest.org/progress-and-dangers) — theaidigest.org
- [The 70% problem: Hard truths about AI-assisted coding](https://addyo.substack.com/p/the-70-problem-hard-truths-about) — addyo.substack.com — Why AI gets you 70% there and humans pay for the last 30%.
- [The Illustrated DeepSeek-R1 (Jay Alammar)](https://newsletter.languagemodels.co/p/the-illustrated-deepseek-r1) — newsletter.languagemodels.co — Jay Alammar's illustrated DeepSeek-R1 walkthrough.
- [Writing Code Was Never The Bottleneck - ordep.dev](https://ordep.dev/posts/writing-code-was-never-the-bottleneck) — ordep.dev — Counter-take on AI productivity claims.
- [Deep Dive into LLMs like ChatGPT - YouTube](https://www.youtube.com/watch?v=7xTGNNLPyMI) — youtube.com
- [DoubleAgents: Fine-tuning LLMs for Covert Malicious Tool Calls | by Justin Albrethsen | Aug, 2025 | AI Mind](https://pub.aimind.so/doubleagents-fine-tuning-llms-for-covert-malicious-tool-calls-b8ff00bf513e) — pub.aimind.so
- [Agentic AI - DeepLearning.AI](https://learn.deeplearning.ai/courses/agentic-ai/lesson/pu5xbv/welcome) — learn.deeplearning.ai — Andrew Ng's Agentic AI course — intro.
- [Talking Postgres with Claire Giordano | Transcript: AI for data engineers with Simon Willison](https://talkingpostgres.com/episodes/ai-for-data-engineers-with-simon-willison/transcript) — talkingpostgres.com
- [No, AI is not Making Engineers 10x as Productive](https://colton.dev/blog/curing-your-ai-10x-engineer-imposter-syndrome/) — colton.dev — Skeptical look at 10x AI productivity claims.
- [Agentic AI - DeepLearning.AI](https://learn.deeplearning.ai/courses/agentic-ai/lesson/pu5xbv/welcome!) — learn.deeplearning.ai
- [OpenAI AGI Roadmap: A Blueprint for the Future - DEV Community](https://dev.to/hyscaler/openai-agi-roadmap-a-blueprint-for-the-future-2a2p) — dev.to
- [Coding as the epicenter of AI progress and the path to general agents](https://www.interconnects.ai/p/coding-as-the-epicenter-of-ai-progress) — interconnects.ai — Nathan Lambert on why coding is the frontier.

### Chinese-language

- [AI Agents - WayToAGI](https://www.waytoagi.com/agents) — waytoagi.com — Chinese-language AI agent directory.
- [魔搭社区](https://www.modelscope.cn/home) — modelscope.cn — Alibaba's model hub (Hugging Face equivalent).

### Misc AI

- [Optimizing and Evaluating Enterprise Retrieval-Augmented Generation (RAG): A Content Design Perspective](https://arxiv.org/pdf/2410.12812) — arxiv.org
- [The latest on AI & ML](https://github.blog/ai-and-ml/) — github.blog
- [Computer-Using Agent | OpenAI](https://openai.com/index/computer-using-agent/) — openai.com
- [Blog | Claude](https://claude.com/blog) — claude.com
- [VS Code API | Visual Studio Code Extension API](https://code.visualstudio.com/api/references/vscode-api#authentication) — code.visualstudio.com
- [A methodical approach to agent evaluation | Google Cloud Blog](https://cloud.google.com/blog/topics/developers-practitioners/a-methodical-approach-to-agent-evaluation) — cloud.google.com
- [File Editing: AI-Assisted Code Modification](https://southbridge-research.notion.site/File-Editing-AI-Assisted-Code-Modification-2055fec70db18100803ff7287c24c6cc) — southbridge-research.notion.site — How AI-assisted code editing tools work under the hood.

---

## Azure

### Functions & App Service

- [Manage connections in Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/manage-connections?tabs=csharp) — learn.microsoft.com
- [Azure/azure-functions-host: The host/runtime that powers Azure Functions](https://github.com/Azure/azure-functions-host) — github.com — Azure Functions runtime host source.
- [Azure Function Apps: Performance Considerations – Technozure](https://blogs.msdn.microsoft.com/amitagarwal/2018/04/03/azure-function-apps-performance-considerations/) — blogs.msdn.microsoft.com

### Storage & data

- [Introducing Microsoft Azure File Service](http://blogs.msdn.com/b/windowsazurestorage/archive/2014/05/12/introducing-microsoft-azure-file-service.aspx) — blogs.msdn.com
- [Persisting connections to Microsoft Azure Files](http://blogs.msdn.com/b/windowsazurestorage/archive/2014/05/27/persisting-connections-to-microsoft-azure-files.aspx) — blogs.msdn.com

### Observability & perf

- [The Azure Cosmos DB Journey to .NET 6](https://devblogs.microsoft.com/dotnet/the-azure-cosmos-db-journey-to-net-6/) — devblogs.microsoft.com
- [Diagnosing Redis errors on the server side](https://gist.github.com/JonCole/9225f783a40564c9879d) — gist.github.com — Diagnosing Azure Redis errors on the server side.
- [Diagnosing Redis errors caused by issues on the client side](https://gist.github.com/JonCole/db0e90bedeb3fc4823c2) — gist.github.com — Diagnosing Azure Redis errors on the client side.
- [Troubleshooting intermittent outbound connection errors in Azure App Service - Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/troubleshoot-intermittent-outbound-connection-errors#avoiding-the-problem) — learn.microsoft.com
- [Azure Log Analytics query language cheat sheet](https://learn.microsoft.com/en-us/azure/log-analytics/log-analytics-log-search-transition) — learn.microsoft.com

### Internals

- [projectkudu/kudu: Kudu is the engine behind git/hg deployments, WebJobs, and various other features in Azure Web Sites. It can also run outside of Azure.](https://github.com/projectkudu/kudu) — github.com — Kudu — the engine behind Azure App Service deployment.
- [Home · projectkudu/kudu Wiki](https://github.com/projectkudu/kudu/wiki) — github.com — Kudu wiki — deployment internals.
- [Antares Architecture](https://www.antares-architecture.com/home.html) — antares-architecture.com — Antares (App Service) architecture overview.

### Misc Azure

- [Autoscaling guidance](https://learn.microsoft.com/en-us/azure/architecture/best-practices/auto-scaling) — learn.microsoft.com
- [Iozone Filesystem Benchmark](http://www.iozone.org/) — iozone.org

---

## .NET

### Async / await

- [Implicit Async Context ("AsyncLocal")](https://blog.stephencleary.com/2013/04/implicit-async-context-asynclocal.html) — blog.stephencleary.com — AsyncLocal deep dive.
- [Fire and Forget on ASP.NET](http://blog.stephencleary.com/2014/06/fire-and-forget-on-asp-net.html) — blog.stephencleary.com — Why fire-and-forget on ASP.NET is dangerous.
- [Returning Early from ASP.NET Requests](http://blog.stephencleary.com/2012/12/returning-early-from-aspnet-requests.html) — blog.stephencleary.com — Patterns for early-return on ASP.NET requests.
- [Async Programming - Introduction to Async/Await on ASP.NET](https://msdn.microsoft.com/en-us/magazine/dn802603.aspx) — msdn.microsoft.com
- [Async/Await - Best Practices in Asynchronous Programming](https://msdn.microsoft.com/en-us/magazine/jj991977.aspx) — msdn.microsoft.com
- [MSDN Magazine: Parallel Computing - It's All About the SynchronizationContext](https://msdn.microsoft.com/magazine/gg598924.aspx) — msdn.microsoft.com
- [Dissecting the ActionBlock: a Short Story About a Nasty Deadlock – Dissecting the code](https://blogs.msdn.microsoft.com/seteplia/2016/12/20/dissecting-the-actionblock-a-short-story-about-a-nasty-deadlock/) — blogs.msdn.microsoft.com

### Runtime / framework

- [Understanding .NET Core, NETStandard, .NET Core applications and ASP.NET Core](https://andrewlock.net/understanding-net-core-netstandard-and-asp-net-core/) — andrewlock.net — Untangles .NET Core, .NET Standard, and ASP.NET Core.
- [HttpClientFactory in ASP.NET Core 2.1 (Part 1) - Steve Gordon - Code with Steve](https://www.stevejgordon.co.uk/introduction-to-httpclientfactory-aspnetcore) — stevejgordon.co.uk — HttpClientFactory primer.
- [.NET Standard 2.0 - Making Sense of .NET Again - Rick Strahl's Web Log](https://weblog.west-wind.com/posts/2016/Nov/23/NET-Standard-20-Making-Sense-of-NET-Again) — weblog.west-wind.com — Rick Strahl on .NET Standard 2.0.

### Language & libraries

- [The ‘in’-modifier and the readonly structs in C# – Dissecting the code](https://blogs.msdn.microsoft.com/seteplia/2018/03/07/the-in-modifier-and-the-readonly-structs-in-c/) — blogs.msdn.microsoft.com
- [MSBuild Property Functions | The Visual Studio Blog](https://blogs.msdn.microsoft.com/visualstudio/2010/04/02/msbuild-property-functions/) — blogs.msdn.microsoft.com

### File paths

- [Naming Files, Paths, and Namespaces](https://learn.microsoft.com/en-us/windows/desktop/FileIO/naming-a-file#maximum-path-length-limitation) — learn.microsoft.com
- [.NET 4.6.2 and long paths on Windows 10 – Jeremy Kuhne's Blog](https://blogs.msdn.microsoft.com/jeremykuhne/2016/07/30/net-4-6-2-and-long-paths-on-windows-10/) — blogs.msdn.microsoft.com
- [More on new .NET path handling – Jeremy Kuhne's Blog](https://blogs.msdn.microsoft.com/jeremykuhne/2016/06/21/more-on-new-net-path-handling/) — blogs.msdn.microsoft.com
- [Long paths in .NET – Jeremy Kuhne's Blog](https://blogs.msdn.microsoft.com/jeremykuhne/2016/06/02/long-paths-in-net/) — blogs.msdn.microsoft.com

### Regex

- [Rex - Regular Expression Exploration - Microsoft Research](https://www.microsoft.com/en-us/research/project/rex-regular-expression-exploration/) — microsoft.com
- [Optimizing Regular Expression Performance, Part II: Taking Charge of Backtracking [Ron Petrusha] – BCL Team Blog](https://blogs.msdn.microsoft.com/bclteam/2010/08/03/optimizing-regular-expression-performance-part-ii-taking-charge-of-backtracking-ron-petrusha/) — blogs.msdn.microsoft.com
- [The .NET Regex Tester | Regex Hero](http://regexhero.net/tester/) — regexhero.net

### Tools & references

- [C# Online Compiler | .NET Fiddle](https://dotnetfiddle.net/) — dotnetfiddle.net
- [quozd/awesome-dotnet: A collection of awesome .NET libraries, tools, frameworks and software](https://github.com/quozd/awesome-dotnet) — github.com — Curated awesome-list of .NET libraries.

### Misc .NET

- [What is cache penetration, cache breakdown and cache avalanche? | Pixelstech.net](https://www.pixelstech.net/article/1586522853-What-is-cache-penetration-cache-breakdown-and-cache-avalanche) — pixelstech.net
- [Which Uri Encoding method should i use in C#/.net? (secretGeek.net)](http://www.secretgeek.net/uri_enconding) — secretgeek.net

---

## Web / API / Protocols

### REST

- [有关REST知识的阅读清单](http://www.infoq.com/cn/articles/rest-reading-list) — infoq.com
- [RESTful Web Services](http://www.crummy.com/writing/RESTful-Web-Services/html/) — crummy.com

### JSON Schema

- [JSON Schema | The home of JSON Schema](http://json-schema.org/) — json-schema.org
- [Understanding JSON Schema — Understanding JSON Schema 1.0 documentation](https://spacetelescope.github.io/understanding-json-schema/index.html) — spacetelescope.github.io
- [Understanding JSON Schema — Understanding JSON Schema 1.0 documentation](https://spacetelescope.github.io/understanding-json-schema/#) — spacetelescope.github.io
- [JSON Schema Validator - Newtonsoft](https://www.jsonschemavalidator.net/) — jsonschemavalidator.net

### OpenAPI / Swagger

- [OpenAPI Specification | Swagger](https://swagger.io/specification/#externalDocumentationObject) — swagger.io
- [A Visual Guide to What's New in Swagger 3.0](https://blog.readme.io/an-example-filled-guide-to-swagger-3-2/) — blog.readme.io

### YAML

- [YAML Ain’t Markup Language (YAML™) Version 1.2](http://yaml.org/spec/1.2/spec.html#id2759572) — yaml.org
- [The Yaml Component (Symfony Docs)](http://symfony.com/doc/current/components/yaml.html) — symfony.com

### GraphQL & Graph APIs

- [Introduction to Graph APIs - The Zapier Engineering Blog | Zapier](https://zapier.com/engineering/graph-apis/) — zapier.com

### Misc web

- [The Web Robots Pages](http://www.robotstxt.org/meta.html) — robotstxt.org
- [Introducing: Log Parser Studio](http://blogs.technet.com/b/exchange/archive/2012/03/07/introducing-log-parser-studio.aspx) — blogs.technet.com

---

## Developer tools

### Regex

- [Online regex tester and debugger: JavaScript, Python, PHP, and PCRE](https://regex101.com/) — regex101.com — Best online regex tester (PCRE/JS/Python).
- [RegExr: Learn, Build, & Test RegEx](http://www.regexr.com/) — regexr.com

### Encoders

- [URL Decode and Encode - Online](https://www.urlencoder.org/) — urlencoder.org
- [Base64 Decode and Encode - Online](https://www.base64encode.org/) — base64encode.org

### Debugging

- [How to capture a crash dump during application startup](http://webdebug.net/2014/03/how-to-capture-a-crash-dump-during-application-startup/) — webdebug.net

### Diagramming

- [Excalidraw Whiteboard](https://excalidraw.com/) — excalidraw.com — Sketch-style whiteboard for diagrams.

### Misc

- [📙 Emojipedia — 😃 Home of Emoji Meanings 💁👌🎍😍](https://emojipedia.org/) — emojipedia.org
- [Creating And Publishing A Package](https://docs.nuget.org/create/creating-and-publishing-a-package) — docs.nuget.org
- [IP Location Finder - Geolocation](https://www.iplocation.net/) — iplocation.net

---

## Architecture

- [Deploying Microservices: Spring Cloud vs. Kubernetes - DZone Cloud](https://dzone.com/articles/deploying-microservices-spring-cloud-vs-kubernetes) — dzone.com
- [The Twelve-Factor App](https://12factor.net/) — 12factor.net — The Twelve-Factor App methodology.
- [DZone Microservices](https://dzone.com/microservices-news-tutorials-tools) — dzone.com
- [How does spam protection work on Stack Exchange? - Stack Overflow Blog](https://stackoverflow.blog/2020/06/25/how-does-spam-protection-work-on-stack-exchange/) — stackoverflow.blog
- [Microservices Architecture pattern](http://microservices.io/patterns/microservices.html) — microservices.io — Microservices pattern catalog.
- [How We Made GitHub Fast](https://github.com/blog/530-how-we-made-github-fast) — github.com
- [Summary of the Amazon DynamoDB Service Disruption in the Northern Virginia (US-EAST-1) Region](https://aws.amazon.com/message/101925/) — aws.amazon.com — AWS postmortem: DynamoDB US-EAST-1 outage.
- [Staff archetypes | StaffEng](https://staffeng.com/guides/staff-archetypes) — staffeng.com — The four archetypes of a Staff Engineer.
- [Resource哪里找 · The DSC Book (中文版)](https://yaowenjie.gitbooks.io/the-dsc-book/content/where-to-find-resources.html) — yaowenjie.gitbooks.io

---

## Security

### CI/CD security

- [Let's Hack a Pipeline: Argument Injection](https://devblogs.microsoft.com/devops/pipeline-argument-injection/) — devblogs.microsoft.com — Argument-injection attacks on Azure DevOps pipelines.
- [Let's Hack a Pipeline: Stealing Another Repo](https://devblogs.microsoft.com/devops/pipeline-stealing-another-repo/) — devblogs.microsoft.com — How a malicious pipeline can steal another repo.
- [Let's Hack a Pipeline: Shared Infrastructure](https://devblogs.microsoft.com/devops/pipeline-shared-infrastructure/) — devblogs.microsoft.com — Pipeline attacks via shared infrastructure.

### Secure development

- [Microsoft Security Development Lifecycle Practices](https://www.microsoft.com/en-us/securityengineering/sdl/practices) — microsoft.com — Microsoft SDL practices reference.

### CTF

- [学习资源 - CTF Wiki](https://ctf-wiki.org/introduction/resources/#ctf-oj) — ctf-wiki.org — CTF learning resources index.

### Misc security

- [ID Token and Access Token: What Is the Difference?](https://auth0.com/blog/id-token-access-token-what-is-the-difference/) — auth0.com — Clear explainer of ID token vs access token.

---

## Auth / OAuth

- [理解OAuth 2.0 - 阮一峰的网络日志](http://www.ruanyifeng.com/blog/2014/05/oauth_2_0.html) — ruanyifeng.com — 阮一峰 on OAuth 2.0 (CN).
- [How to Redirect a Web Page | CSS-Tricks](https://css-tricks.com/redirect-web-page/#html-redirects) — css-tricks.com
- [Android学习笔记——OAuth完全手册_国内篇 - lingyun1120 - 博客园](http://www.cnblogs.com/lingyun1120/archive/2012/07/11/2585767.html) — cnblogs.com
- [OAuth 2 Simplified • Aaron Parecki](https://aaronparecki.com/oauth-2-simplified/) — aaronparecki.com — OAuth 2 in plain language.

---

## PowerShell

- [Building PowerShell Functions: Best Practices – Rambling Cookie Monster](http://ramblingcookiemonster.github.io/Building-PowerShell-Functions-Best-Practices/) — ramblingcookiemonster.github.io
- [Using enums in Powershell | I've got the byte on my side](http://latkin.org/blog/2012/07/08/using-enums-in-powershell/) — latkin.org
- [PowerShell 在线教程 - PowerShell 中文博客](http://www.pstips.net/powershell-online-tutorials/) — pstips.net
- [My 12 PowerShell Best Practices | PowerShell with a Purpose Blog](http://windowsitpro.com/blog/my-12-powershell-best-practices) — windowsitpro.com
- [An Introduction to Error Handling in PowerShell | Keith Babinec's Development Blog](https://blogs.msdn.microsoft.com/kebab/2013/06/09/an-introduction-to-error-handling-in-powershell/) — blogs.msdn.microsoft.com
- [The OldWood Thing: PowerShell, Throwing Exceptions & Exit Codes](http://chrisoldwood.blogspot.sg/2011/05/powershell-throwing-exceptions-exit.html) — chrisoldwood.blogspot.sg

---

## Frontend / JS

- [React 入门实例教程 - 阮一峰的网络日志](http://www.ruanyifeng.com/blog/2015/03/react.html) — ruanyifeng.com
- [跨域资源共享 CORS 详解 - 阮一峰的网络日志](http://www.ruanyifeng.com/blog/2016/04/cors.html) — ruanyifeng.com
- [Node.js 中文网](http://nodejs.cn/) — nodejs.cn

---

## Docs & Markdown

- [Markdown Cheatsheet · adam-p/markdown-here Wiki](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#blockquotes) — github.com — Markdown cheatsheet.
- [babelmark3 | Compare Markdown Implementations](https://babelmark.github.io/) — babelmark.github.io — Compare Markdown implementations side-by-side.
- [Docsy](https://www.docsy.dev/) — docsy.dev — Hugo theme for technical docs.
- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0-beta.2/#summary) — conventionalcommits.org — Conventional Commits spec.
- [Documentation in a DevOps World – Premier Developer](https://blogs.msdn.microsoft.com/premier_developer/2017/04/14/documentation-in-a-devops-world/) — blogs.msdn.microsoft.com
- [Markdown 语法说明(简体中文版)](http://wowubuntu.com/markdown/) — wowubuntu.com
- [Mintlify - The Intelligent Documentation Platform](https://www.mintlify.com/) — mintlify.com — Hosted docs platform.

---

## Personal blogs

- [阮一峰的网络日志](http://www.ruanyifeng.com/blog/) — ruanyifeng.com — 阮一峰's blog — clear technical explainers.
- [Optimize git commit history](https://yufeih.github.io/2020/08/04/optimize-git-commit-history.html) — yufeih.github.io — Practical guide to rewriting git history cleanly.
- [酷壳 – CoolShell.cn](http://coolshell.cn/) — coolshell.cn — 陈皓's CoolShell — programming culture & deep-dives.

---

## Misc

- [Clone a linked list with next and random pointer | Set 1 - GeeksforGeeks](http://www.geeksforgeeks.org/a-linked-list-with-next-and-arbit-pointer/) — geeksforgeeks.org
- [InfoQ: Software Development News, Videos & Books](http://www.infoq.com/) — infoq.com
- [InfoQ - 促进软件开发领域知识与创新的传播](http://www.infoq.com/cn/) — infoq.com
- [Free Online XLIFF Editor - for mobile app translations](https://xliff.brightec.co.uk/) — xliff.brightec.co.uk
- [8 Leadership Principles + Examples of Leadership In Action](https://leaders.com/articles/leadership/leadership-principles/) — leaders.com
