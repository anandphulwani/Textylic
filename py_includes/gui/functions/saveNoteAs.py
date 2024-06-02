import os
import re
import tkinter
from ...gui.window_related.saveAsFolderNameDialog import saveAsFolderNameDialog
from ...gui.functions.saveNote import saveNote
from ... import globalvars

def saveNoteAs(_=False):
    """Save the note as a file in a notes name folder"""

    if not globalvars.saved:
        dialog = saveAsFolderNameDialog(globalvars.window, "Save Note", globalvars.dataPath)
        folderName = dialog.result
        if not folderName:
            return
        noteFolder = os.path.join(globalvars.dataPath, folderName)
    with globalvars.save_fn_lock:
        if not globalvars.saved:
            try:
                os.rename(os.path.dirname(globalvars.openedFileName), noteFolder)
            except Exception as e:
                print(f"Error saving file: {e}")
            globalvars.openedFileName = os.path.join(noteFolder, "notes.txt")
        saveNote(False)
        if not globalvars.saved:
            # Messagebox
            openedFileNameStrip = re.sub("C:/.*/", "", str(globalvars.openedFileName))
            tkinter.messagebox.showinfo("Success", f'Successfully saved note as "{openedFileNameStrip}"')
            globalvars.saved = True
