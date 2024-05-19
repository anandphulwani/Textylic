from .... import globalvars
from ....helpers.tags import remove_tag, update_tag, get_current_tags
import tkinter as tk

def bolder(_=False):
    """Bold button function"""
    try:
        current_tags = get_current_tags(globalvars.notes)
        # print(f'current_tags: {current_tags}')
        if "bold" in current_tags:
            remove_tag(globalvars.notes, "bold")
        else:
            update_tag(globalvars.notes, "bold")
    except tk.TclError:
        pass
    return "break"
