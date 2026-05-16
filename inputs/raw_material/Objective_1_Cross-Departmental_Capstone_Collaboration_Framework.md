# Objective 1: Cross-Departmental Capstone Collaboration Framework

-----

## Objective Statement

**Purpose:** Develop and formalize a cross-departmental collaboration framework between Computer Science and Graphic Design capstone courses by implementing structured processes and assessment methods.

**Requirements:**

- Document and standardize the Creative Brief process with the Graphic Design department
- Establish three formal touchpoints/milestones in the collaboration cycle
- Create rubrics for evaluating cross-team communication and deliverable integration

**Status:** Achieved — January 2026.

-----

## Why This Work Was the Right Call

Before detailing what was built and how, it is worth grounding the decision in what the field already knew.

The question facing any program that trains future software and design professionals is not whether students will work on cross-functional teams — they will. The question is whether they will encounter that dynamic for the first time on the job, or arrive having already navigated it, failed at it, recovered from it, and built the communication habits it requires. That distinction is what this initiative addresses, and it is the reason the framework developed here represents more than a curriculum add-on.

The national employer data makes the stakes concrete. According to the **NACE Job Outlook 2025**, nearly 90% of recruiters actively screen for problem-solving and nearly 80% for teamwork — not as soft preferences, but as primary filters when reviewing new-graduate candidates. By 2026, 70% of employers were using skills-based hiring practices (up from 65% the previous year), while the proportion still relying on GPA had dropped to 42% — down from 73% in 2019. What employers are buying, increasingly, is demonstrated collaborative capability, and GPA is not a proxy for it.

The workforce trajectory amplifies this. The **World Economic Forum's *Future of Jobs Report 2025*** projects that 39% of workers' existing skill sets will be transformed or rendered obsolete by 2030. The skills rising to fill that gap — analytical thinking, creative reasoning, resilience, flexibility — are precisely the outputs of environments where students must negotiate across disciplines under real constraints. Credentials alone don't build them. Cross-functional project experience does.

There is also a documented labor-market premium on professionals who can inhabit multiple roles. **Burning Glass Technologies' *The Hybrid Job Economy*** (2019) found that roles requiring skills at the intersection of design and development grow at approximately twice the rate of the overall job market and command 20–40% higher compensation. These roles don't require mastery of two disciplines simultaneously — they require what IDEO CEO Tim Brown called the T-shape: disciplinary depth *plus* "the disposition for collaboration across disciplines." Without the latter, Brown observed, "you get gray compromises where the best you can achieve is the lowest common denominator."

The research on interdisciplinary CS-and-design education at the postsecondary level confirms that the structural challenge is solvable. Heines, Jeffers, and Kuhn's **"Performamatics"** series (*International Journal of Learning*, 2008; ACM SIGCSE, 2009) documented outcomes from pairing Computer Science and Design Arts students in joint projects at UMass Lowell, demonstrating measurable gains in motivation and engagement. McDonald and Wolfe's work at DePaul (**"Using Computer Graphics to Foster Interdisciplinary Collaboration in Capstone Courses,"** *Journal of Computing Sciences in Colleges*, 2008) noted directly that "working effectively as a member of an interdisciplinary team is a skill highly valued by today's employers" — and built an interdisciplinary capstone accordingly. At scale, Georgia Tech's Junior Design sequence (Hutter, Lawrence, McDaniel & Murrell, ACM SIGCSE, 2018), serving 400–600 CS students per semester, contrasted mere parallel disciplinary labor against genuine integration, concluding that true integration results in "a smoother end product" — because the disciplines are allowed to inform each other rather than run in separate lanes.

As institutions that have already made this investment continue to report stronger student outcomes and employer reception, programs without structured cross-disciplinary capstone experience are asking their graduates to learn in their first job what their peers learned in their last semester of school. This initiative was built on the premise that FTCC's students deserve better than that starting position.

-----

## The Design Problem — And Why Informal Coordination Had Already Failed

