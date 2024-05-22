import ctypes
from .. import globalvars

# Function to get the window title (name) of a window
def get_window_title(hwnd):
    length = globalvars.user32.GetWindowTextLengthW(hwnd)
    buffer = ctypes.create_unicode_buffer(length + 1)
    globalvars.user32.GetWindowTextW(hwnd, buffer, length + 1)
    return buffer.value
