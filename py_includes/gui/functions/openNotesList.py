import os
import subprocess

def openNotesList():
    """Opening the folder in which all the notes are stored"""

    subprocess.Popen(f"explorer {os.path.dirname(os.path.realpath(__file__))}\\Notes", shell=True)
