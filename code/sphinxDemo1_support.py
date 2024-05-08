#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
# ======================================================
#     sphinxDemo1_support.py
#  ------------------------------------------------------
# Created for Full Circle Magazine Issue # 205
# Written by G.D. Walters
# Copyright © 2023, 2024 by G.D. Walters
# This source code is released under the MIT License
# ======================================================
# Support module generated by PAGE version 8.1f
#  in conjunction with Tcl version 8.6
#    May 01, 2024 06:40:18 AM CDT  platform: Linux

import sys
import os.path
import glob
import platform
import webbrowser

import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import sphinxDemo1

_debug = True  # False to eliminate debug printing from callback functions.
location = sphinxDemo1._location


def main(*args):
    """Main entry point for the application."""
    global root
    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", root.destroy)
    # Creates a toplevel widget.
    global _top49, _w49
    _top49 = root
    _w49 = sphinxDemo1.Toplevel1(_top49)
    startup()
    root.mainloop()


def startup():
    """
    This function is run just before the program is presented to the user.  Use this function to get everything initialized and set up before the program starts.

    :parm: none
    :return: none
    """
    themelist = load_tcl_themes(location, True)
    _w49.TComboboxThemes["values"] = themelist
    _w49.TComboboxThemes.bind("<<ComboboxSelected>>", lambda e: on_ComboSelect(e))


def on_btnAbout(*args):
    """
    Callback that will display the 'about' information for the program.

    :param *args: normally none
    :return: none
    """
    if _debug:
        print("sphinxDemo1_support.on_btnAbout")
        for arg in args:
            print("    another arg:", arg)
        sys.stdout.flush()


def on_btnDelete(*args):
    """
    Callback that will handle deleting records from the database.

    :param *args: normally none
    :return: none
    """
    if _debug:
        print("sphinxDemo1_support.on_btnDelete")
        for arg in args:
            print("    another arg:", arg)
        sys.stdout.flush()


def on_btnEdit(*args):
    """
    Callback that will enable editing of database record.

    :param *args: normally none
    :return: none
    """
    if _debug:
        print("sphinxDemo1_support.on_btnEdit")
        for arg in args:
            print("    another arg:", arg)
        sys.stdout.flush()


def on_btnExit(*args):
    """
    Callback that will end the program.

    :param *args: normally none
    :return: none
    """
    if _debug:
        print("sphinxDemo1_support.on_btnExit")
        for arg in args:
            print("    another arg:", arg)
        sys.stdout.flush()
    sys.exit()


def on_btnFind(*args):
    """
    Callback that will search the database for user record.  If found, screen will be loaded with the record information.  If not, a message box will be displayed.

    :param *args: normally none
    :return: none
    """
    if _debug:
        print("sphinxDemo1_support.on_btnFind")
        for arg in args:
            print("    another arg:", arg)
        sys.stdout.flush()


def on_btnHelp(*args):
    """
    Callback that will display the user documentation for the program.

    :param *args: normally none
    :return: none
    """
    if _debug:
        print("sphinxDemo1_support.on_btnHelp")
        for arg in args:
            print("    another arg:", arg)
        sys.stdout.flush()
    # Create the URL of the local documentation
    url = os.path.join(location, "docs", "html", "index.html")
    # Open the default browser, 0=New browser if possible, True=Raise the Browser
    webbrowser.open(url, 0, True)


def on_btnSave(*args):
    """
    Callback that will save any changed information to the database.

    :param *args: normally none
    :return: none
    """
    if _debug:
        print("sphinxDemo1_support.on_btnSave")
        for arg in args:
            print("    another arg:", arg)
        sys.stdout.flush()


def on_popClear(*args):
    """
    Callback for popup menu Clear.  Should clear the Entry Widget display area.

    :param *args: tuple containing a number that relates to the Entry widget that initiated the popup menu.
    :return: none
    """
    if _debug:
        print("sphinxDemo1_support.on_popClear")
        for arg in args:
            print("    another arg:", arg)
        sys.stdout.flush()


def on_popCloseMenu(*args):
    """
    Simply provides a way for the popup menu to be removed from the screen.
    """
    if _debug:
        print("sphinxDemo1_support.on_popCloseMenu")
        for arg in args:
            print("    another arg:", arg)
        sys.stdout.flush()


def on_popCopy(*args):
    """
    Callback for popup menu Copy.  Should copy any information in the Entry Widget display area.

    :param *args: tuple containing a number that relates to the Entry widget that initiated the popup menu.
    :return: none
    """
    if _debug:
        print("sphinxDemo1_support.on_popCopy")
        for arg in args:
            print("    another arg:", arg)
        sys.stdout.flush()


