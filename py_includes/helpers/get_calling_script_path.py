import os
import sys

def get_calling_script_path():
    if getattr(sys, 'frozen', False):
        # If the application is frozen by a tool like PyInstaller
        calling_script_path = os.path.abspath(sys.executable)
    else:
        # Get the absolute path of the main script
        calling_script_path = os.path.abspath(sys.argv[0])
    
    return calling_script_path