The default state for cross-departmental collaboration in higher education is informal coordination: instructors agree in principle, students are told to work together, and friction resolves itself — or it doesn't, and projects absorb the consequences late in the semester. That default state fails reliably and for predictable reasons:

- Departments run on different milestone schedules, so deliverable timing never quite aligns
- Disciplinary terminology diverges in ways neither party recognizes until handoffs break
- Ownership of shared deliverables is ambiguous, so each side waits for the other
- Collaboration quality is either not assessed at all, or assessed only as part of a product grade that obscures whether the team actually functioned

The failure modes here are not character flaws — they are structural deficiencies. The industry literature on design-development collaboration identifies the same pathologies in professional teams. According to the **Nielsen Norman Group's "Creating Design Specs for Development"** (2025), the absence of formal documentation creates "confusion and frustration in design and development teams" that would be preventable with what NN/g describes as a "contract between design and development." The **Interaction Design Foundation's 2026 handoff curriculum** catalogs the most common professional failures: vague specifications, disorganized files, missing edge-case documentation, and an over-the-wall mentality in which design and development treat each other as sequential rather than collaborative.

These are exactly the failure modes students encounter when collaboration structure isn't built into the course. Naming them as industry defects — not just student shortcomings — is part of what makes this framework pedagogically honest.

-----

## Framework Architecture

The framework is organized around one insight: structure doesn't constrain creativity; it creates the conditions in which creativity can be delivered reliably.

### Role Clarity: The GREY Clearance Model

Within the AlgoCratic Futures project context, Graphic Design students were designated **GREY clearance** — a cross-functional specialist role operating within the same project structure as CS teams but under a distinct operational mandate. This framing solved the most persistent problem in cross-disciplinary collaboration: role ambiguity.

When roles are vague, students default to either avoidance (waiting for the other party to define the work) or collision (overlapping efforts, conflicting directions). The GREY designation did four structural things:

1. Established design students as specialized consultants with defined deliverables — not subordinate support, not passive recipients
1. Positioned the Creative Brief as a formal work order between professional roles, creating mutual accountability
1. Integrated both departments into the same Scrum milestone structure, so neither operated on an external or implicit schedule
1. Brought design students into CS Scrum ceremonies — standups, sprint planning, sprint reviews, retrospectives — as full participants

This approach mirrors how professional cross-functional teams actually operate. The **Scrum Alliance** defines cross-functional teams as those whose members "can include developers, testers, designers, and any other roles required to achieve the sprint goal" — an explicit acknowledgment that design is not external to the development process. The **U.S. Digital Service TechFAR Hub** guidance reinforces this: federal agile teams are now expected to be cross-functional by default.

-----

### Deliverable 1: The Standardized Creative Brief Process

**Documentation created:** `26SP_Cross_Discipline_Protocol.md`

The Creative Brief process formalized a staged exchange between CS teams and GRD students across three document types:

- **Product Brief** (CS → GRD): project context, user personas, design requirements
- **Technical Brief** (CS → GRD): constraints, asset formats, integration specifications
- **Design Brief Response** (GRD → CS): concept proposals, mockup iterations, delivery specifications

**Process sequence (Sprint 0 is the pre-build planning sprint; Sprint 1 is the first build sprint):**

|Stage |Event |Timing|
|----------------|--------------------------------------------|------|
|Sprint 0, Wk 2 |CS team submits Product and Technical Briefs|— |
|Sprint 0, Wk 3 |GRD student submits clarifying questions |— |
|Sprint 0, Wk 4 |CS team refines brief with answers |— |
|Sprint 1, Wk 1 |GRD student delivers concept mockups |— |
|Sprint 1, Wk 2 |CS team provides integration feedback |— |
|Sprint 1, Wk 3–4|GRD student delivers production assets |— |

