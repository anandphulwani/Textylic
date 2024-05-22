import ctypes
from .. import globalvars

# Constants for window positions and flags
PROCESS_QUERY_INFORMATION = 0x0400
PROCESS_VM_READ = 0x0010
MAX_PATH = 260

# Function to get the executable name of a window
def get_executable_name(hwnd):
    pid = ctypes.wintypes.DWORD()
    globalvars.user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
    process_handle = globalvars.kernel32.OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, pid.value)
    exe_name = ctypes.create_unicode_buffer(MAX_PATH)
    globalvars.psapi.GetModuleFileNameExW(process_handle, None, exe_name, MAX_PATH)
    globalvars.kernel32.CloseHandle(process_handle)
    return exe_name.value