def on_popCut(*args):
    """
    Callback for popup menu Cut.  Should copy any information from the Entry Widget display area, place it into the system clipboard and clear the entry widget display area.

    :param *args: tuple containing a number that relates to the Entry widget that initiated the popup menu.
    :return: none
    """
    if _debug:
        print("sphinxDemo1_support.on_popCut")
        for arg in args:
            print("    another arg:", arg)
        sys.stdout.flush()


def on_popPaste(*args):
    """
    Callback for popup menu Paste.  Should clear the Entry Widget display area, then paste the system clipboard information.

    :param *args: tuple containing a number that relates to the Entry widget that initiated the popup menu.
    :return: none
    """
    if _debug:
        print("sphinxDemo1_support.on_popPaste")
        for arg in args:
            print("    another arg:", arg)
        sys.stdout.flush()


def load_tcl_themes(folder, silent):
    """
    This function will load all tcl theme files located in <folder>.

    :param folder: string containing the location of the theme folder.
    :type folder: String
    :param silent: True/False - False will print the names of the theme being worked on.  True will supress the print.
    :type silent: Boolean
    :return: none
    """
    # ===================================================
    # This will load the various tcl Themes.
    # ---------------------------------------------------
    # This function is now Windows 10+ compliant and supports
    # the page-legacy theme.
    # ---------------------------------------------------
    # Written by G.D. Walters 3 March, 2024
    # ===================================================
    # version 0.10
    # ===================================================
    # Parameters:
    #    Inputs:
    #        folder: string - The current working directory.
    #                   This allows the parent program to be
    #                   run from any folder, if the program name
    #                   is in '~/.bashrc' or '~/.bash_aliases'
    #        silent: boolean - if False: surpress debugging
    #                   output
    #    Returns:
    #        list containing all ttk themes found in folder
    # Example:
    #     theme_list = load_tcl_themes(curdir, 1)
    # ===================================================
    if silent:
        print(sys.platform)
    sty = ttk.Style()
    localThemes = sty.theme_names()
    currentTheme = sty.theme_use()

    if silent:
        print(f"{currentTheme=}")
    if sys.platform == "win32":
        cthemename = f"\\{currentTheme}.tcl"
    else:
        cthemename = f"/{currentTheme}.tcl"
    filedef = os.path.join(folder, "themes", "*.tcl")
    if silent:
        print(filedef)
    themelist1 = glob.glob(filedef)
    themelist = []
    if silent:
        print(f"{localThemes=}")
        print(f"{themelist1=}")
    for theme in localThemes:
        themelist.append(theme)
    for theme in themelist1:
        _top49.option_clear()
        if silent:
            print(f"{theme=}")
        if theme.endswith(cthemename):
            pass
        elif theme.endswith("page-legacy.tcl"):
            if silent:
                print(f"{theme=}")
            root.tk.eval("set ::xframe #d9d9d9")
            root.tk.eval("set ::xfore #000000")
            root.tk.eval("set ::ana2color beige")
            root.tk.eval("set ::_tabfg1 black")
            root.tk.eval("set ::_tabfg2 black")
            root.tk.eval("set ::_tabbg1 #d9d9d9")
            root.tk.eval("set ::_tabbg2 #afb5cc")
            root.tk.eval("set ::_bgmode light")
            try:
                if sys.platform == "win32":
                    rs = theme.rsplit("\\", 1)[1]
                    nameend = rs.rfind(".tcl")
                    themename = rs[:nameend]
                else:
                    rs = theme.rsplit("/", 1)[1]
                    nameend = rs.rfind(".tcl")
                    themename = rs[:nameend]
                _top49.tk.call("source", theme)
                themelist.append(themename)
            except:
                pass
        else:
            if sys.platform == "win32":
                if silent:
                    print(f"{theme=}")
                rs = theme.rsplit("\\", 1)[1]
                nameend = rs.rfind(".tcl")
                themename = rs[:nameend]
            else:
                rs = theme.rsplit("/", 1)[1]
                nameend = rs.rfind(".tcl")
                themename = rs[:nameend]
            if silent:
                print(f"{themename=}")
            themelist.append(themename)
            _top49.tk.call("source", theme)
    themelist.sort()
    if silent:
        print(f"{themelist=}")
    return themelist


def on_ComboSelect(e):
    """
    When the user selects an item from the TCombobox, that item will be used to change the theme.

    :param e: the virtual event ("<<ComboboxSelected>>")
    :return: none
    """
    print(e)
    sty = ttk.Style()
    selected = _w49.comboThemes.get()
    print(f"Combobox Select: {selected}")
    sty.theme_use(selected)


if __name__ == "__main__":
    sphinxDemo1.start_up()
