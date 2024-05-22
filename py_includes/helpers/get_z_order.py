from ..helpers.is_window_at_bottom import is_window_at_bottom
from ..helpers.get_window_title import get_window_title
from .. import globalvars

# Function to get the Z-order of a window
def get_z_order(hwnd):    
    hwnd_top = globalvars.user32.GetForegroundWindow()
    if hwnd == hwnd_top:
        return 'top'
    elif is_window_at_bottom(get_window_title(hwnd)):
        return 'bottom'
    else:
        return 'other'
