import os
import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk
from ...gui.functions.saveNote import saveNote

class saveAsFolderNameDialog(simpledialog.Dialog):
    def __init__(self, parent, title, initialdir):
        self.initialdir = initialdir
        self.folder_exists = False
        self.validation_photo = None
        super().__init__(parent, title)

    def body(self, master):
        self.geometry("272x80") 
        tk.Label(master, text="Enter notes name:").grid(row=0, column=0)
        self.entry = tk.Entry(master)
        self.entry.grid(row=0, column=1)
        self.entry.bind("<KeyPress>", lambda event: self.check_folder_exists(event, master))
        self.entry.bind("<KeyRelease>", lambda event: self.check_folder_exists(event, master))

        # Placeholder for the image
        self.image_label = tk.Label(master)
        self.image_label.grid(row=0, column=2, padx=(5, 0), pady=5)
        self.update_image("res/images/iconsetx20/blank.png", master)
        saveNote()
        return self.entry

    def check_folder_exists(self, _, master):
        folder_name = self.entry.get()
        folder_path = os.path.join(self.initialdir, folder_name)
        if os.path.exists(folder_path):
            self.folder_exists = True
            self.ok_button.config(state=tk.DISABLED)
            self.update_image("res/images/iconsetx20/cross.png", master)
        else:
            self.folder_exists = False
            self.ok_button.config(state=tk.NORMAL)
            self.update_image("res/images/iconsetx20/check.png", master)

    def update_image(self, image_path, master):
        image = Image.open(image_path)
        image = image.resize((20, 20), Image.LANCZOS)  # Adjust size as needed
        self.validation_photo = ImageTk.PhotoImage(image, master=master)
        self.image_label.config(image=self.validation_photo)
        self.image_label.image  = self.validation_photo  # Keep a reference to avoid garbage collection

    def buttonbox(self):
        box = tk.Frame(self)
        self.ok_button = tk.Button(box, text="OK", width=10, command=self.ok, state=tk.DISABLED)
        self.ok_button.pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(box, text="Cancel", width=10, command=self.cancel).pack(side=tk.LEFT, padx=5, pady=5)
        box.pack()

    def apply(self):
        self.result = self.entry.get()
