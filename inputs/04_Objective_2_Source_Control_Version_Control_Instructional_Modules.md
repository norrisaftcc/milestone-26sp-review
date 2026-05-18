# Objective 2: Source Control & Version Control (SCVC) Instructional Modules

**Instructor:** [REDACTED]
**Course(s):** CSC 289 (Software Development Capstone), CTS 285 (Web Application Development)
**Evaluation Period:** Spring 2026
**Objective Status:** Met.

-----

## Objective Statement

**Original objective (verbatim):** "Four assignments covering the topic 'GitHub collaboration and version control with your team'. 

**Purpose:** Develop four instructional modules covering foundational source control and collaborative development practices — issue tracking, pull request workflow, branch-and-merge strategy, and self/peer code review — along with corresponding hands-on exercises and assessment instruments.

**Stated Requirements:**

- Develop 1+ assignments on branch and merge strategies
- Create and implement a self/peer review framework for code quality
- Integrate issue tracking with the development workflow

**Outcome:** All three stated requirements were met. The four assignments were delivered as the original objective specified, disguised as portions of a 'workforce simulation' (most of the course took place within this simulation: See Objective Zero for additional details.)

-----

## The Problem This Objective Solves

### Why Version Control Workflow Is a Workforce Issue, Not Just a Technical Skill

Anyone who has reviewed a junior developer's onboarding experience knows that knowing Git commands and practicing Git workflow are not the same thing — and employers have become precise about that distinction. Version control workflow ("configuration management") is widely cited in the software-engineering-education literature as a persistent gap between what CS graduates arrive knowing and what employers expect, and industry surveys put Git and pull-request-based collaboration at the center of day-to-day professional practice.<sup>[1][2][3]</sup>

The pedagogical implication is straightforward: a capstone course whose students graduate without fluency in PR-based, issue-tracked, branch-managed collaboration is producing graduates who are literate in code but unprepared for the environment in which that code is written. This objective addresses that gap directly.

### The Gap Standard Instruction Leaves Open

Traditional CS instruction focuses, reasonably, on the technical mechanics of Git: commits, branches, pushes, and merges. What it rarely teaches is the *behavioral discipline* around those mechanics — the habits that prevent lost work, enable parallel development, and support professional accountability. Students learn `git checkout -b`; they do not learn why branching before touching main is a non-negotiable professional norm.

This distinction matters because the industry measures it. The JetBrains/GitKraken 2024 *State of Git Collaboration Report* — drawing on responses from over 150,000 developers — identifies poor communication and lack of context between code changes and their business rationale (i.e., disconnected issue tracking) as the leading productivity drain in software teams.<sup>[4]</sup> Teaching the commands without teaching the workflow produces exactly this outcome at scale: technically capable developers who are difficult to collaborate with.

The modules created under this objective were designed to close that specific gap.

-----

## Framework: The Sacred Workflow

### Design Rationale

The four modules are organized under a single coherent framework called the **Sacred Workflow** — a tongue-in-cheek in-character name for the standard `Issue → Branch → PR → Review → Merge` sequence. Giving the workflow a name, a sequence, and a set of explicit commitments lets students practice the same moves they will encounter on the job — opening a draft PR before code is complete, linking commits to issue numbers, conducting a structured peer review before merging — at reduced scale and reduced stakes.

### The Five Commitments

The Sacred Workflow is organized around five professional commitments that map to daily industry behavior:

1. **Create issues before writing code** — Work is tracked before it begins
1. **Branch before touching main** — No change reaches the integration branch without isolation
1. **Commit early and often** — Progress is preserved in small, reversible increments
1. **Write meaningful commit messages** — The history is documentation
1. **Review before merge** — No code enters the shared codebase without a quality gate

Each commitment corresponds to documented professional practice. Each is assessable. And because they are framed as commitments rather than rules, students relate to them as professional identity rather than compliance requirements.

-----

## Module Descriptions

### Module 1 — Issue Tracking as Work Documentation

**Learning Objectives:** Translate requirements into actionable issue specifications; link commits and pull requests to issues for traceability; use labels and milestones for sprint organization.

Students learn issue tracking not as administrative overhead but as the mechanism by which individual work connects to team goals. The three-tier implementation scaffolds this from structured (instructor-provided issue templates with guided fields) through generative (students decompose requirements into issues) to self-directed (students own the full issue lifecycle, including sprint milestone assignment).

The issue template used in this course — user story, acceptance criteria, technical notes, and explicit definition of done — mirrors industry-standard formats used by professional teams on GitHub, Jira, and Linear. Students who arrive at an employer already fluent in this format reduce their onboarding time and signal professional maturity from day one.

### Module 2 — Branch-and-Merge Workflow

**Learning Objectives:** Isolate features in named branches following convention; commit incrementally with descriptive messages; open and manage pull requests through the full review-and-merge cycle; resolve merge conflicts without losing work.

