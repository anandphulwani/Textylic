import os
import subprocess

def createNewWindow(_=False):
    """Creating a new window"""

    # Check whether the exe or the python script is being used
    exePath = f"{os.path.dirname(os.path.realpath(__file__))}" "\\Textylic.exe"
    if os.path.isfile(exePath):
        subprocess.Popen(exePath, shell=True)
    else:
        subprocess.Popen(f"python {os.path.dirname(os.path.realpath(__file__))}\\main.py", shell=True)
