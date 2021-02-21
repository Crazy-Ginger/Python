#!/usr/bin/env python

import PySimpleGUI as sg
import os

directory = "test"
print(os.listdir(directory))
layout = [[sg.Image(key="-IMAGE-")],
        [sg.Button("Previous"), sg.Button("Favourite"), sg.Button("Next")]]

window = sg.Window("Window Titties", layout, finalize=True)
iterator = 0
while True:
    try:
        file_list = os.listdir("../test/")
    except:
        file_list = []
    window["-IMAGE-"].update(filename = directory + "/" + file_list[iterator])

    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "Favourite":
        print("Favourite")
    elif event == "Next":
        iterator += 1
        print("Next")
    elif event == "Previous":
        iterator -= 1
        print("Previous")

window.close()
