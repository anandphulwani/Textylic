import webbrowser
from ... import globalvars

def openLink(_=False):
    """Open link button function"""

    current_tags = globalvars.notes.tag_names("sel.first")
    if "link" in current_tags:
        url = globalvars.notes.selection_get()
        webbrowser.open_new(url)
    return "break"
