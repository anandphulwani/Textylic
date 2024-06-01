from .. import globalvars
from ..helpers.get_executable_name import get_executable_name
from ..helpers.is_child_window import is_child_window

def is_child_window_of_main_window(child_hwnd):
    return is_child_window(child_hwnd, globalvars.parent_hwnd)
