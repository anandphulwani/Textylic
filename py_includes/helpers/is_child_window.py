from .. import globalvars
from ..helpers.get_executable_name import get_executable_name
from ..helpers.get_process_id import get_process_id

def is_child_window(child_hwnd, parent_hwnd):
    if child_hwnd == 0 or parent_hwnd == 0:
        return False
    if get_process_id(child_hwnd) == globalvars.parent_pid:
        return True
    return False
