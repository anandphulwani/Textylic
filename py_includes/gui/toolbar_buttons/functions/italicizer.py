from ....helpers.configure_font import configure_font
from ....helpers.tags import remove_tag, update_tag, get_current_tag_as_string
from .... import globalvars
import tkinter as tk

def italicizer(_=False):
    """Italic button function"""
    try:
        current_tags = get_current_tag_as_string(globalvars.notes)
        if "italic" in current_tags:
            remove_tag(globalvars.notes, "italic")
        else:
            update_tag(globalvars.notes, "italic")
    except tk.TclError:
        pass
    return "break"
