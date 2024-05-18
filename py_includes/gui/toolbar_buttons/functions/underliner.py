from tkinter import font
from .... import globalvars

def underliner(_=False):
    """Underline button function"""

    under_font = font.Font(globalvars.notes, globalvars.notes.cget("font"))
    under_font.configure(underline=True)

    boldUnder_font = font.Font(globalvars.notes, globalvars.notes.cget("font"))
    boldUnder_font.configure(underline=True, weight="bold")

    italicUnder_font = font.Font(globalvars.notes, globalvars.notes.cget("font"))
    italicUnder_font.configure(underline=True, slant="italic")

    strikeUnder_font = font.Font(globalvars.notes, globalvars.notes.cget("font"))
    strikeUnder_font.configure(overstrike=True, underline=True)

    globalvars.notes.tag_configure("underline", font=under_font)
    globalvars.notes.tag_configure("boldUnder", font=boldUnder_font)
    globalvars.notes.tag_configure("italicUnder", font=italicUnder_font)
    globalvars.notes.tag_configure("strikeUnder", font=strikeUnder_font)
    current_tags = globalvars.notes.tag_names("sel.first")

    if "underline" in current_tags:
        globalvars.notes.tag_remove("underline", "sel.first", "sel.last")
    elif "boldUnder" in current_tags:
        globalvars.notes.tag_remove("boldUnder", "sel.first", "sel.last")
        globalvars.notes.tag_add("bold", "sel.first", "sel.last")
    elif "italicUnder" in current_tags:
        globalvars.notes.tag_remove("italicUnder", "sel.first", "sel.last")
        globalvars.notes.tag_add("italic", "sel.first", "sel.last")
    elif "strikeUnder" in current_tags:
        globalvars.notes.tag_remove("strikeUnder", "sel.first", "sel.last")
        globalvars.notes.tag_add("strikethrough", "sel.first", "sel.last")
    else:
        if "bold" in current_tags:
            globalvars.notes.tag_add("boldUnder", "sel.first", "sel.last")
            globalvars.notes.tag_remove("bold", "sel.first", "sel.last")
        elif "italic" in current_tags:
            globalvars.notes.tag_add("italicUnder", "sel.first", "sel.last")
            globalvars.notes.tag_remove("italic", "sel.first", "sel.last")
        elif "strikethrough" in current_tags:
            globalvars.notes.tag_add("strikeUnder", "sel.first", "sel.last")
            globalvars.notes.tag_remove("strikethrough", "sel.first", "sel.last")
        else:
            globalvars.notes.tag_add("underline", "sel.first", "sel.last")
    return "break"
