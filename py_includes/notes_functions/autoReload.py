from .. import globalvars
from ..gui.functions.openFile import openFile

def autoReload():
    """Auto reloads the note"""

    if not globalvars.window_is_focused:
        openFile(globalvars.openedFileName)
    globalvars.window.after(3000, autoReload)
