# Expression Sheet Specification
## Astrica Visual Novel — Phase 2

---

## Overview

Each character has 6 canonical expressions used as the primary sprite emotion states in-engine.
All expressions are bust/head-and-shoulders crops, transparent background, sized to match
the upper portion of the full-body sprites.

**Standard expression IDs follow this format:**
`char_[name]_expr_[id]_v1`

**In-engine reference format:**
`[Character].[expression_name]`

---

## Shared Technical Rules

- All expressions share the same head, hair, accessories, and clothing from the character's default sprite
- Only eyes, brows, mouth, and subtle cheek/lighting shift between expressions
- No outfit changes within an expression set (outfit is handled by the sprite layer)
- All expressions must read clearly at 1/3 scale (VN dialogue box portrait size)
- Transparent PNG, consistent crop and canvas size across all 6 per character

---

## Alex / Astrica — Expression Set

**Base face:** Large warm brown/gold eyes, soft nose, gentle mouth, star freckle under left eye.
**Accessories always present:** Halo (above head), crescent moon hair clip (right side), star scatter in bangs.
**Palette anchor:** Warm golden highlights in eyes, soft skin tone.

| ID | Expression Name | In-Engine Ref | Description |
|----|----------------|---------------|-------------|
| SSAD-VN-AX-EXPR-01 | Neutral | `Alex.neutral` | Soft, present, attentive. Eyes relaxed and open, slight natural lip curve. The "listening" face. |
| SSAD-VN-AX-EXPR-02 | Happy | `Alex.happy` | Eyes curved up (^-^ energy but not chibi), full smile, cheeks lightly flushed. Warmth that fills the room. |
| SSAD-VN-AX-EXPR-03 | Shy | `Alex.shy` | Eyes slightly averted or downcast, brows soft and drawn in, small embarrassed smile. Cheeks clearly flushed. The "I didn't think anyone noticed" look. |
| SSAD-VN-AX-EXPR-04 | Determined | `Alex.determined` | Eyes wide and direct, brows firm but not angry, mouth set in a quiet line or soft frown. Inner light metaphorically visible. "I'm going to carry this." |
| SSAD-VN-AX-EXPR-05 | Sad | `Alex.sad` | Eyes downcast, brows raised slightly at inner corners (the real sad shape), mouth soft and slightly parted. No tears required — the weight is in the eyes. |
| SSAD-VN-AX-EXPR-06 | Laughing | `Alex.laughing` | Eyes squeezed shut or nearly shut, mouth open in a real laugh, cheeks raised and rosy. Natural joy, not performed idol smile. |

