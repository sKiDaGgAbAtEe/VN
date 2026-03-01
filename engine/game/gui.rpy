## gui.rpy — Astrica Visual Novel
## Visual styling for dialogue boxes, nameplates, menus, and text.
## This is a minimal working config — full UI art pass comes in Phase 3.

## ─────────────────────────────────────────
## COLOR PALETTE
## Matches the VN's dark parchment / gold / violet aesthetic
## ─────────────────────────────────────────

## Background colors
define gui.idle_color          = "#c9a84c"       ## Unselected menu items — gold
define gui.idle_small_color    = "#8a6f32"       ## Small unselected text — dim gold
define gui.hover_color         = "#f5f0e8"       ## Hovered items — parchment
define gui.selected_color      = "#e8d5a0"       ## Selected items — star gold
define gui.insensitive_color   = "#4a4040"       ## Greyed out items
define gui.muted_color         = "#3a2a4a"       ## Muted / disabled
define gui.hover_muted_color   = "#5a3a6a"       ## Hovered muted

## Text colors
define gui.text_color          = "#f5f0e8"       ## Main text — parchment
define gui.interface_text_color = "#c4afd8"      ## UI text — violet pale
define gui.accent_color        = "#c9a84c"       ## Accent — gold


## ─────────────────────────────────────────
## FONTS
## ─────────────────────────────────────────
## Using system fallbacks for now.
## Replace with custom font files in /game/fonts/ when ready.

define gui.text_font           = "DejaVuSans.ttf"
define gui.name_text_font      = "DejaVuSans.ttf"
define gui.interface_text_font = "DejaVuSans.ttf"

define gui.text_size           = 28
define gui.name_text_size      = 30
define gui.interface_text_size = 28
define gui.label_text_size     = 28
define gui.notify_text_size    = 22
define gui.title_text_size     = 60


## ─────────────────────────────────────────
## DIALOGUE BOX
## ─────────────────────────────────────────

define gui.textbox_height      = 220
define gui.textbox_yalign      = 1.0        ## Anchored to bottom of screen

## Text positioning within the box
define gui.text_xpos           = 340
define gui.text_ypos           = 60
define gui.text_xsize          = 900
define gui.text_ysize          = 130
define gui.text_xalign         = 0.0

## Name plate positioning
define gui.name_xpos           = 300
define gui.name_ypos           = 0
define gui.name_xalign         = 0.0
define gui.name_yalign         = 1.0

## Dialogue box colors (used until custom GUI art is in place)
define config.textbox_background = "#0d0b14cc"
define config.name_background    = "#1a0f2ecc"


## ─────────────────────────────────────────
## CHOICE MENUS
## ─────────────────────────────────────────

define gui.choice_button_width    = 790
define gui.choice_button_height   = None
define gui.choice_button_tile     = False
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_idle_color    = gui.idle_color
define gui.choice_button_text_hover_color   = gui.hover_color
define gui.choice_button_text_insensitive_color = gui.insensitive_color


## ─────────────────────────────────────────
## HISTORY
## ─────────────────────────────────────────

define config.history_length    = 250

define gui.history_height       = 210
define gui.history_text_width   = 790


## ─────────────────────────────────────────
## SAVE / LOAD SCREENS
## ─────────────────────────────────────────

define gui.file_slot_cols       = 3
define gui.file_slot_rows       = 2


## ─────────────────────────────────────────
## MISC
## ─────────────────────────────────────────

define gui.confirm_frame_borders = Borders(60, 60, 60, 60)
define gui.skip_transition       = Dissolve(0.25)
define gui.game_menu_transition  = Dissolve(0.25)

define gui.main_menu_background  = "bg placeholder"
define gui.game_menu_background  = "bg placeholder"

## Rounded bars (used in sliders and progress)
define gui.bar_size    = 38
define gui.scrollbar_size = 18
define gui.slider_size = 38
define gui.bar_tile    = False
define gui.scrollbar_tile = False
define gui.slider_tile = False
