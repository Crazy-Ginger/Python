import os
from PIL import Image
import glob
import tkinter
from PIL import ImageTk

os.chdir("D:\\Photos")
viewed = open("viewed.txt")
window = tkinter.Tk()

test_img = "TheySay1980\\alex1.JPG"
window.tile(test_img)
picture = Image.open(test_img)
tk_picture = ImageTk.PhotoImage(test_img)
image_widget = tkinter.Label(window, image=tk_picture)
image_widget.place(x=0, y=0, width=6000, height=4000)
