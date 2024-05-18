from ... import globalvars

def getPos(event):
    """Get the position of the window"""

    xwin = globalvars.window.winfo_x()
    ywin = globalvars.window.winfo_y()
    startx = event.x_root
    starty = event.y_root

    ywin = ywin - starty
    xwin = xwin - startx

    def moveWindow(event):
        """Moving the window on mouse move"""

        globalvars.window.geometry(
            # "410x410" + f'+{event.x_root + xwin}+{event.y_root + ywin}')
            # "310x310" + f'+{event.x_root + xwin}+{event.y_root + ywin}')
            f"+{event.x_root + xwin}+{event.y_root + ywin}"
        )

    startx = event.x_root
    starty = event.y_root

    globalvars.titleBar.bind("<B1-Motion>", moveWindow)
