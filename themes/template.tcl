# template.tcl --
#
# template pixmap theme for the ttk package.
#

package require Tk 8.5.0

namespace eval ttk::theme::template {

    variable version 0.6
    package provide ttk::theme::template $version

    variable colors
    array set colors {
        -fg             "white"
        -bg             "black"
        
        -disabledfg     "white"
        -disabledbg     "black"
        
        -selectfg       "white"
        -selectbg       "black"
        
        -window         "black"
        -focuscolor     "black"
        -checklight     "white"
    }

    proc LoadImages {imgdir} {
        set abs_imgdir [file normalize $imgdir]
        variable I
        foreach file [glob -directory $imgdir *.png] {
            set img [file tail [file rootname $file]]
            set I($img) [image create photo -file $file -format png]
        }
    }

    LoadImages [file join [file dirname [info script]] themes/template]

    ttk::style theme create template -parent default -settings {
        ttk::style configure . \
            -background $colors(-bg) \
            -foreground $colors(-fg) \
            -troughcolor $colors(-bg) \
            -selectbackground $colors(-selectbg) \
            -selectforeground $colors(-selectfg) \
            -fieldbackground $colors(-window) \
            -font "Helvetica 10" \
            -borderwidth 1 \
            -focuscolor $colors(-focuscolor) \
            -highlightcolor $colors(-checklight)

        ttk::style map . -foreground [list disabled $colors(-disabledfg)]

        #
        # Layouts:
        #

        ttk::style layout Vertical.TScrollbar {
            Vertical.Scrollbar.trough -sticky ns -children {
                Vertical.Scrollbar.thumb -expand true
            }
        }

        ttk::style layout Horizontal.TScrollbar {
            Horizontal.Scrollbar.trough -sticky ew -children {
                Horizontal.Scrollbar.thumb -expand true
            }
        }

        #
        # Elements:
        #
        
        ttk::style element create Horizontal.Scrollbar.trough image $I(scrollbar-trough-horiz-active) \
        -border {6 0 6 0} -sticky ew
        ttk::style element create Horizontal.Scrollbar.thumb \
             image [list $I(scrollbar-slider-horiz) \
                        {active !disabled}  $I(scrollbar-slider-horiz-active) \
                        disabled            $I(scrollbar-slider-insens) \
            ] -border {6 0 6 0} -sticky ew

        ttk::style element create Vertical.Scrollbar.trough image $I(scrollbar-trough-vert-active) \
            -border {0 6 0 6} -sticky ns
        ttk::style element create Vertical.Scrollbar.thumb \
            image [list $I(scrollbar-slider-vert) \
                        {active !disabled}  $I(scrollbar-slider-vert-active) \
                        disabled            $I(scrollbar-slider-insens) \
            ] -border {0 6 0 6} -sticky ns
    }
}
