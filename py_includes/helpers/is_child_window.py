from ..helpers.get_executable_name import get_executable_name

def is_child_window(child_hwnd, parent_hwnd):
    if child_hwnd == 0 or parent_hwnd == 0:
        return False
    if get_executable_name(child_hwnd) == get_executable_name(parent_hwnd):
        return True
    return False
