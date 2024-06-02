import win32gui
import win32con
from .. import globalvars

def get_z_ordered_windows():
    hwnd = win32gui.GetTopWindow(None)
    z_ordered_windows = []
    while hwnd:
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            z_ordered_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
        hwnd = win32gui.GetWindow(hwnd, win32con.GW_HWNDNEXT)
    return z_ordered_windows

def compare_z_order():
    prev_z_order = globalvars.prev_z_order
    new_z_order = get_z_ordered_windows()
    returnValue = True
    if len(prev_z_order) != len(new_z_order):
        returnValue = False
    else:
        for old, new in zip(prev_z_order, new_z_order):
            if old != new:
                returnValue = False
                break
    globalvars.prev_z_order = new_z_order
    return returnValue
