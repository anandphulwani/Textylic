import ctypes
import ctypes.wintypes

# Load necessary functions from the Windows API
user32 = ctypes.windll.user32

def get_process_id(hwnd):
    # Define a DWORD to hold the process ID
    pid = ctypes.wintypes.DWORD()
    # Call the function to get the process ID
    user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
    # Return the process ID
    return pid.value
