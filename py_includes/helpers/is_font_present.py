from tkinter import font

def is_font_present(font_name):
    available_fonts = font.families()
    return font_name in available_fonts
