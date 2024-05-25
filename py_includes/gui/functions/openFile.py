import os
from random import randint
import re
from tkinter import PhotoImage
from ... import globalvars
from ...helpers.tags import setup_tags
from ...enums.Color import Color
from ...color_theme import set_color_theme

def openFile(file: str):
    """Open a file with the file dialog"""

    if file is None or file == "":
        return
    
    noteFile = file
    if noteFile:
        globalvars.openedFileName = noteFile
    noteFileFullPath = os.path.join(globalvars.dataPath, noteFile)
    noteFile = open(noteFileFullPath, "r")

    if globalvars.openedFileName_lastModTime == os.path.getmtime(noteFileFullPath):
        return
    globalvars.openedFileName_lastModTime = os.path.getmtime(noteFileFullPath)

    read = noteFile.read()

    matchStyle = re.match(r".*<style>\n(.*)\n</style>", str(read), flags=re.DOTALL | re.MULTILINE)
    matchImg = re.match(r".*<images>\n(.*)\n</images>", str(read), flags=re.DOTALL | re.MULTILINE)
    matchTheme = re.match(
        r".*<colortheme>\n(.*)\n</colortheme>",
        str(read),
        flags=re.DOTALL | re.MULTILINE,
    )
    matchLocation = re.match(
        rf".*<screenlocation>(.*\n{globalvars.machine_identifier}: (.+?)\n.*)</screenlocation>",
        str(read),
        flags=re.DOTALL | re.MULTILINE,
    )

    read = re.sub("<style>.*$", "", read, flags=re.DOTALL | re.MULTILINE)
    read = re.sub("<content>\n", "", read, flags=re.DOTALL | re.MULTILINE)
    read = re.sub("\n*</content>\n\n", "", read, flags=re.DOTALL | re.MULTILINE)

    globalvars.notes.delete("1.0", "end")
    globalvars.notes.insert("end", read)
    
    if matchLocation:
        globalvars.all_screenlocations = matchLocation.group(1)
        location = eval(matchLocation.group(2))
        x, y, width, height = location
        globalvars.window.geometry(globalvars.window.TkGeometryScale(f"{width}x{height}+{x}+{y}"))
    else:
        globalvars.window.geometry(globalvars.window.TkGeometryScale(f"310x310+{str(randint(10, 900))}+{str(randint(10, 500))}"))
    globalvars.window.update()
    
    if matchTheme:
        # Getting the theme of the note
        exec(matchTheme.group(1))

    if matchStyle:
        formatting = eval(matchStyle.group(1))
        setup_tags()
        for format in formatting:
            for tag in format[2]:
                    globalvars.notes.tag_add(str(tag).strip("}{/.\\"), format[0], format[1]) if tag else None

    if matchImg:
        # Getting the list of images
        globalvars.images = eval(matchImg.group(1))
        if globalvars.images is not None:
            globalvars.allImagesGroup = []
            for imageList in globalvars.images:
                # Insert the images at appropriate index
                imageToInsert = PhotoImage(file=f"{imageList[0]}.png")
                globalvars.notes.insert(f"{imageList[1]}-1c", "\n")
                globalvars.notes.image_create(imageList[1], image=imageToInsert, name=imageList[2])
                globalvars.allImagesGroup.append(imageToInsert)

    noteFile.close()
    globalvars.saved = True
    return "break"
