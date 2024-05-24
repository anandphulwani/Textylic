from tkinter import PhotoImage
from . import globalvars

def load_image(button_name, suffix=""):
    sizeConstantForButtons = 310
    file_path = f"res/images/iconset/{button_name}{suffix}.png"
    return PhotoImage(file=file_path).zoom(int(sizeConstantForButtons * 0.07)).subsample(30)

def load_images():
    button_names = [
        "new", "save", "openlink", "menu", "focusunlock", "focuslock", "focuslockapp",
        "close", "bold", "italic", "underline", "strikethrough", "bullet", "code", 
        "createlink", "colortext", "photoinsert"
    ]
    
    for name in button_names:
        setattr(globalvars.window, f"{name}ButtonImage", load_image(name))
        setattr(globalvars.window, f"{name}ButtonImageAfter", load_image(name, "1"))
