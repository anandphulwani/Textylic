def change_image(widget, image):
    """Change the image of a widget."""
    widget.configure(image=image)

def bind_hover_effects(widget, hover_image, normal_image):
    """Bind hover and leave events to a widget."""
    widget.bind("<Enter>", lambda e: change_image(widget, hover_image))
    widget.bind("<Leave>", lambda e: change_image(widget, normal_image))

def mapping_button_images(buttons):
    """Map buttons to their hover and normal images."""
    for _, (widget, hover_image, normal_image) in buttons.items():
        bind_hover_effects(widget, hover_image, normal_image)
