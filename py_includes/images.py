from tkinter import PhotoImage


def load_images(window):
    sizeConstantForButtons = 310
    
    # Getting images (normal) for the buttons:
    window.newButtonImage = PhotoImage(file="res/images/iconset/new.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    window.saveButtonImage = PhotoImage(file="res/images/iconset/save.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    window.linkButtonImage = PhotoImage(file="res/images/iconset/open.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    window.menuButtonImage = PhotoImage(file="res/images/iconset/menu.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    window.closeButtonImage = PhotoImage(file="res/images/iconset/close.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    window.boldButtonImage = PhotoImage(file="res/images/iconset/bold.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    window.italicButtonImage = PhotoImage(file="res/images/iconset/italic.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    window.underButtonImage = PhotoImage(file="res/images/iconset/underline.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    window.strikeButtonImage = PhotoImage(file="res/images/iconset/strikethrough.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    window.bulletButtonImage = PhotoImage(file="res/images/iconset/bullet.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    window.codeButtonImage = PhotoImage(file="res/images/iconset/code.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    window.insertlButtonImage = PhotoImage(file="res/images/iconset/link.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    window.colorButtonImage = PhotoImage(file="res/images/iconset/color.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    window.photoButtonImage = PhotoImage(file="res/images/iconset/photo.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    
    # Getting images (hover) for the buttons:
    window.newButtonImageAfter = PhotoImage(file="res/images/iconset/new1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    window.saveButtonImageAfter = PhotoImage(file="res/images/iconset/save1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    window.linkButtonImageAfter = PhotoImage(file="res/images/iconset/open1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    window.menuButtonImageAfter = PhotoImage(file="res/images/iconset/menu1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    window.closeButtonImageAfter = PhotoImage(file="res/images/iconset/close1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    window.boldButtonImageAfter = PhotoImage(file="res/images/iconset/bold1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    window.italicButtonImageAfter = PhotoImage(file="res/images/iconset/italic1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    window.underButtonImageAfter = PhotoImage(file="res/images/iconset/underline1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    window.strikeButtonImageAfter = PhotoImage(file="res/images/iconset/strikethrough1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    window.bulletButtonImageAfter = PhotoImage(file="res/images/iconset/bullet1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    window.codeButtonImageAfter = PhotoImage(file="res/images/iconset/code1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    window.insertlButtonImageAfter = PhotoImage(file="res/images/iconset/link1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    window.colorButtonImageAfter = PhotoImage(file="res/images/iconset/color1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)
    window.photoButtonImageAfter = PhotoImage(file="res/images/iconset/photo1.png").zoom(int(sizeConstantForButtons * 0.07)).subsample(30)

