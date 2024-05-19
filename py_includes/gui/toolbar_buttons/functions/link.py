from .... import globalvars
import tkinter as tk
from ....helpers.tags import remove_tag, update_tag, get_current_tags

def link(_=False):
    """Link button function"""
    try:
        current_tags = get_current_tags(globalvars.notes)
        # print(f'current_tags: {current_tags}')
        if "link" in current_tags:
            remove_tag(globalvars.notes, "link")
        else:
            update_tag(globalvars.notes, "link")
    except tk.TclError:
        pass
    return "break"
