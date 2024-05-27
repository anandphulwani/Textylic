import tkinter

from ... import globalvars
from ...helpers.tags import toggle_notes_tag
from .functions.photoInserter import photoInserter
from .create_button import create_button

def create_bottom_menu():
    bottom_bar = tkinter.Frame(globalvars.window, relief="flat", bg="#181926", pady=3)
    bottom_bar.grid(row=3, column=0, columnspan=10, rowspan=1, sticky="SWE")

    button_configs = [
        (tag, getattr(globalvars.window, f"{tag}ButtonImage"), lambda t=tag: toggle_notes_tag(t), 0, index + 1)
        for index, tag in enumerate(globalvars.notes_tags_options)
    ]
    button_configs.append(("photoinsert", globalvars.window.photoinsertButtonImage, photoInserter, 0, 9))

    globalvars.bottom_menu_buttons = {}
    for name, image, command, row, column in button_configs:
        globalvars.bottom_menu_buttons[name] = create_button(bottom_bar, image, command, row, column, globalvars.smallPaddingX, globalvars.smallPaddingY, bg="#181926", active_bg="#181926")
