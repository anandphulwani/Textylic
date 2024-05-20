import random
import tkinter as tk
import itertools
from .. import globalvars
from ..helpers.is_font_present import is_font_present
from ..helpers.configure_font import configure_font

def get_current_tag_as_string(text_widget):
    try:
        current_tags = text_widget.tag_names("sel.first")
        print(f'get_current_tag_as_string: {current_tags}')
        notes_tags = [tag for tag in current_tags if all(element in globalvars.notes_tags_options for element in tag.split("+"))]
        return notes_tags[0] if notes_tags else ""
    except tk.TclError:
        return ""

def create_new_tag(existing_tag, new_tag):
    if existing_tag == "":
        return new_tag
    existing_tags = existing_tag.split("+")
    existing_tags.append(new_tag)
    existing_tags.sort()
    new_tag_name = "+".join(existing_tags)
    return new_tag_name

def remove_existing_tag(existing_tag, tag_to_remove):
    existing_tags = existing_tag.split("+")
    if tag_to_remove in existing_tags:
        existing_tags.remove(tag_to_remove)
    existing_tags.sort()
    new_tag_name = "+".join(existing_tags)
    return new_tag_name

def is_notes_tag_present(existing_notes_tag, tag_to_search):
    return tag_to_search in existing_notes_tag.split("+")

def update_tag(text_widget, existing_notes_tag, add_tags, start_selection = "sel.first", end_selection = "sel.last"):
    try:
        new_notes_tag = create_new_tag(existing_notes_tag, add_tags)
        if existing_notes_tag != "":
            text_widget.tag_remove(existing_notes_tag, start_selection, end_selection)
        text_widget.tag_add(new_notes_tag, start_selection, end_selection)
    except tk.TclError:
        pass  # No selection, do nothing

def remove_tag(text_widget, existing_notes_tag, tag_to_remove, start_selection = "sel.first", end_selection = "sel.last"):
    try:
        if existing_notes_tag == "":
            return
        new_notes_tag = remove_existing_tag(existing_notes_tag, tag_to_remove)
        text_widget.tag_remove(existing_notes_tag, start_selection, end_selection)
        if new_notes_tag != "":
            text_widget.tag_add(new_notes_tag, start_selection, end_selection)
    except tk.TclError:
        pass  # No selection, do nothing

def toggle_notes_tag(tag, _=False):
    """Toggle a notes tag (e.g., bold, italic, etc..)"""
    try:
        existing_notes_tag = get_current_tag_as_string(globalvars.notes)
        if tag == "bullet":
            selection = globalvars.notes.selection_get()
            index_1 = globalvars.notes.index("sel.first")
            index_2 = globalvars.notes.index("sel.last")
            is_multi_line = True if "\n" in selection else False
                
            if not is_notes_tag_present(existing_notes_tag, "bullet"):
                selected = "\t•  " + selection.replace("\n", "\n\t•  ") if is_multi_line else "\t•  " + selection
            else:
                selected = selection.replace("\n\t•  ", "\n").replace("\t•  ", "") if is_multi_line else selection.replace("\t•  ", "")
            
            globalvars.notes.delete(index_1, index_2)
            globalvars.notes.insert(index_1, selected)
            len_bullet_string = globalvars.notes.index(f"{index_1} + {len(selected)} chars")

        if is_notes_tag_present(existing_notes_tag, tag):
            remove_tag(globalvars.notes, existing_notes_tag, tag) if tag != "bullet" else remove_tag(globalvars.notes, existing_notes_tag, tag, index_1, len_bullet_string)
        else:
            update_tag(globalvars.notes, existing_notes_tag, tag) if tag != "bullet" else update_tag(globalvars.notes, existing_notes_tag, tag, index_1, len_bullet_string)
    except tk.TclError:
        pass
    return "break"

def setup_tags():
    base_font_name = globalvars.notes.cget("font").split()[0]
    options = globalvars.notes_tags_options

    fonts = {}
    
    # Generate all combinations of options from 1 to 7 elements
    for i in range(1, len(options) + 1):
        for combination in itertools.combinations(options, i):
            combination_name = "+".join(sorted(combination))
            font_kwargs = {
                "weight": "bold" if "bold" in combination else "normal",
                "slant": "italic" if "italic" in combination else "roman",
                "underline": "underline" in combination,
                "overstrike": "strikethrough" in combination,
                "size": 10 if "code" in combination and is_font_present("JetBrainsMono NF") else 11,
                "family": "JetBrainsMono NF" if "code" in combination and is_font_present("JetBrainsMono NF") else base_font_name
            }
            if "link" in combination:
                font_kwargs["underline"] = True
            fonts[combination_name] = configure_font(base_font_name, **font_kwargs)
            # print(combination_name)

    # Configure tags in the Text widget
    for tag, font in fonts.items():
        if "link" in tag:
            globalvars.notes.tag_configure(tag, font=font, foreground="#00AFEC")
        elif "colortext" in tag:
            print(f"{random.randint(0, 1000)} {globalvars.currentThemeColor}")
            color_settings = globalvars.color_map[globalvars.currentThemeColor]
            bg_color = color_settings["bg"]
            globalvars.notes.tag_configure(tag, font=font, foreground=bg_color)
        else:
            globalvars.notes.tag_configure(tag, font=font)