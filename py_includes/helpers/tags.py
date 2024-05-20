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

def update_tag(text_widget, add_tags):
    try:
        existing_notes_tag = get_current_tag_as_string(text_widget)
        new_notes_tag = create_new_tag(existing_notes_tag, add_tags)
        if existing_notes_tag != "":
            text_widget.tag_remove(existing_notes_tag, "sel.first", "sel.last")
        text_widget.tag_add(new_notes_tag, "sel.first", "sel.last")
        print(f'update_tag: existing_notes_tag: {existing_notes_tag}, new_notes_tag: {new_notes_tag}')
    except tk.TclError:
        pass  # No selection, do nothing

def remove_tag(text_widget, tag_to_remove):
    try:
        existing_notes_tag = get_current_tag_as_string(text_widget)
        if existing_notes_tag == "":
            return
        new_notes_tag = remove_existing_tag(existing_notes_tag, tag_to_remove)
        text_widget.tag_remove(existing_notes_tag, "sel.first", "sel.last")
        if new_notes_tag != "":
            text_widget.tag_add(new_notes_tag, "sel.first", "sel.last")
        print(f'remove_tag: existing_notes_tag: {existing_notes_tag}, new_notes_tag: {new_notes_tag}')
    except tk.TclError:
        pass  # No selection, do nothing

def toggle_notes_tag(tag, _=False):
    """Toggle a notes tag (e.g., bold, italic, etc..)"""
    try:
        current_tags = get_current_tag_as_string(globalvars.notes)
        # print(f'current_tags: {current_tags}')
        if is_notes_tag_present(current_tags, tag):
            remove_tag(globalvars.notes, tag)
        else:
            update_tag(globalvars.notes, tag)
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