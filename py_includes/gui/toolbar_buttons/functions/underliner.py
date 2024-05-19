from ....helpers.configure_font import configure_font
from .... import globalvars

def underliner(_=False):
    """Underline button function"""

    underline_font = configure_font(globalvars.notes.cget("font"), underline=True)
    bold_underline_font = configure_font(globalvars.notes.cget("font"), underline=True, weight="bold")
    italic_underline_font = configure_font(globalvars.notes.cget("font"), underline=True, slant="italic")
    strikethrough_underline_font = configure_font(globalvars.notes.cget("font"), overstrike=True, underline=True)

    globalvars.notes.tag_configure("underline", font=underline_font)
    globalvars.notes.tag_configure("bold_underline", font=bold_underline_font)
    globalvars.notes.tag_configure("italic_underline", font=italic_underline_font)
    globalvars.notes.tag_configure("strikethrough_underline", font=strikethrough_underline_font)

    current_tags = globalvars.notes.tag_names("sel.first")

    if "underline" in current_tags:
        globalvars.notes.tag_remove("underline", "sel.first", "sel.last")
    elif "bold_underline" in current_tags:
        globalvars.notes.tag_remove("bold_underline", "sel.first", "sel.last")
        globalvars.notes.tag_add("bold", "sel.first", "sel.last")
    elif "italic_underline" in current_tags:
        globalvars.notes.tag_remove("italic_underline", "sel.first", "sel.last")
        globalvars.notes.tag_add("italic", "sel.first", "sel.last")
    elif "strikethrough_underline" in current_tags:
        globalvars.notes.tag_remove("strikethrough_underline", "sel.first", "sel.last")
        globalvars.notes.tag_add("strikethrough", "sel.first", "sel.last")
    else:
        if "bold" in current_tags:
            globalvars.notes.tag_add("bold_underline", "sel.first", "sel.last")
            globalvars.notes.tag_remove("bold", "sel.first", "sel.last")
        elif "italic" in current_tags:
            globalvars.notes.tag_add("italic_underline", "sel.first", "sel.last")
            globalvars.notes.tag_remove("italic", "sel.first", "sel.last")
        elif "strikethrough" in current_tags:
            globalvars.notes.tag_add("strikethrough_underline", "sel.first", "sel.last")
            globalvars.notes.tag_remove("strikethrough", "sel.first", "sel.last")
        else:
            globalvars.notes.tag_add("underline", "sel.first", "sel.last")

    return "break"
