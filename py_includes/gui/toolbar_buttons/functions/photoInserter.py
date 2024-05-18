from datetime import datetime
from tkinter import PhotoImage, filedialog
from PIL import Image
from .... import globalvars

def photoInserter():
    """'Insert photo' button function"""

    dateTimeNow = str(datetime.now())
    dateTimeNow = dateTimeNow.replace("-", "_")
    dateTimeNow = dateTimeNow.replace(" ", "_")
    dateTimeNow = dateTimeNow.replace(":", "")
    dateTimeNow = dateTimeNow.replace(".", "")

    globalvars.imgNumberName = globalvars.imgNumberName + 1

    photo = filedialog.askopenfilename(
        initialdir="~/Pictures",
        title="Choose an Image:",
        filetypes=(
            ("PNG", "*.png"),
            ("JPG", "*.jpg"),
            ("JPEG", "*.jpeg"),
        ),
    )
    imgFile = Image.open(photo)
    imgFile.thumbnail((globalvars.window.TkScale(280), globalvars.window.TkScale(280)))
    imgFile.save(f"./res/cache_images_/{dateTimeNow}.png")

    imgToInsert = PhotoImage(file=f"./res/cache_images_/{dateTimeNow}.png")
    globalvars.allImagesGroup.append(imgToInsert)
    globalvars.images.append(
        [
            f"./res/cache_images_/{dateTimeNow}",
            globalvars.notes.index("insert"),
            f"image{globalvars.imgNumberName}",
        ]
    )
    globalvars.notes.image_create("insert", image=imgToInsert, name=f"image{globalvars.imgNumberName}")
    imgFile.close()
    photo.close()
