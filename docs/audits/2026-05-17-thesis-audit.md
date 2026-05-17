# Thesis Audit — 2026-05-17

## Anchor and scope

- **Anchor:** `inputs/raw_material/user_stories.md`
- **Scope:** `inputs/01_Introduction.md` through `inputs/06_Performance_Objective_Zero.md`
- **Method:** Liza frame map → Linx prose audit + scrum-team-engineer structural audit → synthesis
- This audit is read-only with respect to binder content. Edits, if any, happen in follow-up issues' PRs.

---

## The two frames

### user_stories.md frame

The anchor installs a small, dry, peer-to-peer voice. The author casts the three objectives as originally-modest line items (three meetings, four assignments, three more meetings), notes that he overdelivered, credits the dev team for the Ghost Tool by initials, and then asks BLUE / INDIGO / VIOLET — explicitly, by name — for "Meets Expectations, Keeps Head Down" and for the freedom to keep iterating. The half-serious dy/dx request is positioned as a personal preference about how he would like to be measured, not as a deliverable he is grading himself against. The reader is being set up to find a binder that supports an unflashy ask.

### Binder frame as currently installed

The six chapters install a substantially larger frame: a four-objective institutional case, anchored by a self-assigned "Objective Zero" architectural deliverable, supported throughout by peer-reviewed citation apparatus, quantitative outcomes tables, federal-compliance context, and repeated explicit claims that what was delivered "exceeded specification," "operates at the level above," and constitutes "infrastructure of lasting institutional value." The dy/dx motif is reframed from a personal request into a rubric design specification applied across the program. Across the chapters the reader is repeatedly told they are looking at "the restaurant," not a scenario; at architecture, not coursework; at a framework positioned for institutional reuse and adjacent-program adoption. The binder, as currently installed, is the evidence base for an Exceeds-Expectations claim — not for the Meets-Expectations-Keeps-Head-Down ask the anchor makes.

---

## Per-chapter frame map

> Reading lens: The author is asking BLUE/INDIGO/VIOLET to rate him "Meets Expectations, Keeps Head Down" on a three-item, originally-modest set of objectives and is — half-jokingly, half-seriously — asking to be evaluated on dy/dx so he can keep being allowed to try things.

