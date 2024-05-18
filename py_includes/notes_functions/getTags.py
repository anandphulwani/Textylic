from .. import globalvars

def getTags(start, end) -> list:
    """
    Get the tags (bold, italic, etc.) and their indices in the Text widget.

    It gets the tags for each character till the end, and stores the end index
    when the tag changes.
    """

    index = start
    tagname = []
    starttagindex = index
    prevtag = globalvars.notes.tag_names(index)

    try:
        tagname.append([starttagindex, "end", globalvars.notes.tag_names(index)])
    except BaseException:
        tagname.append([starttagindex, "end", ("",)])

    while globalvars.notes.compare(index, "<", end):
        if globalvars.notes.tag_names(index) != prevtag:
            # If the tag name at the current index is not equal to the
            # previous index's tag name...
            if len(globalvars.notes.tag_names(index)) <= 0:
                # If the legnth of the tuple containing the tag names at the
                # current index is less that or equal to 0, it means that
                # there are no tags here.
                starttagindex = index
                legnth = len(tagname)
                tagname[legnth - 1][1] = index
                tagname.append([starttagindex, "end", ("",)])
            else:
                # Otherwise, it means that there are tags here.
                starttagindex = index
                legnth = len(tagname)
                tagname[legnth - 1][1] = index
                tagname.append([starttagindex, "end", globalvars.notes.tag_names(index)])

        prevtag = globalvars.notes.tag_names(index)
        index = globalvars.notes.index(f"{index}+1c")

    return tagname
