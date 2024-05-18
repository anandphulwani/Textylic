from tkinter import font
from .... import globalvars

def bolder(_=False):
    """Bold button function"""

    bold_font = font.Font(globalvars.notes, globalvars.notes.cget("font"))
    bold_font.configure(weight="bold")

    italicBold_font = font.Font(globalvars.notes, globalvars.notes.cget("font"))
    italicBold_font.configure(slant="italic", weight="bold")

    underBold_font = font.Font(globalvars.notes, globalvars.notes.cget("font"))
    underBold_font.configure(underline=True, weight="bold")

    strikeBold_font = font.Font(globalvars.notes, globalvars.notes.cget("font"))
    strikeBold_font.configure(overstrike=True, weight="bold")

    globalvars.notes.tag_configure("bold", font=bold_font)
    globalvars.notes.tag_configure("italicBold", font=italicBold_font)
    globalvars.notes.tag_configure("underBold", font=underBold_font)
    globalvars.notes.tag_configure("strikeBold", font=strikeBold_font)
    current_tags = globalvars.notes.tag_names("sel.first")

    if "bold" in current_tags:
        globalvars.notes.tag_remove("bold", "sel.first", "sel.last")
    elif "italicBold" in current_tags:
        globalvars.notes.tag_remove("italicBold", "sel.first", "sel.last")
        globalvars.notes.tag_add("italic", "sel.first", "sel.last")
    elif "underBold" in current_tags:
        globalvars.notes.tag_remove("underBold", "sel.first", "sel.last")
        globalvars.notes.tag_add("underline", "sel.first", "sel.last")
    elif "strikeBold" in current_tags:
        globalvars.notes.tag_remove("strikeBold", "sel.first", "sel.last")
        globalvars.notes.tag_add("strikethrough", "sel.first", "sel.last")
    else:
        if "italic" in current_tags:
            globalvars.notes.tag_remove("italic", "sel.first", "sel.last")
            globalvars.notes.tag_add("italicBold", "sel.first", "sel.last")
        elif "underline" in current_tags:
            globalvars.notes.tag_remove("underline", "sel.first", "sel.last")
            globalvars.notes.tag_add("underBold", "sel.first", "sel.last")
        elif "strikethrough" in current_tags:
            globalvars.notes.tag_remove("strikethrough", "sel.first", "sel.last")
            globalvars.notes.tag_add("strikeBold", "sel.first", "sel.last")
        else:
            globalvars.notes.tag_add("bold", "sel.first", "sel.last")
    return "break"
