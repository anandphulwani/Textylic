from .... import globalvars
from ....helpers.configure_font import configure_font

def bolder(_=False):
    """Bold button function"""

    bold_font = configure_font(globalvars.notes.cget("font"), weight="bold")
    italic_bold_font = configure_font(globalvars.notes.cget("font"), slant="italic", weight="bold")
    underline_bold_font = configure_font(globalvars.notes.cget("font"), underline=True, weight="bold")
    strikethrough_bold_font = configure_font(globalvars.notes.cget("font"), overstrike=True, weight="bold")

    globalvars.notes.tag_configure("bold", font=bold_font)
    globalvars.notes.tag_configure("italic_bold", font=italic_bold_font)
    globalvars.notes.tag_configure("underline_bold", font=underline_bold_font)
    globalvars.notes.tag_configure("strikethrough_bold", font=strikethrough_bold_font)

    current_tags = globalvars.notes.tag_names("sel.first")

    if "bold" in current_tags:
        globalvars.notes.tag_remove("bold", "sel.first", "sel.last")
    elif "italic_bold" in current_tags:
        globalvars.notes.tag_remove("italic_bold", "sel.first", "sel.last")
        globalvars.notes.tag_add("italic", "sel.first", "sel.last")
    elif "underline_bold" in current_tags:
        globalvars.notes.tag_remove("underline_bold", "sel.first", "sel.last")
        globalvars.notes.tag_add("underline", "sel.first", "sel.last")
    elif "strikethrough_bold" in current_tags:
        globalvars.notes.tag_remove("strikethrough_bold", "sel.first", "sel.last")
        globalvars.notes.tag_add("strikethrough", "sel.first", "sel.last")
    else:
        if "italic" in current_tags:
            globalvars.notes.tag_remove("italic", "sel.first", "sel.last")
            globalvars.notes.tag_add("italic_bold", "sel.first", "sel.last")
        elif "underline" in current_tags:
            globalvars.notes.tag_remove("underline", "sel.first", "sel.last")
            globalvars.notes.tag_add("underline_bold", "sel.first", "sel.last")
        elif "strikethrough" in current_tags:
            globalvars.notes.tag_remove("strikethrough", "sel.first", "sel.last")
            globalvars.notes.tag_add("strikethrough_bold", "sel.first", "sel.last")
        else:
            globalvars.notes.tag_add("bold", "sel.first", "sel.last")

    return "break"
