## options.rpy — Astrica Visual Novel
## Global configuration. Edit display name, window size, and build settings here.

init -1 python:
    ## The name of the project, shown in the title bar and about screen.
    build.name = "Astrica"

define config.name = _("Astrica")

## The version of the game.
define config.version = "0.1.0-scaffold"

## The window icon. Replace with your own icon file.
# define config.window_icon = "gui/window_icon.png"

## Window size. 1280x720 is standard VN resolution.
define config.screen_width = 1280
define config.screen_height = 720

## Saves
define config.save_directory = "Astrica-0.1"

## The number of auto saves.
define config.has_autosave = True
define config.autosave_slots = 3

## Transitions
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = None
define config.end_game_transition = None

## Text speed (characters per second). 0 = instant.
define preferences.text_cps = 35

## Developer mode — set to False for release builds
define config.developer = True