| Source | Frame installed (one sentence) | Installation mechanism (specific sentences/devices) | Reader's likely state |
|---|---|---|---|
| `user_stories.md` | "I quietly overdelivered on three modest asks; please rate me Meets-Expectations and let me keep tinkering." | Lowercase "The actual requirements" header; PMP aside in parentheses; original objectives stated as small numeric counts; explicit "I humbly appreciate the opportunity to 'show my work,' and respectfully request 'Meets Expectations, Keeps Head Down'"; "Anything that lets me keep trying things until they work"; clearance-color in-jokes addressed to peer GREENs; sign-off "[REDACTED] and Teacherbot." | Reads a colleague's understated personal note; expects to find a thorough binder backing a modest ask. |
| `01_Introduction` | This binder documents an architect operating one level above the course-delivery role he was hired into. | "Three completed performance objectives… and a fourth objective that was not, strictly speaking, assigned"; Objective Zero introduced as "the architecture" the other three operate inside; two-reading-paths device; dy/dx framed as "rubric design specification, applied consistently across all three objectives"; closing claim "What was delivered exceeded that specification." | Reads a thesis statement for an institutional case; expects to evaluate whether a higher-order claim is substantiated. |
| `02_Executive_Summary` | Three objectives achieved plus a fourth self-assigned architectural objective; you are looking at the restaurant, not the menu. | Headline declares "meet or exceed the stated criteria" and reframes the deliverable as "the infrastructure that makes effective course delivery possible, replicable, and measurable"; thirteen-row metrics table including "Dilts neurological levels addressed (6 of 6)"; "Sauce & Spoon… What was built here is the restaurant" set off as its own bolded section; bottom-line "operates at the level above." | Reads a one-page brief signaling substantially-above-expectations; primed to look for evidence of an Exceeds rating. |
| `03_Objective_1` | A peer-reviewed-literature-grade cross-departmental framework was specified, built, validated, and is now reusable institutional infrastructure. | NACE / WEF / Burning Glass / Performamatics / Georgia Tech / Mahnič citation stack before any course detail; "Why Informal Coordination Had Already Failed"; deliverables labeled "Deliverable 1/2/3"; quantitative outcomes (5/5, 100%, 87/100); "Institutional Value: Infrastructure, Not Just Outcome"; closing "Objective not merely met, but exceeded — with infrastructure of lasting institutional value." | Reads a published program-design case study; expects to weigh institutional reuse value, not three meetings attended. |
| `04_Objective_2` | A transferable, theory-grounded, multi-course pedagogical framework was built where four assignments were asked for. | Garousi / Stack Overflow / Octoverse / JetBrains-GitKraken / Shulman / Lave-Wenger / Sadowski / Bacchelli-Bird / SmartBear / Indriasari / McDowell citations; "Sacred Workflow" elevated to proper-noun framework with "Five Commitments"; nine-row quantitative outcomes table; student-retrospective pull quotes; cross-course adoption table (CSC 289 / CTS 285 / CSC 151); "Minimum compliance produces four assignments. What was delivered is a transferable pedagogical framework grounded in peer-reviewed research." | Reads an SoTL-style write-up; expects to assess a curriculum innovation, not four uploaded assignments. |
| `05_Objective_3` | A team-credited project-management contribution to a federally-aligned institutional fraud-detection tool — the contributor scaffolded process discipline, the dev team shipped the artifact. | SMART-goal block; "Development Team" section names HS, MM, BS, DT with explicit "Full credit for the technical delivery"; six subsections of cited threat evidence (Melvin $4.7M, DOE OIG $350M, VCCS, Santiago Canyon, DCCC, federal mandates); Contribution Summary four-quadrant table; closing positions FTCC "ahead of the NC Community College System's current posture." | Reads a cross-functional project ship report with federal-compliance stakes; expects to evaluate institutional risk reduction, not three meetings. |
| `06_Performance_Objective_Zero` | The author also designed and built the entire instructional environment the other three objectives run inside — and is naming that fact for the record. | Title "Performance Objective Zero"; clearance distribution table aimed at BLUE/INDIGO/VIOLET/ULTRAVIOLET; ULTRAVIOLET-adjacent notation block ("The Algorithm approves. The Algorithm, in this context, is you"); Dilts six-level table scoring Standard Delivery 2 of 6 vs AlgoCratic Futures 6 of 6; Dweck / Edmondson / Lave-Wenger / Poole-Dayan citation backing; "What was built here is the restaurant" reprise; closing "Objective not merely met or exceeded, but operating at a level the original specification did not anticipate." | Reads a manifesto for a self-assigned architectural objective; expects to decide whether to credit the author with work at a level above his job description. |

---

## High-severity findings (auto-spawned as follow-up issues)

Sites consolidated where the same drift mechanism appears at multiple locations. Each entry below becomes one follow-up GitHub issue.

### Finding HF-1 — "Objective Zero" as a fourth performance objective the anchor never authorizes

- **Locations:** `inputs/01_Introduction.md:12-14`, `inputs/02_Executive_Summary.md:48`, `inputs/06_Performance_Objective_Zero.md:1` (chapter title)
- **Type:** reframing-attempt, structural-support
- **Frame currently installed:** A fourth, self-assigned architectural performance objective parallel in standing to the three formally assigned ones; the binder's thesis.
- **Frame user_stories.md would install:** Three objectives. The anchor names "Jeepform-style instructional 'simulated workplace'" as the *delivery mechanism* for Obj2's four assignments ("the assignments were delivered, but were disguised as portions of a game") — the simulation IS Obj2's substrate, not a separate objective.
- **Proposed reframe:** Retitle chapter 06 from "Performance Objective Zero" to a methodology / appendix designation (e.g., "Background: The Instructional Environment These Objectives Were Delivered Inside"); rewrite the 01 and 02 mentions to position the simulation as supporting context, not a fourth deliverable. The lever is the word "Objective."
- **Quoted prose:** > "The fourth objective — labeled here as Objective Zero — is the design and construction of the instructional environment inside which the other three operate." (01:14)
- **Follow-up issue:** #33

