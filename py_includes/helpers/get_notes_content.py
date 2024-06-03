import re
from .. import globalvars
from ..enums.Color import Color
from ..notes_functions.getTags import getTags
from ..helpers.get_window_coordinates import get_window_coordinates
from ..helpers.obfuscate_deobfuscate_xor import obfuscate_text_by_lines

def get_notes_content():
    """Get the content of the notes"""
    new_content = []
    new_content.append("<content>\n{}\n</content>\n\n".format(obfuscate_text_by_lines(globalvars.notes.get(1.0, "end")[:-1])))
    new_content.append("<style>\n{}\n</style>\n\n".format(getTags("1.0", "end")))
    new_content.append("<images>\n{}\n</images>\n\n".format(globalvars.images))

    new_content.append(f"<colortheme>\nset_color_theme(Color.{globalvars.currentThemeColor.to_string()})\n</colortheme>\n\n")
    if globalvars.all_screenlocations is None:
        new_content.append(f"<screenlocation>\n{globalvars.machine_identifier}: {get_window_coordinates()}: Enabled\n</screenlocation>\n\n")
    else:
        updated_screenlocations = re.sub(
            rf"({globalvars.machine_identifier}: .+?\n)", f"{globalvars.machine_identifier}: {get_window_coordinates()}: Enabled\n",
            globalvars.all_screenlocations, flags=re.DOTALL | re.MULTILINE)
        new_content.append(f"<screenlocation>{updated_screenlocations}</screenlocation>\n\n")

    new_content_str = "".join(new_content)
    return new_content_str
