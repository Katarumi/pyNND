import vlc
from Tkinter import *


def printmrl():
	i = player.next()
	print i 
	print s 

root = Tk()
frame = Frame(root)
frame.pack()

vlc_instance = vlc.Instance()
player = vlc_instance.media_list_player_new()
media = vlc_instance.media_new("./flac/BadBye.flac")
media2 = vlc_instance.media_new("./flac/Test.flac")
mediaList = vlc_instance.media_list_new()
mediaList.add_media(media)
mediaList.add_media(media2)
test = mediaList.item_at_index(1)
s = test.get_mrl()
print s 
player.set_media_list(mediaList)
player.play()

Button(text = "Next", command=printmrl).pack(fill=X)

root.mainloop()
