import win32gui
import win32con

def is_topmost(hwnd):
    ex_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
    return bool(ex_style & win32con.WS_EX_TOPMOST)
