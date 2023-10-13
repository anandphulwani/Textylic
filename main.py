import tkinter
import tkinter.messagebox
import pygetwindow as gw
import os
import sys
import webbrowser
import re
import glob
import argparse
import tkinter.ttk
import subprocess
import ctypes
import winreg
from tkinter import font
from random import randint
from tkinter import filedialog
from tkinter import PhotoImage
from tkinter import simpledialog
from tkinter import ttk
from string import ascii_uppercase
from PIL import Image
from datetime import datetime

appdata_path = os.environ.get('APPDATA')
dataPath = os.path.join(appdata_path, 'Textylyc')

# Ensure the path exists, if not, create it
if not os.path.exists(dataPath):
    os.makedirs(dataPath)

# Argument Parser
parser = argparse.ArgumentParser(description="Open a file")
parser.add_argument(
    "file",
    default=None,
    nargs="?",
    help="Name of the file to load")

args = parser.parse_args()


# Optimization for high DPI
def Get_HWND_DPI(window_handle):
    """
    Detecting high DPI displays and avoid the need
    to set Windows compatibility flags
    """

    if os.name == "nt":
        from ctypes import windll, pointer, wintypes
        try:
            windll.shcore.SetProcessDpiAwareness(1)
        except BaseException:
            pass

        DPI100pc = 96  # DPI 96 is 100% scaling
        DPI_type = 0
        winH = wintypes.HWND(window_handle)
        monitorhandle = windll.user32.MonitorFromWindow(
            winH, wintypes.DWORD(2))
        X = wintypes.UINT()
        Y = wintypes.UINT()
        try:
            windll.shcore.GetDpiForMonitor(
                monitorhandle, DPI_type, pointer(X), pointer(Y))
            return X.value, Y.value, (X.value + Y.value) / (2 * DPI100pc)
        except Exception:
            return 96, 96, 1  # Assume standard Windows DPI & scaling
    else:
        return None, None, 1


def TkGeometryScale(s, cvtfunc):
    """
    Scaling the window geomtry
    """

    patt = r"(?P<W>\d+)x(?P<H>\d+)\+(?P<X>\d+)\+(?P<Y>\d+)"
    R = re.compile(patt).search(s)
    G = str(cvtfunc(R.group("W"))) + "x"
    G += str(cvtfunc(R.group("H"))) + "+"
    G += str(cvtfunc(R.group("X"))) + "+"
    G += str(cvtfunc(R.group("Y")))
    return G


def MakeTkDPIAware(TKGUI):
    """
    Makes Tkinter DPI aware
    """
    TKGUI.DPI_X, TKGUI.DPI_Y, TKGUI.DPI_scaling = Get_HWND_DPI(
        TKGUI.winfo_id())
    TKGUI.TkScale = lambda v: int(float(v) * TKGUI.DPI_scaling)
    TKGUI.TkGeometryScale = lambda s: TkGeometryScale(s, TKGUI.TkScale)


# Optimize for high DPI
# try:
#     ctypes.windll.shcore.SetProcessDpiAwareness(2)
# except BaseException:
#     ctypes.windll.user32.SetProcessDPIAware()

# Defining Window Properties
root = tkinter.Tk()
root.withdraw()

window = tkinter.Toplevel()
window.title("Textylic")
MakeTkDPIAware(window)
window.attributes("-toolwindow", True, "-alpha", "0.99")
window.overrideredirect(1)
if args.file is not None:
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Textylyc\\' + args.file)
        x = int(winreg.QueryValueEx(key, 'x')[0])
        y = int(winreg.QueryValueEx(key, 'y')[0])
        width = int(winreg.QueryValueEx(key, 'width')[0])
        height = int(winreg.QueryValueEx(key, 'height')[0])
        winreg.CloseKey(key)
        window.geometry(window.TkGeometryScale(
            f"{width}x{height}+{x}+{y}"))
    except FileNotFoundError:
        window.geometry(window.TkGeometryScale(
            f"310x310+{str(randint(10, 900))}+{str(randint(10, 500))}"))
    except Exception as e:
        tkinter.messagebox.showinfo(
            " ", f"An error occurred: {str(e)}")
else:
    window.geometry(window.TkGeometryScale(
        f"310x310+{str(randint(10, 900))}+{str(randint(10, 500))}"))

window.config(bg="#040412")
window.wait_visibility(window)

icon = PhotoImage(file="./res/images/icons/iconx32.png")
root.iconphoto(True, icon)

# Configuring grid
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(1, weight=1)

window_is_focused = False
openedFileName = False  # Getting opened file name
openedFileName_lastModTime = False

saved = False  # The saved variable

images = []  # The list with all images, index, and name

# Default values of the themes
global pinkTheme
global yellowTheme
global greenTheme
global blueTheme
pinkTheme = False
yellowTheme = False
greenTheme = False
blueTheme = True

