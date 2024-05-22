import ctypes
from .. import globalvars

# Function to get the window class name of a window
def get_window_class_name(hwnd):
    buffer = ctypes.create_unicode_buffer(256)
    globalvars.user32.GetClassNameW(hwnd, buffer, 256)
    return buffer.value
