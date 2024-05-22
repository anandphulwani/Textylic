import ctypes

# Function to get the handle of the window
def get_hwnd(window):
    return ctypes.windll.user32.GetParent(window.winfo_id())
