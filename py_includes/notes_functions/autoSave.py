from .. import globalvars
from ..gui.functions.saveNote import saveNote

def autoSave():
    """Auto saves the note"""

    if globalvars.window_is_focused:
        saveNote()
    globalvars.window.after(3000, autoSave)
