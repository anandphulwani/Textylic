from tkinter import PhotoImage
from . import globalvars

def load_images():
    sizeConstantForButtons = 310
    
    # Getting images (normal) for the buttons:
    globalvars.window.newButtonImage = PhotoImage(file="res/images/iconset/new.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    globalvars.window.saveButtonImage = PhotoImage(file="res/images/iconset/save.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    globalvars.window.openlinkButtonImage = PhotoImage(file="res/images/iconset/open.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    globalvars.window.menuButtonImage = PhotoImage(file="res/images/iconset/menu.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    globalvars.window.closeButtonImage = PhotoImage(file="res/images/iconset/close.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    globalvars.window.boldButtonImage = PhotoImage(file="res/images/iconset/bold.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    globalvars.window.italicButtonImage = PhotoImage(file="res/images/iconset/italic.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    globalvars.window.underlineButtonImage = PhotoImage(file="res/images/iconset/underline.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    globalvars.window.strikethroughButtonImage = PhotoImage(file="res/images/iconset/strikethrough.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    globalvars.window.bulletButtonImage = PhotoImage(file="res/images/iconset/bullet.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    globalvars.window.codeButtonImage = PhotoImage(file="res/images/iconset/code.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    globalvars.window.insertlButtonImage = PhotoImage(file="res/images/iconset/link.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    globalvars.window.colortextButtonImage = PhotoImage(file="res/images/iconset/color.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    globalvars.window.photoinsertButtonImage = PhotoImage(file="res/images/iconset/photo.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    
    # Getting images (hover) for the buttons:
    globalvars.window.newButtonImageAfter = PhotoImage(file="res/images/iconset/new1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    globalvars.window.saveButtonImageAfter = PhotoImage(file="res/images/iconset/save1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    globalvars.window.openlinkButtonImageAfter = PhotoImage(file="res/images/iconset/open1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    globalvars.window.menuButtonImageAfter = PhotoImage(file="res/images/iconset/menu1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    globalvars.window.closeButtonImageAfter = PhotoImage(file="res/images/iconset/close1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    globalvars.window.boldButtonImageAfter = PhotoImage(file="res/images/iconset/bold1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    globalvars.window.italicButtonImageAfter = PhotoImage(file="res/images/iconset/italic1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    globalvars.window.underlineButtonImageAfter = PhotoImage(file="res/images/iconset/underline1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    globalvars.window.strikethroughButtonImageAfter = PhotoImage(file="res/images/iconset/strikethrough1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    globalvars.window.bulletButtonImageAfter = PhotoImage(file="res/images/iconset/bullet1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    globalvars.window.codeButtonImageAfter = PhotoImage(file="res/images/iconset/code1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    globalvars.window.insertlButtonImageAfter = PhotoImage(file="res/images/iconset/link1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    globalvars.window.colortextButtonImageAfter = PhotoImage(file="res/images/iconset/color1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    globalvars.window.photoinsertButtonImageAfter = PhotoImage(file="res/images/iconset/photo1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
