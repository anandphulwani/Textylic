from .... import globalvars
# from ....enums.Color import Color
import tkinter as tk
from ....helpers.tags import remove_tag, update_tag, get_current_tag_as_string

def setColor():
    """Change Text Color"""    
    try:
        current_tags = get_current_tag_as_string(globalvars.notes)
        # print(f'current_tags: {current_tags}')
        if "colortext" in current_tags:
            remove_tag(globalvars.notes, "colortext")
        else:
            update_tag(globalvars.notes, "colortext")
    except tk.TclError:
        pass
    return "break"
