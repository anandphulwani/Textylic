import glob
import os
import re
from ... import globalvars

def clearCache():
    """Clearing the unused images from the `cache_images_` folder"""

    imagesToBeSaved = []
    pathToNotes = "./Notes"
    pathToNotes = os.path.join(pathToNotes, "*.txtlyc")
    pathToNotes = pathToNotes.replace("\\", "/")

    pathToImages = "./res/cache_images_"
    pathToImages = os.path.join(pathToImages, "*.*")
    pathToImages = pathToImages.replace("\\", "/")

    for filename in glob.glob(pathToNotes):
        # For all the images in the `cache_images_` folder check if they are
        # in the `images` list for every note
        formattedFileName = filename.replace("\\", "/")
        noteFile = open(os.path.join(globalvars.datapath, f"{formattedFileName}"), "r")
        readContent = noteFile.read()
        matchImg = re.match(
            r".*<images>\n(.*)\n</images>",
            str(readContent),
            flags=re.DOTALL | re.MULTILINE,
        )

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
