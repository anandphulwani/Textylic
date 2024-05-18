from .. import globalvars

from .window_related.getPos import getPos
from .toolbar_buttons.functions.bolder import bolder
from .toolbar_buttons.functions.italicizer import italicizer
from .toolbar_buttons.functions.underliner import underliner
from .toolbar_buttons.functions.codify import codify
from .functions.windowdestroy import windowdestroy
from .functions.saveNote import saveNote
from .toolbar_buttons.functions.link import link
from .functions.openLink import openLink
from .toolbar_buttons.functions.strikethrough import strikethrough

def attach_keyboard_shortcuts():
    # Keyboard Shortcuts
    globalvars.titleBar.bind("<Button-1>", getPos)
    globalvars.notes.bind("<Control-Key-b>", bolder)
    globalvars.notes.bind("<Control-Key-i>", italicizer)
    globalvars.notes.bind("<Control-Key-u>", underliner)
    globalvars.notes.bind("<Control-Key-t>", codify)
    globalvars.notes.bind("<Control-Key-q>", windowdestroy)
    globalvars.notes.bind("<Control-Key-s>", saveNote)
    globalvars.notes.bind("<Control-Key-k>", link)
    globalvars.notes.bind("<Control-Key-o>", openLink)
    globalvars.notes.bind("<Control-slash>", strikethrough)