**Why this structure maps to industry norms:** NN/g's framing of design specifications as a "contract" between teams is not metaphorical — it reflects how high-functioning product teams assign accountability. When a student can point to a brief they submitted, a question they asked, and an asset they delivered to specification, they are rehearsing the documentation habits professional product teams depend on. They are also generating the paper trail that allows assessment to be specific rather than impressionistic.

**Previous state:** Each CS/GRD pairing negotiated its own process, with no standardized artifacts and no baseline for evaluation.
**Current state:** A documented protocol with clear handoffs, defined deliverable formats, and a repeatable sequence.

-----

### Deliverable 2: Three Formal Touchpoints

**Documentation created:** `26SP_Platform_Project_Matrix.md`

Milestones do more than mark time — they convert vague expectations into specific commitments. Industry project management converges on the principle that milestones must define "what 'done' looks like at various intervals" to shift teams from activity-based to outcome-based execution. In interdisciplinary student teams, this distinction is particularly consequential: activity is easy to perform and easy to confuse with progress. Milestones prevent that confusion.

**Touchpoint 1: Creative Brief Exchange** — End of Sprint 0

Both parties have committed deliverables: CS submits product and technical briefs; GRD submits concept questions. The assessment criterion at this stage is brief completeness and clarity. The outcome is a shared, documented understanding of project vision and constraints — replacing the assumption of alignment with evidence of it.

**Touchpoint 2: Concept Review and Iteration** — Sprint 1, Weeks 1–2

GRD presents initial mockups. CS provides integration feedback and technical feasibility assessment. A joint design critique establishes approved direction. The assessment criterion at this stage is communication quality and iteration responsiveness — capturing the collaboration behavior, not just the artifact. The outcome is an approved design direction with technical validation on record.

**Touchpoint 3: Asset Delivery and Integration** — Sprint 1, Weeks 3–4

GRD delivers production-ready assets to specification. CS integrates them into a working application. Both parties co-present at the Graduate Showcase. Assessment criteria at this stage include technical integration success and design implementation fidelity — measuring whether the collaboration produced a coherent whole rather than two well-executed halves that don't quite fit together.

**Integration with Scrum ceremonies:** Design students participated in daily async standups, Sprint 1 planning, the Graduate Showcase Sprint Review, and a cross-departmental retrospective. This is the same ceremony structure Mahnič documented in his longitudinal Scrum capstone study (**"A Capstone Course on Agile Software Development Using Scrum,"** *IEEE Transactions on Education*, 2012), which found that these ceremonies produced "overwhelmingly positive" student outcomes with measurable improvements in planning and estimation — outcomes students explicitly linked to their employability.

-----

### Deliverable 3: Collaboration Rubrics

**Documentation created:** `Pitch_Presentation_Rubric.md`

The rubric is where good intentions about collaboration become assessable commitments. The principle underlying the design is straightforward: if collaboration behaviors are not separately measured, they are not taught. Students learn to optimize for what gets scored. A rubric that only evaluates individual deliverable quality is, functionally, a rubric that treats collaboration as optional.

The research supports this design choice. The **Interprofessional Collaborator Assessment Rubric** (Curran et al., grounded in the WHO 2010 *Framework for Action on Interprofessional Education & Collaborative Practice*) is the most-cited validated instrument of this type, and its architecture — assessing collaboration as a competency in its own right — is directly applicable here. A 2024 meta-analysis by Panadero et al. (*Educational Psychology Review*) found a moderate positive effect (g = 0.45) of rubric use on academic performance, with the effect strongest when criteria are explicit and distributed in advance.

**Rubric structure:**

|Category |Points|What It Measures |
|-----------------------|------|------------------------------------------------------------------------------|
|Communication Quality |20 |Clarity of briefs, responsiveness, professionalism, documentation completeness|
|Deliverable Integration|25 |Technical spec adherence, asset quality, integration success, fidelity |
|Collaboration Process |20 |Milestone adherence, iteration responsiveness, problem-solving approach |
|Final Product Quality |35 |UX enhancement, professional polish, technical implementation, completeness |

