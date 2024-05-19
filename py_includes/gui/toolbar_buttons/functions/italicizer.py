from ....helpers.configure_font import configure_font
from .... import globalvars

def italicizer(_=False):
    """Italic button function"""

    italic_font = configure_font(globalvars.notes.cget("font"), slant="italic")
    bold_italic_font = configure_font(globalvars.notes.cget("font"), slant="italic", weight="bold")
    underline_italic_font = configure_font(globalvars.notes.cget("font"), underline=True, slant="italic")
    strikethrough_italic_font = configure_font(globalvars.notes.cget("font"), overstrike=True, slant="italic")

    globalvars.notes.tag_configure("italic", font=italic_font)
    globalvars.notes.tag_configure("bold_italic", font=bold_italic_font)
    globalvars.notes.tag_configure("underline_italic", font=underline_italic_font)
    globalvars.notes.tag_configure("strikethrough_italic", font=strikethrough_italic_font)

    current_tags = globalvars.notes.tag_names("sel.first")

    if "italic" in current_tags:
        globalvars.notes.tag_remove("italic", "sel.first", "sel.last")
    elif "bold_italic" in current_tags:
        globalvars.notes.tag_remove("bold_italic", "sel.first", "sel.last")
        globalvars.notes.tag_add("bold", "sel.first", "sel.last")
    elif "underline_italic" in current_tags:
        globalvars.notes.tag_remove("underline_italic", "sel.first", "sel.last")
        globalvars.notes.tag_add("underline", "sel.first", "sel.last")
    elif "strikethrough_italic" in current_tags:
        globalvars.notes.tag_remove("strikethrough_italic", "sel.first", "sel.last")
        globalvars.notes.tag_add("strikethrough", "sel.first", "sel.last")
    else:
        if "bold" in current_tags:
            globalvars.notes.tag_remove("bold", "sel.first", "sel.last")
            globalvars.notes.tag_add("bold_italic", "sel.first", "sel.last")
        elif "underline" in current_tags:
            globalvars.notes.tag_remove("underline", "sel.first", "sel.last")
            globalvars.notes.tag_add("underline_italic", "sel.first", "sel.last")
        elif "strikethrough" in current_tags:
            globalvars.notes.tag_remove("strikethrough", "sel.first", "sel.last")
            globalvars.notes.tag_add("strikethrough_italic", "sel.first", "sel.last")
        else:
            globalvars.notes.tag_add("italic", "sel.first", "sel.last")

    return "break"
