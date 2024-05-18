import tkinter
from . import globalvars
from .enums.Color import Color

def set_color_theme(color: Color):
    """Set the accent color and update theme flags"""
    if color == Color.BLUE:
        bg_color = "#2292FF"
    elif color == Color.YELLOW:
        bg_color = "#FBC02d"
    elif color == Color.GREEN:
        bg_color = "#65BA5A"
    elif color == Color.PINK:
        bg_color = "#EB8EC6"
    
    globalvars.currentThemeColor = color
    
    for item in globalvars.accentItems:
        item.configure(bg=bg_color)
        if not isinstance(item, tkinter.Frame):
            item.configure(activebackground=bg_color)
    
    globalvars.titleBar.configure(bg=bg_color)
    globalvars.menu_button.configure(activebackground=bg_color)
    globalvars.notes.tag_configure("emphColor", foreground=bg_color)
    globalvars.window.update()
