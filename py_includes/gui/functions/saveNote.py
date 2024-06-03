import os
from ... import globalvars
from ...notes_functions.getTags import getTags
from ...helpers.get_notes_content import get_notes_content

def saveNote(isAutoSave):
    """Save the note"""

    with globalvars.save_fn_lock:
        if not isAutoSave:
            images_dir = os.path.join(os.path.dirname(globalvars.openedFileName), "images")
            deletedImages = [f for f in os.listdir(images_dir) if os.path.isfile(os.path.join(images_dir, f))]        
            retainedImages = deletedImages.copy()
            
            # Extract image names from globalvars.notes.image_names()
            image_names = globalvars.notes.image_names()
            corresponding_filenames = []
            for entry in globalvars.images:
                if entry[2] in image_names:
                    corresponding_filenames.append(f"{entry[0]}.png")
            if all(filename in retainedImages for filename in corresponding_filenames):
                retainedImages[:] = [filename for filename in retainedImages if filename in corresponding_filenames]
            else:
                print("Not all corresponding filenames are found in retainedImages.")
                exit(1)
            deletedImages = list(set(deletedImages) - set(retainedImages))

            # Deleting the unused images from `images` list and deleting them from disk
            for deletedImage in deletedImages:
                try:
                    deletedImage_no_ext = os.path.splitext(deletedImage)[0]
                    globalvars.images = [image for image in globalvars.images if image[0] != deletedImage_no_ext]
                    deletedImage = os.path.join(images_dir, deletedImage)
                    deletedImage = deletedImage.replace(os.sep, '/') if os.name == 'nt' else deletedImage
                    if os.path.exists(deletedImage):
                        os.remove(deletedImage)
                except BaseException:
                    pass

        # Update location of image in the notes file, if image location is changed
        for entry in globalvars.images:
            if entry[0] is not None and entry[2] is not None:
                try:
                    curr_location = globalvars.notes.index(entry[2])
                except Exception:
                    globalvars.images.remove(entry)
                    continue
                if entry[1] != curr_location:
                    entry[1] = curr_location
                
        new_content_str = get_notes_content()

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
        getTags("1.0", "end")
    return "break"
