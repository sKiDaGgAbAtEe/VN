## definitions.rpy — Astrica Visual Novel
## Central registry for all characters, image aliases, and audio.
## Add new assets here as they are approved and placed in /game/images/

## ─────────────────────────────────────────
## CHARACTERS
## ─────────────────────────────────────────

## Alex / Astrica
## Color: warm gold — matches her halo/star identity
define alex = Character(
    "Alex",
    color="#c9a84c",
    who_outlines=[(2, "#0d0b14", 0, 0)],
    what_color="#f5f0e8",
    what_outlines=[(1, "#0d0b14", 0, 0)],
)

## Rose
## Color: deep rose/amber — her golden eyes, gothic warmth
define rose = Character(
    "Rose",
    color="#c4748a",
    who_outlines=[(2, "#0d0b14", 0, 0)],
    what_color="#f5f0e8",
    what_outlines=[(1, "#0d0b14", 0, 0)],
)

## Skida (player character — shown as narrator-adjacent voice)
## Color: soft blue — his hair/eyes
define skida = Character(
    "Skida",
    color="#7ab3d4",
    who_outlines=[(2, "#0d0b14", 0, 0)],
    what_color="#f5f0e8",
    what_outlines=[(1, "#0d0b14", 0, 0)],
)

## Narrator / inner voice
define narrator = Character(
    None,
    what_color="#d4c9e8",
    what_italic=True,
)


## ─────────────────────────────────────────
## SPRITE IMAGE DECLARATIONS — ALEX
## ─────────────────────────────────────────
## Naming convention: image [character] [outfit] [expression]
## In-scene call:     show alex idol neutral

## Base sprites
image alex idol neutral    = "images/alex/alex_idol_v1.png"
image alex pjs neutral     = "images/alex/alex_outfit_pjs_v1.png"
image alex snuggie neutral = "images/alex/alex_outfit_snuggie_v1.png"
image alex swim neutral    = "images/alex/alex_outfit_swim_v1.png"

## Expressions (bust crops — overlay on body sprite or standalone)
image alex neutral    = "images/alex/expressions/alex_expr_01_v1.png"
image alex happy      = "images/alex/expressions/alex_expr_02_v1.png"
image alex shy        = "images/alex/expressions/alex_expr_03_v1.png"
image alex determined = "images/alex/expressions/alex_expr_04_v1.png"
image alex sad        = "images/alex/expressions/alex_expr_05_v1.png"
image alex laughing   = "images/alex/expressions/alex_expr_06_v1.png"


## ─────────────────────────────────────────
## SPRITE IMAGE DECLARATIONS — ROSE
## ─────────────────────────────────────────

image rose sweater neutral  = "images/rose/rose_outfit_sweater_v1.png"
image rose pjs neutral      = "images/rose/rose_outfit_pjs_v1.png"
image rose business neutral = "images/rose/rose_outfit_business_v1.png"
image rose swim neutral     = "images/rose/rose_outfit_swim_v1.png"

image rose neutral   = "images/rose/expressions/rose_expr_01_v1.png"
image rose happy     = "images/rose/expressions/rose_expr_02_v1.png"
image rose smug      = "images/rose/expressions/rose_expr_03_v1.png"
image rose concerned = "images/rose/expressions/rose_expr_04_v1.png"
image rose sad       = "images/rose/expressions/rose_expr_05_v1.png"
image rose laughing  = "images/rose/expressions/rose_expr_06_v1.png"


## ─────────────────────────────────────────
## SPRITE IMAGE DECLARATIONS — SKIDA
## ─────────────────────────────────────────

image skida shirt neutral  = "images/skida/skida_base_v1.png"
image skida pjs neutral    = "images/skida/skida_outfit_pjs_v1.png"
image skida hoodie neutral = "images/skida/skida_outfit_hoodie_v1.png"

image skida neutral   = "images/skida/expressions/skida_expr_01_v1.png"
image skida warm      = "images/skida/expressions/skida_expr_02_v1.png"
image skida focused   = "images/skida/expressions/skida_expr_03_v1.png"
image skida concerned = "images/skida/expressions/skida_expr_04_v1.png"
image skida tired     = "images/skida/expressions/skida_expr_05_v1.png"
image skida laughing  = "images/skida/expressions/skida_expr_06_v1.png"


## ─────────────────────────────────────────
## BACKGROUND IMAGE DECLARATIONS
## ─────────────────────────────────────────
## Placeholder — replace paths once background art is generated

image bg black      = "#000000"
image bg white      = "#ffffff"
image bg placeholder = "#1a1025"

## Future backgrounds (uncomment as art is added):
# image bg practice_room_day   = "images/bg/bg_practice_room_day.png"
# image bg practice_room_night = "images/bg/bg_practice_room_night.png"
# image bg apartment_day       = "images/bg/bg_apartment_day.png"
# image bg apartment_night     = "images/bg/bg_apartment_night.png"
# image bg beach_day           = "images/bg/bg_beach_day.png"
# image bg rooftop_night       = "images/bg/bg_rooftop_night.png"
# image bg neon_street_night   = "images/bg/bg_neon_street_night.png"


## ─────────────────────────────────────────
## AUDIO DECLARATIONS
## ─────────────────────────────────────────
## Placeholder — fill in as audio is sourced/composed

## Music
# define audio.theme_main   = "audio/music/theme_main.ogg"
# define audio.cozy_lofi    = "audio/music/cozy_lofi.ogg"
# define audio.kpop_stage   = "audio/music/kpop_stage.ogg"
# define audio.night_mood   = "audio/music/night_mood.ogg"
# define audio.emotional    = "audio/music/emotional_climax.ogg"

## SFX
# define audio.sfx_page     = "audio/sfx/page_turn.ogg"
# define audio.sfx_chime    = "audio/sfx/star_chime.ogg"
# define audio.sfx_notify   = "audio/sfx/notification.ogg"