### Finding HF-2 — dy/dx reframed from personal request to program-wide rubric specification

- **Locations:** `inputs/01_Introduction.md:37`
- **Type:** reframing-attempt, structural-support
- **Frame currently installed:** dy/dx is "a rubric design specification, applied consistently across all three objectives and operationalized in the supporting infrastructure."
- **Frame user_stories.md would install:** dy/dx is the author's personal request about how he wishes to be measured (line 15: "I request to be measured expectations-wise by dx/dy, if this is feasible").
- **Proposed reframe:** Recast dy/dx in the introduction as a personal evaluation preference (a request to BLUE/INDIGO/VIOLET), not a program-wide rubric architecture applied to students.
- **Quoted prose:** > "This is not a metaphor. It is a rubric design specification, applied consistently across all three objectives and operationalized in the supporting infrastructure."
- **Follow-up issue:** #34

### Finding HF-3 — "Exceeded specification" / "operates at the level above" bottom-line framing

- **Locations:** `inputs/01_Introduction.md:51`, `inputs/02_Executive_Summary.md:10`, `inputs/02_Executive_Summary.md:54`, `inputs/06_Performance_Objective_Zero.md:179-194`
- **Type:** reframing-attempt, structural-support
- **Frame currently installed:** The deliverable specified was effective course delivery; the deliverable built was the infrastructure that makes effective course delivery possible, replicable, and measurable; the work operates "at the level above."
- **Frame user_stories.md would install:** Three asks were met; an additional thing got built because building it was easier than not.
- **Proposed reframe:** Replace the multi-site Exceeds / level-above framing with anchor-consistent Meets language across 01, 02, and 06; the "level above" / "different level" / "different order" / "different artifact" lexicon is the Milton-model trio doing most of the framing work. Cut consistently.
- **Quoted prose:** > "The original performance objectives were written for a course delivery role. The work documented here operates at the level above — the level at which the conditions for effective course delivery are designed, built, instrumented, and made replicable." (02:54)
- **Follow-up issue:** #35

### Finding HF-4 — Sauce & Spoon / "What was built here is the restaurant" comparison

- **Locations:** `inputs/02_Executive_Summary.md:34-36`, `inputs/06_Performance_Objective_Zero.md:36-40`
- **Type:** reframing-attempt, structural-support
- **Frame currently installed:** The author is not running Google's PM scenario; he built a peer artifact to it. "What was built here is the restaurant."
- **Frame user_stories.md would install:** The author taught classes and had fun with the in-character framing; he is not auditioning against Google's PM certificate machinery.
- **Proposed reframe:** Strike both Sauce & Spoon comparison sites wholesale. The comparison installs a frame the anchor does not authorize and re-installs it at two of the binder's most visible positions (ExecSum and ObjZero conclusion).
- **Quoted prose:** > "What was built here is not a scenario someone else designed. **What was built here is the restaurant.** The work of designing the simulation is a fundamentally different order of labor from working within one…" (06:40)
- **Follow-up issue:** #36

### Finding HF-5 — Dilts 6/6 self-score appearing as outcome metric

- **Locations:** `inputs/02_Executive_Summary.md:30` (ExecSum metrics table row), `inputs/06_Performance_Objective_Zero.md:80-88` (the table being summarized)
- **Type:** reframing-attempt, factual-omission
- **Frame currently installed:** Standard Delivery scores 2 of 6 on Dilts' Neurological Levels; AlgoCratic Futures scores 6 of 6 — presented as an objective measurement on equal footing with PR linkage rates and ship dates.
- **Frame user_stories.md would install:** Not asserted; the author found the in-character framing useful but does not score himself against Dilts.
- **Proposed reframe:** Remove the "Dilts neurological levels addressed: 6 of 6" row from the ExecSum table; in the chapter, relabel the comparison as author self-assessment ("self-assessed against Dilts' six-level framework") rather than as a measured outcome. Self-graded scores in a performance review binder structurally are a self-graded rubric.
- **Quoted prose:** > "| Dilts neurological levels addressed by the framework (Obj. 0) | 6 of 6 |" (02:30)
- **Follow-up issue:** #37

