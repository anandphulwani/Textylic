from .... import globalvars
from ....helpers.is_font_present import is_font_present
from ....helpers.tags import remove_tag, update_tag, get_current_tags
import tkinter as tk

def codify(_=False):
    """Code button function"""
    try:
        current_tags = get_current_tags(globalvars.notes)
        # print(f'current_tags: {current_tags}')
        if "code" in current_tags:
            remove_tag(globalvars.notes, "code")
        else:
            update_tag(globalvars.notes, "code")
    except tk.TclError:
        pass
    return "break"
