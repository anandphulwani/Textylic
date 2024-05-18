from ... import globalvars

def on_focus_out(event):
    globalvars.window_is_focused = False
