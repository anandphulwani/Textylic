import tkinter

from ... import globalvars
from ...helpers.tags import toggle_notes_tag
from .functions.photoInserter import photoInserter
from .create_button import create_button

def create_bottom_menu():
    bottom_bar = tkinter.Frame(globalvars.window, relief="flat", bg="#181926", pady=3)
    bottom_bar.grid(row=3, column=0, columnspan=10, rowspan=1, sticky="SWE")

    button_configs = [
        ("bold", globalvars.window.boldButtonImage, lambda: toggle_notes_tag('bold'), 0, 1),
        ("italic", globalvars.window.italicButtonImage, lambda: toggle_notes_tag('italic'), 0, 2),
        ("underline", globalvars.window.underlineButtonImage, lambda: toggle_notes_tag('underline'), 0, 3),
        ("strikethrough", globalvars.window.strikethroughButtonImage, lambda: toggle_notes_tag('strikethrough'), 0, 4),
        ("bullet", globalvars.window.bulletButtonImage, lambda: toggle_notes_tag('bullet'), 0, 5),
        ("code", globalvars.window.codeButtonImage, lambda: toggle_notes_tag('code'), 0, 6),
        ("insertl", globalvars.window.insertlButtonImage, lambda: toggle_notes_tag('link'), 0, 7),
        ("colortext", globalvars.window.colortextButtonImage, lambda: toggle_notes_tag('colortext'), 0, 8),
        ("photoinsert", globalvars.window.photoinsertButtonImage, photoInserter, 0, 9),
    ]

    globalvars.bottom_menu_buttons = {}
    for name, image, command, row, column in button_configs:
        globalvars.bottom_menu_buttons[name] = create_button(bottom_bar, image, command, row, column, globalvars.smallPaddingX, globalvars.smallPaddingY)
