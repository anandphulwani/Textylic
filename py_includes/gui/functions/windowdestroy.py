import os
import re
import tkinter
import shutil
from ... import globalvars
from .saveNoteAs import saveNoteAs
from .saveNote import saveNote

def windowdestroy(_=False):
    """Close the window"""
    
    def whitespaceStr(strg, search=re.compile(r"[^\s]+").search):
        return not bool(search(strg))

    if (not globalvars.saved) and (not whitespaceStr(globalvars.notes.get("1.0", "end"))):
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
            shutil.rmtree(os.path.dirname(globalvars.openedFileName))
            globalvars.root.destroy()
        else:
            pass
    else:
        saveNote(False)
        globalvars.root.destroy()