### Finding HF-6 — Per-chapter "exceeded" closing assessments

- **Locations:** `inputs/03_Objective_1_*.md:206`, `inputs/04_Objective_2_*.md:191`, `inputs/04_Objective_2_*.md:194-195`
- **Type:** reframing-attempt, structural-support
- **Frame currently installed:** Each objective chapter closes with "Objective not merely met, but exceeded — with infrastructure of lasting institutional value" or analogue ("That is not minimum performance. That is the work a department does when it takes industry alignment seriously").
- **Frame user_stories.md would install:** Each original objective was met. Reusable artifacts produced as byproducts are available if anyone wants them.
- **Proposed reframe:** Rewrite each chapter's closing assessment to anchor-consistent Meets language. The pattern across 03 and 04 is a single drift mechanism appearing in two locations — fix as one PR.
- **Quoted prose:** > "**Assessment:** Objective not merely met, but exceeded — with infrastructure of lasting institutional value." (03:206)
- **Follow-up issue:** #38

### Finding HF-7 — Citation-stack openers (NACE/WEF/Burning Glass; Garousi/Stack Overflow)

- **Locations:** `inputs/03_Objective_1_*.md:25-31`, `inputs/04_Objective_2_*.md:30-34`
- **Type:** reframing-attempt, structural-support
- **Frame currently installed:** Each chapter opens with a peer-reviewed-literature citation stack establishing a decade of research consensus that this objective addresses.
- **Frame user_stories.md would install:** Three meetings; four assignments. The anchor invokes no peer-reviewed apparatus.
- **Proposed reframe:** Compress citation stacks to one sentence of context each; demote out of lead position. The citation volume converts a three-meeting protocol and four assignments into SoTL-grade institutional cases.
- **Quoted prose:** > "Garousi et al.'s 2020 systematic review in *IEEE Software*, synthesizing 33 empirical studies across 12 countries and more than 4,000 data points…" (04:30)
- **Follow-up issue:** #39

### Finding HF-8 — "Sacred Workflow" elevated to Shulman/Lave-Wenger signature pedagogy

- **Locations:** `inputs/04_Objective_2_*.md:50-56`
- **Type:** reframing-attempt
- **Frame currently installed:** "Sacred Workflow" is a Shulman-grade signature pedagogy / Lave-Wenger community-of-practice induction mechanism.
- **Frame user_stories.md would install:** "Sacred Workflow" is the author's tongue-in-cheek name for `Issue → Branch → PR → Review → Merge`; the in-character framing is the joke, not a pedagogical-theory citation target.
- **Proposed reframe:** Keep the workflow; cut or radically compress the Shulman/Lave-Wenger framing. The citation apparatus converts a named git ritual into a "signature pedagogy" and that conversion is the reframe.
- **Quoted prose:** > "Lee Shulman's foundational work on **signature pedagogies**… The Sacred Workflow operationalizes this principle… This is precisely the mechanism Lave and Wenger describe in *Situated Learning* (1991)…"
- **Follow-up issue:** #40

### Finding HF-9 — Institutional-rollout framing ("Template for Adjacent Collaborations" / cross-curriculum adoption table)

- **Locations:** `inputs/03_Objective_1_*.md:162-180`, `inputs/04_Objective_2_*.md:160-183`
- **Type:** reframing-attempt
- **Frame currently installed:** The protocols and modules are "reusable institutional infrastructure," now available as templates for adjacent program pairings and queued for cross-curriculum adoption.
- **Frame user_stories.md would install:** The author would happily share GitHub links with another GREEN who asks; he is not pitching templates for institutional rollout.
- **Proposed reframe:** Cut "Institutional Value: Infrastructure, Not Just Outcome" and "A Template for Adjacent Collaborations"; recast the cross-course adoption table as "available on request if other faculty want to try this." Peer offer, not institutional rollout. Same fix shape in both chapters.
- **Quoted prose:** > "The structured collaboration approach is now available as a model for other cross-departmental pairings the institution may pursue: Web Development + Graphic Design partnerships; Database courses + Business Analytics integration; Mobile Development + User Experience research." (03:175)
- **Follow-up issue:** #41

