from .. import globalvars

def get_button_images(window):
    """Generate a dictionary of button widgets and their images."""
    
    button_names = [
        "bold", "italic", "underline", "strikethrough", "bullet", "code", 
        "new", "save", "openlink", "menu", "close", "createlink", 
        "colortext", "photoinsert"
    ]

    button_dict = {}
    
    for name in button_names:
        if name in globalvars.bottom_menu_buttons:
            button_widget = globalvars.bottom_menu_buttons[name]
        elif name in globalvars.top_menu_buttons:
            button_widget = globalvars.top_menu_buttons[name]
        else:
            continue
        
        button_dict[name] = (
            button_widget, 
            getattr(window, f"{name}ButtonImageAfter"), 
            getattr(window, f"{name}ButtonImage")
        )
    
    return button_dict
