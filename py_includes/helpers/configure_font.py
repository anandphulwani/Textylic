from tkinter import font as tkFont

def configure_font(base_font_name, **kwargs):
    font_config = {"family": base_font_name}
    font_config.update(kwargs)
    return tkFont.Font(**font_config)
