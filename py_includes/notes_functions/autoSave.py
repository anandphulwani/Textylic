from .. import globalvars
from ..gui.functions import saveNote

def autoSave():
    """Auto saves the note"""

    if globalvars.window_is_focused and globalvars.saved is True:
        saveNote()
    globalvars.window.after(3000, autoSave)