The hands-on exercise structure scaffolds complexity in three phases: solo individual practice (Solo Burger), pair collaboration with a live merge conflict scenario (Team Lunch), and full team parallel-branch development (Full Sprint). This progression mirrors how organizations of increasing size experience version control: sole contributor → small team → cross-functional team.

Sadowski et al.'s 2018 study of code review practice at Google — covering more than 25,000 developers and 20,000 source changes per workday — found that the median change reviewed at Google involved fewer than 24 lines of code and completed review in under four hours.<sup>[7]</sup> This finding shapes the module's emphasis on *small, frequent commits with clear context* rather than large, infrequent batch submissions. Students learn to work at the scale and rhythm professional review requires.

### Module 3 — Pull Request Process

**Learning Objectives:** Write PR descriptions that communicate context, not just changes; use draft PR status to solicit early feedback; iterate through review cycles as a normal part of development, not a sign of failure.

The pull request is the unit of professional contribution — the moment at which individual work becomes team property. Teaching students to open PRs early, describe their intent clearly, and treat revision as standard process produces graduates who collaborate without friction.

Of particular instructional importance is the **draft PR workflow**: students learn to open a PR before their work is complete, flagging it as a discussion point rather than a submission. This practice, standard at companies like Google and Microsoft, interrupts the student habit of treating submission as a high-stakes, one-shot event. It normalizes iteration — a professional disposition that transfers far beyond version control.

### Module 4 — Self and Peer Code Review

**Learning Objectives:** Conduct structured code reviews using consistent quality categories; provide feedback that is specific, actionable, and respectful; receive critique professionally and respond with follow-up commits or documented rationale.

Review is assessed in four categories — functionality, readability, adherence to best practices, and improvement opportunities — matching the categorical frameworks documented in modern code review research. Bacchelli and Bird's 2013 ICSE study, analyzing hundreds of review comments across Microsoft teams, found that while defect detection motivates review, its most significant outcomes are **knowledge transfer, increased team awareness, and the generation of alternative solutions**.<sup>[8]</sup> These outcomes are precisely what a capstone course should produce.

The SmartBear *State of Code Review* survey — conducted annually across approximately 800 software professionals — has identified peer code review as the **number-one method for improving software quality for five consecutive years**.<sup>[9]</sup> Eighty percent of respondents satisfied with their software quality participate in tool-based code review with explicit guidelines.<sup>[9]</sup> The capstone's review framework provides exactly those guidelines, preparing students for an environment where review discipline is expected, not optional.

The CS education research literature confirms the classroom effectiveness of this practice. Indriasari, Luxton-Reilly, and Denny's 2020 systematic review in *ACM Transactions on Computing Education* — examining 51 empirical studies — found that peer code review in higher education consistently produces gains in **programming-related skill development, engagement, and communication competency**.<sup>[10]</sup> McDowell et al.'s foundational pair-programming research at UCSC further documents that collaborative code review correlates with improved retention, higher program quality, and increased likelihood of continuing in computer science — findings particularly relevant in a community college context where retention is an institutional priority.<sup>[11]</sup>

-----

## Integration: The Complete Workflow in Practice

All four modules converge into a single end-to-end workflow that students practice repeatedly across the semester:

```
Issue Created → Branch Made → Code Written → Commits Pushed →
Draft PR Opened → Self-Review → Peer Review → Changes Addressed →
PR Approved → Merge to Main → Issue Closed
```

This cycle — practiced at low stakes in Sprint 0, at moderate stakes in Sprint 1, and at full team complexity in Sprints 2 and 3 — builds the kind of **procedural automaticity** that Shulman identifies as the goal of signature-pedagogical formation: students stop *thinking about* the workflow and start *enacting* it reflexively.

The workflow maps directly onto Scrum ceremonies, reinforcing agile methodology instruction across the capstone simultaneously: sprint planning produces issues; standups reference branch and PR status; sprint review demonstrates merged work; retrospective evaluates workflow effectiveness. Students are not learning two separate things; they are learning one integrated professional practice.

-----

## Evidence of Effectiveness

### Quantitative Outcomes — CSC 289, Spring 2026

The following data was collected from course artifacts and assessment instruments:

|Metric |Result |
|------------------------------------------------------------------|-----------|
|Students creating issues before code (by Sprint 2) |100% [SOURCE NEEDED: GH org export / issue-creation timestamps vs first-commit timestamps] |
|Average issue completeness score |92/100 [SOURCE NEEDED: graded rubric file] |
|PRs properly linked to issues |95% [SOURCE NEEDED: GH org export of PR bodies] |
|Students resolving merge conflicts without instructor intervention|89% [SOURCE NEEDED: instructor log / TA intake tickets] |
|Work lost due to Git errors |0 instances [SOURCE NEEDED: instructor log; method of counting unclear] |
|Average PR cycle time (create → merge) |2.3 days [SOURCE NEEDED: GH org export or analytics tool — what tool generated this?] |
|Average peer review score |85/100 [SOURCE NEEDED: graded peer-review rubric file] |
|Students who addressed review feedback constructively |94% [SOURCE NEEDED: graded rubric / reviewer follow-up log] |
|Interpersonal conflicts arising from peer review process |0 [SOURCE NEEDED: instructor log] |

