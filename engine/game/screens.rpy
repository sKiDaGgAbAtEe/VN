## screens.rpy — Astrica Visual Novel
## Core UI screens. Minimal and functional.
## Full UI art pass (Phase 3) will replace these with custom designs.

## ─────────────────────────────────────────
## MAIN MENU
## ─────────────────────────────────────────

screen main_menu():
    tag menu

    add gui.main_menu_background

    ## Dark overlay
    add "#0d0b1499"

    ## Title block
    vbox:
        xalign 0.5
        yalign 0.38
        spacing 8

        text "ASTRICA" style "main_menu_title"
        text "Visual Novel" style "main_menu_subtitle"

    ## Navigation
    vbox:
        xalign 0.5
        yalign 0.72
        spacing 16

        textbutton _("Begin") action Start() style "main_menu_button"
        textbutton _("Load")  action ShowMenu("load") style "main_menu_button"
        textbutton _("About") action ShowMenu("about") style "main_menu_button"
        textbutton _("Quit")  action Quit(confirm=not main_menu) style "main_menu_button"

style main_menu_title:
    font gui.text_font
    size 72
    color "#e8d5a0"
    outlines [(3, "#0d0b14", 0, 0)]
    xalign 0.5

style main_menu_subtitle:
    font gui.text_font
    size 28
    color "#c4afd8"
    italic True
    xalign 0.5

style main_menu_button:
    xalign 0.5
    xsize 300
    ysize 56
    background "#1a0f2ecc"
    hover_background "#4a2d6e99"
    padding (20, 12)

style main_menu_button_text:
    font gui.text_font
    size 26
    color "#c9a84c"
    hover_color "#f5f0e8"
    xalign 0.5
    idle_outlines [(1, "#0d0b14", 0, 0)]


## ─────────────────────────────────────────
## SAY (DIALOGUE BOX)
## ─────────────────────────────────────────

screen say(who, what):

    window:
        id "window"
        style "say_window"

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who" style "say_label"

        text what id "what" style "say_dialogue"

    ## Click to advance indicator
    add SpriteParticles(
        "images/gui/ctc.png" if renpy.loadable("images/gui/ctc.png") else None
    ) xalign 1.0 yalign 1.0 xoffset -20 yoffset -20 alpha 0.0

style say_window:
    background "#0d0b14cc"
    padding (60, 30, 60, 30)
    xfill True
    ysize gui.textbox_height
    yalign 1.0

style namebox:
    background "#1a0f2ecc"
    padding (20, 8, 20, 8)
    xpos 60
    ypos -42

style say_label:
    font gui.name_text_font
    size gui.name_text_size
    color gui.accent_color
    outlines [(2, "#0d0b14", 0, 0)]

style say_dialogue:
    font gui.text_font
    size gui.text_size
    color gui.text_color
    xpos 60
    xsize 1160
    ypos 20
    line_leading 8


## ─────────────────────────────────────────
## CHOICE MENU
## ─────────────────────────────────────────

screen choice(items):

    vbox:
        xalign 0.5
        yalign 0.6
        spacing 12

        for i in items:
            textbutton i.caption:
                action i.action
                style "choice_button"

style choice_button:
    xalign 0.5
    xsize gui.choice_button_width
    ysize 64
    background "#1a0f2ecc"
    hover_background "#4a2d6e99"
    padding (30, 16)

style choice_button_text:
    font gui.text_font
    size gui.text_size
    color gui.idle_color
    hover_color gui.hover_color
    xalign 0.5


## ─────────────────────────────────────────
## GAME MENU (Pause overlay)
## ─────────────────────────────────────────

screen game_menu(title, scroll=None, yinitial=0.0):
    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    add "#0d0b14cc"

    frame:
        style "game_menu_outer_frame"

        hbox:
            frame:
                style "game_menu_navigation_frame"

                vbox:
                    style_prefix "navigation"
                    spacing 4

                    if main_menu:
                        textbutton _("Start Game") action Start()
                    else:
                        textbutton _("History")    action ShowMenu("history")
                        textbutton _("Save")       action ShowMenu("save")

                    textbutton _("Load")       action ShowMenu("load")
                    textbutton _("Preferences") action ShowMenu("preferences")

                    if _in_replay:
                        textbutton _("End Replay") action EndReplay(confirm=True)
                    elif not main_menu:
                        textbutton _("Main Menu") action MainMenu()

                    textbutton _("Quit") action Quit(confirm=not main_menu)

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":
                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        yinitial yinitial
                        transclude
                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial yinitial
                        transclude
                else:
                    transclude

    label title style "game_menu_label"

style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_label is label
style game_menu_button is button
style game_menu_button_text is button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120
    background "#0d0b14e6"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_label:
    xpos 75
    ysize 120
    size_group "game_menu_label"

