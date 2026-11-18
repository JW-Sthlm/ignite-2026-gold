# Ignite 2026, sorted for customers

**Version:** 18 November 2026
**Sources:** the [Microsoft Ignite 2026 Book of News](https://news.microsoft.com/events/ignite/2026/book-of-news/) and the official Microsoft blog linked under each item.
**Compiled by:** Johan Wallquist, Cloud & AI Advisor at Microsoft. A personal project, not an official Microsoft document.

The Book of News has almost 60 announcements. This file keeps the 28 that matter most to companies already running on Microsoft, in six groups. Each status is copied the way Microsoft worded it on 18 November 2026, and statuses change. There are no prices here on purpose. Check the linked source before you decide anything.

To use it with Copilot: attach this file together with the prompt from https://jw-sthlm.github.io/ignite-2026-gold/

## Status words

- **Generally available (GA):** released and supported for production use.
- **Preview:** you can try it, but features and terms can change before release.
- **Private preview:** invite only.
- **Frontier program:** Microsoft's early-access program for new Copilot features.
- **Rolling out:** announced and arriving over the coming weeks.

---

## 1. How people work: the new Copilot

Microsoft now describes a job as four kinds of work. You ask (Chat), you hand off (Cowork), you build (Code) and you follow through (Autopilot). Ignite moved all four forward.

### 1.1 Home: Chat and Cowork in one place

- **Status:** Home is rolling out worldwide. Auto's suggestion to move a task from Chat to Cowork is generally available.
- **For:** everyone
- **What it is:** One starting point in the Copilot app. Ask a quick question in Chat or hand a multi-step job to Cowork. Auto picks the model and effort for each request, suggests Cowork when a task gets complex and brings your context along.
- **Why it matters:** Most people still use Copilot for questions. Cowork is for whole tasks, like a customer briefing or a month-end close package.
- **Source:** https://aka.ms/MicrosoftIgnite26Blog

### 1.2 Office in Copilot

- **Status:** Generally available.
- **For:** everyone
- **What it is:** Full Word, Excel and PowerPoint inside the Copilot app. Files are saved to OneDrive and keep your permissions, sensitivity labels and compliance controls.
- **Why it matters:** You go from a conversation to a finished document without copying text between apps.
- **Source:** https://aka.ms/MicrosoftIgnite26Blog

### 1.3 Copilot Code

- **Status:** Available in the Frontier program on Windows, web, iOS and Android. Generally available in December. Copilot Managed Runtime, which hosts the apps, is generally available.
- **For:** business users, IT
- **What it is:** Describe a dashboard, a tracker or a small app and Copilot builds it, using the same agent technology as GitHub Copilot. Apps run in a sandbox inside your tenant. IT sees and manages them in the Microsoft 365 admin center.
- **Why it matters:** The person closest to a problem can build the fix, while IT keeps the identity and governance controls it already uses.
- **Source:** https://aka.ms/MicrosoftIgnite26Blog and https://aka.ms/CopilotManagedRuntime-Ignite-Blog

### 1.4 Autopilot

- **Status:** Rolling out to Frontier program customers.
- **For:** everyone, IT
- **What it is:** A personal agent that keeps working without a new prompt. It follows up threads, runs recurring work and can pick a project back up days later. Colleagues can @mention your Autopilot in Teams. Each Autopilot has its own Microsoft Entra Agent ID and a named manager, and IT can scope or block it.
- **Why it matters:** Microsoft's first long-running agent for personal work, with identity and audit trails from day one. A good pilot is one recurring process, like a weekly status round.
- **Source:** https://aka.ms/MicrosoftIgnite26Blog

### 1.5 Copilot Workspaces

- **Status:** Available in the Frontier program.
- **For:** teams
- **What it is:** A shared space in the Copilot app where a team and its agents work on the same documents. Copilot shows what changed, what is unresolved and what needs action. It is the next version of Copilot Notebooks, and personal Autopilots will be able to join soon.
- **Why it matters:** Copilot has mostly been used one person at a time. Workspaces makes it a team tool.
- **Source:** https://aka.ms/MicrosoftIgnite26Blog

### 1.6 Today

- **Status:** Starting to roll out in private preview through the Frontier program.
- **For:** everyone
- **What it is:** A personal view in the Copilot app and Outlook of what needs your attention across mail, calendar, chats and meetings. It also prepares drafts and scheduling changes for you to approve. The morning brief is included with a Microsoft 365 Copilot license, while the feed that refreshes through the day uses Copilot credits.
- **Why it matters:** The inbox is where many people want help first.
- **Source:** https://aka.ms/MicrosoftIgnite26Blog

### 1.7 Skills for sales, finance and service

- **Status:** Dynamics 365 Sales plugin and Dynamics 365 ERP apps plugin: generally available. Salesforce in Copilot: preview.
- **For:** sales, finance and service teams
- **What it is:** Plugins that bring CRM and ERP data, actions and ready-made skills into Copilot. Sellers can build account plans and prepare for meetings. Finance teams can handle purchase requisitions and orders in Cowork and Excel. Salesforce in Copilot has more than 38 prebuilt sales skills.
- **Why it matters:** Copilot can work in the systems where your business data already is, Microsoft or Salesforce.
- **Source:** https://aka.ms/D365Ignite2026 and https://aka.ms/AA1457n5

---

## 2. Your company's know-how: Microsoft IQ

Every company can buy the same AI models. The difference is context: how your business runs, what your people know and the data you have built up over the years. In his keynote, Satya Nadella talked about "ownership over your organization's intelligence and learning".

### 2.1 Microsoft IQ

- **Status:** Generally available. No new SKU or subscription.
- **For:** business leaders, IT
- **What it is:** One platform for the context that apps and agents use. Work IQ covers how people work, Fabric IQ your business data and metrics, Foundry IQ your documents, and Web IQ the public web. It works across Microsoft Copilot, GitHub Copilot, Microsoft Foundry and other agents through MCP.
- **Why it matters:** Skills, tools and agents that work can be reused across teams. What you build now becomes the starting point for the next agent.
- **Source:** https://aka.ms/miq-ignitelaunchblog

### 2.2 Business plugins

- **Status:** Available in the Frontier program.
- **For:** business leaders, IT
- **What it is:** Your experts write down once which data, tools, skills and sources an agent should use for a scenario, and every agent in the organization can inherit it. Microsoft's example is a supply disruption: the plugin tells the agent to find affected orders in Fabric, check late-delivery terms in the supplier contracts and find out who owns the decision.
- **Why it matters:** Expert know-how gets applied the same way everywhere, with sensitivity labels and change auditing. Microsoft's stated goal is better results at lower token cost.
- **Source:** https://aka.ms/miq-ignitelaunchblog

### 2.3 Fabric IQ in Copilot, Excel, ChatGPT and Claude

- **Status:** In Microsoft Copilot: generally available. In Excel: preview. Connectors for ChatGPT and Claude: preview.
- **For:** finance and data teams
- **What it is:** Answers grounded in your Power BI semantic models and Fabric data, in whichever assistant people use.
- **Why it matters:** A revenue figure in ChatGPT or Claude will match the one in your quarterly business review, as long as both come from the same governed model.
- **Source:** https://aka.ms/miq-ignitelaunchblog

---

## 3. Your systems: modernization

"Agents are only as useful as the systems they can act on," says Microsoft's Azure blog for Ignite. In a Forrester survey quoted by Microsoft, 91% of IT leaders said modernization is necessary for AI. On average, only 32% of their applications were AI-ready.

### 3.1 Azure Catalyst

- **Status:** Generally available. Several new capabilities, such as AI-powered application discovery and deeper modernization planning, are in preview.
- **For:** CIOs, IT, developers
- **What it is:** One agent-led flow for modernizing applications, data and infrastructure, in four stages: discover, decide, design, execute. It brings Azure Migrate and GitHub Copilot modernization together. Its agents map dependencies across servers and databases and trace them into the code.
- **Why it matters:** IT and developers plan from the same picture. The business case (Value Uplift) puts resiliency, agility and productivity gains next to the cost savings, so modernization is argued on value as well as TCO. Microsoft experts can also help with deployment through Cloud Accelerate Factory, working alongside your partner. Ask your account team whether your project qualifies.
- **Go deeper:** session BRK412, "Rethink modernization end to end with agents" (recorded)
- **Source:** https://aka.ms/modernization-ignite26

### 3.2 GitHub Copilot modernization

- **Status:** Rulebooks and bring-your-own-model support: generally available. Combined app and database modernization, and BizTalk to Azure Logic Apps: preview.
- **For:** developers, architects
- **What it is:** Agents that upgrade and move Java, .NET and database workloads from the command line or the IDE. Rulebooks let your architects set the standards that every agent-generated plan must follow.
- **Why it matters:** Upgrades can run across many applications in parallel, under your rules. One Ignite lightning talk is called "How Microsoft Intune reduced app modernization from four weeks to one" (LTG1282).
- **Source:** https://aka.ms/modernization-ignite26

### 3.3 Database moves: SQL Server, Oracle and PostgreSQL

- **Status:** Azure SQL Managed Instance link for SQL Server Always On availability groups: generally available. Oracle-to-PostgreSQL migration in Azure Database Migration Service: preview. Azure HorizonDB: generally available.
- **For:** IT and data teams
- **What it is:** The Managed Instance link replicates every database in an availability group to Azure in near real time, for migrations with minimal downtime or for disaster recovery. Azure Database Migration Service gets a first-party path from Oracle to PostgreSQL. HorizonDB is Microsoft's PostgreSQL-compatible database for mission-critical apps, with vector search built in.
- **Why it matters:** Modernization often stalls at the database. These go after two classic blockers: downtime during the move and converting Oracle code and schemas.
- **Source:** https://aka.ms/ignite26/mssql, https://aka.ms/Ignite26/Postgres_on_Azure and https://aka.ms/ignite26/horizondb

### 3.4 SAP ECC to Dynamics 365, with agents

- **Status:** Rolling out from 17 November and over the coming weeks. The Salesforce migration experience: generally available.
- **For:** CIOs, finance, IT
- **What it is:** Dynamics 365 Activate now covers ERP. Agents analyze your SAP ECC processes, configurations and customizations, then help with requirements, configuration and data migration. Project teams review and validate every recommendation.
- **Why it matters:** With SAP ECC approaching the end of mainstream maintenance, many companies have to decide what to move, simplify or redesign. This gives that decision a faster first draft.
- **Source:** https://aka.ms/D365Ignite2026

### 3.5 When an old system has no API: Windows 365 for Agents

- **Status:** Computer use in Copilot Studio (Standard harness): available. Access to on-premises apps with agent identities: preview. Persistent Cloud PCs: preview in the Frontier program. Foundry support through MCP: preview early next year.
- **For:** IT, process owners
- **What it is:** Agents that operate business applications through a governed Cloud PC, the way a person would. Built for legacy systems without APIs.
- **Why it matters:** A useful bridge while you modernize. Agents that click through screens are usually slower and more fragile than agents that call an API.
- **Source:** https://aka.ms/W365Ignite26Blog

### 3.6 Windows Server 2028

- **Status:** Preview through the Windows Server Insider Program. The AI features are in an early access program for a limited number of customers.
- **For:** IT
- **What it is:** The next Windows Server. It is more secure by default, with post-quantum cryptography and automated certificate management, and you can manage it with Intune and Azure Arc. It can also run AI inference close to on-premises applications and data.
- **Why it matters:** Workloads that must stay on-premises can get AI next to them, managed the same way as the cloud.
- **Source:** https://aka.ms/WindowsServer2028Announcement

---

## 4. Running it: operations and infrastructure

### 4.1 Agents in cloud operations

- **Status:** Azure Monitor health models: generally available. Natural-language planning and deployment in Azure Monitor: generally available. New Azure SRE Agent capabilities: preview. Oracle and SAP in Azure Workload Center: private preview.
- **For:** IT operations
- **What it is:** Health models turn telemetry into a live map of what is affected and how much it matters to the business. Azure SRE Agent investigates incidents, finds root causes and suggests fixes. New controls give it customer-managed keys, its own identity through Entra Agent ID and Agent 365, a Teams integration and investigations across other clouds.
- **Why it matters:** Operations is a natural first place for agents. The signals already exist, the work repeats and people still approve the fix.
- **Source:** https://aka.ms/ignite2026/agenticops

### 4.2 Database agents

- **Status:** Database Hub in Fabric: generally available. SQL and PostgreSQL database agents: preview.
- **For:** data teams, IT
- **What it is:** One place to monitor and manage databases across Azure, Fabric, on-premises and other clouds. The agents watch the estate, explain issues and carry out fixes you approve, within existing permissions.
- **Why it matters:** Database teams spend less time firefighting and more time approving.
- **Source:** https://aka.ms/ignite26/databases

### 4.3 Azure Cobalt 200

- **Status:** Generally available.
- **For:** IT, platform teams
- **What it is:** Virtual machines on Microsoft's own Arm-based processor, with up to 50% better CPU performance than Cobalt 100. Already deployed in Sweden Central, among other regions.
- **Why it matters:** Agents do much of their work outside the model, on ordinary CPUs, so CPU speed affects how fast agent tasks get done.
- **Source:** https://aka.ms/Cobalt200VMs-GA

### 4.4 Foundry models and agents on your own Kubernetes

- **Status:** Preview.
- **For:** platform teams, IT
- **What it is:** Deploy open-weight models and agents from Microsoft Foundry to your own Azure Kubernetes Service clusters, under your own security policies. You choose GPUs and regions based on cost, latency and data residency. Related previews: Agent Grid for central policy across agents, models and tools, and Agent Sandbox for running agent-written code in isolation.
- **Why it matters:** More control over where AI runs and what it costs. Relevant when data residency is a requirement.
- **Source:** https://aka.ms/ai-infra-ignite26

---

## 5. Building AI

### 5.1 Continuous improvement in Foundry

- **Status:** Agent optimizer, multi-turn evaluation and production insights: generally available. New training options: preview.
- **For:** developers, AI teams
- **What it is:** Foundry groups recurring failures from production, proposes changes to an agent and tests them against your own evaluations. When configuration changes stop helping, you can train the model further on your data.
- **Why it matters:** Agents improve from real use, measured against your definition of good. Each improvement becomes the next baseline.
- **Source:** https://aka.ms/miq-ignitelaunchblog

### 5.2 Fabric apps and Rayfin

- **Status:** Generally available. Custom data apps in Power BI Desktop for Power BI Pro customers: preview.
- **For:** business builders, data teams
- **What it is:** Build complete business apps on trusted Fabric data, with database, authentication and governance included. Builders created more than 100,000 apps with Rayfin during the preview.
- **Why it matters:** Apps built with AI still need a real backend and governed data. This gives them both.
- **Source:** https://aka.ms/FabricApps-Ignite26

### 5.3 Microsoft Copilot SDK 2.0

- **Status:** Generally available.
- **For:** developers
- **What it is:** The agent harness Microsoft and GitHub run in production, packaged for your own applications. Native Rust runtime, six programming languages and support for multi-tenant scale.
- **Why it matters:** You start from a harness Microsoft already runs at scale instead of writing your own.
- **Source:** https://aka.ms/copilot-sdk/blog-2.0

---

## 6. Trust, control and cost

### 6.1 AI spend and value in Agent 365

- **Status:** Cost Management: preview. Forecasting and Agent 365 Business Analytics: available in the Frontier program.
- **For:** CFOs, CIOs, business leaders
- **What it is:** One view of what AI costs across Copilot Cowork, Copilot Code, GitHub Copilot CLI, Copilot Studio, Autopilot and more, with spending limits and alerts. Business Analytics shows value for specific tasks, such as success rate and assisted hours.
- **Why it matters:** AI spend is growing and moving beyond IT. Leaders need cost and value side by side to decide where to invest next.
- **Source:** https://aka.ms/a365analytics

### 6.2 Governing agents in Agent 365

- **Status:** Plugin and skill governance for Copilot and Cowork: generally available. Governance for MCP servers and for local and shadow agents: preview. Action center: private preview in December.
- **For:** IT, security
- **What it is:** Central control over which plugins, skills, tools and agents people can use, including agents running on laptops. The action center starts with inactive and ownerless agents.
- **Why it matters:** Agents multiply fast and many start on someone's laptop. You can only govern what you can see.
- **Source:** https://news.microsoft.com/events/ignite/2026/book-of-news/

### 6.3 Microsoft Perception

- **Status:** Generally available.
- **For:** security teams
- **What it is:** Specialized security agents and playbooks. The triage agent covers about 80% of alerts in a typical Microsoft Defender queue. Other agents investigate attacks, write detections and test web applications.
- **Why it matters:** AI is changing how fast vulnerabilities are found and exploited. Perception helps defenders keep up, with approvals and audit logs.
- **Source:** https://aka.ms/perceptionignite

### 6.4 Local AI agents under control

- **Status:** Defender runtime protection for local AI agents: generally available for Defender for Endpoint P2 customers. Entra Agent ID for discovered local agents, and Intune governance of local agents: preview.
- **For:** security, IT
- **What it is:** Protection and control for AI agents that run on employees' PCs, such as GitHub Copilot CLI and Claude Code. Defender scans agent calls for malicious instructions, and Intune can mark devices with unapproved agents as noncompliant.
- **Why it matters:** Local agents act with the user's access. A hidden instruction in a file or web page can trigger actions nobody intended.
- **Source:** https://aka.ms/ignite/entra and the Book of News

### 6.5 Purview for Copilot

- **Status:** Public preview in January 2027, according to Microsoft's Purview blog for Ignite.
- **For:** compliance, IT
- **What it is:** Data loss prevention that can stop Copilot from referencing files with sensitive information even when they aren't labeled, and protection for prompts with attachments and linked files. It also covers AI agents running on Windows.
- **Why it matters:** Worries about oversharing slow down many Copilot rollouts. Protection that doesn't depend on perfect labeling helps.
- **Source:** https://techcommunity.microsoft.com/blog/microsoft-security-blog/secure-the-data-that-fuels-ai-with-microsoft-purview/4573266

---

## Watch on demand

- Opening keynote with Satya Nadella (KEY01): https://ignite.microsoft.com/en-US/sessions/KEY01
- All Ignite 2026 sessions: https://ignite.microsoft.com/en-US/sessions
