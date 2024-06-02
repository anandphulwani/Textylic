from .. import globalvars
from ..gui.functions.openFile import openFile
from ..gui.functions.saveNote import saveNote
from ..helpers.is_child_window_of_main_window import is_child_window_of_main_window

def autoSaveOrReloadAcToFocus():
    """Auto saves or reloads the note"""
    hwnd_top = globalvars.user32.GetForegroundWindow()
    if is_child_window_of_main_window(hwnd_top):
        with globalvars.save_fn_lock:
            saveNote(True)
    else:
        openFile(globalvars.openedFileName)
    globalvars.window.after(3000, autoSaveOrReloadAcToFocus)   