sizeConstantForButtons = 310
# Getting images (normal) for the buttons:
newButtonImage = PhotoImage(file="res/images/iconset/new.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
saveButtonImage = PhotoImage(file="res/images/iconset/save.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
linkButtonImage = PhotoImage(file="res/images/iconset/open.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
menuButtonImage = PhotoImage(file="res/images/iconset/menu.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
closeButtonImage = PhotoImage(file="res/images/iconset/close.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
boldButtonImage = PhotoImage(file="res/images/iconset/bold.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
italicButtonImage = PhotoImage(file="res/images/iconset/italic.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
underButtonImage = PhotoImage(file="res/images/iconset/underline.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
strikeButtonImage = PhotoImage(file="res/images/iconset/strikethrough.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
bulletButtonImage = PhotoImage(file="res/images/iconset/bullet.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
codeButtonImage = PhotoImage(file="res/images/iconset/code.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
insertlButtonImage = PhotoImage(file="res/images/iconset/link.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
colorButtonImage = PhotoImage(file="res/images/iconset/color.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
photoButtonImage = PhotoImage(file="res/images/iconset/photo.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)


# Getting images (hover) for the buttons:
newButtonImageAfter = PhotoImage(file="res/images/iconset/new1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
saveButtonImageAfter = PhotoImage(file="res/images/iconset/save1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
linkButtonImageAfter = PhotoImage(file="res/images/iconset/open1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
menuButtonImageAfter = PhotoImage(file="res/images/iconset/menu1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
closeButtonImageAfter = PhotoImage(file="res/images/iconset/close1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
boldButtonImageAfter = PhotoImage(file="res/images/iconset/bold1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
italicButtonImageAfter = PhotoImage(file="res/images/iconset/italic1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
underButtonImageAfter = PhotoImage(file="res/images/iconset/underline1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
strikeButtonImageAfter = PhotoImage(
    file="res/images/iconset/strikethrough1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
bulletButtonImageAfter = PhotoImage(file="res/images/iconset/bullet1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
codeButtonImageAfter = PhotoImage(file="res/images/iconset/code1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
insertlButtonImageAfter = PhotoImage(file="res/images/iconset/link1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
colorButtonImageAfter = PhotoImage(file="res/images/iconset/color1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
photoButtonImageAfter = PhotoImage(file="res/images/iconset/photo1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)

allImagesGroup = []  # Reference list with images in it
imgNumberName = 0  # A variable used to name images in chronological order

accentItems = []  # List that holds all items that have accent color

deletedImages = []  # List that holds all images that need to be deleted


def fetchDrivePath() -> str:
    """The drive in which the script is running"""

    for drive in ascii_uppercase:
        if os.path.exists(f"{drive}:\\Users"):
            return drive + ":\\"
    return ""


def createNewWindow(_=False):
    """Creating a new window"""

    # Check whether the exe or the python script is being used
    exePath = f"{os.path.dirname(os.path.realpath(__file__))}" \
        "\\Textylic.exe"
    if os.path.isfile(exePath):
        subprocess.Popen(
            exePath,
            shell=True)
    else:
        subprocess.Popen(
            f"python {os.path.dirname(os.path.realpath(__file__))}\\main.py",
            shell=True)


def openNotesList():
    """Opening the folder in which all the notes are stored"""

    subprocess.Popen(
        f"explorer {os.path.dirname(os.path.realpath(__file__))}\\Notes",
        shell=True)


def bolder(_=False):
    """Bold button function"""

    bold_font = font.Font(notes, notes.cget("font"))
    bold_font.configure(weight="bold")

    italicBold_font = font.Font(notes, notes.cget("font"))
    italicBold_font.configure(slant="italic", weight="bold")

    underBold_font = font.Font(notes, notes.cget("font"))
    underBold_font.configure(underline=True, weight="bold")

    strikeBold_font = font.Font(notes, notes.cget("font"))
    strikeBold_font.configure(overstrike=True, weight="bold")

    notes.tag_configure("bold", font=bold_font)
    notes.tag_configure("italicBold", font=italicBold_font)
    notes.tag_configure("underBold", font=underBold_font)
    notes.tag_configure("strikeBold", font=strikeBold_font)
    current_tags = notes.tag_names("sel.first")

    if "bold" in current_tags:
        notes.tag_remove("bold", "sel.first", "sel.last")
    elif "italicBold" in current_tags:
        notes.tag_remove("italicBold", "sel.first", "sel.last")
        notes.tag_add("italic", "sel.first", "sel.last")
    elif "underBold" in current_tags:
        notes.tag_remove("underBold", "sel.first", "sel.last")
        notes.tag_add("underline", "sel.first", "sel.last")
    elif "strikeBold" in current_tags:
        notes.tag_remove("strikeBold", "sel.first", "sel.last")
        notes.tag_add("strikethrough", "sel.first", "sel.last")
    else:
        if "italic" in current_tags:
            notes.tag_remove("italic", "sel.first", "sel.last")
            notes.tag_add("italicBold", "sel.first", "sel.last")
        elif "underline" in current_tags:
            notes.tag_remove("underline", "sel.first", "sel.last")
            notes.tag_add("underBold", "sel.first", "sel.last")
        elif "strikethrough" in current_tags:
            notes.tag_remove("strikethrough", "sel.first", "sel.last")
            notes.tag_add("strikeBold", "sel.first", "sel.last")
        else:
            notes.tag_add("bold", "sel.first", "sel.last")
    return "break"


def italicizer(_=False):
    """Italic button function"""

    italic_font = font.Font(notes, notes.cget("font"))
    italic_font.configure(slant="italic")

    boldItalic_font = font.Font(notes, notes.cget("font"))
    boldItalic_font.configure(slant="italic", weight="bold")

    underItalic_font = font.Font(notes, notes.cget("font"))
    underItalic_font.configure(underline=True, slant="italic")

    strikeItalic_font = font.Font(notes, notes.cget("font"))
    strikeItalic_font.configure(overstrike=True, slant="italic")

    notes.tag_configure("italic", font=italic_font)
    notes.tag_configure("boldItalic", font=boldItalic_font)
    notes.tag_configure("underItalic", font=underItalic_font)
    notes.tag_configure("strikeItalic", font=strikeItalic_font)
    current_tags = notes.tag_names("sel.first")

    if "italic" in current_tags:
        notes.tag_remove("italic", "sel.first", "sel.last")
    elif "boldItalic" in current_tags:
        notes.tag_remove("boldItalic", "sel.first", "sel.last")
        notes.tag_add("bold", "sel.first", "sel.last")
    elif "underItalic" in current_tags:
        notes.tag_remove("underItalic", "sel.first", "sel.last")
        notes.tag_add("underline", "sel.first", "sel.last")
    elif "strikeItalic" in current_tags:
        notes.tag_remove("strikeItalic", "sel.first", "sel.last")
        notes.tag_add("strikethrough", "sel.first", "sel.last")
    else:
        if "bold" in current_tags:
            notes.tag_remove("bold", "sel.first", "sel.last")
            notes.tag_add("boldItalic", "sel.first", "sel.last")
        elif "underline" in current_tags:
            notes.tag_remove("underline", "sel.first", "sel.last")
            notes.tag_add("underItalic", "sel.first", "sel.last")
        elif "strikethrough" in current_tags:
            notes.tag_remove("strikethrough", "sel.first", "sel.last")
            notes.tag_add("strikeItalic", "sel.first", "sel.last")
        else:
            notes.tag_add("italic", "sel.first", "sel.last")
    return "break"


def codify(_=False):
    """Code button function"""

    desired_font = ("JetBrainsMono NF", 10) if is_font_present("JetBrainsMono NF") else "Consolas 11"
    notes.tag_configure("code", font=desired_font)
    current_tags = notes.tag_names("sel.first")

    if "code" in current_tags:
        notes.tag_remove("code", "sel.first", "sel.last")
    else:
        notes.tag_add("code", "sel.first", "sel.last")
    return "break"


def underliner(_=False):
    """Underline button function"""

    under_font = font.Font(notes, notes.cget("font"))
    under_font.configure(underline=True)

    boldUnder_font = font.Font(notes, notes.cget("font"))
    boldUnder_font.configure(underline=True, weight="bold")

    italicUnder_font = font.Font(notes, notes.cget("font"))
    italicUnder_font.configure(underline=True, slant="italic")

    strikeUnder_font = font.Font(notes, notes.cget("font"))
    strikeUnder_font.configure(overstrike=True, underline=True)

    notes.tag_configure("underline", font=under_font)
    notes.tag_configure("boldUnder", font=boldUnder_font)
    notes.tag_configure("italicUnder", font=italicUnder_font)
    notes.tag_configure("strikeUnder", font=strikeUnder_font)
    current_tags = notes.tag_names("sel.first")

    if "underline" in current_tags:
        notes.tag_remove("underline", "sel.first", "sel.last")
    elif "boldUnder" in current_tags:
        notes.tag_remove("boldUnder", "sel.first", "sel.last")
        notes.tag_add("bold", "sel.first", "sel.last")
    elif "italicUnder" in current_tags:
        notes.tag_remove("italicUnder", "sel.first", "sel.last")
        notes.tag_add("italic", "sel.first", "sel.last")
    elif "strikeUnder" in current_tags:
        notes.tag_remove("strikeUnder", "sel.first", "sel.last")
        notes.tag_add("strikethrough", "sel.first", "sel.last")
    else:
        if "bold" in current_tags:
            notes.tag_add("boldUnder", "sel.first", "sel.last")
            notes.tag_remove("bold", "sel.first", "sel.last")
        elif "italic" in current_tags:
            notes.tag_add("italicUnder", "sel.first", "sel.last")
            notes.tag_remove("italic", "sel.first", "sel.last")
        elif "strikethrough" in current_tags:
            notes.tag_add("strikeUnder", "sel.first", "sel.last")
            notes.tag_remove("strikethrough", "sel.first", "sel.last")
        else:
            notes.tag_add("underline", "sel.first", "sel.last")
    return "break"


def strikethrough(_=False):
    """Strikethrough button function"""

    strike_font = font.Font(notes, notes.cget("font"))
    strike_font.configure(overstrike=True)

    boldStrike_font = font.Font(notes, notes.cget("font"))
    boldStrike_font.configure(overstrike=True, weight="bold")

    italicStrike_font = font.Font(notes, notes.cget("font"))
    italicStrike_font.configure(overstrike=True, slant="italic")

    underStrike_font = font.Font(notes, notes.cget("font"))
    underStrike_font.configure(overstrike=True, underline=True)

    notes.tag_configure("strikethrough", font=strike_font)
    current_tags = notes.tag_names("sel.first")

    if "strikethrough" in current_tags:
        notes.tag_remove("strikethrough", "sel.first", "sel.last")
        notes.tag_add("strikethrough", "sel.first", "sel.last")
    elif "boldStrike" in current_tags:
        notes.tag_remove("boldStrike", "sel.first", "sel.last")
        notes.tag_add("bold", "sel.first", "sel.last")
    elif "italicStrike" in current_tags:
        notes.tag_remove("italicStrike", "sel.first", "sel.last")
        notes.tag_add("italic", "sel.first", "sel.last")
    elif "underStrike" in current_tags:
        notes.tag_remove("underStrike", "sel.first", "sel.last")
        notes.tag_add("underline", "sel.first", "sel.last")
    else:
        if "bold" in current_tags:
            notes.tag_remove("bold", "sel.first", "sel.last")
            notes.tag_add("boldStrike", "sel.first", "sel.last")
        elif "italic" in current_tags:
            notes.tag_remove("italic", "sel.first", "sel.last")
            notes.tag_add("italicStrike", "sel.first", "sel.last")
        elif "underline" in current_tags:
            notes.tag_remove("underline", "sel.first", "sel.last")
            notes.tag_add("underStrike", "sel.first", "sel.last")
        else:
            notes.tag_add("strikethrough", "sel.first", "sel.last")

    return "break"


def bulletList():
    """Bulleted list button function"""

    selection = notes.selection_get()
    current_tags = notes.tag_names("sel.first")

    if "\n" not in selection:
        if "bullet" not in current_tags:
            index_1 = float(notes.index("sel.first"))
            index_2 = float(notes.index("sel.last"))
            bulleted_str = "\t•  " + str(selection)
            notes.delete(index_1, index_2)
            notes.insert(index_1, bulleted_str)
            lenBulletString = len(bulleted_str)
            lenBulletString = notes.index(index_1 + lenBulletString)
            notes.tag_add("bullet", index_1, lenBulletString)
        elif "bullet" in current_tags:
            index_1 = float(notes.index("sel.first"))
            index_2 = float(notes.index("sel.last"))
            selected = notes.selection_get()
            selected = str(selected)
            selected = selected.replace("\t•  ", "")
            notes.insert("sel.first", selected)
            notes.delete("sel.first", "sel.last")
            lenBulletString = len(selected)
            lenBulletString = notes.index(lenBulletString)
            notes.tag_remove("bullet", index_1, lenBulletString)
    elif "\n" in selection:
        if "bullet" not in current_tags:
            index_1 = float(notes.index("sel.first"))
            index_2 = float(notes.index("sel.last"))
            select = notes.selection_get()
            bulleted_str = select.replace("\n", "\n\t•  ")
            bulleted_str = "\t•  " + str(bulleted_str)
            notes.delete(str(index_1), str(index_2))
            notes.insert(index_1, bulleted_str)
            lenBulletString = len(bulleted_str)
            lenBulletString = notes.index(index_1 + lenBulletString)
            notes.tag_add("bullet", index_1, lenBulletString)
        elif "bullet" in current_tags:
            index_1 = float(notes.index("sel.first"))
            index_2 = float(notes.index("sel.last"))
            selected = selection.replace("\n\t•  ", "\n")
            selected = selected.replace("\t•  ", "")
            notes.insert("sel.first", selected)
            notes.delete("sel.first", "sel.last")
            lenBulletString = len(selected)
            lenBulletString = notes.index(lenBulletString)
            notes.tag_remove("bullet", index_1, lenBulletString)
    return "break"


def link(_=False):
    """Link button function"""

    under_font = font.Font(notes, notes.cget("font"))
    under_font.configure(underline=True)

    notes.tag_configure("link", font=under_font, foreground="#00AFEC")
    current_tags = notes.tag_names("sel.first")

    if "link" in current_tags:
        notes.tag_remove("link", "sel.first", "sel.last")
    else:
        notes.tag_add("link", "sel.first", "sel.last")
    return "break"


def setColor():
    """Change Text Color"""

    global pinkTheme
    global yellowTheme
    global greenTheme
    global blueTheme

    if yellowTheme is True:
        notes.tag_configure("emphColor", foreground="#E6B905")
    elif pinkTheme is True:
        notes.tag_configure("emphColor", foreground="#EB8EC6")
    elif greenTheme is True:
        notes.tag_configure("emphColor", foreground="#65BA5A")
    elif blueTheme is True:
        notes.tag_configure("emphColor", foreground="#59C0E7")
    current_tags = notes.tag_names("sel.first")

    if "emphColor" in current_tags:
        notes.tag_remove("emphColor", "sel.first", "sel.last")
    else:
        notes.tag_add("emphColor", "sel.first", "sel.last")

    return "break"


def openLink(_=False):
    """Open link button function"""

    current_tags = notes.tag_names("sel.first")
    if "link" in current_tags:
        url = notes.selection_get()
        webbrowser.open_new(url)
    return "break"


def openReadme(_=False):
    """Open the README.md on GitHub and the Textylic website"""

    webbrowser.open_new(
        "https://github.com/akhilesh-balaji/Textylic/blob/master/README.md")
    webbrowser.open_new("https://akhilesh-balaji.github.io/Textylic/")
    return "break"


def hoverImageBold(_=False):
    """Changing the image of bold button on hover"""

    bold.configure(image=boldButtonImageAfter)


def NormalImageBold(_=False):
    """Getting the normal image for the bold button function"""

    bold.configure(image=boldButtonImage)


def hoverImageItalic(_=False):
    """Changing the image of italic button on hover"""

    italic.configure(image=italicButtonImageAfter)


def NormalImageItalic(_=False):
    """Getting the normal image for the italic button function"""

    italic.configure(image=italicButtonImage)


def hoverImageUnder(_=False):
    """Changing the image of underline button on hover"""

    underline.configure(image=underButtonImageAfter)


def NormalImageUnder(_=False):
    """Getting the normal image for the underline button function"""

    underline.configure(image=underButtonImage)


def hoverImageStrike(_=False):
    """Changing the image of strikethrough button on hover"""

    strikeThrough.configure(image=strikeButtonImageAfter)


def NormalImageStrike(_=False):
    """Getting the normal image for the strikethrough button function"""

    strikeThrough.configure(image=strikeButtonImage)


def hoverImageBullet(_=False):
    """Changing the image of bulleted list button on hover"""

    bullet.configure(image=bulletButtonImageAfter)


def NormalImageBullet(_=False):
    """Getting the normal image for the bulleted list button function"""

    bullet.configure(image=bulletButtonImage)


def hoverImageCode(_=False):
    """Changing the image of code-ify button on hover"""

    code.configure(image=codeButtonImageAfter)


def NormalImageCode(_=False):
    """Getting the normal image for the code-ify button function"""

    code.configure(image=codeButtonImage)


def hoverImageNew(_=False):
    """Changing the image of new button on hover"""

    new.configure(image=newButtonImageAfter)


def NormalImageNew(_=False):
    """Getting the normal image for the new button function"""

    new.configure(image=newButtonImage)


def hoverImageSave(_=False):
    """Changing the image of save button on hover"""

    save.configure(image=saveButtonImageAfter)


def NormalImageSave(_=False):
    """Getting the normal image for the save button function"""

    save.configure(image=saveButtonImage)


def hoverImageOpen(_=False):
    """Changing the image of open note button on hover"""

    openlink.configure(image=linkButtonImageAfter)


def NormalImageOpen(_=False):
    """Getting the normal image for the open note button function"""

    openlink.configure(image=linkButtonImage)


def hoverImageMenu(_=False):
    """Changing the image of menu button on hover"""

    menu.configure(image=menuButtonImageAfter)


def NormalImageMenu(_=False):
    """Getting the normal image for the menu button function"""

    menu.configure(image=menuButtonImage)


def hoverImageClose(_=False):
    """Changing the image of close button on hover"""

    close_button.configure(image=closeButtonImageAfter)


def NormalImageClose(_=False):
    """Getting the normal image for the close button function"""

    close_button.configure(image=closeButtonImage)


def hoverImageLink(_=False):
    """Changing the image of hyperlink button on hover"""

    insertl.configure(image=insertlButtonImageAfter)


def NormalImageLink(_=False):
    """Getting the normal image for the hyperlink button function"""

    insertl.configure(image=insertlButtonImage)


def hoverImageTsize(_=False):
    """Changing the image of color button on hover"""

    colorText.configure(image=colorButtonImageAfter)


def NormalImageTsize(_=False):
    """Getting the normal image for the color button function"""

    colorText.configure(image=colorButtonImage)


def hoverImagePhoto(_=False):
    """Changing the image of image button on hover"""

    photoInsert.configure(image=photoButtonImageAfter)


def NormalImagePhoto(_=False):
    """Getting the normal image for the image button function"""

    photoInsert.configure(image=photoButtonImage)


def getTags(start, end) -> list:
    """
    Get the tags (bold, italic, etc.) and their indices in the Text widget.

    It gets the tags for each character till the end, and stores the end index
    when the tag changes.
    """

    index = start
    tagname = []
    starttagindex = index
    prevtag = notes.tag_names(index)

    try:
        tagname.append([starttagindex, "end", notes.tag_names(index)])
    except BaseException:
        tagname.append([starttagindex, "end", ("",)])

    while notes.compare(index, "<", end):
        if notes.tag_names(index) != prevtag:
            # If the tag name at the current index is not equal to the
            # previous index's tag name...
            if len(notes.tag_names(index)) <= 0:
                # If the legnth of the tuple containing the tag names at the
                # current index is less that or equal to 0, it means that
                # there are no tags here.
                starttagindex = index
                legnth = len(tagname)
                tagname[legnth - 1][1] = index
                tagname.append([starttagindex, "end", ("",)])
            else:
                # Otherwise, it means that there are tags here.
                starttagindex = index
                legnth = len(tagname)
                tagname[legnth - 1][1] = index
                tagname.append([starttagindex, "end", notes.tag_names(index)])

        prevtag = notes.tag_names(index)
        index = notes.index(f"{index}+1c")

    return tagname


def photoInserter():
    """'Insert photo' button function"""

    global allImagesGroup
    global saved
    global images
    global imgNumberName
    global dateTimeNow
    global openedFileName

    dateTimeNow = str(datetime.now())
    dateTimeNow = dateTimeNow.replace("-", "_")
    dateTimeNow = dateTimeNow.replace(" ", "_")
    dateTimeNow = dateTimeNow.replace(":", "")
    dateTimeNow = dateTimeNow.replace(".", "")

    imgNumberName = imgNumberName + 1

    photo = filedialog.askopenfilename(
        initialdir="~/Pictures",
        title="Choose an Image:",
        filetypes=(
            ("PNG",
             "*.png"),
            ("JPG",
             "*.jpg"),
            ("JPEG",
             "*.jpeg"),
        ))
    imgFile = Image.open(photo)
    imgFile.thumbnail((window.TkScale(280), window.TkScale(280)))
    imgFile.save(f"./res/cache_images_/{dateTimeNow}.png")

    imgToInsert = PhotoImage(file=f"./res/cache_images_/{dateTimeNow}.png")
    allImagesGroup.append(imgToInsert)
    images.append(
        [f"./res/cache_images_/{dateTimeNow}",
            notes.index("insert"),
            f"image{imgNumberName}"])
    notes.image_create(
        "insert",
        image=imgToInsert,
        name=f"image{imgNumberName}")
    imgFile.close()
    photo.close()


def openFile(file: str):
    """Open a file with the file dialog"""

    global saved
    global images
    global allImagesGroup
    global openedFileName_lastModTime

    noteFile = file
    if noteFile:
        global openedFileName
        openedFileName = noteFile
    noteFileFullPath = os.path.join(dataPath, noteFile)    
    noteFile = open(noteFileFullPath, "r")

    if openedFileName_lastModTime == os.path.getmtime(noteFileFullPath):
        return
    openedFileName_lastModTime = os.path.getmtime(noteFileFullPath)

    read = noteFile.read()

    matchStyle = re.match(
        r".*<style>\n(.*)\n</style>",
        str(read),
        flags=re.DOTALL | re.MULTILINE)
    matchImg = re.match(
        r".*<images>\n(.*)\n</images>",
        str(read),
        flags=re.DOTALL | re.MULTILINE)
    matchTheme = re.match(
        r".*<colortheme>\n(.*)\n</colortheme>",
        str(read),
        flags=re.DOTALL | re.MULTILINE)

    read = re.sub("<style>.*$", "", read, flags=re.DOTALL | re.MULTILINE)
    read = re.sub("<content>\n", "", read, flags=re.DOTALL | re.MULTILINE)
    read = re.sub("\n*</content>\n\n", "", read,
                  flags=re.DOTALL | re.MULTILINE)

    notes.delete("1.0", "end")
    notes.insert("end", read)

    if matchStyle:
        # Bold fonts and tags
        formatting = matchStyle.group(1)
        formatting = eval(formatting)

        bold_font = font.Font(notes, notes.cget("font"))
        bold_font.configure(weight="bold")

        italicBold_font = font.Font(notes, notes.cget("font"))
        italicBold_font.configure(slant="italic", weight="bold")

        underBold_font = font.Font(notes, notes.cget("font"))
        underBold_font.configure(underline=True, weight="bold")

        strikeBold_font = font.Font(notes, notes.cget("font"))
        strikeBold_font.configure(overstrike=True, weight="bold")

        notes.tag_configure("bold", font=bold_font)
        notes.tag_configure("italicBold", font=italicBold_font)
        notes.tag_configure("underBold", font=underBold_font)
        notes.tag_configure("strikeBold", font=strikeBold_font)

        # Italic fonts and tags
        italic_font = font.Font(notes, notes.cget("font"))
        italic_font.configure(slant="italic")

        boldItalic_font = font.Font(notes, notes.cget("font"))
        boldItalic_font.configure(slant="italic", weight="bold")

        underItalic_font = font.Font(notes, notes.cget("font"))
        underItalic_font.configure(underline=True, slant="italic")

        strikeItalic_font = font.Font(notes, notes.cget("font"))
        strikeItalic_font.configure(overstrike=True, slant="italic")

        notes.tag_configure("italic", font=italic_font)
        notes.tag_configure("boldItalic", font=boldItalic_font)
        notes.tag_configure("underItalic", font=underItalic_font)
        notes.tag_configure("strikeItalic", font=strikeItalic_font)

        # Code font and tags
        desired_font = ("JetBrainsMono NF", 10) if is_font_present("JetBrainsMono NF") else "Consolas 11"
        notes.tag_configure("code", font=desired_font)

        # Underline font and tags
        under_font = font.Font(notes, notes.cget("font"))
        under_font.configure(underline=True)

        boldUnder_font = font.Font(notes, notes.cget("font"))
        boldUnder_font.configure(underline=True, weight="bold")

        italicUnder_font = font.Font(notes, notes.cget("font"))
        italicUnder_font.configure(underline=True, slant="italic")

        strikeUnder_font = font.Font(notes, notes.cget("font"))
        strikeUnder_font.configure(overstrike=True, underline=True)

        notes.tag_configure("underline", font=under_font)
        notes.tag_configure("boldUnder", font=boldUnder_font)
        notes.tag_configure("italicUnder", font=italicUnder_font)
        notes.tag_configure("strikeUnder", font=strikeUnder_font)

        # Link font
        notes.tag_configure("link", font=under_font, foreground="#00AFEC")

        # Text color
        global pinkTheme
        global yellowTheme
        global greenTheme
        global blueTheme
        if yellowTheme is True:
            notes.tag_configure("emphColor", foreground="#fbc02d")
        elif pinkTheme is True:
            notes.tag_configure("emphColor", foreground="#EB8EC6")
        elif greenTheme is True:
            notes.tag_configure("emphColor", foreground="#65BA5A")
        elif blueTheme is True:
            notes.tag_configure("emphColor", foreground="#2292ff")

        for format in formatting:
            # Apply formatting
            for tag in format[2]:
                notes.tag_add(str(tag).strip("}{/.\\"), format[0], format[1])

    if matchImg:
        # Getting the list of images
        images = eval(matchImg.group(1))
        allImagesGroup = []
        for imageList in images:
            # Insert the images at appropriate index
            imageToInsert = PhotoImage(file=f"{imageList[0]}.png")
            notes.insert(f"{imageList[1]}-1c", "\n")
            notes.image_create(
                imageList[1],
                image=imageToInsert,
                name=imageList[2])
            allImagesGroup.append(imageToInsert)

    if matchTheme:
        # Getting the theme of the note
        exec(matchTheme.group(1))

    noteFile.close()
    saved = True
    return "break"


def openFileChoose(_=False):
    """Open a file with the file dialog"""

    openFile((filedialog.askopenfilename(initialdir="./notes",
                                         title="Choose a note:", filetypes=(
                                             ("Textylic file", "*.txtlyc"),))))
    return "break"


def saveNoteAs(_=False):
    """Save the note as a file name"""

    noteFile = filedialog.asksaveasfilename(
        confirmoverwrite=True,
        defaultextension=".txtlyc",
        filetypes=(
            ("Textylic file", "*.txtlyc"),),
        initialdir="./notes",
        title="Save your note:")
    if noteFile:
        global saved
        saved = True
        global openedFileName
        openedFileName = noteFile
        noteFile = open(os.path.join(dataPath, noteFile), "w")
        noteFile.write(notes.get(1.0, "end"))
        noteFile.close()
        # Messagebox
        openedFileNameStrip = re.sub("C:/.*/", "", str(openedFileName))
        tkinter.messagebox.showinfo(
            " ", f"Successfully saved note as \"{openedFileNameStrip}\"   ")
    return "break"


def saveNote(_=False):
    """Save the note"""

    global saved
    global openedFileName
    global images
    global deletedImages
    global allImagesGroup
    global pinkTheme
    global yellowTheme
    global greenTheme
    global blueTheme

    for imgName in notes.image_names():
        # Saving the list of image names
        index = notes.index(str(imgName))

        for image in images:
            # Deleting unused images from the list
            if image[2] in notes.image_names():
                if image[2] == imgName:
                    image[1] = index
            else:
                deletedImages.append(image)

    for deletedImage in deletedImages:
        # Deleting the unused images from `images` list
        try:
            images.remove(deletedImage)
        except BaseException:
            pass

    if openedFileName:
        # If a file is not being saved the first time, append additional data
        # to it
        noteFile = open(os.path.join(dataPath, openedFileName), "w")
        noteFile.write(
            "<content>\n{}\n</content>\n\n".format(notes.get(1.0, "end")))
        noteFile.write(
            "<style>\n{}\n</style>\n\n".format(getTags("1.0", "end")))
        noteFile.write("<images>\n{}\n</images>\n\n".format(images))

        if blueTheme is True:
            noteFile.write("<colortheme>\naccentblue()\n</colortheme>")
        elif pinkTheme is True:
            noteFile.write("<colortheme>\naccentpink()\n</colortheme>")
        elif yellowTheme is True:
            noteFile.write("<colortheme>\naccentyellow()\n</colortheme>")
        elif greenTheme is True:
            noteFile.write("<colortheme>\naccentgreen()\n</colortheme>")

        noteFile.close()
        saved = True
        getTags("1.0", "end")
    else:
        saveNoteAs()
    return "break"


def clearCache():
    """Clearing the unused images from the `cache_images_` folder"""

    imagesToBeSaved = []
    pathToNotes = "./Notes"
    pathToNotes = os.path.join(pathToNotes, '*.txtlyc')
    pathToNotes = pathToNotes.replace("\\", "/")

    pathToImages = "./res/cache_images_"
    pathToImages = os.path.join(pathToImages, '*.*')
    pathToImages = pathToImages.replace("\\", "/")

    for filename in glob.glob(pathToNotes):
        # For all the images in the `cache_images_` folder check if they are
        # in the `images` list for every note
        formattedFileName = filename.replace("\\", "/")
        noteFile = open(os.path.join(dataPath, f"{formattedFileName}"), "r")
        readContent = noteFile.read()
        matchImg = re.match(
            r".*<images>\n(.*)\n</images>",
            str(readContent),
            flags=re.DOTALL | re.MULTILINE)

        if matchImg:
            images = eval(matchImg.group(1))
            for image in images:
                imagesToBeSaved.append(f"{image[0]}.png")

        noteFile.close()

    for imageFile in glob.glob(pathToImages):
        # Deleting the unused images
        imagesToBeSavedSet = set(imagesToBeSaved)
        formattedImgFileName = imageFile.replace("\\", "/")
        if formattedImgFileName not in imagesToBeSavedSet:
            os.remove(formattedImgFileName)


def autoSave():
    """Auto saves the note"""

    global saved
    if window_is_focused and saved is True:
        saveNote()
    window.after(3000, autoSave)


def autoReload():
    """Auto reloads the note"""

    global saved
    global openedFileName
    if not window_is_focused and saved is True:
        openFile(openedFileName)
    window.after(3000, autoReload)


def windowdestroy(_=False):
    """Close the window"""

    global openedFileName

    def whitespaceStr(strg, search=re.compile(r"[^\s]+").search):
        return not bool(search(strg))

    # Save window position to registry before closing
    x, y = window.winfo_x(), window.winfo_y()
    width, height = window.winfo_width(), window.winfo_height()
    key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, 'Software\\Textylyc\\' + openedFileName)
    winreg.SetValueEx(key, 'x', 0, winreg.REG_SZ, str(x))
    winreg.SetValueEx(key, 'y', 0, winreg.REG_SZ, str(y))
    winreg.SetValueEx(key, 'width', 0, winreg.REG_SZ, str(width))
    winreg.SetValueEx(key, 'height', 0, winreg.REG_SZ, str(height))
    winreg.CloseKey(key)
    
    if (not openedFileName) and (not whitespaceStr(notes.get("1.0", "end"))):
        # Confirmbox
        confirmSave = tkinter.messagebox.askyesnocancel("Confirmation",
                                                        "Do you want to save this note \
                                            before you leave?   ",
                                                        icon="warning",
                                                        default="no")
        if confirmSave is True:
            saveNoteAs()
        elif confirmSave is False:
            root.destroy()
        else:
            pass
    else:
        root.destroy()


def on_focus_in(event):
    global window_is_focused
    window_is_focused = True

def on_focus_out(event):
    global window_is_focused
    window_is_focused = False

def accentpink():
    """Pink accent color"""

    global pinkTheme
    global yellowTheme
    global greenTheme
    global blueTheme
    pinkTheme = True
    yellowTheme = False
    greenTheme = False
    blueTheme = False
    for item in accentItems:
        item.configure(bg="#EB8EC6")
        if not isinstance(item, tkinter.Frame):
            item.configure(activebackground="#EB8EC6")
    titleBar.configure(bg="#EB8EC6")
    menu.configure(activebackground="#EB8EC6")
    notes.tag_configure("emphColor", foreground="#EB8EC6")
    window.update()


def accentyellow():
    """Yellow accent color"""

    global pinkTheme
    global yellowTheme
    global greenTheme
    global blueTheme
    pinkTheme = False
    yellowTheme = True
    greenTheme = False
    blueTheme = False
    for item in accentItems:
        item.configure(bg="#fbc02d")
        if not isinstance(item, tkinter.Frame):
            item.configure(activebackground="#fbc02d")
    titleBar.configure(bg="#fbc02d")
    notes.tag_configure("emphColor", foreground="#fbc02d")
    menu.configure(activebackground="#fbc02d")
    window.update()


def accentgreen():
    """Green accent color"""

    global pinkTheme
    global yellowTheme
    global greenTheme
    global blueTheme
    pinkTheme = False
    yellowTheme = False
    greenTheme = True
    blueTheme = False
    for item in accentItems:
        item.configure(bg="#65BA5A")
        if not isinstance(item, tkinter.Frame):
            item.configure(activebackground="#65BA5A")
    titleBar.configure(bg="#65BA5A")
    notes.tag_configure("emphColor", foreground="#65BA5A")
    menu.configure(activebackground="#65BA5A")
    window.update()


def accentblue():
    """Blue accent color"""

    global pinkTheme
    global yellowTheme
    global greenTheme
    global blueTheme
    pinkTheme = False
    yellowTheme = False
    greenTheme = False
    blueTheme = True
    for item in accentItems:
        item.configure(bg="#2292ff")
        if not isinstance(item, tkinter.Frame):
            item.configure(activebackground="#2292ff")
    titleBar.configure(bg="#2292ff")
    notes.tag_configure("emphColor", foreground="#2292ff")
    menu.configure(activebackground="#2292ff")
    window.update()


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
        window.deiconify()
        window.lift()
        window.attributes("-topmost", True)
    else:
        if windows.isMaximized:
            window.lower()
            window.attributes("-topmost", False)
        elif (not windows.isMaximized and windows.title != "" and
                windows.title != "Textylic" and windows.title !=
                "Choose a note:" and windows.title != "Save your note:" and
                windows.title != "Choose an Image:" and windows.title != "tk"):
            window.deiconify()
            window.attributes("-topmost", False)
            window.lower()
        elif (not windows.isMaximized and windows.title != "" and
                windows.title == "Textylic" or windows.title ==
                "Choose a note:" or windows.title == "Save your note:" or
                windows.title == "Choose an Image:"):
            window.attributes("-topmost", False)
        elif windows.title == "tk":
            window.deiconify()
            window.lift()
            window.attributes("-topmost", True)
        else:
            window.deiconify()
            window.lift()
            window.attributes("-topmost", True)

    window.after(200, topOrNot)


def getPos(event):
    """Get the position of the window"""

    xwin = window.winfo_x()
    ywin = window.winfo_y()
    startx = event.x_root
    starty = event.y_root

    ywin = ywin - starty
    xwin = xwin - startx

    def moveWindow(event):
        """Moving the window on mouse move"""

        window.geometry(
            # "410x410" + f'+{event.x_root + xwin}+{event.y_root + ywin}')
            # "310x310" + f'+{event.x_root + xwin}+{event.y_root + ywin}')
            f'+{event.x_root + xwin}+{event.y_root + ywin}')

    startx = event.x_root
    starty = event.y_root

    titleBar.bind('<B1-Motion>', moveWindow)

def is_font_present(font_name):
    available_fonts = font.families()
    return font_name in available_fonts

winDrive = fetchDrivePath()  # The windows directory letter

# Defining Title Bar Elements
titleBar = tkinter.Frame(window, relief="flat", bg="#2292ff")

# smallPaddingX = 7
smallPaddingX = window.TkScale(5)
smallPaddingY = window.TkScale(4)

new = tkinter.Button(
    titleBar,
    image=newButtonImage,
    bd=0,
    bg="#2292ff",
    command=createNewWindow,
    activebackground="#2292ff")
new.image = newButtonImage
new.grid(row=0, column=0, padx=smallPaddingX, sticky="W", pady=smallPaddingY)
new.image = newButtonImage
accentItems.append(new)

# Save
save = tkinter.Button(
    titleBar,
    image=saveButtonImage,
    bd=0,
    bg="#2292ff",
    pady=4,
    activebackground="#2292ff",
    command=saveNote)
save.image = saveButtonImage
save.grid(row=0, column=1, padx=smallPaddingX, sticky="W", pady=smallPaddingY)
accentItems.append(save)

# Link opening button
openlink = tkinter.Button(
    titleBar,
    image=linkButtonImage,
    bd=0,
    bg="#2292ff",
    pady=4,
    command=openLink,
    activebackground="#2292ff")
openLink.image = linkButtonImage
openlink.grid(
    row=0,
    column=2,
    padx=smallPaddingX,
    sticky="W",
    pady=smallPaddingY)
accentItems.append(openlink)

# Notes Text widget container
notesFrame = tkinter.Frame(
    window,
    relief="flat",
    bg="#040412",
    height=window.TkScale(244),
    width=window.TkScale(320))
notesFrame.grid(row=1, column=0, columnspan=5, sticky="NSEW")
notesFrame.grid_rowconfigure(0, weight=1)
notesFrame.grid_columnconfigure(0, weight=1)

# Main Text input
notes = tkinter.Text(
    notesFrame,
    undo=True,
    font="Arial 11",
    bg="#040412",
    padx=smallPaddingX,
    pady=10,
    bd=0,
    fg="white",
    insertbackground="white",
    relief="flat",
    selectbackground="#30324c",
    wrap="word",
    height=10.5,
    width=39,
    tabs=(
        "0.5c",
        "3c",
         "5c"))
notes.grid(row=0, column=0, rowspan=5, columnspan=5, sticky="NSEW")
notes.delete("1.0", "end")
segoe_font = font.Font(notes, notes.cget("font"))
window.update_idletasks()
segoe_font.configure(family="Arial", size=window.TkScale(11))
notes.configure(font=segoe_font)

# Extra Menu
menu = tkinter.Menubutton(
    titleBar,
    image=menuButtonImage,
    bd=0,
    bg="#2292ff",
    relief="flat",
    pady=4,
    activebackground="#2292ff")
menu.image = menuButtonImage
menu.grid(row=0, column=3, padx=smallPaddingX, sticky="W", pady=smallPaddingY)
accentItems.append(menu)

segoe_font_menu = font.Font()
segoe_font_menu.configure(family="Arial", size=window.TkScale(10))

menu.menu = tkinter.Menu(
    menu,
    tearoff=0,
    bd=0,
    relief="solid",
    font=segoe_font_menu,
    activeborderwidth=0,
    activebackground="#c4c4c4",
    activeforeground="#000000",
    selectcolor="black")

advancedMenu = tkinter.Menu(
    menu.menu,
    tearoff=0,
    bd=0,
    relief="solid",
    font=segoe_font_menu,
    activeborderwidth=0,
    activebackground="#c4c4c4",
    activeforeground="#000000",
    selectcolor="black")
advancedMenu.add_command(label="Notes List", command=openNotesList)
advancedMenu.add_command(label="Clear Cache", command=clearCache)
# advancedMenu.add_command(label="Minimize to systray", command=minSysTray)

menu["menu"] = menu.menu

menu.menu.add_command(label="Choose theme:")
menu.menu.add_radiobutton(label="Blue", command=accentblue)
menu.menu.add_radiobutton(label="Yellow", command=accentyellow)
menu.menu.add_radiobutton(label="Green", command=accentgreen)
menu.menu.add_radiobutton(label="Pink", command=accentpink)

menu.menu.add_separator()

menu.menu.add_command(label="Open Note", command=openFileChoose)
menu.menu.add_command(
    label="Save Note",
    command=saveNote,
    accelerator="(Ctr+s)")
menu.menu.add_cascade(label="More...", menu=advancedMenu)
menu.menu.add_separator()
menu.menu.add_command(
    label="Undo",
    command=notes.edit_undo,
    accelerator="(Ctr+z)")
menu.menu.add_command(
    label="Redo",
    command=notes.edit_redo,
    accelerator="(Ctr+y)")
menu.menu.add_command(
    label="Quit",
    command=windowdestroy,
    accelerator="(Ctr+q)")
menu.menu.add_command(label="Help/About", command=openReadme)

spacer = tkinter.Frame(titleBar, bg="#2292ff")
spacer.grid(row=0, column=5, sticky="we")
accentItems.append(spacer)

close_button = tkinter.Button(
    titleBar,
    image=closeButtonImage,
    bd=0,
    bg="#2292ff",
    command=windowdestroy,
    pady=4,
    activebackground="#2292ff")
close_button.image = closeButtonImage
close_button.grid(
    row=0,
    column=6,
    sticky="E",
    padx=(
        window.TkScale(10),
        window.TkScale(10)))
accentItems.append(close_button)

# # Bottom formatting bar

bottom_bar = tkinter.Frame(window, relief="flat", bg="#181926", pady=3)
bottom_bar.grid(row=3, column=0, columnspan=10, rowspan=1, sticky="SWE")

bold = tkinter.Button(
    bottom_bar,
    image=boldButtonImage,
    bd=0,
    bg="#181926",
    command=bolder,
    pady=4,
    activebackground="#181926",
    fg="white",
    padx=3)
bold.image = boldButtonImage
bold.grid(row=0, column=1, padx=smallPaddingX, sticky="W", pady=smallPaddingY)

italic = tkinter.Button(
    bottom_bar,
    image=italicButtonImage,
    bd=0,
    bg="#181926",
    command=italicizer,
    pady=4,
    activebackground="#181926",
    fg="white",
    padx=3)
italic.image = italicButtonImage
italic.grid(
    row=0,
    column=2,
    padx=smallPaddingX,
    sticky="W",
    pady=smallPaddingY)

underline = tkinter.Button(
    bottom_bar,
    image=underButtonImage,
    bd=0,
    bg="#181926",
    command=underliner,
    pady=4,
    activebackground="#181926",
    fg="white",
    padx=3)
underline.image = underButtonImage
underline.grid(
    row=0,
    column=3,
    padx=smallPaddingX,
    sticky="W",
    pady=smallPaddingY)

strikeThrough = tkinter.Button(
    bottom_bar,
    image=strikeButtonImage,
    bd=0,
    bg="#181926",
    pady=4,
    command=strikethrough,
    activebackground="#181926",
    fg="white",
    padx=3)
strikeThrough.image = strikeButtonImage
strikeThrough.grid(
    row=0,
    column=4,
    padx=smallPaddingX,
    sticky="W",
    pady=smallPaddingY)

bullet = tkinter.Button(
    bottom_bar,
    image=bulletButtonImage,
    bd=0,
    bg="#181926",
    pady=4,
    command=bulletList,
    activebackground="#181926",
    fg="white",
    padx=3)
bullet.image = bulletButtonImage
bullet.grid(
    row=0,
    column=5,
    padx=smallPaddingX,
    sticky="W",
    pady=smallPaddingY)

code = tkinter.Button(
    bottom_bar,
    image=codeButtonImage,
    bd=0,
    bg="#181926",
    pady=4,
    command=codify,
    activebackground="#181926",
    fg="white",
    padx=3)
code.image = codeButtonImage
code.grid(row=0, column=6, padx=smallPaddingX, sticky="W", pady=smallPaddingY)

insertl = tkinter.Button(
    bottom_bar,
    image=insertlButtonImage,
    bd=0,
    bg="#181926",
    pady=4,
    command=link,
    activebackground="#181926",
    fg="white",
    padx=3)
insertl.image = insertlButtonImage
insertl.grid(
    row=0,
    column=7,
    padx=smallPaddingX,
    sticky="W",
    pady=smallPaddingY)

colorText = tkinter.Button(
    bottom_bar,
    image=colorButtonImage,
    bd=0,
    bg="#181926",
    pady=4,
    command=setColor,
    activebackground="#181926",
    fg="white",
    padx=3)
colorText.image = colorButtonImage
colorText.grid(
    row=0,
    column=8,
    padx=smallPaddingX,
    sticky="W",
    pady=smallPaddingY)

photoInsert = tkinter.Button(
    bottom_bar,
    image=photoButtonImage,
    bd=0,
    bg="#181926",
    pady=4,
    command=photoInserter,
    activebackground="#181926",
    fg="white",
    padx=3)
photoInsert.image = colorButtonImage
photoInsert.grid(
    row=0,
    column=9,
    padx=smallPaddingX,
    sticky="W",
    pady=smallPaddingY)

# Positioning title bar and adding drag function
titleBar.grid(row=0, column=0, columnspan=5, sticky="WE")
titleBar.grid_columnconfigure(5, weight=1)
titleBar.grid_columnconfigure(6, weight=0)


# Keyboard Shortcuts
titleBar.bind("<Button-1>", getPos)
notes.bind("<Control-Key-b>", bolder)
notes.bind("<Control-Key-i>", italicizer)
notes.bind("<Control-Key-u>", underliner)
notes.bind("<Control-Key-t>", codify)
notes.bind("<Control-Key-q>", windowdestroy)
notes.bind("<Control-Key-s>", saveNote)
notes.bind("<Control-Key-k>", link)
notes.bind("<Control-Key-o>", openLink)
notes.bind("<Control-slash>", strikethrough)

# Hover Effects
bold.bind("<Enter>", hoverImageBold)
bold.bind("<Leave>", NormalImageBold)
italic.bind("<Enter>", hoverImageItalic)
italic.bind("<Leave>", NormalImageItalic)
underline.bind("<Enter>", hoverImageUnder)
underline.bind("<Leave>", NormalImageUnder)
strikeThrough.bind("<Enter>", hoverImageStrike)
strikeThrough.bind("<Leave>", NormalImageStrike)
bullet.bind("<Enter>", hoverImageBullet)
bullet.bind("<Leave>", NormalImageBullet)
code.bind("<Enter>", hoverImageCode)
code.bind("<Leave>", NormalImageCode)
new.bind("<Enter>", hoverImageNew)
new.bind("<Leave>", NormalImageNew)
save.bind("<Enter>", hoverImageSave)
save.bind("<Leave>", NormalImageSave)
openlink.bind("<Enter>", hoverImageOpen)
openlink.bind("<Leave>", NormalImageOpen)
menu.bind("<Enter>", hoverImageMenu)
menu.bind("<Leave>", NormalImageMenu)
close_button.bind("<Enter>", hoverImageClose)
close_button.bind("<Leave>", NormalImageClose)
insertl.bind("<Enter>", hoverImageLink)
insertl.bind("<Leave>", NormalImageLink)
colorText.bind("<Enter>", hoverImageTsize)
colorText.bind("<Leave>", NormalImageTsize)
photoInsert.bind("<Enter>", hoverImagePhoto)
photoInsert.bind("<Leave>", NormalImagePhoto)

# Bind the focus events
window.bind("<FocusIn>", on_focus_in)
window.bind("<FocusOut>", on_focus_out)

# Desktop Gadget and Autosave
window.after(200, topOrNot)
window.after(3000, autoSave)
window.after(3000, autoReload)

# Open a file
if args.file is not None:
    file_path = os.path.join(dataPath, args.file)
    if not os.path.exists(file_path):
        tkinter.messagebox.showerror("Error", f"File {args.file} does not exist.")
        sys.exit(1) 
    openFile(args.file)
else:
    # Ask for a filename
    filename = simpledialog.askstring("Input", "Please enter a filename:")
    file_path = os.path.join(dataPath, filename)
    
    # Check if file exists
    if os.path.exists(file_path):
        tkinter.messagebox.showerror("Error", f"File {filename} already exists.")
        sys.exit(1)  # Exit the application
    else:
        # Create and save a blank file
        with open(file_path, 'w') as file:
            file.write("")

def start_resize(event):
    global start_x, start_y, start_width, start_height
    start_x = event.x_root
    start_y = event.y_root
    start_width = window.winfo_width()
    start_height = window.winfo_height()

def perform_resize(event):
    delta_x = event.x_root - start_x
    delta_y = event.y_root - start_y
    new_width = start_width + delta_x
    new_height = start_height + delta_y
    window.geometry(f"{new_width}x{new_height}")

style = ttk.Style()
style.layout("Black.TSizegrip",
             [('Sizegrip.sizegrip', {'sticky': 'nswe'})])
style.configure("Black.TSizegrip", background='#181926', foreground='#181926')

# Add the gripper for resizing the window with the new style
grip = ttk.Sizegrip(window, style="Black.TSizegrip")
grip.place(relx=1.0, rely=1.0, anchor="se")

# Bind mouse events for resizing
grip.bind("<ButtonPress-1>", start_resize)
grip.bind("<B1-Motion>", perform_resize)

# Update the window
window.mainloop()
