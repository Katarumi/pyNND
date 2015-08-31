from fileFuncs import *
from utaite import Utaite
from Tkinter import *
import Tkinter
from tkFileDialog import askopenfilename


# -*- coding: utf-8 -*-

root = Tk()
frame = Frame(root)
frame.pack()

def addInfo():
	filename = askopenfilename()
	if filename != "":
		addToUtaiteInfo(filename, utaiteList)

def quit():
	saveUtaiteInfo(utaiteList)
	root.quit()

def loadFromBackup():
	filename = askopenfilename()
	if filename != "":
		loadFromUtaiteInfo(utaiteList)

menubar = Menu(root)


#filemenu = Menu(menubar, tearoff=0)
#filemenu.add_command(label="Test", command=hello)
#filemenu.add_command(label="Simple", command=hello)
#filemenu.add_separator()
#filemenu.add_command(label="exit", command=root.quit)
#menubar.add_cascade(label="File", menu=filemenu)


#root.config(menu=menubar)

utaiteList = []

Tkinter.Button(text = "Add Info", command=addInfo).pack(fill=X)
Tkinter.Button(text = "Load Backup", command=quit).pack(fill=X)
Tkinter.Button(text = "Quit", command=quit).pack(fill=X)

loadFromUtaiteInfo(utaiteList)

#convertAndTag(0,46, utaiteList)

#addToUtaiteInfo("1.html", utaiteList)
#addToUtaiteInfo("2.html", utaiteList)
#addToUtaiteInfo("3.html", utaiteList)

saveUtaiteInfo(utaiteList)

root.mainloop()
