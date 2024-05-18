import tkinter
from ... import globalvars

def create_button(parent, image, command, row, column, padx, pady, sticky="W", bg="#181926", active_bg="#181926", bd=0, fg="white", add_to_accent_items=False):
    button = tkinter.Button(parent, image=image, bd=bd, bg=bg, command=command, activebackground=active_bg, fg=fg, padx=3, pady=4)
    button.image = image
    button.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)

    if add_to_accent_items:
        globalvars.accentItems.append(button)

    return button
