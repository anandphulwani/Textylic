import os
import re
from tkinter import font
from tkinter import PhotoImage
from ...enums.Color import Color
from ... import globalvars
from ...helpers.is_font_present import is_font_present
from ...color_theme import set_color_theme

def openFile(file: str):
    """Open a file with the file dialog"""

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

    read = re.sub("<style>.*$", "", read, flags=re.DOTALL | re.MULTILINE)
    read = re.sub("<content>\n", "", read, flags=re.DOTALL | re.MULTILINE)
    read = re.sub("\n*</content>\n\n", "", read, flags=re.DOTALL | re.MULTILINE)

    globalvars.notes.delete("1.0", "end")
    globalvars.notes.insert("end", read)

    if matchStyle:
        # Bold fonts and tags
        formatting = matchStyle.group(1)
        formatting = eval(formatting)

        bold_font = font.Font(globalvars.notes, globalvars.notes.cget("font"))
        bold_font.configure(weight="bold")

        italicBold_font = font.Font(globalvars.notes, globalvars.notes.cget("font"))
        italicBold_font.configure(slant="italic", weight="bold")

        underBold_font = font.Font(globalvars.notes, globalvars.notes.cget("font"))
        underBold_font.configure(underline=True, weight="bold")

        strikeBold_font = font.Font(globalvars.notes, globalvars.notes.cget("font"))
        strikeBold_font.configure(overstrike=True, weight="bold")

        globalvars.notes.tag_configure("bold", font=bold_font)
        globalvars.notes.tag_configure("italicBold", font=italicBold_font)
        globalvars.notes.tag_configure("underBold", font=underBold_font)
        globalvars.notes.tag_configure("strikeBold", font=strikeBold_font)

        # Italic fonts and tags
        italic_font = font.Font(globalvars.notes, globalvars.notes.cget("font"))
        italic_font.configure(slant="italic")

        boldItalic_font = font.Font(globalvars.notes, globalvars.notes.cget("font"))
        boldItalic_font.configure(slant="italic", weight="bold")

        underItalic_font = font.Font(globalvars.notes, globalvars.notes.cget("font"))
        underItalic_font.configure(underline=True, slant="italic")

        strikeItalic_font = font.Font(globalvars.notes, globalvars.notes.cget("font"))
        strikeItalic_font.configure(overstrike=True, slant="italic")

        globalvars.notes.tag_configure("italic", font=italic_font)
        globalvars.notes.tag_configure("boldItalic", font=boldItalic_font)
        globalvars.notes.tag_configure("underItalic", font=underItalic_font)
        globalvars.notes.tag_configure("strikeItalic", font=strikeItalic_font)

        # Code font and tags
        desired_font = ("JetBrainsMono NF", 10) if is_font_present("JetBrainsMono NF") else "Consolas 11"
        globalvars.notes.tag_configure("code", font=desired_font)

        # Underline font and tags
        under_font = font.Font(globalvars.notes, globalvars.notes.cget("font"))
        under_font.configure(underline=True)

        boldUnder_font = font.Font(globalvars.notes, globalvars.notes.cget("font"))
        boldUnder_font.configure(underline=True, weight="bold")

        italicUnder_font = font.Font(globalvars.notes, globalvars.notes.cget("font"))
        italicUnder_font.configure(underline=True, slant="italic")

        strikeUnder_font = font.Font(globalvars.notes, globalvars.notes.cget("font"))
        strikeUnder_font.configure(overstrike=True, underline=True)

        globalvars.notes.tag_configure("underline", font=under_font)
        globalvars.notes.tag_configure("boldUnder", font=boldUnder_font)
        globalvars.notes.tag_configure("italicUnder", font=italicUnder_font)
        globalvars.notes.tag_configure("strikeUnder", font=strikeUnder_font)

        # Link font
        globalvars.notes.tag_configure("link", font=under_font, foreground="#00AFEC")

        # Text color
        color_settings = globalvars.color_map[globalvars.currentThemeColor]
        bg_color = color_settings["bg"]
        globalvars.notes.tag_configure("emphColor", foreground=bg_color)
        
        for format in formatting:
            # Apply formatting
            for tag in format[2]:
                globalvars.notes.tag_add(str(tag).strip("}{/.\\"), format[0], format[1])

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

    if matchTheme:
        # Getting the theme of the note
        exec(matchTheme.group(1))

    noteFile.close()
    globalvars.saved = True
    return "break"
