from ....helpers.configure_font import configure_font
from .... import globalvars

def strikethrough(_=False):
    """Strikethrough button function"""

    strikethrough_font = configure_font(globalvars.notes.cget("font"), overstrike=True)
    bold_strikethrough_font = configure_font(globalvars.notes.cget("font"), overstrike=True, weight="bold")
    italic_strikethrough_font = configure_font(globalvars.notes.cget("font"), overstrike=True, slant="italic")
    underline_strikethrough_font = configure_font(globalvars.notes.cget("font"), overstrike=True, underline=True)

    globalvars.notes.tag_configure("strikethrough", font=strikethrough_font)
    globalvars.notes.tag_configure("bold_strikethrough", font=bold_strikethrough_font)
    globalvars.notes.tag_configure("italic_strikethrough", font=italic_strikethrough_font)
    globalvars.notes.tag_configure("underline_strikethrough", font=underline_strikethrough_font)

    current_tags = globalvars.notes.tag_names("sel.first")

    if "strikethrough" in current_tags:
        globalvars.notes.tag_remove("strikethrough", "sel.first", "sel.last")
    elif "bold_strikethrough" in current_tags:
        globalvars.notes.tag_remove("bold_strikethrough", "sel.first", "sel.last")
        globalvars.notes.tag_add("bold", "sel.first", "sel.last")
    elif "italic_strikethrough" in current_tags:
        globalvars.notes.tag_remove("italic_strikethrough", "sel.first", "sel.last")
        globalvars.notes.tag_add("italic", "sel.first", "sel.last")
    elif "underline_strikethrough" in current_tags:
        globalvars.notes.tag_remove("underline_strikethrough", "sel.first", "sel.last")
        globalvars.notes.tag_add("underline", "sel.first", "sel.last")
    else:
        if "bold" in current_tags:
            globalvars.notes.tag_remove("bold", "sel.first", "sel.last")
            globalvars.notes.tag_add("bold_strikethrough", "sel.first", "sel.last")
        elif "italic" in current_tags:
            globalvars.notes.tag_remove("italic", "sel.first", "sel.last")
            globalvars.notes.tag_add("italic_strikethrough", "sel.first", "sel.last")
        elif "underline" in current_tags:
            globalvars.notes.tag_remove("underline", "sel.first", "sel.last")
            globalvars.notes.tag_add("underline_strikethrough", "sel.first", "sel.last")
        else:
            globalvars.notes.tag_add("strikethrough", "sel.first", "sel.last")

    return "break"
