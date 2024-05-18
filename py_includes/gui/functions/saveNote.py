import os
from ...enums.Color import Color
from ... import globalvars
from ...notes_functions import getTags
from .saveNoteAs import saveNoteAs

def saveNote(_=False):
    """Save the note"""

    for imgName in globalvars.notes.image_names():
        # Saving the list of image names
        index = globalvars.notes.index(str(imgName))

        for image in globalvars.images:
            # Deleting unused images from the list
            if image[2] in globalvars.notes.image_names():
                if image[2] == imgName:
                    image[1] = index
            else:
                globalvars.deletedImages.append(image)

    for deletedImage in globalvars.deletedImages:
        # Deleting the unused images from `images` list
        try:
            globalvars.images.remove(deletedImage)
        except BaseException:
            pass

    if globalvars.openedFileName:
        new_content = []
        new_content.append("<content>\n{}\n</content>\n\n".format(globalvars.notes.get(1.0, "end")))
        new_content.append("<style>\n{}\n</style>\n\n".format(getTags("1.0", "end")))
        new_content.append("<images>\n{}\n</images>\n\n".format(globalvars.images))

        if globalvars.currentThemeColor == Color.BLUE:
            new_content.append("<colortheme>\nset_color_theme(Color.BLUE)\n</colortheme>")
        elif globalvars.currentThemeColor == Color.YELLOW:
            new_content.append("<colortheme>\nset_color_theme(Color.YELLOW)\n</colortheme>")
        elif globalvars.currentThemeColor == Color.GREEN:
            new_content.append("<colortheme>\nset_color_theme(Color.GREEN)\n</colortheme>")
        elif globalvars.currentThemeColor == Color.PINK:
            new_content.append("<colortheme>\nset_color_theme(Color.PINK)\n</colortheme>")
        
        new_content_str = "".join(new_content)

        # Get the current content of the file
        note_file_path = os.path.join(globals.datapath, globalvars.openedFileName)
        try:
            with open(note_file_path, "r") as noteFile:
                current_content = noteFile.read()
        except FileNotFoundError:
            current_content = ""

        # Compare the current content with the new content
        if current_content != new_content_str:
            # If the contents are different, write the new content to the file
            with open(note_file_path, "w") as noteFile:
                noteFile.write(new_content_str)
        globalvars.saved = True
        getTags("1.0", "end")
    else:
        saveNoteAs()
    return "break"
