# Spring 2026 Performance Objectives — Documentation

The following documents three performance objectives completed during the Spring 2026 review period, undertaken in support of CSC 289 (Programming Capstone) and adjacent courses. Together they form an arc: Objectives 1 and 2 built the pedagogical frameworks used in capstone; Objective 3 applied the same methodology to support a live institutional project outside the classroom.

---

## Context

CSC 289 was previously taught using waterfall methodology, with course resources for CSC 289 and CTS 285 consisting of the Shelley Cashman *Systems Analysis and Design* textbook and MS Project licenses. The standard expectation for these courses did not include developing a novel pedagogical framework, writing original research syntheses, constructing custom software infrastructure, or producing a documentation library of this scope — the work described below went beyond that baseline deliberately.

The objectives below reflect a transition to agile/Scrum methodology aligned with current industry practice, undertaken because the existing course structure no longer matched the workflow students encounter in entry-level software roles. A unifying design principle runs through all three: measure **learning velocity** — the rate at which students develop competency — rather than absolute skill at a single point in time. This shapes the scaffolded progressions, iteration-rewarding rubrics, and assessment artifacts referenced below.

---

## Objective 1: Cross-Departmental Capstone Collaboration Framework

**Status:** Completed, Spring 2026.

**Purpose:** Formalize collaboration between CSC capstone teams and Graphic Design (GRD) capstone students with documented process, milestone structure, and assessment criteria.

**Requirements:**
- Document and standardize the Creative Brief process with the Graphic Design department
- Establish three formal touchpoints in the collaboration cycle
- Create rubrics evaluating cross-team communication and deliverable integration

**Delivered:**

- **Cross-Discipline Protocol** (`26SP_Cross_Discipline_Protocol.md`) — three-document brief exchange (Product Brief, Technical Brief, Design Brief Response) with a milestone-anchored handoff schedule across Sprint 0 (the pre-build planning sprint) and Sprint 1.
- **GREY-clearance role definition** for GRD students within the AlgoCratic Futures simulation framework. GRD students participate in CSC team Scrum ceremonies (sprint planning, async standups, sprint review, retrospective) as full cross-functional collaborators.
- **Three formal touchpoints:**
  1. Creative Brief Exchange — end of Sprint 0
  2. Concept Review & Iteration — Sprint 1, weeks 1–2
  3. Asset Delivery & Integration — Sprint 1, weeks 3–4
- **Pitch Presentation Rubric** (`Pitch_Presentation_Rubric.md`) — 100-point rubric across four axes: Communication Quality (20), Deliverable Integration (25), Collaboration Process (20), Final Product Quality (35).
- **Platform Project Matrix** (`26SP_Platform_Project_Matrix.md`) documenting all CSC/GRD pairings for the term.

**Outcomes:**

- 5 CSC capstone teams paired with GRD students; 5 completed projects with integrated design assets co-presented at the Graduate Showcase.
- 100% milestone completion across pairings.
- Average collaboration rubric score: 87/100.
- Both departments expressed intent to continue and refine the protocol for Fall 2026.
- Framework engagement extended bidirectionally: four GRD students used AlgoCratic Futures as the creative-brief context for their own portfolio marketing deliverables — adopting the simulation as a vehicle for their own discipline's work rather than only receiving briefs from CS teams.

**Continuation:** Protocol designed for reuse; documentation and rubrics are available as a template for adjacent cross-program pairings (e.g., Web Development + GRD, Database + Business Analytics).

---

## Objective 2: Source Control & Version Control (SCVC) Instructional Modules

**Status:** Completed; deployed in CSC 289 Spring 2026; extending to CTS 285.

**Purpose:** Build instructional modules covering core SCVC competencies on GitHub — Issues, Pull Requests, Branch & Merge Workflow, Self/Peer Review — with hands-on exercises.

**Requirements:**
- One or more assignments on branch and merge strategies
- Self/peer review framework for code quality
- Issue tracking integrated with the development workflow

**Delivered:** Four integrated modules anchored to the **Sacred Workflow** — the named, repeatable process students practice through capstone:

> Issue → Branch → Draft PR → Code & Test → Finish PR → Review → Merge