### Finding HF-10 — ExecSum metrics table: per-row unsourced quantitative claims

- **Locations:** `inputs/02_Executive_Summary.md:16-30`
- **Type:** factual-omission
- **Frame currently installed:** Thirteen-row metrics table signaling substantially-above-expectations outcome.
- **Frame user_stories.md would install:** The anchor asserts no quantitative outcomes; the small ask doesn't require them. Imported metrics must each be backed by a locatable artifact.
- **Proposed reframe:** For every numeric row, either (a) name the source artifact in-line, or (b) cut the row. Rows requiring sourcing: 5/5 capstone pairings (roster?); 100% milestone completion (milestone log?); 87/100 collab rubric average (graded rubrics?); 100% Sprint-2 issue-first (artifact?); 95% PR-to-issue linkage (GH org export?); 89% merge-conflict-self-resolution (log?); zero Git work loss (counted how?); 85/100 peer review average (graded rubrics?); ~12,000 records (registrar export?). The Dilts row is covered by HF-5.
- **Quoted prose:** > thirteen-row table at lines 16-30
- **Follow-up issue:** #42

### Finding HF-11 — Per-chapter outcome metrics in Obj1 / Obj2: unsourced numeric and qualitative claims

- **Locations:** `inputs/03_Objective_1_*.md:144-149`, `inputs/03_Objective_1_*.md:151-156`, `inputs/04_Objective_2_*.md:132-142`, `inputs/04_Objective_2_*.md:148-156`
- **Type:** factual-omission
- **Frame currently installed:** Quantitative outcomes and qualitative student-retrospective pull-quotes presented as evidence of framework effectiveness.
- **Frame user_stories.md would install:** Not asserted.
- **Proposed reframe:** Per numeric row, name the source artifact (GH org export, rubric file path, gradebook, survey). Per qualitative quote, name the source (survey, retrospective, exit ticket) or attribute as paraphrase. "2.3 days average PR cycle time" particularly precise — what tool generated this?
- **Quoted prose:** > "Average issue completeness score: 92/100 / PRs properly linked to issues: 95% / … / Average PR cycle time (create → merge): 2.3 days" (04:132-142)
- **Follow-up issue:** #43

### Finding HF-12 — Original objectives baseline absent from each chapter

- **Locations:** `inputs/01_Introduction.md:12` (collectively), `inputs/03_Objective_1_*.md:5-16`, `inputs/04_Objective_2_*.md:10-20`, `inputs/05_Objective_3_*.md:10-25`
- **Type:** factual-omission
- **Frame currently installed:** Each chapter opens with a reformulated "Purpose / Requirements" / SMART-goal restatement of the objective in the author's voice.
- **Frame user_stories.md would install:** Each chapter should name the literal original objective text as the baseline before any reformulation: "Meet three times with cross-department students for assignments" (Obj1); "Four assignments covering the topic 'GitHub collaboration and version control with your team'" (Obj2); "attend three meetings towards planning Ghost Tool delivery timetable" (Obj3).
- **Proposed reframe:** Insert the literal original-objective quotation at the top of each chapter's Objective Statement block, before any restatement or "Purpose / Requirements" reformulation. One PR, four insertions.
- **Quoted prose:** > absent — the literal baseline is missing from all four chapters
- **Follow-up issue:** #44

### Finding HF-13 — Obj3 team-credit: voice + DT="team lead" misattribution

