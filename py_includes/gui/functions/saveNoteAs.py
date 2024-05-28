import os
import re
import tkinter
from tkinter import filedialog
from ...gui.functions.saveNote import saveNote
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
    os.rename(globalvars.openedFileName, noteFile)
    globalvars.openedFileName = noteFile
    saveNote()
    # Messagebox
    openedFileNameStrip = re.sub("C:/.*/", "", str(globalvars.openedFileName))
    tkinter.messagebox.showinfo(" ", f'Successfully saved note as "{openedFileNameStrip}"   ')
    globalvars.saved = True
