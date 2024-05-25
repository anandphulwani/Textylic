﻿import os
from ...enums.Color import Color
from ... import globalvars
from ...notes_functions.getTags import getTags
from .saveNoteAs import saveNoteAs
from ...helpers.get_calling_script_path import get_calling_script_path

def saveNote(_=False):
    """Save the note"""

    deletedImages = []  # List that holds all images that need to be deleted
    image_names = globalvars.notes.image_names()
    if image_names:
        for imgName in image_names:
            # Saving the list of image names
            index = globalvars.notes.index(str(imgName))

            for image in globalvars.images:
                # Deleting unused images from the list
                if image[2] in image_names:
                    if image[2] == imgName:
                        image[1] = index
                else:
                    if image not in deletedImages:
                        deletedImages.append(image)
    else:
        # Handle case where image_names is empty
        for image in globalvars.images:
            if image not in deletedImages:
                deletedImages.append(image)

    for deletedImage in deletedImages:
        # Deleting the unused images from `images` list
        try:
            globalvars.images.remove(deletedImage)            
            deletedImage[0] = os.path.join(os.path.dirname(get_calling_script_path()), deletedImage[0] + ".png")
            deletedImage[0] = deletedImage[0].replace(os.sep, '/') if os.name == 'nt' else deletedImage[0]
            if os.path.exists(deletedImage[0]):
                os.remove(deletedImage[0])
        except BaseException:
            pass

    if globalvars.openedFileName:
        new_content = []
        new_content.append("<content>\n{}\n</content>\n\n".format(globalvars.notes.get(1.0, "end")))
        new_content.append("<style>\n{}\n</style>\n\n".format(getTags("1.0", "end")))
        new_content.append("<images>\n{}\n</images>\n\n".format(globalvars.images))

        new_content.append(f"<colortheme>\nset_color_theme(Color.{globalvars.currentThemeColor.to_string()})\n</colortheme>\n\n")

        new_content_str = "".join(new_content)

        # Get the current content of the file
        note_file_path = os.path.join(globalvars.dataPath, globalvars.openedFileName)
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
