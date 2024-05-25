from .. import globalvars

def get_window_coordinates():
    x, y = globalvars.window.winfo_x(), globalvars.window.winfo_y()
    width, height = globalvars.window.winfo_width(), globalvars.window.winfo_height()
    return (x, y, width, height)
