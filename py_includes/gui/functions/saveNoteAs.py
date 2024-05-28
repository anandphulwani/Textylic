import os
import re
import tkinter
from tkinter import filedialog
from ... import globalvars

def saveNoteAs(_=False):
    """Save the note as a file name"""

    with globalvars.save_fn_lock:
    noteFile = filedialog.asksaveasfilename(
        confirmoverwrite=True,
        defaultextension=".txtlyc",
        filetypes=(("Textylic file", "*.txtlyc"),),
        initialdir="./notes",
        title="Save your note:",
    )
    if not noteFile:
        return
        globalvars.saved = True
        globalvars.openedFileName = noteFile
        noteFile = open(os.path.join(globalvars.dataPath, noteFile), "w")
        noteFile.write(globalvars.notes.get(1.0, "end"))
        noteFile.close()
        # Messagebox
        openedFileNameStrip = re.sub("C:/.*/", "", str(globalvars.openedFileName))
        tkinter.messagebox.showinfo(" ", f'Successfully saved note as "{openedFileNameStrip}"   ')
    return "break"
