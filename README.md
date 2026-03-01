# Astrica Visual Novel — Project Repository
**Repo:** sKiDaGgAbAtEe/VN
**Phase:** 1 — Character Design & Art Provenance Complete

---

## What This Is

A visual novel centered on three characters: **Alex/Astrica** (celestial idol), **Rose** (chaos therapist), and **Skida** (field anchor). The story hasn't been written yet — this repo is the foundational art, ethics, and provenance scaffolding that everything else will be built on.

---

## Repository Structure

```
VN/
├── assets/
│   └── characters/
│       ├── alex/         # Alex sprites + _prov.yml files
│       ├── rose/         # Rose sprites + _prov.yml files
│       └── skida/        # Skida sprites + _prov.yml files
├── concept/
│   ├── alex/             # Internal concept art (source images)
│   ├── rose/             # Rose's original art + concept pieces
│   └── skida/            # Skida avatar references
├── ssad_cards/           # SSAD root cards (one per character)
├── provenance/
│   ├── master_artists.yml   # Public-domain artist lineage index
│   └── audit_log.md         # Running log of all provenance actions
└── docs/
    ├── ai_art_ethics_statement.md
    ├── character_sheet_alex.md
    ├── character_sheet_rose.md
    └── character_sheet_skida.md
```

---

## Art Ethics in One Paragraph

Every asset in this project has a provenance file (`_prov.yml`) that records how it was made, what references informed it, and who is responsible for it. We only cite public-domain artists as stylistic references (see `provenance/master_artists.yml`). AI tools are used as assistive instruments, not as invisible engines, and are never listed as contributors. Rose's original artwork is used with her explicit permission. Skida's likeness is used with his explicit consent. For the full policy, see `docs/ai_art_ethics_statement.md`.

---

## Characters

| Character | Role | SSAD Root |
|---|---|---|
| Alex / Astrica | Celestial idol, emotional anchor | SSAD-VN-ASTRICA-0001 |
| Rose | Chaos therapist, 4'10" powerhouse | SSAD-VN-ROSE-0001 |
| sKiDa / Skida | Field anchor, nurturing masculine | SSAD-VN-SKIDA-ROOT |

Character sheets: `docs/character_sheet_*.md`

---

## Phase 1 Status

- [x] Character designs: Alex, Rose, Skida
- [x] Outfit specifications: all primary + secondary outfits documented
- [x] SSAD root cards: all three characters
- [x] Provenance files: all specified assets
- [x] Master artist index: 9 public-domain entries
- [x] AI ethics statement
- [x] Audit log initialized

## Phase 2 — Next

- [ ] Repo file structure populated with actual image assets
- [ ] Expression sheets (6 expressions × 3 characters)
- [ ] Pending outfit sprites (suit, neon, scruffy, beach for Skida; everyday/astral for Alex; office/street for Rose)
- [ ] Background / environment art + provenance
- [ ] UI elements (dialogue box, nameplates, title screen)
- [ ] Engine setup (Ren'Py or web)
- [ ] Story bible — premise, routes, key scenes
- [ ] Lock the VN title

---

## Provenance Workflow

```
1. Define asset concept
2. Select style references from master_artists.yml
3. Generate / create asset
4. Draft _prov.yml with status: draft
5. Provenance Steward reviews ethics + lineage
6. Set status: approved
7. Log in provenance/audit_log.md
8. Integrate into build
```

Assets with `status: draft` are **not approved for final builds**.

---

*Built under the Micro-SSAD Art Provenance Protocol (Option A).*
