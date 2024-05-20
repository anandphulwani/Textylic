from ....helpers.configure_font import configure_font
from ....helpers.tags import remove_tag, update_tag, get_current_tag_as_string
from .... import globalvars
import tkinter as tk

def strikethrough(_=False):
    """Strikethrough button function"""
    try:
        current_tags = get_current_tag_as_string(globalvars.notes)
        if "strikethrough" in current_tags:
            remove_tag(globalvars.notes, "strikethrough")
        else:
            update_tag(globalvars.notes, "strikethrough")
    except tk.TclError:
        pass
    return "break"
