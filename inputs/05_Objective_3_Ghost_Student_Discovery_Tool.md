# Objective 3: Ghost Student Discovery Tool

**Employee:** [REDACTED]
**Department:** Computer & Information Technology / Programming — Platform Team
**Review Period:** Spring 2026
**Classification:** Special Project Contribution (Cross-Functional)

---

## Objective Statement

**Original objective (verbatim):** "attend three meetings towards planning Ghost Tool delivery timetable."

-----

## SMART Goal (reformulation)

**Specific:** Support the CPD Tools Group development team's delivery of the Ghost Student Discovery Tool — an internal fraud detection utility targeting fraudulent enrollment and financial aid abuse — by providing project management, gathering and documenting customer requirements from stakeholder departments, identifying and resolving planning and technical obstacles during the development cycle, and reinforcing the team's Scrum/GitHub workflow discipline as a non-optional project standard.

**Measurable:** The tool shipped in May 2026. Four discrete contribution areas were verified by the development team:

1. Project management support — planning, milestone tracking, and obstacle resolution
2. Agile/Scrum mentoring and establishment of a GitHub-based workflow as the development standard
3. Customer requirements gathering from institutional stakeholders
4. Documentation — user-facing materials and configuration documentation

**Achievable:** This objective fell within the scope of the Platform Team's mission to provide enabling tooling and process infrastructure across the institution. The contributor operated in a supporting project management capacity alongside the development team, consistent with the Team Topologies "platform team" model already adopted by the department.

**Relevant:** The Ghost Student Discovery Tool directly addresses a documented institutional and systemic risk. The evidence below establishes both the severity of the threat in our region and the alignment of this tool with federal, state, and industry responses to the crisis.

**Time-Bound:** The tool shipped May 2026, coinciding with the federal compliance timeline established by the U.S. Department of Education's mid-2025 identity verification mandates and ahead of the Fall 2026 enrollment cycle.

---

## Development Team

The Ghost Student Discovery Tool was designed, built, tested, and shipped by the CPD Tools Group development team:

- **HS** and **MM** — lead developers; primary design, implementation, and ship-readiness work.
- **BS** — supporting developer.
- **Chair (DT)** — Chair; thanked by the contributor for his collaboration on the project.
- **[REDACTED]** (the contributor documented here) — project management support, as detailed in the Contribution Summary below.

Full credit for the technical delivery belongs to the development team; the objective documented here covers the project-management, requirements, and process-discipline scaffolding that ran alongside their work.

---

## Supporting Evidence: Why This Tool Matters

The regional threat is concrete: the Melvin prosecution (sentenced June 2025) named FTCC among the NC community colleges targeted by a $4.7M fraudulent financial aid scheme operated from Fayetteville. The federal compliance timeline is the U.S. Department of Education's Summer 2025 identity verification mandate for flagged FAFSA applicants at Title IV institutions, with a permanent centralized screening process launched for Fall 2025. The Ghost Tool's May 2026 ship date is aligned with that timeline. Full threat brief (regional cases, national OIG figures, community-college targeting analysis, peer-institution deployment outcomes, federal mandate detail) relocated — see fenced block at end of chapter.

---

## Contribution Summary

| Contribution Area | Description | Impact |
|---|---|---|
| **Project Management Support** | Coordinated planning, milestone tracking, and obstacle resolution across the development cycle; surfaced and helped resolve cross-team blockers; maintained brief-and-feedback cadences modeled on the Sprint-review patterns codified in Objectives 1 and 2. | Kept the project on track for a May 2026 ship date aligned with federal compliance timelines and ahead of Fall 2026 enrollment. |
| **Agile/Scrum Mentoring** | Advocated for and established Scrum methodology and GitHub-based version control, issue tracking, and pull-request workflows as non-optional project standards for the team — the same Sacred Workflow taught in CSC 289 (Objective 2), now applied to a live institutional project. | Provided the process discipline necessary for a cross-functional tool with institutional compliance implications, consistent with AACRAO guidance recommending structured workflows for fraud prevention teams. |
| **Requirements Gathering** | Collected and documented customer requirements from institutional stakeholders (Student Services, financial aid, admissions, registrar, IT). Translated stakeholder-observed fraud patterns — shared phone numbers across applicants, mismatched and out-of-state addresses, synthetic email constructions, target-program concentration — into structured signal categories handed to the development team as action items. | All requested detection signals shipped as implemented capabilities in the May 2026 release. |
| **Documentation** | Produced and maintained user-facing materials for non-technical Student Services staff and configuration documentation for IT; sustained brief artifacts and stakeholder communications across iteration cycles. | Reduced onboarding friction for downstream users and produced reusable documentation artifacts for the team's continued refinement and for any future similar engagements. |

---

## Tool Capabilities

Delivered by the development team (lead developers **HS** and **MM**, supporting developer **BS**, with **Chair (DT)**); summarized here for binder context. Full technical credit belongs to the team.

- Composite-signal duplicate detection across names, addresses, emails, and phone numbers.
- Configurable sensitivity thresholds with weighted confidence scoring.
- Flagged-record reporting with field-level match breakdown for staff review.

---

## Outcomes

