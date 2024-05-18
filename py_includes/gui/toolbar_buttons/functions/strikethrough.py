from tkinter import font
from .... import globalvars

def strikethrough(_=False):
    """Strikethrough button function"""

    strike_font = font.Font(globalvars.notes, globalvars.notes.cget("font"))
    strike_font.configure(overstrike=True)

    boldStrike_font = font.Font(globalvars.notes, globalvars.notes.cget("font"))
    boldStrike_font.configure(overstrike=True, weight="bold")

    italicStrike_font = font.Font(globalvars.notes, globalvars.notes.cget("font"))
    italicStrike_font.configure(overstrike=True, slant="italic")

    underStrike_font = font.Font(globalvars.notes, globalvars.notes.cget("font"))
    underStrike_font.configure(overstrike=True, underline=True)

    globalvars.notes.tag_configure("strikethrough", font=strike_font)
    current_tags = globalvars.notes.tag_names("sel.first")

    if "strikethrough" in current_tags:
        globalvars.notes.tag_remove("strikethrough", "sel.first", "sel.last")
        globalvars.notes.tag_add("strikethrough", "sel.first", "sel.last")
    elif "boldStrike" in current_tags:
        globalvars.notes.tag_remove("boldStrike", "sel.first", "sel.last")
        globalvars.notes.tag_add("bold", "sel.first", "sel.last")
    elif "italicStrike" in current_tags:
        globalvars.notes.tag_remove("italicStrike", "sel.first", "sel.last")
        globalvars.notes.tag_add("italic", "sel.first", "sel.last")
    elif "underStrike" in current_tags:
        globalvars.notes.tag_remove("underStrike", "sel.first", "sel.last")
        globalvars.notes.tag_add("underline", "sel.first", "sel.last")
    else:
        if "bold" in current_tags:
            globalvars.notes.tag_remove("bold", "sel.first", "sel.last")
            globalvars.notes.tag_add("boldStrike", "sel.first", "sel.last")
        elif "italic" in current_tags:
            globalvars.notes.tag_remove("italic", "sel.first", "sel.last")
            globalvars.notes.tag_add("italicStrike", "sel.first", "sel.last")
        elif "underline" in current_tags:
            globalvars.notes.tag_remove("underline", "sel.first", "sel.last")
            globalvars.notes.tag_add("underStrike", "sel.first", "sel.last")
        else:
            globalvars.notes.tag_add("strikethrough", "sel.first", "sel.last")

    return "break"
