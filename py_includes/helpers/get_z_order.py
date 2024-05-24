from ..helpers.get_window_class_name import get_window_class_name
from ..helpers.get_executable_name import get_executable_name
from ..helpers.get_window_title import get_window_title
from ..helpers.is_child_window import is_child_window
from ..helpers.is_window_at_bottom import is_window_at_bottom
from ..helpers.is_topmost import is_topmost

from .. import globalvars

# Function to get the Z-order of a window
def get_z_order(hwnd):
    hwnd_top = globalvars.user32.GetForegroundWindow()
    if get_window_title(hwnd_top) == "" and get_executable_name(hwnd_top) == "C:\\Windows\\explorer.exe" and get_window_class_name(hwnd_top) != 'Shell_TrayWnd':
        if is_topmost(hwnd):
            return 'donothing'
        else:
            return 'forcetop'
    elif is_child_window(hwnd_top, hwnd):
        return 'donothing'
    elif hwnd == hwnd_top:
        return 'top'
    elif is_window_at_bottom(get_window_title(hwnd)):
        return 'bottom'
    else:
        return 'other'