**Module 1 — Issue Tracking** (`ISSUE_TEMPLATE.md`)
Issue template with user story, acceptance criteria, technical notes, and definition-of-done. Three-tier scaffolding: instructor-created issues → student-created issues → self-organized issue management with milestones.

**Module 2 — Branch & Merge Workflow** (`WORKFLOW_GUIDE.md`)
Full feature-branch lifecycle documented as the Sacred Workflow's ten steps. Phased practice: **Solo Burger** (individual) → **Team Lunch** (pair) → **Full Sprint** (team).

**Module 3 — Pull Request Process**
PR template requiring related-issue link, changes summary, testing documentation, screenshots, and questions for reviewers. The Draft PR workflow — opening a pull request before the work is finished, to surface direction early — is taught explicitly as the early-feedback mechanism.

**Module 4 — Self/Peer Review** (`Capstone_GameFAQs_Walkthrough.md`)
Review framework with four categories (Functionality, Readability, Best Practices, Improvement Opportunities). Three-stage cycle: self-review → peer review → author response. Review quality itself graded to incentivize thoughtful feedback rather than rubber-stamping.

**Assessment:** YELLOW Exit Ticket rubrics (`YELLOW_Exit_Ticket_Rubric.md`) — brief end-of-module competency checks, named for the in-simulation clearance tier — tied to each module.

**Outcomes (CSC 289 Spring 2026):**

- 100% of students creating issues before code by Sprint 2.
- 95% of pull requests properly linked to issues.
- 89% of students handled merge conflicts without instructor intervention.
- Zero instances of work lost due to Git mistakes.
- Average peer review score: 85/100.

**Cross-course extension:** Reduced-scope implementation planned for CTS 285 (Web Development); issue-tracking module under consideration for CSC 151. Materials are modular for selective adoption by other instructors.

---

## Objective 3: Ghost Tool — Project Management & Requirements Support

**Status:** Tool delivered by the development team; support role complete.

**Purpose:** Provide project management, documentation, and requirements-gathering support to the Ghost Tool development team — a team objective focused on detecting duplicate and potentially fraudulent enrollment patterns across the college's ~12,000 student records.

**Approach:** This objective applied the same methodology codified in Objectives 1 and 2 — structured product and technical briefs, milestone-anchored handoffs, and the Sacred Workflow's documentation discipline — to a live institutional project outside the classroom. The frameworks built for capstone instruction provided the blueprint for the support role here.

**Personal contribution:**

- **Requirements gathering** from Student Services stakeholders: interviews with administrative staff, documentation of the existing manual review process, identification of pain points, articulation of acceptance criteria for duplicate detection.
- **Brief development** using the same dual-document structure taught in CSC 289 (product context and user needs; technical constraints and integration requirements).
- **Documentation support** across the development cycle — user-facing materials for non-technical Student Services staff and configuration documentation for IT.
- **Stakeholder feedback coordination** across iteration cycles, applying the same Sprint-review pattern students practice in capstone.

**Tool capabilities (delivered by the development team, for context):**

- Composite-signal duplicate detection across names, addresses, emails, and phone numbers
- Configurable sensitivity thresholds with weighted confidence scoring
- Flagged-record reporting with field-level match breakdown for staff review

**Outcomes:**

- Tool operational and in use by Student Services for ongoing enrollment-cycle screening.
- Manual review burden reduced from ~12,000 records to a tractable flagged subset.
- Requirements and documentation artifacts available for the team's continued refinement and for any future similar engagements.
- The engagement served as a live application of the curriculum methodology outside the classroom — the same briefing, milestone, and feedback patterns used in CSC 289 operating in a cross-stakeholder institutional context.

---

## Adjacent Faculty Engagement

Beyond the formal collaboration structures in Objective 1, the work has generated informal engagement from peer faculty during the review period. Colleagues from adjacent departments have approached the instructor regarding AI-assisted development practices in their own teaching, and a peer instructor has independently developed an LLM-powered subnetting tutor during the same period. These engagements were not systematically tracked, but are noted here as evidence that the methodology has begun circulating beyond the formal pairings.

---

*Supporting materials referenced above are available in the project repository and via separate cover for confidential items (Ghost Tool documentation and flagged-records report).*
