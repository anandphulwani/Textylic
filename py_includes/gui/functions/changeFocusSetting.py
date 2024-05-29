from ... import globalvars
from ...images_effects import bind_hover_effects

def changeFocusSetting(_=False):
    """Change the focus setting and update button appearance."""
    current_mode = globalvars.current_focus_mode
    
    if current_mode == "unlock":
        globalvars.current_focus_mode = "lock"
        new_image = globalvars.window.focuslockButtonImage
        hover_image = globalvars.window.focuslockButtonImageAfter
    elif current_mode == "lock":
        globalvars.current_focus_mode = "pinapp"
        new_image = globalvars.window.focuspinappButtonImage
        hover_image = globalvars.window.focuspinappButtonImageAfter
    else:
        globalvars.current_focus_mode = "unlock"
        new_image = globalvars.window.focusunlockButtonImage
        hover_image = globalvars.window.focusunlockButtonImageAfter
        
    
    # Update the button image and background color
    button = globalvars.top_menu_buttons["focusunlock"]
    button.config(image=new_image)
    bind_hover_effects(button, hover_image, new_image)
    button.image = new_image  # Prevent garbage collection
