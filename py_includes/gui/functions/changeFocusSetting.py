from ... import globalvars

def changeFocusSetting(_=False):
    """Change the focus setting and update button appearance."""
    current_mode = globalvars.current_focus_mode
    
    if current_mode == "unlock":
        globalvars.current_focus_mode = "lock"
        new_image = globalvars.window.focuslockButtonImage
    elif current_mode == "lock":
        globalvars.current_focus_mode = "lockapp"
        new_image = globalvars.window.focuslockappButtonImage
    else:
        globalvars.current_focus_mode = "unlock"
        new_image = globalvars.window.focusunlockButtonImage
        
    
    # Update the button image and background color
    button = globalvars.top_menu_buttons["focusunlock"]
    button.config(image=new_image)
    button.image = new_image  # Prevent garbage collection
