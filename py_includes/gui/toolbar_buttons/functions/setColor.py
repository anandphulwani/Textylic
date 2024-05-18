from .... import globalvars
from ....enums.Color import Color

def setColor():
    """Change Text Color"""

    if globalvars.currentThemeColor == Color.YELLOW:
        globalvars.notes.tag_configure("emphColor", foreground="#E6B905")
    elif globalvars.currentThemeColor == Color.PINK:
        globalvars.notes.tag_configure("emphColor", foreground="#EB8EC6")
    elif globalvars.currentThemeColor == Color.GREEN:
        globalvars.notes.tag_configure("emphColor", foreground="#65BA5A")
    elif globalvars.currentThemeColor == Color.BLUE:
        globalvars.notes.tag_configure("emphColor", foreground="#59C0E7")
    current_tags = globalvars.notes.tag_names("sel.first")

    if "emphColor" in current_tags:
        globalvars.notes.tag_remove("emphColor", "sel.first", "sel.last")
    else:
        globalvars.notes.tag_add("emphColor", "sel.first", "sel.last")

    return "break"
