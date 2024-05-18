import tkinter
from . import globalvars
from .enums.Color import Color

def set_color_theme(color: Color):
    """Set the accent color and update theme flags"""

    if color in globalvars.color_map:
        color_settings = globalvars.color_map[color]
        bg_color = color_settings["bg"]
        
        globalvars.currentThemeColor = color

        for item in globalvars.accentItems:
            item.configure(bg=bg_color)
            if not isinstance(item, tkinter.Frame):
                item.configure(activebackground=bg_color)

        globalvars.titleBar.configure(bg=bg_color)
        globalvars.menu_button.configure(activebackground=bg_color)
        globalvars.notes.tag_configure("emphColor", foreground=bg_color)
        globalvars.window.update()
