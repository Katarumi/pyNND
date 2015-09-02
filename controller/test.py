import vlc

def setup_player(filename):
	vlc_instance = vlc.Instance()
	player = vlc_instance.media_player_new()
	player.set_mrl(filename)
	player.play()
	print player.get_length()#Time duration of file
	print player.get_state()#Player's state

setup_player("./BadBye.m4a")
