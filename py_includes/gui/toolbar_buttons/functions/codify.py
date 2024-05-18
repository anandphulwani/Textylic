from .... import globalvars
from ....helpers.is_font_present import is_font_present

def codify(_=False):
    """Code button function"""

    desired_font = ("JetBrainsMono NF", 10) if is_font_present("JetBrainsMono NF") else "Consolas 11"
    globalvars.notes.tag_configure("code", font=desired_font)
    current_tags = globalvars.notes.tag_names("sel.first")

    if "code" in current_tags:
        globalvars.notes.tag_remove("code", "sel.first", "sel.last")
    else:
        globalvars.notes.tag_add("code", "sel.first", "sel.last")
    return "break"