This three-axis structure — individual craft, collaboration behaviors, integration quality — directly addresses the dominant failure mode of group projects in higher education: one student absorbs the load while others contribute minimally. When collaboration behaviors carry 20 points and are assessed against concrete criteria (Was the brief complete? Were questions responded to within the milestone window? Did the team adapt when problems arose?), there is no longer a grade structure that rewards passengers.

-----

## Results: Graduate Showcase, May 2026

**Quantitative outcomes:**

- 5 CS capstone teams paired with GRD students across the full semester
- 5 completed projects with integrated, professional-quality design assets
- 100% milestone completion across all five pairings
- Average collaboration rubric score: **87/100**

**Qualitative outcomes:**

- CS teams reported that design integration substantially improved perceived project quality
- GRD students reported meaningful gains in understanding technical constraints and iterative feedback processes
- Both cohorts identified the formal handoff structure as the element most responsible for reducing last-minute communication crises
- Both departments expressed interest in continuing the protocol for subsequent terms

**What the Graduate Showcase demonstrated to external stakeholders:** Faculty, industry partners, and fellow students encountered polished, professionally integrated web applications — not student prototypes that looked like student prototypes. That visible quality gap between AlgoCratic Futures projects and typical capstone output is the observable return on the structural investment described above.

-----

## Institutional Value: Infrastructure, Not Just Outcome

### A Replicable Framework

The protocols created here are not semester-specific documentation — they are reusable infrastructure. When a process is documented once and works, the cost of repeating it falls dramatically. When it fails in some respect, the documentation makes the failure diagnosable and correctable rather than mysterious.

- **Spring 2026:** First full implementation (completed).
- **Fall 2026:** Protocol refinement based on retrospective feedback.
- **Future terms:** Standardized framework with embedded continuous improvement.

### A Template for Adjacent Collaborations

The structured collaboration approach is now available as a model for other cross-departmental pairings the institution may pursue:

- Web Development + Graphic Design partnerships
- Database courses + Business Analytics integration
- Mobile Development + User Experience research

Any program pairing where disciplinary handoffs are the primary design challenge can adopt this framework's milestone structure, brief protocol, and rubric architecture without building from scratch.

### Career Readiness in the Language Employers Use

The NACE Career Readiness framework identifies eight core competencies employers expect from new graduates. The framework developed here directly develops four: **Teamwork/Collaboration**, **Professionalism/Work Ethic**, **Critical Thinking/Problem Solving**, and **Communication** — the four in which the NACE 2024 Student Survey vs. Job Outlook 2025 comparison reveals the largest perception gaps between student self-assessment and employer rating. Students routinely overestimate their proficiency in these areas because they have never been assessed against them with specificity.

What this capstone framework does, structurally, is close that gap before graduation rather than after it. When students leave FTCC having written a formal brief, delivered it on a milestone schedule, received structured feedback from an external collaborator, integrated that feedback into a working product, and had their collaboration behaviors scored against explicit criteria — they have done the work. That is what the rubric measures. That is what the Graduate Showcase makes visible.

-----

## Conclusion: Objective Exceeded

**Minimum requirement:** Document Creative Brief process, establish three touchpoints, create collaboration rubrics.

**Actual delivery:**

- Comprehensive cross-departmental framework with full process documentation
- Milestone structure integrated with Scrum methodology and Scrum Alliance cross-functional team norms
- Multi-dimensional assessment rubric with empirical grounding in collaboration-competency literature
- Successful first implementation with five completed, publicly presented projects
- Replicable protocol positioned for institutional reuse and adjacent-program adoption

The research had already established that this approach works. The employer data had already established that these skills are what the market requires. What remained was the institutional will to build it and the execution discipline to make it run.

Both are now demonstrated.

**Assessment:** Objective not merely met, but exceeded — with infrastructure of lasting institutional value.

-----

*Full research evidence base, citations, and source details: see Appendix — "Evidence Base for a CS / Graphic Design Cross-Departmental Capstone Framework."*
