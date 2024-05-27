import uuid
import tkinter
import tkinter.messagebox
import os
import sys
import argparse
import tkinter.ttk
from random import randint
from tkinter import font, PhotoImage, ttk
from string import ascii_uppercase

from py_includes import globalvars
from py_includes.color_theme import set_color_theme
from py_includes.dpi_aware import MakeTkDPIAware
from py_includes.gui.focus_related.on_focus_in import on_focus_in
from py_includes.gui.focus_related.on_focus_out import on_focus_out
from py_includes.gui.functions.openFile import openFile, setup_tags
from py_includes.gui.shortcuts_binding import attach_keyboard_shortcuts
from py_includes.gui.toolbar_buttons.create_bottom_menu import create_bottom_menu
from py_includes.gui.window_related.perform_resize import perform_resize
from py_includes.gui.window_related.start_resize import start_resize
from py_includes.gui.window_related.check_and_set_window_to_top_or_bottom import check_and_set_window_to_top_or_bottom
from py_includes.gui.toolbar_buttons.create_top_menu import create_top_menu
from py_includes.helpers.get_button_images import get_button_images
from py_includes.images import load_images
from py_includes.images_effects import mapping_button_images
from py_includes.notes_functions.autoReload import autoReload
from py_includes.notes_functions.autoSave import autoSave

# Argument Parser
parser = argparse.ArgumentParser(description="Open a file")
parser.add_argument("file", default=None, nargs="?", help="Name of the file to load")

args = parser.parse_args()

globalvars.root = tkinter.Tk()
globalvars.root.withdraw()

globalvars.window = tkinter.Toplevel()
globalvars.window.title("Textylic")
MakeTkDPIAware(globalvars.window)
globalvars.window.attributes("-toolwindow", True, "-alpha", "0.99")

globalvars.window.overrideredirect(True)
globalvars.window.config(bg="#040412")
globalvars.window.wait_visibility(globalvars.window)

icon = PhotoImage(file="./res/images/icons/iconx32.png")
globalvars.root.iconphoto(True, icon)

# Configuring grid
globalvars.window.grid_columnconfigure(0, weight=1)
globalvars.window.grid_columnconfigure(1, weight=1)
globalvars.window.grid_rowconfigure(1, weight=1)

globalvars.smallPaddingX = globalvars.window.TkScale(5)
globalvars.smallPaddingY = globalvars.window.TkScale(4)

images = []  # The list with all images, index, and name

# Default values of the themes
load_images()

def fetchDrivePath() -> str:
    """The drive in which the script is running"""
    for drive in ascii_uppercase:
        if os.path.exists(f"{drive}:\\Users"):
            return drive + ":\\"
    return ""

winDrive = fetchDrivePath()  # The windows directory letter

# Notes Text widget container
globalvars.notesFrame = tkinter.Frame(
    globalvars.window,
    relief="flat",
    bg="#040412",
    height=globalvars.window.TkScale(244),
    width=globalvars.window.TkScale(320),
)
globalvars.notesFrame.grid(row=1, column=0, columnspan=5, sticky="NSEW")
globalvars.notesFrame.grid_rowconfigure(0, weight=1)
globalvars.notesFrame.grid_columnconfigure(0, weight=1)

# Main Text input
globalvars.notes = tkinter.Text(
    globalvars.notesFrame,
    undo=True,
    font="Arial 11",
    bg="#040412",
    padx=globalvars.smallPaddingX,
    pady=10,
    bd=0,
    fg="white",
    insertbackground="white",
    relief="flat",
    selectbackground="#30324c",
    wrap="word",
    height=10.5,
    width=39,
    tabs=("0.5c", "3c", "5c"),
)
globalvars.notes.grid(row=0, column=0, rowspan=5, columnspan=5, sticky="NSEW")
globalvars.notes.delete("1.0", "end")
segoe_font = font.Font(globalvars.notes, globalvars.notes.cget("font"))
# globalvars.window.update_idletasks()
segoe_font.configure(family="Arial", size=globalvars.window.TkScale(11))
globalvars.notes.configure(font=segoe_font)

setup_tags()

create_top_menu()
create_bottom_menu()

# Positioning title bar and adding drag function
globalvars.titleBar.grid(row=0, column=0, columnspan=5, sticky="WE")
globalvars.titleBar.grid_columnconfigure(5, weight=1)
globalvars.titleBar.grid_columnconfigure(6, weight=0)

attach_keyboard_shortcuts()

# Mapping of buttons to their images, Generate buttons dictionary and apply hover effects
buttons = get_button_images(globalvars.window)
mapping_button_images(buttons)

# Bind the focus events
globalvars.window.bind("<FocusIn>", on_focus_in)
globalvars.window.bind("<FocusOut>", on_focus_out)

# Desktop Gadget and Autosave
globalvars.window.after(200, check_and_set_window_to_top_or_bottom)
globalvars.window.after(3000, autoSave)
globalvars.window.after(3000, autoReload)

# Open a file
if args.file is not None:
    file_path = os.path.join(globalvars.dataPath, args.file)
    if not os.path.exists(file_path):
        tkinter.messagebox.showerror("Error", f"File {args.file} does not exist.")
        sys.exit(1)
    openFile(args.file)
else:
    unsaved_data_path = os.path.join(globalvars.dataPath, "unsaved")
    if not os.path.exists(unsaved_data_path):
        os.makedirs(unsaved_data_path)

    random_filename = str(uuid.uuid4()) + ".txtlyc"
    file_path = os.path.join(unsaved_data_path, random_filename)

    # Check if file exists
    if os.path.exists(file_path):
        tkinter.messagebox.showerror("Error", f"File {random_filename} already exists.")
        sys.exit(1)  # Exit the application
    else:
        # Create and save a blank file
        with open(file_path, "w") as file:
            file.write("")
        globalvars.window.geometry(globalvars.window.TkGeometryScale(f"310x310+{str(randint(10, 900))}+{str(randint(10, 500))}"))

# Add the style for the gripper which resizes the window
style = ttk.Style()
style.layout("Black.TSizegrip", [("Sizegrip.sizegrip", {"sticky": "nswe"})])
style.configure("Black.TSizegrip", background="#181926", foreground="#181926")

# Add the gripper for resizing the window with the new style
grip = ttk.Sizegrip(globalvars.window, style="Black.TSizegrip")
grip.place(relx=1.0, rely=1.0, anchor="se")

# Bind mouse events for resizing
grip.bind("<ButtonPress-1>", start_resize)
grip.bind("<B1-Motion>", perform_resize)

# Update the window
globalvars.window.deiconify()
globalvars.root.mainloop()
