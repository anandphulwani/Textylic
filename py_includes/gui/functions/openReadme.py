import webbrowser

def openReadme(_=False):
    """Open the README.md on GitHub and the Textylic website"""

    webbrowser.open_new("https://github.com/anandphulwani/Textylic/blob/master/README.md")
    webbrowser.open_new("https://anandphulwani.github.io/Textylic/")
    return "break"
