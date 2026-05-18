# Performance Objective Zero: Design and Implement a Multi-Level Immersive Instructional Environment

**Instructor:** [REDACTED]
**Program:** CTS 285 / CSC 289 · [REDACTED] Technical Community College
**Review Period:** 2025-2026
**Status:** Architecture complete; active delivery, Spring 2026
**Classification:** Instructor OOC / Performance Documentation · Voice register: Direct

---

[RELOCATE PER HF-16(a): "Document Clearance Distribution" table is a peer-register clearance-color in-joke aimed at BLUE/INDIGO/VIOLET/ULTRAVIOLET. The anchor (user_stories.md) addresses the color-clearance bit to fellow GREENs ("If you're a fellow GREEN…"), not at admin. Move to a peer-facing appendix (does not yet exist) or cut.]

[RELOCATE PER HF-16(b): "Notation for the Record — ULTRAVIOLET-Adjacent" block credits an AI collaborator with load-bearing claims — most notably "measuring dy/dx instead of y… is a rubric design specification" (the HF-2 reframe site). An AI collaborator the reviewer cannot interrogate cannot carry a load-bearing pedagogical claim. Either relocate to a methodology note early in the binder where its contribution can be evaluated against the rest of the work, or cut.]

---

## A Note on Why This Objective Appears Last in Numbering but First in Logic

This objective was not formally assigned, because it was not formally anticipated. The three objectives that follow it describe work done inside an environment. This objective describes the construction of that environment. It is documented here because the work it describes is the enabling condition for every other objective in this review.

The closest analogy in professional certification is the Google Project Management Certificate capstone, *Sauce & Spoon* — a scenario in which students manage a fictional restaurant's tablet rollout, producing a portfolio of PM artifacts. Sauce & Spoon is a well-regarded credential. Thousands of practitioners have completed it. It is a good scenario.

What was built here is not a scenario someone else designed. **What was built here is the restaurant.** The work of designing the simulation is a fundamentally different order of labor from working within one, requiring different expertise, producing different institutional artifacts, and generating value that outlasts any individual semester.

---

## Why This Work Was the Right Call

The theoretical case for simulation-based immersive learning in technical education is well established. The practical case for building it at a community college serving the Research Triangle job market is stronger still.

The core problem in CS education at the community college level is not primarily a capability problem. What students lack, reliably and predictably, is the identity of a person who uses technical information — the belief that they can, the environmental anchors that make that belief feel real, the experience of having done hard technical work and survived it.