These figures reflect not just technical competency but professional behavioral formation — the actual outcome the objective was designed to produce.

### Qualitative Outcomes

Student retrospective comments indicate that the ceremonial framing achieved its purpose:

> *"The Sacred Workflow felt silly at first, but now I do it automatically."* [SOURCE NEEDED: survey/retro/exit-ticket]

> *"Draft PRs saved me from redoing work twice."* [SOURCE NEEDED: survey/retro/exit-ticket]

> *"Peer review taught me to write clearer code even before review."* [SOURCE NEEDED: survey/retro/exit-ticket]

Exit interview data indicates students could describe the PR-based workflow fluently, recognized it from internship and early job experiences, and reported confidence discussing version control discipline in job interviews. [SOURCE NEEDED: exit interview instrument + responses]

-----

## Materials available on request

The same workflow currently runs in CSC 289 (full four-module implementation) and in CTS 285 (issue tracking and basic branch workflow). If any other faculty member wants to try it — in CSC 151 or elsewhere — the supporting materials are available:

- `WORKFLOW_GUIDE.md` — Complete Sacred Workflow documentation
- `ISSUE_TEMPLATE.md` — Issue creation template and guidelines
- `Capstone_GameFAQs_Walkthrough.md` — Student-facing workflow guide
- `YELLOW_Exit_Ticket_Rubric.md` — Competency assessment rubric
- `DAY_1_ESSENTIALS.md` — Day 1 orientation and setup guide
- Sprint planning integration guide, peer review rubrics, and scaffolding progression documentation

Happy to share GitHub links with anyone who asks.

-----

## Assessment

The original objective specified four assignments on GitHub collaboration and version control with a team, delivered as portions of a game. Four assignments were delivered, in that form. The objective is met.

The supporting framework (the named workflow, the cross-course materials, the scaffolded exercise progression) is the form the four assignments took; it is available to anyone in the department who wants to reuse it.

-----

## Summary

|Requirement |Delivered |
|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
|1+ branch-and-merge assignments|Three-phase exercise progression (solo → pair → full team) with sprint integration |
|Self/peer review framework |Four-category rubric system with self-review checklist, reviewer assessment, and response protocol |
|Issue tracking integration |Three-tier scaffolded implementation (INFRARED through GREEN); full sprint-lifecycle traceability |
|**Beyond requirements** |Pedagogical framework grounded in learning theory; cross-course implementation plan; reusable institutional materials; quantified student outcomes|

-----

## References

1. Garousi, V., Giray, G., Tuzun, E., Catal, C., & Felderer, M. (2020). Closing the gap between software engineering education and industrial needs. *IEEE Software, 37*(2), 68–77. https://arxiv.org/pdf/1812.01954
1. Stack Overflow. (2024). *Stack Overflow Developer Survey 2024* (n = 65,437). https://survey.stackoverflow.co/2024/
1. GitHub. (2025). *Octoverse 2025: A new developer joins GitHub every second.* https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/
1. JetBrains & GitKraken. (2024). *State of Git Collaboration Report.* https://blog.jetbrains.com/team/2024/03/05/are-dev-teams-surviving-or-thriving-in-2024-insights-from-jetbrains-and-gitkraken-s-state-of-git-collaboration-report/
1. Shulman, L. S. (2005). Signature pedagogies in the professions. *Daedalus, 134*(3), 52–59.
1. Lave, J., & Wenger, E. (1991). *Situated learning: Legitimate peripheral participation.* Cambridge University Press.
1. Sadowski, C., Söderberg, E., Church, L., Sipko, M., & Bacchelli, A. (2018). Modern code review: A case study at Google. *ICSE-SEIP '18*, 181–190. https://doi.org/10.1145/3183519.3183525
1. Bacchelli, A., & Bird, C. (2013). Expectations, outcomes, and challenges of modern code review. *ICSE '13*, 712–721. https://doi.org/10.1109/ICSE.2013.6606617
1. SmartBear. (2021). *State of software quality: Code review* (8th annual report, n ≈ 800). https://smartbear.com/blog/top-10-insights-on-the-state-of-code-review/
1. Indriasari, T. D., Luxton-Reilly, A., & Denny, P. (2020). A review of peer code review in higher education. *ACM Transactions on Computing Education, 20*(3), Article 22. https://doi.org/10.1145/3403935
1. McDowell, C., Werner, L., Bullock, H. E., & Fernald, J. (2006). Pair programming improves student retention, confidence, and program quality. *Communications of the ACM, 49*(8), 90–95. https://doi.org/10.1145/1145287.1145293