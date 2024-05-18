from tkinter import font
from .... import globalvars

def italicizer(_=False):
    """Italic button function"""

    italic_font = font.Font(globalvars.notes, globalvars.notes.cget("font"))
    italic_font.configure(slant="italic")

    boldItalic_font = font.Font(globalvars.notes, globalvars.notes.cget("font"))
    boldItalic_font.configure(slant="italic", weight="bold")

    underItalic_font = font.Font(globalvars.notes, globalvars.notes.cget("font"))
    underItalic_font.configure(underline=True, slant="italic")

    strikeItalic_font = font.Font(globalvars.notes, globalvars.notes.cget("font"))
    strikeItalic_font.configure(overstrike=True, slant="italic")

    globalvars.notes.tag_configure("italic", font=italic_font)
    globalvars.notes.tag_configure("boldItalic", font=boldItalic_font)
    globalvars.notes.tag_configure("underItalic", font=underItalic_font)
    globalvars.notes.tag_configure("strikeItalic", font=strikeItalic_font)
    current_tags = globalvars.notes.tag_names("sel.first")

    if "italic" in current_tags:
        globalvars.notes.tag_remove("italic", "sel.first", "sel.last")
    elif "boldItalic" in current_tags:
        globalvars.notes.tag_remove("boldItalic", "sel.first", "sel.last")
        globalvars.notes.tag_add("bold", "sel.first", "sel.last")
    elif "underItalic" in current_tags:
        globalvars.notes.tag_remove("underItalic", "sel.first", "sel.last")
        globalvars.notes.tag_add("underline", "sel.first", "sel.last")
    elif "strikeItalic" in current_tags:
        globalvars.notes.tag_remove("strikeItalic", "sel.first", "sel.last")
        globalvars.notes.tag_add("strikethrough", "sel.first", "sel.last")
    else:
        if "bold" in current_tags:
            globalvars.notes.tag_remove("bold", "sel.first", "sel.last")
            globalvars.notes.tag_add("boldItalic", "sel.first", "sel.last")
        elif "underline" in current_tags:
            globalvars.notes.tag_remove("underline", "sel.first", "sel.last")
            globalvars.notes.tag_add("underItalic", "sel.first", "sel.last")
        elif "strikethrough" in current_tags:
            globalvars.notes.tag_remove("strikethrough", "sel.first", "sel.last")
            globalvars.notes.tag_add("strikeItalic", "sel.first", "sel.last")
        else:
            globalvars.notes.tag_add("italic", "sel.first", "sel.last")
    return "break"
