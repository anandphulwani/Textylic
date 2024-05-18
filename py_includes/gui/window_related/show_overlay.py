import tkinter
from ... import globalvars

def show_overlay():
    x, y = globalvars.window.winfo_x(), globalvars.window.winfo_y()
    width, height = globalvars.window.winfo_width(), globalvars.window.winfo_height()

    globalvars.overlay = tkinter.Toplevel(globalvars.root)
    globalvars.overlay.attributes("-alpha", 0.90)  # Adjust transparency
    globalvars.overlay.geometry(f"{width}x{height}+{x}+{y}")
    globalvars.overlay.overrideredirect(1)
    globalvars.overlay.grab_set()

    canvas = tkinter.Canvas(globalvars.overlay, width=width, height=height, bd=0, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    canvas.create_rectangle(0, 0, width, height, fill="#333")  # , stipple="gray25")

    overlay_label = tkinter.Label(globalvars.overlay, text="Loading...", font=("Arial", 16), bg="#333", fg="white")
    overlay_label.place(relx=0.5, rely=0.5, anchor="center")

    globalvars.isOverlayEnabled = True
