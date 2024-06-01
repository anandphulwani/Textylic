from datetime import datetime
import os
from tkinter import PhotoImage, filedialog
from PIL import Image
from .... import globalvars

def photoInserter():
    """'Insert photo' button function"""

    # Ensure the directory exists
    images_dir = os.path.join(os.path.dirname(globalvars.openedFileName), "images")
    os.makedirs(images_dir, exist_ok=True)
        
    dateTimeNow = str(datetime.now())
    dateTimeNow = dateTimeNow.replace("-", "_")
    dateTimeNow = dateTimeNow.replace(" ", "_")
    dateTimeNow = dateTimeNow.replace(":", "")
    dateTimeNow = dateTimeNow.replace(".", "")

    globalvars.imgNumberName = globalvars.imgNumberName + 1

    photo = filedialog.askopenfilename(
        initialdir="~/Desktop",
        title="Choose an Image:",
        filetypes=(
            ("PNG", "*.png"),
            ("JPG", "*.jpg"),
            ("JPEG", "*.jpeg"),
        ),
    )
    imgFile = Image.open(photo)
    imgFile.thumbnail((globalvars.window.TkScale(280), globalvars.window.TkScale(280)))
    imgFilename = os.path.join(images_dir, f"{dateTimeNow}")
    imgFile.save(f"{imgFilename}.png")

    imgToInsert = PhotoImage(file=f"{imgFilename}.png")
    globalvars.allImagesGroup.append(imgToInsert)
    globalvars.images.append(
        [
            imgFilename,
            globalvars.notes.index("insert"),
            f"image{globalvars.imgNumberName}",
        ]
    )
    globalvars.notes.image_create("insert", image=imgToInsert, name=f"image{globalvars.imgNumberName}")
    imgFile.close()
