import ctypes
import win32gui
import win32con
from ...helpers.get_hwnd import get_hwnd
from ...helpers.get_z_order import get_z_order
from ... import globalvars

SWP_NOMOVE = 0x0002
SWP_NOSIZE = 0x0001
SWP_NOACTIVATE = 0x0010
HWND_TOPMOST = -1

# Function to periodically check and set the window to the bottom
def check_and_set_window_to_top_or_bottom():
    hwnd = get_hwnd(globalvars.window)
    z_order = get_z_order(hwnd)
    
    if z_order == 'donothing':
        pass
    if z_order == 'forcetop':
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_TOPMOST)
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_NOACTIVATE)
    elif globalvars.window_is_focused == True and z_order != 'top':
        print(f'Setting the window to the TOP, window_is_focused: {globalvars.window_is_focused}, z_order: {z_order}')
        # Setting the window to the top
        ctypes.windll.user32.SetWindowPos(hwnd, HWND_TOPMOST, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE)
    elif globalvars.window_is_focused == False and z_order != 'bottom':
        print(f'Setting the window to the BOTTOM, window_is_focused: {globalvars.window_is_focused}, z_order: {z_order}')
        # Setting the window to the bottom
        ctypes.windll.user32.SetWindowPos(hwnd, 1, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE | SWP_NOACTIVATE)
        # Setting the desktop as the foreground window
        hwnd_desktop = ctypes.windll.user32.GetDesktopWindow()
        ctypes.windll.user32.SetForegroundWindow(hwnd_desktop)
    globalvars.window.after(100, check_and_set_window_to_top_or_bottom)
