import ctypes
from ...helpers.get_hwnd import get_hwnd
from ...helpers.get_z_order import get_z_order
from ... import globalvars

SWP_NOMOVE = 0x0002
SWP_NOSIZE = 0x0001
SWP_NOACTIVATE = 0x0010

# Function to periodically check and set the window to the bottom
def check_and_set_window_to_top_or_bottom():
    hwnd = get_hwnd(globalvars.window)
    z_order = get_z_order(hwnd)
    if globalvars.window_is_focused == True and z_order != 'top':
        # Setting the window to the top
        ctypes.windll.user32.SetWindowPos(hwnd, -1, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE)
    elif globalvars.window_is_focused == False and z_order != 'bottom':
        # Setting the window to the bottom
        ctypes.windll.user32.SetWindowPos(hwnd, 1, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE | SWP_NOACTIVATE)
        # Setting the desktop as the foreground window
        hwnd_desktop = ctypes.windll.user32.GetDesktopWindow()
        ctypes.windll.user32.SetForegroundWindow(hwnd_desktop)
    else:
        print('')
    globalvars.window.after(500, check_and_set_window_to_top_or_bottom)
