import vlc
from Tkinter import *
from tkFileDialog import askopenfilename

def setup_player():

	top = Toplevel()
	top.title("Song Inputs")
	Label(top, text="???").grid(row=0)
	Button(top,text = "Set Song Info", command=lambda: setInfo(media)).grid(row=1)
	Button(top,text = "Set Song as DNP", command=lambda: dnp(media)).grid(row=2)
	Button(top,text = "Mark Song for Redownload", command=lambda: redl(media)).grid(row=3)
	Button(top,text = "Exit Song", command=lambda: quitSong(top,player)).grid(row=4)


	vlc_instance = vlc.Instance()
	player = vlc_instance.media_player_new()
        filename = askopenfilename()
        media = vlc_instance.media_new(filename)
        player.set_media(media)
        player.play()

        print media.get_mrl()
        print player.get_title()
        print player.get_length()
        print player.get_state()

	mainloop ()

def quitSong(top, player):
	player.stop()
	top.destroy()
	

def setInfo(media):
	top = Toplevel()
	top.title("Set Info")
	Label(top,text="Title: ").grid(row=1,column=1)
	eTitle = Entry(top)
	eTitle.grid(row=1,column=2)
	Label(top,text="Artist: ").grid(row=2,column=1)
	eArtist = Entry(top)
	eArtist.grid(row=2,column=2)

	Button(top, text="Done", command=lambda: apSet(media,top,eTitle.get(),eArtist.get())).grid(row=5,column=2)
	mainloop ()

def apSet(media, top,title,artist):
	mrl = media.get_mrl()[7:]
	apCall = "atomicparsley " + mrl + " --artist \"" + str(artist) + "\" --title \"" + str(title) + "\" --overWrite"
	mvCall = "mv " + mrl + " media/" + str(title) 
	print apCall
	print mvCall
	top.destroy()

def dnp(media):
	mrl = media.get_mrl()[7:]
	mvCall = "mv " + mrl + " dnp/ > /dev/null"
	subprocess.call(mvCall, shell=True)	

def redl(media):
	name = media.get_mrl()
	if name != "":
		mrl = media.get_mrl()[7:]
		print mrl
	print name


def setup_bigPlayer(utaiteList = []):

	vlc_instance = vlc.Instance()
	player = vlc_instance.media_player_new()
	media = vlc_instance.media_list_new()
	dlNameList = []
	i = 0
	while i < len(utaiteList):
		dl = utaiteList[i].dlCount
		j = 0
		while j < int(dl):
			s = "./flac/" + utaiteList[i].dlList[j]
			print s
			#media.add_media(s)
			j = j +1
		i = i + 1

	while i < len(dlNameList):
		#print dlNameList[i]
		pass