Standard course delivery intervenes at two of the six levels Robert Dilts identified in his Neurological Levels model (mid-1980s, adapted from Gregory Bateson's levels of learning): capability and behavior. These are necessary but not sufficient. Each level in the Dilts hierarchy directly affects those below it — meaning interventions at lower levels will be undermined by unaddressed problems at higher ones.

> A student who has internalized "I'm not a programmer" at the identity level will encounter every capability-level intervention through that filter. The filter will win.
>
> This is not a motivation problem. It is an architecture problem.

Carol Dweck's research on mindset (*Mindset: The New Psychology of Success*, Ballantine Books, 2006) established that students who believed their intelligence could be developed outperformed those who believed it was fixed — and that teachers who endorsed growth mindset in language but not in classroom practice produced students trending toward fixed mindset. Claiming growth mindset is not installing it. Installation requires a designed environment.

Amy Edmondson's foundational research ("Psychological Safety and Learning Behavior in Work Teams," *Administrative Science Quarterly*, 44(2), 1999) demonstrated that team psychological safety — a shared belief that the team is safe for interpersonal risk-taking — is associated with learning behavior, and learning behavior mediates between safety and team performance. The satirical wrapper of AlgoCratic Futures addresses this structurally: failure inside the simulation is the system's absurdity, not the student's inadequacy. The dystopia absorbs the shame. The student keeps the learning.

Lave and Wenger's situated learning theory (*Situated Learning: Legitimate Peripheral Participation*, Cambridge University Press, 1991) established that learning is not a matter of acquiring abstract knowledge and later applying it — it is a matter of becoming a participant in a community of practice. If the goal is professional software development identity, students must be situated in an environment that is, in meaningful ways, that community — with its norms, its roles, its ceremonies, its vocabulary, and its stakes.

One structural dimension warrants explicit documentation. Poole-Dayan, Roy, and Kabbara ("LLM Targeted Underperformance Disproportionately Impacts Vulnerable Users," arXiv:2406.17737, 2024) document a consistent pattern across state-of-the-art LLMs: users with lower English proficiency, less formal education, and non-US origin receive measurably worse AI assistance — higher rates of misinformation, more frequent refusals, and a documented tendency toward condescending responses. These are precisely the populations community colleges disproportionately serve. System 1's per-group context injection ensures every student team accesses AI assistance through a configured pedagogical context rather than through writing-style inference, and the `CLAUDE.md` guardrail files instruct the AI to explain iteratively at the student's level rather than inferring competence from surface signals. The Algorithm, in the AlgoCratic frame, treats everyone and everything fairly. In the actual implementation, this is not the satirical part.

---

## The Design Problem — And Why Standard Course Delivery Had Already Failed These Students

The default state — identify the skills, design exercises that practice them, assess whether students can perform them — fails community college CS students for reasons that are structural, not personal.

Measuring absolute skill level at the end of a course systematically disadvantages students who begin behind. A student who enters knowing nothing and finishes at the 50th percentile has grown more than one who enters at the 60th and finishes at the 65th. The transmission model counts the second student as the stronger performer. This is pedagogically backwards and practically harmful: it discourages students with the most growth potential and misrepresents what an employer actually wants, which is a person who learns.

The transmission model also has no mechanism for identity-level work. Students told — by prior educational experiences, by cultural messaging, by their own internalized histories — that technical fields are not for people like them will not be reached by more skillfully delivered technical content. They need an environment that installs a different story about who they are. This is not therapy. It is instructional design.

---

## Framework Architecture: A Six-Level Pedagogical System

The framework is organized around a single design principle derived from Dilts: intervene at the level where the problem actually lives, and ensure every level above capability is actively supporting — not undermining — the capability work.

| Level | Question | Standard Delivery | AlgoCratic Futures |
|---|---|:---:|:---:|
| **6 — PURPOSE** | *What for?* | ○ | **●** |
| **5 — IDENTITY** | *Who am I?* | ○ | **●** |
| **4 — BELIEFS/VALUES** | *Why?* | ○ | **●** |
| **3 — CAPABILITY** | *How?* | **●** | **●** |
| **2 — BEHAVIOR** | *What?* | **●** | **●** |
| **1 — ENVIRONMENT** | *Where/When?* | ○ | **●** |
| **TOTAL LEVELS ADDRESSED** | | **2** | **6** |

### Level 1: Environment — Where does this happen?

The AlgoCratic Futures environment is not a classroom with a theme. It is a deliberately constructed learning context with consistent visual identity (IBM Plex Mono typeface, phosphor green and amber accents, CRT scanline aesthetic), ceremonial artifacts (lanyards, clearance designations, GitHub organization structure), and a spatial logic that signals: this is not a normal class, and you are not a normal student here. The Day 1 Calibration Ceremony installs an environmental anchor during the highest-leverage moment of the semester — when students are identity-flexible and impression-forming — before any technical content is delivered.

### Level 2: Behavior — What is required, specifically?

The Sacred Workflow — `Issue → Branch → Draft PR → Code/Test → Finish PR → Review → Merge` — is embedded in the tooling, the rubrics, and the in-world vocabulary. The Scrum ceremonies are structural: they are how the work is organized, not optional enrichment activities. Behavioral change that depends on instructor monitoring does not transfer. Behavioral change built into the environment does.

### Level 3: Capability — What can students do?

Git/GitHub workflows, Flask web development, AI-assisted development, SQL and PostgreSQL, deployment via Render, Scrum methodology. The simulation is the delivery vehicle, not the destination. Every in-world assignment maps to a specific technical competency, scaffolded by the clearance level system.

### Level 4: Beliefs and Values — Why does this matter?

When the grading system measures rate of improvement rather than absolute position, the message is encoded structurally: what you do next matters more than where you started. The satirical corporate frame also operates at this level — students who learn to deliver functional work despite contradictory instructions are rehearsing a belief: *I can navigate this. The system is sometimes absurd. That is not my problem.*

### Level 5: Identity — Who are you here?

The clearance progression system is an identity system, not merely a difficulty rating. Students do not complete levels; they become clearance levels. The ceremonies, the Discord role changes, the visual markers are identity anchors. The Flask login page — the moment a student has a working authenticated web application — is the concrete identity threshold: the point at which "I am learning to build things" becomes "I build things."

### Level 6: Purpose — What is this all for?

Students who have spent a semester navigating an exaggerated corporate dystopia are not naive about the environments they are entering. They have already practiced maintaining technical competence inside a system that is sometimes absurd, frequently contradictory, and occasionally designed by people who do not fully understand what they are asking for. When they encounter their first impossible deadline in a real job, the frame they reach for is: *I've handled worse.*

---

## The Growth Velocity Innovation: dy/dx as the Unit of Assessment

In standard assessment, the question is: *Can this student do X?* The answer is a point on a scale, measured once, at the end.

In this framework, the question is: *How fast is this student improving, and in what direction?* The answer is a trajectory, measured across iterations, throughout the semester.

> Measuring **y** (position) identifies who started ahead.
>
> Measuring **dy/dx** (rate of change) identifies who is learning.
>
> These are not the same population.
>
> Treating them as equivalent is one of the most consequential errors in standard technical education.

The student who arrives at zero and finishes at fifty has demonstrated something more important for a hiring manager than the student who arrives at sixty and finishes at sixty-five: they demonstrated that they will not stay where they started. This is operationalized through rubric architecture that rewards documented iteration, through GitHub commit-history analysis that makes growth visible, and through a startup-aesthetic performance dashboard that reports velocity metrics in professional vocabulary while measuring genuine pedagogical outcomes underneath.

---

## Key Deliverables

| Deliverable | Status | Institutional Function |
|---|---|---|
| AlgoCratic Futures world and clearance system | Complete | Identity / environment architecture |
| CTS 285 full assignment library | Complete | Capability curriculum, INFRARED–YELLOW |
| CSC 289 capstone framework and sprint structure | Complete | Capstone delivery infrastructure |
| Sacred Workflow documentation | Complete | Behavior-level norm embedding |
| Student survival guides (Underground voice) | Complete | Psychological safety / beliefs-level |
| Instructor Growth Protocol (Dilts integration) | Complete | Instructor capability development |
| System 1: Flask app, auth, context injection, logging | Built & deployed | Per-group AI access infrastructure |
| System 2: Claude Code per-group setup documentation | Complete | AI tool integration scaffolding |
| `CLAUDE.md` dual-purpose guardrail files | Complete | Pedagogical AI guardrails |
| Growth gamification system (GitHub Actions + METRICS.md) | Designed; in progress | Learning-velocity measurement |
| GRAY Clearance instructional design onboarding brief | Complete | Cross-disciplinary integration |
| Wireframing instructional deck (HTML/JS) | Complete | Gap-filling instructional content |
| Group 4 late-start catch-up package | Complete | Differentiated access / resilient infrastructure |
| AlgoCratic GitHub Pages site | In progress | Public-facing program identity |

---

## Results: Spring 2026

The framework is in active delivery across two courses (CTS 285 and CSC 289) with multiple student groups building distinct web applications. The Graduate Showcase in May 2026 produced publicly presented, professionally integrated projects — not student prototypes that look like student prototypes.

Projects include a financial aid tracker, a recommendation engine, a biometrics/fitness tracker, a task manager, and a mathematics learning platform (DataMan), all developed through the Sacred Workflow under the Scrum structure, with AI tool integration as a required component. Group 4 — an online cohort that joined six weeks late — was successfully onboarded using a comprehensive catch-up package built specifically for their situation, demonstrating that the infrastructure is robust enough to absorb significant edge cases without rebuilding from scratch.

---

## Institutional Value: A Platform, Not a Semester

### Replicable Infrastructure

AlgoCratic Futures is not a set of lesson plans for one semester. It is a documented, version-controlled, pedagogically grounded instructional platform. Any instructor willing to invest in understanding the framework can deploy it. The documentation exists. The infrastructure exists. The assessment architecture exists. The iteration cost of running it a second time is a fraction of the build cost.

### Future-Ready Alignment

The expectations this review is measured against were written for a course delivery role. What was built exceeds that role not by doing more of the same thing, but by building at a different level — the level at which the conditions for effective course delivery are created. The market graduates are entering will require fluency with AI-assisted development, Scrum workflows, cross-functional collaboration, and the capacity to operate inside imperfect systems without losing technical focus. AlgoCratic Futures was built to that specification, not the specification that existed when the job description was written.

### A Template for Adjacent Collaborations

The structured cross-disciplinary approach is now available as a model for other departmental pairings: Web Development + Graphic Design, Database + Business Analytics, Mobile Development + UX Research. Any program pairing where disciplinary handoffs are the primary design challenge can adopt this framework's milestone structure, brief protocol, and rubric architecture without rebuilding from scratch.

---

## Conclusion: Objective Redefined and Exceeded

**Minimum requirement:** Deliver assigned courses.

**Actual delivery:**

- An original, theoretically grounded, six-level immersive pedagogical environment built from scratch.
- Assessment architecture that measures learning velocity rather than position, operationalizing growth-mindset research in rubric form.
- Technical infrastructure (System 1, System 2, `CLAUDE.md` guardrails) enabling AI-tool integration as a first-class curricular component.
- Cross-disciplinary collaboration framework built on the GRAY clearance model (Objective 1).
- Fully documented, replicable platform positioned for multi-semester deployment and institutional adoption.
- Graduate Showcase output demonstrating professional-quality, publicly presented student work.

> **Assessment:** Objective not merely met or exceeded, but operating at a level the original specification did not anticipate. The deliverable specified was effective course delivery. The deliverable built was the infrastructure that makes effective course delivery possible — and replicable, and improvable, and future-ready.

The standard capstone is Sauce & Spoon. You are given a scenario. You practice the skills. You produce the portfolio. **This is not that.** This is the work of designing the scenario — and then delivering it, iterating on it, instrumenting it for measurement, and making it replicable. That is a different job. It requires a different skill set. It produces a different institutional artifact.

*Source bibliography is inline above — citations to Dilts (Neurological Levels, 1980s), Dweck (*Mindset*, Ballantine Books, 2006), Edmondson (*ASQ*, 1999), Lave and Wenger (*Situated Learning*, Cambridge University Press, 1991), and Poole-Dayan et al. (arXiv:2406.17737, 2024) constitute the theoretical grounding for this chapter.*
