from fileFuncs import *
from utaite import Utaite
from Tkinter import *
from tkFileDialog import askopenfilename
from playerFuncs import *
import vlc

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
		del utaiteList[:]
		loadFromSpecificUtaiteInfo(filename, utaiteList)

def printName():
	i = 0
	while i < len(utaiteList):
		print utaiteList[i].name
		i = i + 1 

def dl():
	top = Toplevel()
	top.title("DL Info")
	entries = []
	i = 0
	while i < len(utaiteList): 
		Label(top, text=utaiteList[i].name).grid(row=i)
		entries.append(Entry(top))
		entries[i].grid(row=i,column= 1)
		print entries[i].get()
		i = i + 1

	Button(top, text="Done", command=lambda: go(top,entries)).grid(row=i+1)
		
	mainloop ()

	

def go(top,entries = []):
	i = 0
	while i < len(utaiteList):
		print entries[i].get()
		if entries[i].get() != "":
			dlSongs(entries[i].get(),i,utaiteList)
		i = i + 1
	top.destroy()


menubar = Menu(root)


#filemenu = Menu(menubar, tearoff=0)
#filemenu.add_command(label="Test", command=hello)
#filemenu.add_command(label="Simple", command=hello)
#filemenu.add_separator()
#filemenu.add_command(label="exit", command=root.quit)
#menubar.add_cascade(label="File", menu=filemenu)


#root.config(menu=menubar)

#filename = "./media"
#vlc_instance = vlc.Instance()
#player = vlc_instance.media_player_new()

utaiteList = []

Button(text = "Add Info", command=addInfo).pack(fill=X)
Button(text = "Load Backup", command=loadFromBackup).pack(fill=X)
Button(text = "Debug Print Name", command=printName).pack(fill=X)
Button(text = "Download", command=dl).pack(fill=X)
Button(text = "Play Song", command=setup_player).pack(fill=X)
Button(text = "Play All Songs", command=setup_bigPlayer).pack(fill=X)
Button(text = "Quit", command=quit).pack(fill=X)


loadFromUtaiteInfo(utaiteList)

saveUtaiteInfo(utaiteList)

root.mainloop()
