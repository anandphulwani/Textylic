from ... import globalvars

def start_resize(event):
    globalvars.start_x = event.x_root
    globalvars.start_y = event.y_root
    globalvars.start_width = globalvars.window.winfo_width()
    globalvars.start_height = globalvars.window.winfo_height()
