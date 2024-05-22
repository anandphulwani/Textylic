from pywinauto import Desktop

def is_window_at_bottom(window_title):
    all_windows = Desktop(backend="uia").windows()
    for win in reversed(all_windows):
        if win.window_text() == "" or win.window_text() == "Program Manager":
            continue
        if win.window_text() == window_title:
            return True
        else:
            return False
    return False
