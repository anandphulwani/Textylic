import tkinter

from ... import globalvars
from .functions.bolder import bolder
from .functions.italicizer import italicizer
from .functions.underliner import underliner
from .functions.strikethrough import strikethrough
from .functions.bulletList import bulletList
from .functions.codify import codify
from .functions.link import link
from .functions.setColor import setColor
from .functions.photoInserter import photoInserter
from .create_button import create_button

def create_bottom_menu():
    bottom_bar = tkinter.Frame(globalvars.window, relief="flat", bg="#181926", pady=3)
    bottom_bar.grid(row=3, column=0, columnspan=10, rowspan=1, sticky="SWE")

    button_configs = [
        ("bold", globalvars.window.boldButtonImage, bolder, 0, 1),
        ("italic", globalvars.window.italicButtonImage, italicizer, 0, 2),
        ("underline", globalvars.window.underlineButtonImage, underliner, 0, 3),
        ("strikethrough", globalvars.window.strikethroughButtonImage, strikethrough, 0, 4),
        ("bullet", globalvars.window.bulletButtonImage, bulletList, 0, 5),
        ("code", globalvars.window.codeButtonImage, codify, 0, 6),
        ("insertl", globalvars.window.insertlButtonImage, link, 0, 7),
        ("colortext", globalvars.window.colortextButtonImage, setColor, 0, 8),
        ("photoinsert", globalvars.window.photoinsertButtonImage, photoInserter, 0, 9),
    ]

    globalvars.bottom_menu_buttons = {}
    for name, image, command, row, column in button_configs:
        globalvars.bottom_menu_buttons[name] = create_button(bottom_bar, image, command, row, column, globalvars.smallPaddingX, globalvars.smallPaddingY)
