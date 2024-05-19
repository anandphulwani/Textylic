import os
import re
from tkinter import font
from tkinter import PhotoImage
from ...enums.Color import Color
from ... import globalvars
from ...helpers.is_font_present import is_font_present
from ...helpers.configure_font import configure_font
from ...color_theme import set_color_theme

def setup_tags():
    base_font = globalvars.notes.cget("font")
    fonts = {
        "bold": configure_font(base_font, weight="bold"),
        "italic": configure_font(base_font, slant="italic"),
        "underline": configure_font(base_font, underline=True),
        "strikethrough": configure_font(base_font, overstrike=True),
        "bold_italic": configure_font(base_font, weight="bold", slant="italic"),
        "bold_underline": configure_font(base_font, weight="bold", underline=True),
        "italic_underline": configure_font(base_font, slant="italic", underline=True),
        "strikethrough_bold": configure_font(base_font, overstrike=True, weight="bold"),
        "strikethrough_italic": configure_font(base_font, overstrike=True, slant="italic"),
        "strikethrough_underline": configure_font(base_font, overstrike=True, underline=True),
        "strikethrough_bold_italic": configure_font(base_font, overstrike=True, weight="bold", slant="italic"),
        "bold_italic_underline": configure_font(base_font, weight="bold", slant="italic", underline=True),
        "strikethrough_bold_underline": configure_font(base_font, overstrike=True, weight="bold", underline=True),
        "strikethrough_italic_underline": configure_font(base_font, overstrike=True, slant="italic", underline=True),
        "strikethrough_bold_italic_underline": configure_font(base_font, overstrike=True, weight="bold", slant="italic", underline=True),
        "code": configure_font("JetBrainsMono NF", size=10) if is_font_present("JetBrainsMono NF") else configure_font("Consolas", size=11),
        "link": configure_font(base_font, underline=True),
        "color_text": configure_font(base_font),  # Add color separately
    }

    color_settings = globalvars.color_map[globalvars.currentThemeColor]
    bg_color = color_settings["bg"]

    for tag, font in fonts.items():
        if tag == "link":
            globalvars.notes.tag_configure(tag, font=font, foreground="#00AFEC")
        elif tag == "color_text":
            globalvars.notes.tag_configure(tag, font=font, foreground=bg_color)
        else:
            globalvars.notes.tag_configure(tag, font=font)

def apply_formatting(formatting):
    for format in formatting:
        combined_tags = []
        for tag in format[2]:
            tag_name = str(tag).strip("}{/.\\")

            # Combine basic tags for bold, italic, underline, and strikethrough
            if tag_name in ["bold", "italic", "underline", "strikethrough"]:
                combined_tags.append(tag_name)

        if combined_tags:
            combined_tag = '_'.join(sorted(combined_tags))
            globalvars.notes.tag_add(combined_tag, format[0], format[1])
        else:
            for tag in format[2]:
                tag_name = str(tag).strip("}{/.\\")

                # Add other tags as they are
                globalvars.notes.tag_add(tag_name, format[0], format[1])

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

    read = re.sub("<style>.*$", "", read, flags=re.DOTALL | re.MULTILINE)
    read = re.sub("<content>\n", "", read, flags=re.DOTALL | re.MULTILINE)
    read = re.sub("\n*</content>\n\n", "", read, flags=re.DOTALL | re.MULTILINE)

    globalvars.notes.delete("1.0", "end")
    globalvars.notes.insert("end", read)

    if matchStyle:
        formatting = eval(matchStyle.group(1))
        setup_tags()
        apply_formatting(formatting)

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