- Tool operational and in use by Student Services for ongoing enrollment-cycle screening.
- Manual review burden reduced from ~12,000 records to a tractable flagged subset.
- Stakeholder validation: Student Services confirmed the tool's signal set — phone, address, program-placement, and email-design patterns — matches the patterns they encounter operationally (25–40 suspected applications per average week, hundreds at peak two weeks before first day of class).
- Requirements and documentation artifacts available for the team's continued refinement and for any future similar engagements.
- The engagement served as a live application of the curriculum methodology outside the classroom — the same briefing, milestone, and feedback patterns used in CSC 289 operating in a cross-stakeholder institutional context.

---

## Alignment with Institutional Mission

The Ghost Student Discovery Tool directly protects FTCC's ability to serve legitimate students by reducing enrollment fraud, safeguarding federal financial aid eligibility, and closing vulnerabilities that have already been exploited in documented, prosecuted cases targeting this institution. The tool aligns with the U.S. Department of Education's escalating enforcement posture.

---

*Evidence compiled from federal court records, DOJ press releases, DOE/OIG reports, investigative journalism (ABC News, ABC11, Fortune, WJLA), and higher education industry sources (EDUCAUSE Review, AACRAO, IntelliBoard, EdSource). Full research brief available on request.*

---

`[RELOCATED PER HF-15: belongs in tool-context appendix that does not yet exist]`

```
### The regional threat is severe and actively prosecuted

The largest ghost student fraud prosecution in North Carolina history was sentenced in June 2025 — a Fayetteville-based scheme that generated over **$4.7 million in fraudulent financial aid awards** across multiple NC community colleges, including FTCC, Wake Tech, and Cape Fear CC. The perpetrator recruited approximately 80 individuals whose identities were used to submit fraudulent admissions applications and FAFSAs. Over $3.5 million was actually disbursed before the scheme was detected.
*(Sources: CBS17, June 2025; DOJ Eastern District of NC press releases; ABC11 Raleigh-Durham, January 2026)*

A second NC prosecution involved a Clayton man sentenced to 53 months for stealing over $400,000 using stolen identities at multiple colleges. A third case — a Cumberland County woman — involved fabricated high school transcripts used to enroll unqualified individuals in Wake Tech online programs.
*(Sources: DOJ EDNC, January 2023; DOJ EDNC, Cumberland County indictment)*

The U.S. Attorney for the Eastern District of NC confirmed in January 2026 that **multiple additional investigations remain active** in the district.
*(Source: ABC11, January 2026)*

### The national scale dwarfs individual cases

The Department of Education's Office of Inspector General maintains **more than 200 open investigations** into ghost student schemes nationally, with investigated fraud exceeding **$350 million** over five years — a figure OIG officials describe as a fraction of the true total. In 2025, the DOE reported preventing **$1 billion** in fraudulent student loan payments after enhanced screening flagged approximately 150,000 suspect identities in a single week.
*(Sources: WJLA I-Team investigation, 2025; U.S. Department of Education press releases, June 2025)*

### Community colleges are the primary target

Ghost student schemes exploit structural features specific to community colleges: open-enrollment admissions with no application fees, low tuition that maximizes cash refunds from Pell Grants (up to ~$7,400/year), asynchronous online courses requiring no physical presence, and minimal identity verification at the point of enrollment. Automation has amplified the problem — one institution reported receiving 50 fraudulent applications within two seconds.
*(Sources: Carahsoft/HUMAN Security, 2025; AACRAO guidance document; IntelliBoard, 2025)*

### FTCC's home region is specifically implicated

The Melvin prosecution directly named **Fayetteville Technical Community College** as one of the victimized institutions. The perpetrator operated from Fayetteville and recruited straw students from the Cumberland County area. This is not an abstract or distant threat — it is a documented, prosecuted attack on this institution's enrollment and financial aid systems.
*(Sources: CBS17, June 2025; WECT, June 2025; Old North News, June 2025)*

### Peer institutions that deployed detection tools saw dramatic results

Schools that adopted AI-powered fraud screening and identity verification have documented transformative outcomes:

- **Virginia Community College System** reduced fraudulent applications from 15% of all submissions to under 1% after implementing ID verification in 2024.
- **Santiago Canyon College** (CA) detected and removed 8,000 fraudulent enrollments after deploying LightLeap.AI; the following semester, 7,500 real students reclaimed those seats.
- **Delaware County Community College** (PA) went from 500+ ghost students in 2023 to just 2 in 2025 after deploying the S.A.F.E. screening platform.
- Across 500,000+ applications processed by LightLeap, the tool identified **79,016 fraudulent submissions** — roughly twice the number caught by human staff alone.

*(Sources: EDUCAUSE Review, February 2025; EdSource, 2025; Fortune, July 2025; AMSA Connect, 2025)*

### Federal mandates now require action

Effective Summer 2025, the U.S. Department of Education implemented mandatory identity verification for flagged FAFSA applicants at all Title IV institutions, including photo ID requirements compliant with NIST IAL-2 standards. A permanent centralized screening process launched for Fall 2025, flagging approximately 300,000 applications for enhanced verification. The DOE also resumed cross-referencing student aid records against the Social Security Death Index, immediately identifying $30 million in aid previously disbursed to deceased individuals.
*(Sources: U.S. Department of Education press release, June 2025; FSA Partners electronic announcement, June 2025)*
```
