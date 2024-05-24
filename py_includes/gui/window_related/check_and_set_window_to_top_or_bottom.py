import ctypes
from ...helpers.add_always_on_top import add_always_on_top
from ...helpers.remove_always_on_top import remove_always_on_top
from ...helpers.is_topmost import is_topmost
from ...helpers.get_hwnd import get_hwnd
from ...helpers.get_executable_name import get_executable_name
from ...helpers.get_window_class_name import get_window_class_name
from ...helpers.get_z_order import get_z_order
from ... import globalvars

SWP_NOMOVE = 0x0002
SWP_NOSIZE = 0x0001
SWP_NOACTIVATE = 0x0010
HWND_TOPMOST = -1
  
# Function to periodically check and set the window to the bottom
def check_and_set_window_to_top_or_bottom():
    hwnd = get_hwnd(globalvars.window)
    
    if globalvars.current_focus_mode == "lock" and not is_topmost(hwnd):
        globalvars.focus_lockapp_window = None
        add_always_on_top(hwnd)
    elif globalvars.current_focus_mode == "lockapp":
        hwnd_top = globalvars.user32.GetForegroundWindow()
        if not (get_executable_name(hwnd_top) == 'C:\\Windows\\explorer.exe' and get_window_class_name(hwnd_top) == 'Shell_TrayWnd'):
            if hwnd_top != "" and hwnd_top != hwnd:
                if globalvars.focus_lockapp_window == None:
                    globalvars.focus_lockapp_window = hwnd_top
                if hwnd_top == globalvars.focus_lockapp_window and not is_topmost(hwnd):
                    add_always_on_top(hwnd)
                else:
                    remove_always_on_top(hwnd)
        else:
            remove_always_on_top(hwnd)
    elif globalvars.current_focus_mode == "unlock":
        globalvars.focus_lockapp_window = None
        z_order = get_z_order(hwnd)
        if z_order != 'donothing':
            if z_order == 'forcetop':
                add_always_on_top(hwnd)
            elif globalvars.window_is_focused == True and z_order != 'top':
                # Setting the window to the top
                ctypes.windll.user32.SetWindowPos(hwnd, HWND_TOPMOST, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE)
            elif globalvars.window_is_focused == False and z_order != 'bottom':
                # Setting the window to the bottom
                ctypes.windll.user32.SetWindowPos(hwnd, 1, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE | SWP_NOACTIVATE)
                # Setting the desktop as the foreground window
                hwnd_desktop = ctypes.windll.user32.GetDesktopWindow()
                ctypes.windll.user32.SetForegroundWindow(hwnd_desktop)
    globalvars.window.after(100, check_and_set_window_to_top_or_bottom)
