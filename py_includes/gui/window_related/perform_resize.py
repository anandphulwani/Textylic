from ... import globalvars

def perform_resize(event):
    delta_x = event.x_root - globalvars.start_x
    delta_y = event.y_root - globalvars.start_y
    new_width = globalvars.start_width + delta_x
    new_height = globalvars.start_height + delta_y
    globalvars.window.geometry(f"{new_width}x{new_height}")
