from .... import globalvars
from ....enums.Color import Color

def setColor():
    """Change Text Color"""
    
    color_settings = globalvars.color_map[globalvars.currentThemeColor]
    notesfrm_color = color_settings["notesfrm_color"]
    globalvars.notes.tag_configure("emphColor", foreground=notesfrm_color)

    current_tags = globalvars.notes.tag_names("sel.first")
    
    if "emphColor" in current_tags:
        globalvars.notes.tag_remove("emphColor", "sel.first", "sel.last")
    else:
        globalvars.notes.tag_add("emphColor", "sel.first", "sel.last")

    return "break"
