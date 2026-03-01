# Astrica VN — Ren'Py Engine Scaffold

## Overview

This folder contains the Ren'Py game scaffold for the Astrica Visual Novel.
It is a working skeleton — all characters wire up, all expressions are declared,
and the test scene runs. Backgrounds and audio are stubbed out pending art generation.

---

## Setup Instructions

### 1. Install Ren'Py

Download the Ren'Py SDK from https://www.renpy.org/latest.html

Recommended: **Ren'Py 8.x** (Python 3)

### 2. Point Ren'Py at this project

Open the Ren'Py launcher.
Click **"+ Create New Project"** — but instead of creating a blank project,
navigate to `C:\Users\kyuri\Visual Novel\VN\engine\` and point it there,
or use **"preferences"** to add this folder as a project location.

Alternatively: place the entire `engine/` folder contents where Ren'Py expects
a project (inside your Ren'Py projects directory), then open it from the launcher.

### 3. Run the test scene

Hit **Launch Project** in the Ren'Py launcher.
The test scene will cycle through all three characters and all expressions.
If a sprite image is missing, Ren'Py will show a red error — that just means
the art file hasn't been placed yet.

---

## File Map

```
engine/
└── game/
    ├── script.rpy       ← Entry point. label start: is here.
    ├── definitions.rpy  ← ALL characters, image aliases, audio declared here.
    ├── options.rpy      ← Window size, save directory, transitions.
    ├── gui.rpy          ← Colors, fonts, dialogue box layout.
    ├── screens.rpy      ← Main menu, save/load, preferences, history UI.
    └── images/          ← Art goes here (mirrors assets/characters/ structure)
        ├── alex/
        │   ├── alex_idol_v1.png         ← copy from assets/characters/alex/
        │   ├── alex_outfit_pjs_v1.png
        │   └── expressions/
        │       ├── alex_expr_01_v1.png
        │       └── ...
        ├── rose/
        │   └── (same pattern)
        └── skida/
            └── (same pattern)
```

---

## Adding New Scenes

Create a new `.rpy` file in `game/` for each chapter or scene cluster.
Example: `game/scene_chapter01.rpy`

Then route to it from `script.rpy`:
```renpy
label start:
    jump scene_chapter01
```

---

## Adding New Art

1. Place the `.png` in the correct `game/images/` subfolder
2. Declare the image alias in `definitions.rpy`
3. Use it in a scene with `show [character] [outfit] [expression]`

---

## Character In-Engine Reference

| Character | Outfit       | In-Engine Call                      |
|-----------|-------------|--------------------------------------|
| Alex      | idol        | `show alex idol neutral`             |
| Alex      | pjs         | `show alex pjs neutral`              |
| Alex      | snuggie     | `show alex snuggie neutral`          |
| Alex      | swim        | `show alex swim neutral`             |
| Rose      | sweater     | `show rose sweater neutral`          |
| Rose      | pjs         | `show rose pjs neutral`              |
| Rose      | business    | `show rose business neutral`         |
| Rose      | swim        | `show rose swim neutral`             |
| Skida     | shirt       | `show skida shirt neutral`           |
| Skida     | pjs         | `show skida pjs neutral`             |
| Skida     | hoodie      | `show skida hoodie neutral`          |

**Expression swap (no outfit change):**
```renpy
show alex happy
show rose smug
show skida tired
```

**Position shortcuts:**
```renpy
show alex idol neutral at left
show rose sweater neutral at center
show skida shirt neutral at right
```

---

## Expression Reference

### Alex
| ID | In-Engine | Description |
|----|-----------|-------------|
| 01 | `alex neutral`    | Listening, present, soft |
| 02 | `alex happy`      | Genuine warmth |
| 03 | `alex shy`        | Caught being seen |
| 04 | `alex determined` | She's decided |
| 05 | `alex sad`        | Quiet grief |
| 06 | `alex laughing`   | The real laugh |

### Rose
| ID | In-Engine | Description |
|----|-----------|-------------|
| 01 | `rose neutral`   | Knowing smirk |
| 02 | `rose happy`     | Rare genuine warmth |
| 03 | `rose smug`      | Called it |
| 04 | `rose concerned` | Therapist mode |
| 05 | `rose sad`       | Mask drops |
| 06 | `rose laughing`  | Gremlin cackle |

### Skida
| ID | In-Engine | Description |
|----|-----------|-------------|
| 01 | `skida neutral`   | I'm here |
| 02 | `skida warm`      | Quiet warmth |
| 03 | `skida focused`   | Locked in |
| 04 | `skida concerned` | Holding space |
| 05 | `skida tired`     | Weary grace |
| 06 | `skida laughing`  | Real laugh |