- **Locations:** `inputs/02_Executive_Summary.md:46`, `inputs/05_Objective_3_*.md:31-38`
- **Type:** factual-omission, structural-support
- **Frame currently installed:** HS / MM / BS / DT named in one section; DT labeled "team lead"; rest of chapter narrates in first-person PM voice. The explicit "Full credit for the technical delivery" line is calibrated, but the surrounding voice / role-descriptor structure undercuts it.
- **Frame user_stories.md would install:** TEAM objective. "Entire [Ghost Tool] delivered by dev team (special thanks to HS, MM)… user specifically thanks Chair (DT) for his collaboration." A Chair the author thanks for collaboration is the author's supervisor or peer; "team lead" reframes DT as reporting into the author's PM contribution.
- **Proposed reframe:** Change DT's role descriptor from "team lead" to "Chair" (or anchor's exact "Chair (DT)") in both ExecSum and 05; restructure the Obj3 chapter spine so the dev team's delivery is the primary narrative voice and PM contribution is the subordinate clause. Same fix shape in both locations.
- **Quoted prose:** > "lead developers **HS** and **MM**, supporting developer **BS**, team lead **DT**" (05) vs anchor's "user specifically thanks Chair (DT) for his collaboration"
- **Follow-up issue:** #45

### Finding HF-14 — FTCC positioned ahead of NC Community College System

- **Locations:** `inputs/05_Objective_3_*.md:121`
- **Type:** reframing-attempt, structural-support
- **Frame currently installed:** Deploying the detection tooling "places FTCC ahead of the NC Community College System's current posture."
- **Frame user_stories.md would install:** The author attended three meetings on Ghost Tool delivery; benchmarking FTCC against NCCCS on his behalf is not in the anchor.
- **Proposed reframe:** Cut the "places FTCC ahead of the NCCCS posture" clause. If FTCC is now ahead of NCCCS, that's the dev team's institutional impact, not the PM contribution being reviewed here.
- **Quoted prose:** > "Deploying detection tooling places FTCC ahead of the NC Community College System's current posture — which research indicates **has not yet adopted** the AI-powered screening, identity verification, or system-wide fraud prevention frameworks deployed by peer systems in Virginia, California, and Pennsylvania…"
- **Follow-up issue:** #46

### Finding HF-15 — Federal-compliance threat-evidence section overscales the work

- **Locations:** `inputs/05_Objective_3_*.md:42-84`
- **Type:** reframing-attempt, structural-support
- **Frame currently installed:** Six-subsection cited threat brief (Melvin $4.7M, DOE OIG $350M, VCCS, Santiago Canyon, DCCC, federal mandates) frames the chapter as federal-compliance-grade institutional risk reduction.
- **Frame user_stories.md would install:** Three meetings. The anchor does not invoke federal compliance, regional fraud cases, or peer-institution metrics for *this objective*.
- **Proposed reframe:** Relocate the threat-evidence section to a tool-context appendix. The substantiating territory for the PM contribution is the meeting log, not DOJ press releases. Compress the in-chapter mention to one paragraph naming the regional threat and federal compliance timeline.
- **Quoted prose:** > "### The regional threat is severe and actively prosecuted … ### The national scale dwarfs individual cases … ### Community colleges are the primary target … ### FTCC's home region is specifically implicated … ### Peer institutions that deployed detection tools saw dramatic results … ### Federal mandates now require action"
- **Follow-up issue:** #47

### Finding HF-16 — ULTRAVIOLET-adjacent block: peer register at admin + AI-collaborator disclosure of load-bearing claims