style game_menu_label_text:
    font gui.text_font
    size gui.label_text_size
    color gui.accent_color
    yalign 0.5

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    color gui.idle_color
    hover_color gui.hover_color
    size gui.interface_text_size


## ─────────────────────────────────────────
## SAVE / LOAD
## ─────────────────────────────────────────

screen save():
    tag menu
    use file_slots(_("Save"))

screen load():
    tag menu
    use file_slots(_("Load"))

screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):
        fixed:
            order_reverse True

            button:
                style "page_label"
                key_events True
                xalign 0.5
                action page_name_value.Toggle()
                input:
                    style "page_label_text"
                    value page_name_value

            hbox:
                style_prefix "page_button"
                xalign 0.5
                spacing 5
                for page in ["auto", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
                    textbutton (page if page.isdigit() else _(page.capitalize())):
                        action FilePage(page)

            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"
                xalign 0.5
                yalign 0.5
                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1
                    button:
                        action FileAction(slot)
                        has vbox

                        add FileScreenshot(slot) xalign 0.5
                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"
                        text FileSaveName(slot):
                            style "slot_name_text"
                        key "save_delete" action FileDelete(slot)


## ─────────────────────────────────────────
## PREFERENCES
## ─────────────────────────────────────────

screen preferences():
    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:
            spacing 20

            ## Text speed
            hbox:
                label _("Text Speed")
                bar:
                    xsize 400
                    value Preference("text speed")

            ## Auto-forward time
            hbox:
                label _("Auto-Forward Time")
                bar:
                    xsize 400
                    value Preference("auto-forward time")

            ## Music volume
            hbox:
                label _("Music Volume")
                bar:
                    xsize 400
                    value Preference("music volume")

            ## SFX volume
            hbox:
                label _("Sound Effects Volume")
                bar:
                    xsize 400
                    value Preference("sound volume")

            ## Voice volume (placeholder)
            hbox:
                label _("Voice Volume")
                bar:
                    xsize 400
                    value Preference("voice volume")

            ## Fullscreen toggle
            hbox:
                label _("Display")
                textbutton _("Window")     action Preference("display", "window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")

            ## Skip settings
            hbox:
                label _("Skip")
                textbutton _("Unseen Text") action Preference("skip", "toggle")
                textbutton _("After Choices") action Preference("after choices", "toggle")
                textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))


## ─────────────────────────────────────────
## HISTORY
## ─────────────────────────────────────────

screen history():
    tag menu

    predict False

    use game_menu(_("History"), scroll="vpgrid", yinitial=1.0):

        style_prefix "history"

        for h in _history_list:
            window:
                has fixed:
                    yfit True

                if h.who:
                    label h.who:
                        style "history_name"
                        substitute False

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## ─────────────────────────────────────────
## SKIP / FAST FORWARD INDICATOR
## ─────────────────────────────────────────

screen skip_indicator():
    zorder 100
    style_prefix "skip"

    frame:
        hbox:
            spacing 9
            text _("Skipping")
            text "▸▸" style "skip_triangle"

style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background "#0d0b14cc"
    padding (24, 8)

style skip_text:
    size 22
    color gui.accent_color

style skip_triangle:
    color gui.accent_color


## ─────────────────────────────────────────
## CONFIRM (Yes/No dialogs)
## ─────────────────────────────────────────

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    style_prefix "confirm"

    add "#0d0b1499"

    frame:
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100
                textbutton _("Yes") action yes_action
                textbutton _("No")  action no_action

    key "game_menu" action no_action

style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background "#1a0f2ef0"
    padding (60, 40, 60, 40)

style confirm_prompt_text:
    color gui.text_color
    text_align 0.5
    layout "subtitle"

style confirm_button_text:
    color gui.idle_color
    hover_color gui.hover_color


## ─────────────────────────────────────────
## ABOUT SCREEN
## ─────────────────────────────────────────

screen about():
    tag menu

    use game_menu(_("About")):
        style_prefix "about"

        vbox:
            spacing 20
            xalign 0.5

            text "[config.name!t]" style "about_title"
            text _("Version [config.version!t]") style "about_version"

            null height 20

            text _("""Astrica Visual Novel
Created by sKiDa

Art produced under the Micro-SSAD Ethical AI Art Protocol.
All character art carries traceable provenance.

github.com/sKiDaGgAbAtEe/VN"""):
                style "about_body"
                xalign 0.5
                text_align 0.5

style about_title:
    font gui.text_font
    size 48
    color gui.accent_color
    xalign 0.5

style about_version:
    font gui.text_font
    size 22
    color gui.interface_text_color
    xalign 0.5

style about_body:
    font gui.text_font
    size 24
    color gui.text_color
    line_leading 8
