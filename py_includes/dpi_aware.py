import os
from ctypes import windll, pointer, wintypes

# Optimization for high DPI
def Get_HWND_DPI(window_handle):
    if os.name == "nt":
        try:
            windll.shcore.SetProcessDpiAwareness(1)
        except BaseException:
            pass

        DPI100pc = 96
        DPI_type = 0
        winH = wintypes.HWND(window_handle)
        monitorhandle = windll.user32.MonitorFromWindow(winH, wintypes.DWORD(2))
        X = wintypes.UINT()
        Y = wintypes.UINT()
        try:
            windll.shcore.GetDpiForMonitor(monitorhandle, DPI_type, pointer(X), pointer(Y))
            return X.value, Y.value, (X.value + Y.value) / (2 * DPI100pc)
        except Exception:
            return 96, 96, 1
    else:
        return None, None, 1


def TkGeometryScale(s, cvtfunc):
    import re

    patt = r"(?P<W>\d+)x(?P<H>\d+)\+(?P<X>\d+)\+(?P<Y>\d+)"
    R = re.compile(patt).search(s)
    G = str(cvtfunc(R.group("W"))) + "x"
    G += str(cvtfunc(R.group("H"))) + "+"
    G += str(cvtfunc(R.group("X"))) + "+"
    G += str(cvtfunc(R.group("Y")))
    return G


def MakeTkDPIAware(TKGUI):
    TKGUI.DPI_X, TKGUI.DPI_Y, TKGUI.DPI_scaling = Get_HWND_DPI(TKGUI.winfo_id())
    TKGUI.TkScale = lambda v: int(float(v) * TKGUI.DPI_scaling)
    TKGUI.TkGeometryScale = lambda s: TkGeometryScale(s, TKGUI.TkScale)


# Optimize for high DPI
# try:
#     ctypes.windll.shcore.SetProcessDpiAwareness(2)
# except BaseException:
#     ctypes.windll.user32.SetProcessDPIAware()

# Defining Window Properties
