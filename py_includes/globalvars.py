import os
import ctypes

from .helpers.get_machine_identifier import get_machine_identifier
from .enums.Color import Color

appdata_path = os.environ.get("APPDATA")
dataPath = os.path.join(appdata_path, "Textylyc")

# Ensure the path exists, if not, create it
if not os.path.exists(dataPath):
    os.makedirs(dataPath)

window = None
root = None
titleBar = None
menu_button = None
notes = None
notesFrame = None

start_x = None
start_y = None
start_width = None
start_height = None

window_is_focused = False
current_focus_mode = "unlock"
focus_pinapp_window = None

openedFileName = False  # Getting opened file name
openedFileName_lastModTime = False

saved = False  # The saved variable

overlay = False
isOverlayEnabled = False

smallPaddingX = None
smallPaddingY = None

top_menu_buttons = None
bottom_menu_buttons = None

allImagesGroup = []  # Reference list with images in it
imgNumberName = 0  # A variable used to name images in chronological order
accentItems = []  # List that holds all items that have accent color

images = []

color_map = {
    Color.BLUE: {"bg": "#2292FF", "notesfrm_color": "#59C0E7"},
    Color.YELLOW: {"bg": "#FBC02D", "notesfrm_color": "#E6B905"},
    Color.GREEN: {"bg": "#65BA5A", "notesfrm_color": "#65BA5A"},
    Color.PINK: {"bg": "#EB8EC6", "notesfrm_color": "#EB8EC6"}
}

currentThemeColor = Color.BLUE

notes_tags_options = ["bold", "italic", "underline", "strikethrough", "bullet", "code", "createlink", "colortext"]

psapi = ctypes.WinDLL('Psapi.dll')
kernel32 = ctypes.WinDLL('kernel32.dll')
user32 = ctypes.WinDLL('user32.dll')

machine_identifier = get_machine_identifier()
all_screenlocations = None
