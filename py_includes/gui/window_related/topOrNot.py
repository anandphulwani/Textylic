import pygetwindow as gw
from ... import globalvars

def topOrNot():
    """
    Detects whether the window should be shown or not.

    Makes it act like a Desktop widget.
    """

    # TODO: Refine this logic
    # HELP WANTED

    windows = gw.getActiveWindow()

    # Desktop Widget logic
    if windows is None:
        globalvars.window.deiconify()
        globalvars.window.lift()
        if globalvars.isOverlayEnabled:
            globalvars.window.attributes("-topmost", False)
            globalvars.overlay.attributes("-topmost", True)
        else:
            globalvars.window.attributes("-topmost", True)
    else:
        if windows.isMaximized:
            if globalvars.isOverlayEnabled:
                globalvars.window.lower()
                globalvars.window.attributes("-topmost", False)
                globalvars.overlay.lower()
                globalvars.overlay.attributes("-topmost", False)
            else:
                globalvars.window.lower()
                globalvars.window.attributes("-topmost", False)
        elif (
            not windows.isMaximized
            and windows.title != ""
            and windows.title != "Textylic"
            and windows.title != "Choose a note:"
            and windows.title != "Save your note:"
            and windows.title != "Choose an Image:"
            and windows.title != "tk"
        ):
            if globalvars.isOverlayEnabled:
                globalvars.overlay.deiconify()
                globalvars.overlay.attributes("-topmost", False)
                globalvars.overlay.lower()
                globalvars.window.deiconify()
                globalvars.window.attributes("-topmost", False)
                globalvars.window.lower()
            else:
                globalvars.window.deiconify()
                globalvars.window.attributes("-topmost", False)
                globalvars.window.lower()
        elif (
            not windows.isMaximized
            and windows.title != ""
            and windows.title == "Textylic"
            or windows.title == "Choose a note:"
            or windows.title == "Save your note:"
            or windows.title == "Choose an Image:"
        ):
            if globalvars.isOverlayEnabled:
                globalvars.overlay.attributes("-topmost", False)
                globalvars.window.attributes("-topmost", False)
            else:
                globalvars.window.attributes("-topmost", False)
        elif windows.title == "tk":
            if globalvars.isOverlayEnabled:
                globalvars.window.attributes("-topmost", False)
                globalvars.overlay.deiconify()
                globalvars.overlay.lift()
                globalvars.overlay.attributes("-topmost", True)
            else:
                globalvars.window.deiconify()
                globalvars.window.lift()
                globalvars.window.attributes("-topmost", True)
        else:
            if globalvars.isOverlayEnabled:
                globalvars.window.lower()
                globalvars.window.attributes("-topmost", False)
                globalvars.overlay.deiconify()
                globalvars.overlay.lift()
                globalvars.overlay.attributes("-topmost", True)
            else:
                globalvars.window.deiconify()
                globalvars.window.lift()
                globalvars.window.attributes("-topmost", True)
    globalvars.window.after(200, topOrNot)
