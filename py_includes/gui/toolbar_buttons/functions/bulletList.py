from .... import globalvars

def bulletList():
    """Bulleted list button function"""

    selection = globalvars.notes.selection_get()
    current_tags = globalvars.notes.tag_names("sel.first")

    if "\n" not in selection:
        if "bullet" not in current_tags:
            index_1 = float(globalvars.notes.index("sel.first"))
            index_2 = float(globalvars.notes.index("sel.last"))
            bulleted_str = "\t•  " + str(selection)
            globalvars.notes.delete(index_1, index_2)
            globalvars.notes.insert(index_1, bulleted_str)
            lenBulletString = len(bulleted_str)
            lenBulletString = globalvars.notes.index(index_1 + lenBulletString)
            globalvars.notes.tag_add("bullet", index_1, lenBulletString)
        elif "bullet" in current_tags:
            index_1 = float(globalvars.notes.index("sel.first"))
            index_2 = float(globalvars.notes.index("sel.last"))
            selected = globalvars.notes.selection_get()
            selected = str(selected)
            selected = selected.replace("\t•  ", "")
            globalvars.notes.insert("sel.first", selected)
            globalvars.notes.delete("sel.first", "sel.last")
            lenBulletString = len(selected)
            lenBulletString = globalvars.notes.index(lenBulletString)
            globalvars.notes.tag_remove("bullet", index_1, lenBulletString)
    elif "\n" in selection:
        if "bullet" not in current_tags:
            index_1 = float(globalvars.notes.index("sel.first"))
            index_2 = float(globalvars.notes.index("sel.last"))
            select = globalvars.notes.selection_get()
            bulleted_str = select.replace("\n", "\n\t•  ")
            bulleted_str = "\t•  " + str(bulleted_str)
            globalvars.notes.delete(str(index_1), str(index_2))
            globalvars.notes.insert(index_1, bulleted_str)
            lenBulletString = len(bulleted_str)
            lenBulletString = globalvars.notes.index(index_1 + lenBulletString)
            globalvars.notes.tag_add("bullet", index_1, lenBulletString)
        elif "bullet" in current_tags:
            index_1 = float(globalvars.notes.index("sel.first"))
            index_2 = float(globalvars.notes.index("sel.last"))
            selected = selection.replace("\n\t•  ", "\n")
            selected = selected.replace("\t•  ", "")
            globalvars.notes.insert("sel.first", selected)
            globalvars.notes.delete("sel.first", "sel.last")
            lenBulletString = len(selected)
            lenBulletString = globalvars.notes.index(lenBulletString)
            globalvars.notes.tag_remove("bullet", index_1, lenBulletString)
    return "break"
