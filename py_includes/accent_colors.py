import tkinter

def set_accent_color(window, accentItems, titleBar, menu, notes, bg_color, pink, yellow, green, blue):
    """Set the accent color and update theme flags"""
    global pinkTheme
    global yellowTheme
    global greenTheme
    global blueTheme
    pinkTheme = pink
    yellowTheme = yellow
    greenTheme = green
    blueTheme = blue
    
    for item in accentItems:
        item.configure(bg=bg_color)
        if not isinstance(item, tkinter.Frame):
            item.configure(activebackground=bg_color)
    
    titleBar.configure(bg=bg_color)
    menu.configure(activebackground=bg_color)
    notes.tag_configure("emphColor", foreground=bg_color)
    window.update()

def accentpink(window, accentItems, titleBar, menu, notes):
    """Pink accent color"""
    set_accent_color(window, accentItems, titleBar, menu, notes, "#EB8EC6", True, False, False, False)

def accentyellow(window, accentItems, titleBar, menu, notes):
    """Yellow accent color"""
    set_accent_color(window, accentItems, titleBar, menu, notes, "#fbc02d", False, True, False, False)

def accentgreen(window, accentItems, titleBar, menu, notes):
    """Green accent color"""
    set_accent_color(window, accentItems, titleBar, menu, notes, "#65BA5A", False, False, True, False)

def accentblue(window, accentItems, titleBar, menu, notes):
    """Blue accent color"""
    set_accent_color(window, accentItems, titleBar, menu, notes, "#2292ff", False, False, False, True)
