from tkinter import font as tkFont

def configure_font(base_font_name, size=None, weight=None, slant=None, underline=None, overstrike=None):
    # Create a dictionary to store font configuration options
    font_config = {"family": base_font_name}

    # Update the dictionary with provided attributes if they are not None
    if size is not None:
        font_config["size"] = size
    if weight is not None:
        font_config["weight"] = weight
    if slant is not None:
        font_config["slant"] = slant
    if underline is not None:
        font_config["underline"] = underline
    if overstrike is not None:
        font_config["overstrike"] = overstrike

    # Create and return a new Font object with the specified configuration
    return tkFont.Font(**font_config)
