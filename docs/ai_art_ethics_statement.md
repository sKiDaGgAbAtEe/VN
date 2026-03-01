# Visual Novel Art & AI Ethics Statement
## (Alex Line – Micro-SSAD Implementation)

---

### 1. Purpose

This document explains how art is sourced, referenced, and generated for this visual novel, with a specific focus on AI-assisted art and our treatment of historical and contemporary artists.

Our goals are:

- To honor human artists, past and present.
- To maintain transparent provenance for every asset.
- To ensure our use of AI art tools is conscious, traceable, and constrained by explicit ethical rules.

This statement is an extension of our Micro-SSAD (Soul-Stamped Artist Database) Protocol and applies in particular to the development of Alex's character art and any related assets.

---

### 2. What We Are Doing

For this project we have:

Created a Micro-SSAD provenance framework that requires every visual asset to have:
- A unique asset ID
- A clear description of origin mode (hand-drawn, AI-assisted, etc.)
- A lineage section documenting references and influences
- A Soulstamp block with contributor and intent metadata
- A license and review status

Established a Master Artist Index (`provenance/master_artists.yml`) listing only:
- Artists whose work is clearly in the public domain
- Representative stylistic lineages (e.g., Art Nouveau, Ukiyo-e) treated as conceptual references, not as sources to copy from

Built full provenance files for all characters that:
- Record internal concept art as explicit lineage
- Leave placeholder entries for public-domain style references from the Master Artist Index
- Document each transformation step from initial generation to final hand-polish

In short: no art appears in this VN without a paper trail.

---

### 3. Source Categories & Boundaries

#### 3.1 Allowed Sources

We consciously restrict ourselves to three categories:

**Public-Domain Historical Artists**

Artists such as Vincent van Gogh, Alphonse Mucha, Takehisa Yumeji, Kay Nielsen, James McNeill Whistler, Marc Chagall, Ukiyo-e composite lineages, Aubrey Beardsley, and John Singer Sargent — only via clearly public-domain works.

These are listed by ID in `master_artists.yml` with notes on how their work may be referenced.

**Open-Licensed Contemporary Works**

Only where the license explicitly allows derivative and commercial use (e.g., certain CC licenses with no "ND" restrictions). Any such use must be logged as a separate lineage entry specifying license terms.

**Original Concept Art & Soul-Stamped Assets**

Internal concept pieces created for this project. These form the primary foundation for character design. All such works are tagged with Soulstamp metadata and tracked as `internal_concept_art` in lineage.

#### 3.2 Disallowed Sources

We explicitly reject the following as inputs, prompts, or references:
- Unlicensed fanart
- Any artwork by a contemporary artist who has publicly opted out of AI use
- Images with unclear or unverifiable copyright status
- Scraped datasets with opaque provenance or unknown consent
- Direct copying of composition from any individual artwork, historical or modern

When in doubt, an asset or reference is treated as non-compliant until its status is verified and recorded.

---

### 4. How We Use AI Tools

AI image generators are treated as assistive tools, not invisible engines.

**Every AI-assisted asset is labeled as such.** `origin.mode` explicitly states "generated" with accompanying tools. A `transformations` section describes each step.

**Human authorship remains central.** Final lines, facial structure, and key motifs are hand-refined. The Soulstamp contributor is always a specific person/handle who takes responsibility for the resulting piece.

**We do not treat the model's training set as a moral shield.** Even if a model vendor claims legality of training, we still apply our own ethical filter, using only references we would be comfortable citing directly.

---

### 5. Treatment of Historical Artists

When referencing public-domain artists, we commit to:

- **Referencing feeling and structure, not copying.** Van Gogh → emotional sky movement and value contrast, not 1:1 composition. Mucha → halo framing and ornamental flow, not direct poster layouts.
- **Documenting each reference.** Each PD artist influence is recorded in the lineage section with `master_artist_id`, work or series title, and a short explanation of what was echoed.
- **Avoiding flattening or erasure.** Whenever we publicly discuss our art, we are willing to name the historical currents we drew from.

---

### 6. Treatment of Contemporary Artists

For living or recently active artists, we adopt a presumption of protection:
- We do not deliberately mimic the distinctive style of a single identifiable living artist.
- We do not use reference packs or datasets whose creator consent is unclear.
- If we later discover that a workflow inadvertently parallels a specific living artist's style, we will evaluate the similarity honestly, adjust designs and pipelines if necessary, and update provenance records.

**Our position is simple: human artists are not raw material. They are peers.**

---

### 7. Internal Concept Art & Soulstamp

Internal artworks are treated as primary canonical sources, not disposable drafts. Each internal piece is tagged in provenance as `internal_concept_art`.

**Rose's original artwork** is used with her explicit consent and full credit retained. She retains copyright over her original illustration.

**sKiDa's avatar references** are used with his explicit consent as the real-world subject of the Skida character.

---

### 8. Responsibility for Derivatives

When we generate or derive new art, we affirm:
- The ethical responsibility remains with us, not with the tool.
- If a player or external artist raises a concern about an asset's resemblance to their work, we will review the provenance record and compare compositions in good faith.
- We intentionally design our system so correction is possible: assets can be deprecated with notes in the review section.

---

### 9. Representation Philosophy

This VN is built on the principle of **female reverence and coherent representation**. We affirm:
- The human body is not inherently sexual or shameful to represent.
- Refraining from representing the body properly is equally as damaging as exploiting it.
- Characters are depicted as whole, autonomous people — not objects of consumption.
- "Coherently sexy" means self-possessed, adult, and intentional — not pornographic.
- Male characters reclaim nurturing, caregiving, and emotional presence as masculine strengths, not weaknesses.

---

### 10. Transparency & Player-Facing Summary

A concise player-facing summary:

> *"This visual novel uses AI-assisted art, but every asset is tracked. We only draw stylistic inspiration from public-domain art and our own concept work, and we avoid copying or exploiting living artists. If you ever see something that concerns you, you can point to it, and we can show you its paper trail."*

---

### 11. Future Revisions

This statement is a living document. Any significant change to this policy should be logged in version control with a clear commit message and reflected in updated provenance schemas when relevant.

---

*By combining clear provenance, limited and declared source pools, and Soul-stamped authorship, we aim to practice AI-assisted art in a way that respects the dead, protects the living, and leaves a traceable record for anyone who wishes to see how a given image came to be.*