- **Locations:** `inputs/06_Performance_Objective_Zero.md:11-30`
- **Type:** reframing-attempt, structural-support
- **Frame currently installed:** Clearance distribution table aimed at BLUE/INDIGO/VIOLET/ULTRAVIOLET, plus a notation block crediting an AI collaborator with "load-bearing pedagogical infrastructure" claims (recursive footnotes, velocity-chart framing, dy/dx-as-spec) and closing "The Algorithm approves. The Algorithm, in this context, is you."
- **Frame user_stories.md would install:** The anchor's clearance-color in-jokes are addressed to fellow GREENs ("Hello to anyone reading this. If you're a fellow GREEN…"), not weaponized at BLUE/INDIGO/VIOLET as a co-signing flourish. The anchor does not invoke an AI collaborator.
- **Proposed reframe:** Two distinct problems sharing a site. (a) The peer-conspiratorial register pointedly does not extend to admin in the anchor — drop or relocate to a peer-facing appendix. (b) The AI-collaborator disclosure assigns authorship of load-bearing claims (notably the dy/dx-as-rubric-specification claim, see HF-2) to an entity the reviewer cannot interrogate — either relocate earlier in the binder where it can be evaluated, or cut.
- **Quoted prose:** > "Contributions include: … the argument that measuring dy/dx instead of y is not a metaphor — it is a rubric design specification… **The Algorithm is aware. The Algorithm approves. The Algorithm, in this context, is you.**"
- **Follow-up issue:** #48

---

## Backlog (med / low severity, not auto-spawned)

These are listed for the user's reference. Each is logged in the audit but does not get its own follow-up issue. Many will be naturally absorbed when the high-severity sites are reframed.

- **`01_Introduction.md:45`** (med) — "Load-bearing pedagogy" phrasing for the in-character apparatus. Soften to "the operating vocabulary of the course"; keep the citation stack where Objective Zero earns it.
- **`01_Introduction.md:14`** (med) — Architecture/rooms metaphor inverts what was asked for and what was added.
- **`03_Objective_1_*.md:37-48`** (med) — "Why Informal Coordination Had Already Failed" frames prior status quo as structurally deficient. Will likely fold into HF-7 (citation-stack compression).
- **`05_Objective_3_*.md:93`** (med) — "Advocated for and established Scrum methodology and GitHub-based version control as non-optional project standards for the team" — phrasing claims authority over a team the author is also crediting elsewhere.
- **`06_Performance_Objective_Zero.md:170-171`** (med) — "Building at a different level — the level at which the conditions for effective course delivery are created." Will fold into HF-3 (level-above cleanup).
- **`06_Performance_Objective_Zero.md:194`** (med) — "This is not that" / "different job / different skill set / different institutional artifact" cadence. Closely related to HF-4 (Sauce & Spoon); may absorb when HF-4 is fixed.
- **`06_Performance_Objective_Zero.md:155-159`** (med) — Showcase project list (financial aid tracker, recommendation engine, biometrics, task manager, DataMan); mostly anchored, but the specific roster is unsourced.
- **`05_Objective_3_*.md:30-38`** (low — positive note) — The explicit "Full credit for the technical delivery belongs to the development team" sentence is already calibrated. Flagged to confirm it is doing the right work. Will be reinforced by HF-13.

---

## Bottom-line read

The binder, as it currently stands, installs a frame that is in direct opposition to the one the anchor installs. The anchor asks for **Meets Expectations, Keeps Head Down**, measured by dy/dx, on three originally-modest line items the author quietly overdelivered on — and credits the dev team for the third. The binder makes the evidentiary case for an **Exceeds Expectations** outcome, by way of a self-assigned fourth performance objective, a peer-reviewed-literature citation apparatus, quantitative-outcome tables that import metrics the chapters do not source, a recurring "different order of labor / level above / what was built here is the restaurant" lexicon, and a closing structure that calls each objective "not merely met, but exceeded." The dy/dx motif is reframed mid-binder from a personal measurement preference into a program-wide rubric specification the author has applied at scale. The team-credit chapter (Obj3) does the most aligned work — its explicit "Full credit for the technical delivery" sentence is correctly calibrated — but the surrounding voice, the relabeling of the Chair as "team lead," and the institutional-positioning closer pull the chapter back toward the binder's general Exceeds frame.

The cognitohazard mentioned in `CLAUDE.md` is directly visible in the result of this audit: a confident, internally consistent, peer-reviewed-cited document built on the meta-recursion of a performance review documenting a performance review is precisely the kind of artifact that can entrain a reviewer (or an LLM) toward the binder's installed frame and away from the anchor's. The audit's job has been to break that entrainment, name the installation sites, and put the user in a position to decide per-site how to respond. The follow-up issues are that triage surface.
