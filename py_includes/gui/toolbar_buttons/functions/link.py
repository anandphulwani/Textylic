from .... import globalvars
from tkinter import font

def link(_=False):
    """Link button function"""

    under_font = font.Font(globalvars.notes, globalvars.notes.cget("font"))
    under_font.configure(underline=True)

    globalvars.notes.tag_configure("link", font=under_font, foreground="#00AFEC")
    current_tags = globalvars.notes.tag_names("sel.first")

    if "link" in current_tags:
        globalvars.notes.tag_remove("link", "sel.first", "sel.last")
    else:
        globalvars.notes.tag_add("link", "sel.first", "sel.last")
    return "break"
