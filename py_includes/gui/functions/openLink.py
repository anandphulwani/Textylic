import webbrowser
from ... import globalvars
import tkinter

def openLink(_=False):
    """Open link button function"""
    
    # Get the index of the current cursor position
    cursor_index = globalvars.notes.index(tkinter.INSERT)
    
    # Get all tags at the cursor position
    current_tags = globalvars.notes.tag_names(cursor_index)
    
    if "createlink" in current_tags:
        # Find the start and end indices of the link
        start = cursor_index
        while "createlink" in globalvars.notes.tag_names(f"{start} -1c"):
            start = globalvars.notes.index(f"{start} -1c")
        end = cursor_index
        while "createlink" in globalvars.notes.tag_names(f"{end} +1c"):
            end = globalvars.notes.index(f"{end} +1c")
        end = globalvars.notes.index(f"{end} +1c")
        
        # Select the full link
        url = globalvars.notes.get(start, end)
        
        # Open the URL in a web browser
        webbrowser.open_new(url)
        
    return "break"
