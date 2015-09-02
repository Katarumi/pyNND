from fileFuncs import *
from utaite import Utaite
from Tkinter import *
from tkFileDialog import askopenfilename
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

def setup_player():
	filename = askopenfilename()
	media = vlc_instance.media_new(filename)
	player.set_media(media)
	player.play()
	
	print media.get_mrl()
	print player.get_title()
	print player.get_length()
	print player.get_state()

def setInfo():
	top = Toplevel()
	top.title("Set Info")
	Label(top,text="Title: ").grid(row=1,column=1)
	eTitle = Entry(top)
	eTitle.grid(row=1,column=2)
	Label(top,text="Artist: ").grid(row=2,column=1)
	eArtist = Entry(top)
	eArtist.grid(row=2,column=2)

	Button(top, text="Done", command=lambda: apSet(top,eTitle.get(),eArtist.get())).grid(row=5,column=2)
	mainloop ()

def apSet(top,title,artist):
	mrl = media.get_mrl()[7:]
	apCall = "atomicparsley " + mrl + " --artist \"" + str(artist) + "\" --title \"" + str(title) + "\" --overWrite"
	mvCall = "mv " + mrl + " media/" + str(title) 
	print apCall
	print mvCall
	top.destroy()

def dnp():
	mrl = media.get_mrl()[7:]
	mvCall = "mv " + mrl + " dnp/mrl > /dev/null"
	subprocess.call(mvCall, shell=True)	

def redl():
	name = media.get_mrl()[53:]
	if name != "":
		mrl = media.get_mrl()[7:]
	print mrl
	print name


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

vlc_instance = vlc.Instance()
player = vlc_instance.media_player_new()

utaiteList = []

Button(text = "Add Info", command=addInfo).pack(fill=X)
Button(text = "Load Backup", command=loadFromBackup).pack(fill=X)
Button(text = "Debug Print Name", command=printName).pack(fill=X)
Button(text = "Download", command=dl).pack(fill=X)
Button(text = "Play Song", command=setup_player).pack(fill=X)
Button(text = "Set Song Info", command=setInfo).pack(fill=X)
Button(text = "Set Song as DNP", command=dnp).pack(fill=X)
Button(text = "Mark Song for Redownload", command=redl).pack(fill=X)
Button(text = "Quit", command=quit).pack(fill=X)


loadFromUtaiteInfo(utaiteList)

#convertAndTag(0,46, utaiteList)

#addToUtaiteInfo("1.html", utaiteList)
#addToUtaiteInfo("2.html", utaiteList)
#addToUtaiteInfo("3.html", utaiteList)

saveUtaiteInfo(utaiteList)

root.mainloop()
