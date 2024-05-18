import tkinter
from tkinter import font
from ...enums.Color import Color
from ... import globalvars
from ..functions.clearCache import clearCache
from ..functions.createNewWindow import createNewWindow
from ..functions.openFileChoose import openFileChoose
from ..functions.openLink import openLink
from ..functions.openNotesList import openNotesList
from ..functions.openReadme import openReadme
from ..functions.saveNote import saveNote
from ..functions.windowdestroy import windowdestroy
from ...color_theme import set_color_theme

def create_button(parent, image, command, row, column, padx, pady, sticky="W", bg="#2292FF", active_bg="#2292FF"):
    """Create a button and add it to the accent items list."""
    button = tkinter.Button(
        parent,
        image=image,
        bd=0,
        bg=bg,
        activebackground=active_bg,
        command=command,
    )
    button.image = image
    button.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)
    globalvars.accentItems.append(button)
    return button


def create_menu_button(parent, image, menu_config, row, column, padx, pady, bg="#2292FF", active_bg="#2292FF"):
    """Create a menu button, configure it, and add it to the accent items list."""
    btn = tkinter.Menubutton(parent, image=image, bd=0, bg=bg, relief="flat", activebackground=active_bg)
    btn.image = image
    btn.grid(row=row, column=column, padx=padx, pady=pady, sticky="W")
    globalvars.accentItems.append(btn)

    menu = tkinter.Menu(
        btn, tearoff=0, bd=0, relief="solid", font=menu_config["font"], activeborderwidth=0, activebackground="#c4c4c4", activeforeground="#000000", selectcolor="black"
    )
    btn["menu"] = menu
    btn.menu = menu

    return btn


def create_top_menu():
    """
    Creates the top menu bar.

    Args:
        None

    Returns:
        None
    """
    # Defining Title Bar Elements
    globalvars.titleBar = tkinter.Frame(globalvars.window, relief="flat", bg="#2292FF")
    globalvars.titleBar.grid(row=0, column=0, sticky="ew")

    # Configure font for menu
    segoe_font_menu = font.Font(family="Arial", size=globalvars.window.TkScale(10))

    # Create buttons
    globalvars.top_menu_buttons = {}
    globalvars.top_menu_buttons["new"] = create_button(
        globalvars.titleBar, globalvars.window.newButtonImage, createNewWindow, 0, 0, globalvars.smallPaddingX, globalvars.smallPaddingY
    )
    globalvars.top_menu_buttons["save"] = create_button(globalvars.titleBar, globalvars.window.saveButtonImage, saveNote, 0, 1, globalvars.smallPaddingX, globalvars.smallPaddingY)
    globalvars.top_menu_buttons["openlink"] = create_button(
        globalvars.titleBar, globalvars.window.openlinkButtonImage, openLink, 0, 2, globalvars.smallPaddingX, globalvars.smallPaddingY
    )

    # Create menu button and its menu
    globalvars.menu_button = create_menu_button(
        globalvars.titleBar, globalvars.window.menuButtonImage, {"font": segoe_font_menu}, 0, 3, globalvars.smallPaddingX, globalvars.smallPaddingY
    )
    menu = globalvars.menu_button.menu

    # Add commands to the menu
    menu.add_command(label="Choose theme:")
    for color in Color:
        menu.add_radiobutton(label=color.label(), command=lambda c=color: set_color_theme(c))
    menu.add_separator()
    menu.add_command(label="Open Note", command=openFileChoose)
    menu.add_command(label="Save Note", command=saveNote, accelerator="(Ctr+s)")

    # Create advanced menu
    advancedMenu = tkinter.Menu(
        menu, tearoff=0, bd=0, relief="solid", font=segoe_font_menu, activeborderwidth=0, activebackground="#c4c4c4", activeforeground="#000000", selectcolor="black"
    )
    advancedMenu.add_command(label="Notes List", command=openNotesList)
    advancedMenu.add_command(label="Clear Cache", command=clearCache)
    # advancedMenu.add_command(label="Minimize to systray", command=minSysTray)
    menu.add_cascade(label="More...", menu=advancedMenu)

    menu.add_separator()
    menu.add_command(label="Undo", command=globalvars.notes.edit_undo, accelerator="(Ctr+z)")
    menu.add_command(label="Redo", command=globalvars.notes.edit_redo, accelerator="(Ctr+y)")
    menu.add_command(label="Quit", command=windowdestroy, accelerator="(Ctr+q)")
    menu.add_command(label="Help/About", command=openReadme)

    # Spacer
    spacer = tkinter.Frame(globalvars.titleBar, bg="#2292FF")
    spacer.grid(row=0, column=4, sticky="ew")
    globalvars.accentItems.append(spacer)

    # Create close button
    globalvars.top_menu_buttons["close"] = create_button(
        globalvars.titleBar,
        globalvars.window.closeButtonImage,
        windowdestroy,
        0,
        5,
        (globalvars.window.TkScale(10), globalvars.window.TkScale(10)),
        globalvars.smallPaddingY,
        sticky="E",
    )