**Alex expression notes:**
- Her halo should pulse or glow slightly brighter on Happy and Determined
- Her star freckle should always be visible (it's a canon non-negotiable)
- Avoid making Sad too weepy — Alex carries quietly, she doesn't perform grief
- Laughing should feel like a surprise, like she forgot she was allowed to

---

## Rose — Expression Set

**Base face:** Golden/amber catlike eyes, black rectangular glasses, sharp but warm features.
**Accessories always present:** Black rectangular glasses, black choker (on default expressions), red rose hair clip.
**Hair:** Black-to-blonde ombré, long, parted slightly.
**Palette anchor:** Deep amber-gold eyes glow behind dark frames.

| ID | Expression Name | In-Engine Ref | Description |
|----|----------------|---------------|-------------|
| SSAD-VN-ROSE-EXPR-01 | Neutral | `Rose.neutral` | Small knowing smirk. Eyes half-lidded and perceptive. "I already know what you're about to say." Calm authority. |
| SSAD-VN-ROSE-EXPR-02 | Happy | `Rose.happy` | Rare and genuine — eyes wider than usual, full warm smile. The glasses make it even more disarming. "Oh. This actually got me." |
| SSAD-VN-ROSE-EXPR-03 | Smug | `Rose.smug` | Classic gremlin. One brow raised, eyes lidded, corners of mouth pulled in a sharp satisfied smirk. "Called it." |
| SSAD-VN-ROSE-EXPR-04 | Concerned | `Rose.concerned` | Professional therapist face: brows slightly drawn, eyes soft and focused, mouth neutral or slightly pursed. "Tell me more." Not pitying — present. |
| SSAD-VN-ROSE-EXPR-05 | Sad | `Rose.sad` | The rare moment the mask drops. Eyes downcast, brows drawn together slightly, mouth pressed quietly. The "I'm fine" that obviously isn't. |
| SSAD-VN-ROSE-EXPR-06 | Laughing | `Rose.laughing` | Full genuine laugh — head tilted, eyes crinkled behind glasses, mouth open. The gremlin cackle finally let loose. |

**Rose expression notes:**
- Her "Neutral" IS her smirk — Rose doesn't really do blank faces
- Smug and Neutral sit close together; the difference is brow height and eye intensity
- Sad is the most powerful one to get right — it must feel like a privilege to see it
- Glasses should always catch a light reflection; it's part of her visual signature
- Choker stays on for all professional/default expressions; can be noted as optional for PJ expressions

---

## Skida — Expression Set

**Base face:** Soft almond-shaped blue eyes, straight nose, relaxed jaw, adult male proportions.
**Hair:** Deep blue/indigo, messy-neat side-swept, layered.
**No accessories** (unless suit-mode adds tie as visual anchor).
**Palette anchor:** Deep blue hair with lighter highlights, calm blue irises.

| ID | Expression Name | In-Engine Ref | Description |
|----|----------------|---------------|-------------|
| SSAD-VN-SKIDA-EXPR-01 | Neutral | `Skida.neutral` | Calm, attentive presence. Eyes open and direct, brows relaxed, mouth at natural rest. "I'm here." Not blank — there's depth. |
| SSAD-VN-SKIDA-EXPR-02 | Warm | `Skida.warm` | Soft smile, eyes slightly curved. The look someone gets when something they care about is okay. Not a full grin — quiet warmth. |
| SSAD-VN-SKIDA-EXPR-03 | Focused | `Skida.focused` | Brows drawn slightly, eyes intent, jaw set. The "I am solving this" face. Not angry — locked in. |
| SSAD-VN-SKIDA-EXPR-04 | Concerned | `Skida.concerned` | Brows raised slightly at inner corners, eyes softer and lower, mouth slightly tightened. The look he gives when someone he's holding space for is struggling. |
| SSAD-VN-SKIDA-EXPR-05 | Tired | `Skida.tired` | Eyes slightly drooped, brows even, a faint wry smile or neutral mouth. The look of someone who has been carrying things and is still showing up. Not defeated. |
| SSAD-VN-SKIDA-EXPR-06 | Laughing | `Skida.laughing` | The rare real laugh — eyes crinkled, head slightly tilted, mouth open. The kind of laugh that makes people around him laugh too. |

**Skida expression notes:**
- His face should always read as adult male — firm jawline even in soft expressions
- Tired is NOT despair; it's a specific kind of weary grace. Important distinction.
- Focused should feel like stillness, not anger — he doesn't intimidate, he concentrates
- Warm is his most important expression for building player connection
- Blue eyes should catch light distinctly in Happy/Laughing; dim slightly in Tired/Sad

---

## File Naming Convention

```
assets/characters/[name]/expressions/
  [name]_expr_[01-06]_v1.png          ← art file (to be generated/placed)
  [name]_expr_[01-06]_v1_prov.yml     ← provenance file
```

Example:
```
assets/characters/alex/expressions/
  alex_expr_01_v1.png
  alex_expr_01_v1_prov.yml
  alex_expr_02_v1.png
  alex_expr_02_v1_prov.yml
  ...
```

---

## Generation Prompt Template

When generating expression art, use this structure as your image prompt base:

**Alex:**
> Anime-style bust portrait, female character, charcoal wavy hair mid-back length with warm highlights, large warm brown-gold eyes, star freckle under left eye, soft facial features, golden halo above head, crescent moon hair ornament on right side, gold star clips in bangs, off-shoulder purple idol outfit visible at shoulder, transparent background, consistent proportions, [EXPRESSION DESCRIPTOR]

**Rose:**
> Anime-style bust portrait, adult female character, long dark-to-blonde ombré hair, golden-amber catlike eyes, black rectangular glasses, black choker collar with buckle, red rose hair clip, oversized dark sweater visible at shoulder, small stature but adult proportions, transparent background, consistent proportions, [EXPRESSION DESCRIPTOR]

**Skida:**
> Anime-style bust portrait, adult male character, deep blue-indigo messy side-swept hair with lighter highlights, soft almond-shaped blue eyes, calm adult facial proportions, firm jawline, white shirt with open collar visible at shoulder, lean adult build, transparent background, consistent proportions, [EXPRESSION DESCRIPTOR]
