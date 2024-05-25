import re
import tkinter
import winreg
from ... import globalvars
from . import saveNoteAs

def windowdestroy(_=False):
    """Close the window"""
    
    def whitespaceStr(strg, search=re.compile(r"[^\s]+").search):
        return not bool(search(strg))

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
