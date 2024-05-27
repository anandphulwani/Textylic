import os
import shutil
from ...helpers.get_calling_script_path import get_calling_script_path
from ...generate_imgs_from_json import generate_image_from_json

def check_and_create_colored_scrollbar_if_not_exist(colorHex: str):
    script_path = os.path.dirname(get_calling_script_path())
    # Create the colored scrollbar template if it does not exist
    tclFile = os.path.join(script_path, "themes", colorHex + ".tcl")
    if not os.path.exists(tclFile):
        os.makedirs(os.path.join(script_path, "themes", colorHex), exist_ok = True)
        shutil.copyfile(os.path.join(script_path, "themes", "template", "scrollbar-trough-horiz-active.png"), 
                        os.path.join(script_path, "themes", colorHex, "scrollbar-trough-horiz-active.png"))
        shutil.copyfile(os.path.join(script_path, "themes", "template", "scrollbar-trough-vert-active.png"), 
                        os.path.join(script_path, "themes", colorHex, "scrollbar-trough-vert-active.png"))
        shutil.copyfile(os.path.join(script_path, "themes", "template", "scrollbar-slider-insens.png"), 
                        os.path.join(script_path, "themes", colorHex, "scrollbar-slider-insens.png"))
        generate_image_from_json(os.path.join(script_path, "themes", "template", "scrollbar-slider-horiz.json"), colorHex, 
                                 os.path.join(script_path, "themes", colorHex, "scrollbar-slider-horiz.png"))
        generate_image_from_json(os.path.join(script_path, "themes", "template", "scrollbar-slider-horiz-active.json"), colorHex, 
                                 os.path.join(script_path, "themes", colorHex, "scrollbar-slider-horiz-active.png"))
        generate_image_from_json(os.path.join(script_path, "themes", "template", "scrollbar-slider-vert.json"), colorHex, 
                                 os.path.join(script_path, "themes", colorHex, "scrollbar-slider-vert.png"))
        generate_image_from_json(os.path.join(script_path, "themes", "template", "scrollbar-slider-vert-active.json"), colorHex, 
                                 os.path.join(script_path, "themes", colorHex, "scrollbar-slider-vert-active.png"))
        with open(os.path.join(script_path, "themes", "template.tcl")) as f:
            file_contents = f.read()
        with open(os.path.join(script_path, "themes", colorHex + ".tcl"), "w") as f:
            f.write(file_contents.replace("template", colorHex))
