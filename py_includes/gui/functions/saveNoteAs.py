import os
import re
import tkinter
from tkinter import filedialog
from ...gui.functions.saveNote import saveNote
from ... import globalvars

def saveNoteAs(_=False):
    """Save the note as a file name"""

    with globalvars.save_fn_lock:
        if not globalvars.saved:
            noteFile = filedialog.asksaveasfilename(
                confirmoverwrite=True,
                defaultextension=".txtlyc",
                filetypes=(("Textylic file", "*.txtlyc"),),
                initialdir = globalvars.dataPath,
                title="Save your note:",
            )
            if not noteFile:
                return
            os.rename(globalvars.openedFileName, noteFile)
            globalvars.openedFileName = noteFile
        saveNote()
        if not globalvars.saved:
            # Messagebox
            openedFileNameStrip = re.sub("C:/.*/", "", str(globalvars.openedFileName))
            tkinter.messagebox.showinfo(" ", f'Successfully saved note as "{openedFileNameStrip}"   ')
            globalvars.saved = True
