## script.rpy — Astrica Visual Novel
## Main entry point. Routes to the opening scene.
## This is the file Ren'Py launches first.

## ─────────────────────────────────────────
## GAME START
## ─────────────────────────────────────────

label start:

    ## Jump to the opening scene.
    ## Swap this for your actual first scene label as the story develops.
    jump scene_test


## ─────────────────────────────────────────
## TEST SCENE
## Validates that sprites, expressions, and
## dialogue all wire up correctly.
## Replace with real scenes when ready.
## ─────────────────────────────────────────

label scene_test:

    scene bg placeholder
    with fade

    ## ── ALEX ──
    show alex idol neutral at center
    with dissolve

    narrator "The stage is quiet before the performance."

    alex happy "Oh — you're here already?"

    alex shy "I wasn't sure if... nevermind. I'm glad."

    alex determined "Let's do this right."

    alex sad "Sometimes I wonder if anyone actually hears it."

    alex laughing "Okay, okay — that was actually funny."

    hide alex
    with dissolve

    ## ── ROSE ──
    show rose sweater neutral at center
    with dissolve

    narrator "She's already three steps ahead of you."

    rose neutral "Took you long enough."

    rose smug "Called it. I told you the third option was a trap."

    rose concerned "Hey. Talk to me. What's actually going on?"

    rose happy "Okay — that genuinely surprised me. Well done."

    rose sad "..."

    rose laughing "I can't — stop — I hate you both."

    hide rose
    with dissolve

    ## ── SKIDA ──
    show skida shirt neutral at center
    with dissolve

    narrator "He doesn't say much. He doesn't need to."

    skida warm "I've got you."

    skida focused "Give me a minute. I'm working on it."

    skida concerned "Something's off. You doing okay?"

    skida tired "Still here. Always."

    skida laughing "Alright, alright — that one got me."

    hide skida
    with dissolve

    ## ── ALL THREE ──
    narrator "Three people. One strange little universe."

    show alex idol neutral at left
    show rose sweater neutral at center
    show skida shirt neutral at right
    with dissolve

    alex happy "So what now?"

    rose smug "Now we figure it out. Obviously."

    skida warm "Together."

    hide alex
    hide rose
    hide skida
    with dissolve

    scene bg black
    with fade

    ## End of test scene — route to actual content here
    return
