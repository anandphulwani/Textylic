from tkinter import filedialog
from .openFile import openFile

def openFileChoose(_=False):
    """Open a file with the file dialog"""

    openFile(
        (
            filedialog.askopenfilename(
                initialdir="./notes",
                title="Choose a note:",
                filetypes=(("Textylic file", "*.txtlyc"),),
            )
        )
    )
    return "break"
