import re
import tkinter
import winreg
from ... import globalvars
from . import saveNoteAs

def windowdestroy(_=False):
    """Close the window"""
    
    def whitespaceStr(strg, search=re.compile(r"[^\s]+").search):
        return not bool(search(strg))

    # Save window position to registry before closing
    x, y = globalvars.window.winfo_x(), globalvars.window.winfo_y()
    width, height = globalvars.window.winfo_width(), globalvars.window.winfo_height()
    key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, "Software\\Textylyc\\" + globalvars.openedFileName)
    winreg.SetValueEx(key, "x", 0, winreg.REG_SZ, str(x))
    winreg.SetValueEx(key, "y", 0, winreg.REG_SZ, str(y))
    winreg.SetValueEx(key, "width", 0, winreg.REG_SZ, str(width))
    winreg.SetValueEx(key, "height", 0, winreg.REG_SZ, str(height))
    winreg.CloseKey(key)

    if (not globalvars.openedFileName) and (not whitespaceStr(globalvars.notes.get("1.0", "end"))):
        # Confirmbox
        confirmSave = tkinter.messagebox.askyesnocancel(
            "Confirmation",
            "Do you want to save this note \
                                            before you leave?   ",
            icon="warning",
            default="no",
        )
        if confirmSave is True:
            saveNoteAs()
        elif confirmSave is False:
            globalvars.root.destroy()
        else:
            pass
    else:
        globalvars.root.destroy()
