import tkinter
from tkinter import ttk

from . import globalvars
from .gui.window_related.configure_scrollbar_style import configure_scrollbar_style
from .gui.window_related.check_and_create_colored_scrollbar_if_not_exist import check_and_create_colored_scrollbar_if_not_exist
from .gui.window_related.load_theme import load_theme
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

        check_and_create_colored_scrollbar_if_not_exist(bg_color)
        
        existing_themes = ttk.Style().theme_names()
        if bg_color not in existing_themes:
            theme = load_theme(f'.\\themes\\{bg_color}.tcl')
            globalvars.root.tk.eval(theme)
        
        # Configure scrollbar style with new colors
        configure_scrollbar_style("Custom", bg_color, trough_color="#000000", thumb_color="#000000", arrow_color="#000000")
        # Ensure scrollbar and notes share the same parent
        scrollbar = ttk.Scrollbar(globalvars.notesFrame, orient=tkinter.VERTICAL, command=globalvars.notes.yview, style="Custom.Vertical.TScrollbar")
        scrollbar.grid(row=0, column=5, sticky="NS")
        globalvars.notes.config(yscrollcommand=scrollbar.set)

        globalvars.titleBar.configure(bg=bg_color)
        globalvars.menu_button.configure(activebackground=bg_color)
        globalvars.notes.tag_configure("emphColor", foreground=bg_color)
        globalvars.window.update()
