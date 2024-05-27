from tkinter import ttk

def configure_scrollbar_style(style_name, theme, trough_color, thumb_color, arrow_color):
    style = ttk.Style()
    style.theme_use(theme)
    style.configure(style_name + ".Vertical.TScrollbar",
                    troughcolor=trough_color,
                    background=thumb_color,
                    arrowcolor=arrow_color)
    style.map(style_name + ".Vertical.TScrollbar",
              background=[('active', thumb_color), ('disabled', trough_color)])

    style.configure(style_name + ".Horizontal.TScrollbar",
                    troughcolor=trough_color,
                    background=thumb_color,
                    arrowcolor=arrow_color)
    style.map(style_name + ".Horizontal.TScrollbar",
              background=[('active', thumb_color), ('disabled', trough_color)])
