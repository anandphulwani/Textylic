def load_theme(theme_path):
    with open(theme_path, 'r') as file:
        return file.read()
