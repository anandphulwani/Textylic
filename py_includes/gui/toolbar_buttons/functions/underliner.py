from ....helpers.configure_font import configure_font
from ....helpers.tags import remove_tag, update_tag, get_current_tags
from .... import globalvars
import tkinter as tk

def underliner(_=False):
    """Underline button function"""
    try:
        current_tags = get_current_tags(globalvars.notes)
        if "underline" in current_tags:
            remove_tag(globalvars.notes, "underline")
        else:
            update_tag(globalvars.notes, "underline")
    except tk.TclError:
        pass
    return "break"
