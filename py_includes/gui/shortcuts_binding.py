from .. import globalvars

from .window_related.getPos import getPos
from .functions.windowdestroy import windowdestroy
from .functions.saveNote import saveNote
from .functions.openLink import openLink
from ..helpers.tags import toggle_notes_tag

def attach_keyboard_shortcuts():
    # Keyboard Shortcuts
    globalvars.titleBar.bind("<Button-1>", getPos)
    globalvars.notes.bind("<Control-Key-b>", lambda event: toggle_notes_tag('bold'))
    globalvars.notes.bind("<Control-Key-i>", lambda event: toggle_notes_tag('italic'))
    globalvars.notes.bind("<Control-Key-u>", lambda event: toggle_notes_tag('underline'))
    globalvars.notes.bind("<Control-Key-t>", lambda event: toggle_notes_tag('code'))
    globalvars.notes.bind("<Control-Key-q>", windowdestroy)
    globalvars.notes.bind("<Control-Key-s>", saveNote)
    globalvars.notes.bind("<Control-Key-k>", lambda event: toggle_notes_tag('link'))
    globalvars.notes.bind("<Control-Key-o>", openLink)
    globalvars.notes.bind("<Control-slash>", lambda event: toggle_notes_tag('strikethrough'))
