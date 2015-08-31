from utaite import Utaite
import subprocess
import random

def oldloadFromUtaiteInfo(utaiteList = []):
#{
	file = open("utaiteInfo.out", 'r')
	curr = Utaite()
	currSongCount = 0;
	for line in file:
		if ('NAME:' in line):	
			if (curr.name!="empty"):
				utaiteList.append(curr)
				curr = Utaite()
			curr.name= line[6:]
		elif ('SC:' in line):
			curr.songCount = line[4:]	
		else:
			curr.songList.append(line)
			currSongCount = currSongCount +1
	utaiteList.append(curr)
	file.close()
#}

def loadFromUtaiteInfo(utaiteList = []):
#{
	f = open("UtaiteInfo.out", 'r')
	curr = Utaite()
	currUtaiteNum = 0
	currSongCount = 0;
	currDlCount = 0;
	
	utaiteNum = f.readline();
	while currUtaiteNum < int(utaiteNum):
		curr.name = f.readline();
		curr.songCount = int(f.readline())
		curr.dlCount = int(f.readline())
		while (currSongCount < curr.songCount):
			curr.songList.append(f.readline())
			currSongCount=currSongCount+1
		while (currDlCount < curr.dlCount):
			curr.dlList.append(f.readline())
			currDlCount=currDlCount+1
		utaiteList.append(curr)
		curr = Utaite()
		currUtaiteNum = currUtaiteNum + 1
		currSongCount = 0
		currDlCount = 0
#}

def addToUtaiteInfo(filename, utaiteList=[]):
#{
	s = "./sedtest2.sh " + filename + " out"
	subprocess.call(s, shell=True)
	file = open("out", 'r')
	curr = Utaite()
	curr.songCount = 0
	curr.name = file.readline()
	for line in file:
		curr.songList.append(line)
		curr.songCount = curr.songCount + 1
	utaiteList.append(curr)
#}

def saveUtaiteInfo(utaiteList=[]):
#{
	f = open("UtaiteInfo.out",'w')
	i = 0
	j = 0
	f.write(str(len(utaiteList)) + "\n")
	while i < len(utaiteList):
		f.write(utaiteList[i].name)
		f.write(str(utaiteList[i].songCount) + "\n")
		f.write(str(utaiteList[i].dlCount) + "\n")
		while j < int(utaiteList[i].songCount):
			if utaiteList[i].songCount != 0:
				f.write(utaiteList[i].songList[j])
				j = j+1
		j = 0
		while j < int(utaiteList[i].dlCount):
			if utaiteList[i].dlCount != 0:	
				f.write(utaiteList[i].dlList[j])
				j = j+1
		j = 0
		i = i +1
	f.close()
#}

def dlSongs(dlNumber, utaiteList = []):
#{
	i = 0
	while i < int(dlNumber):
		uNum = random.randint(0,len(utaiteList)-1)
		sNum = random.randint(0,int(utaiteList[uNum].songCount)-1)
		sysCall = "./ytdl.sh " + utaiteList[uNum].songList[sNum][:-1] + " " + "http://www.nicovideo.jp/watch/" + utaiteList[uNum].songList[sNum][:-1]
		subprocess.call(sysCall, shell=True)

		# Conversion and tagging
		convertAndTag(uNum, sNum, utaiteList)

		# List Manipulation:
		utaiteList[uNum].dlList.append(utaiteList[uNum].songList)
		utaiteList[uNum].songCount = int(utaiteList[uNum].songCount) -1
		utaiteList[uNum].dlCount = int(utaiteList[uNum].dlCount) + 1

		del utaiteList[uNum].songList[sNum-1:sNum+1]
		i = i+1

#}

def convertAndTag(uNum, sNum, utaiteList = []):
#{
	avconvCall = "avconv -i " + utaiteList[uNum].songList[sNum][:-1] + " -vn -c:a alac " + utaiteList[uNum].songList[sNum][:-1] + ".m4a"
	subprocess.call(avconvCall, shell=True)
	getTitleCall = "./getTitle.sh " + "http://www.nicovideo.jp/watch/" + utaiteList[uNum].songList[sNum][:-1]
	subprocess.call(getTitleCall, shell=True)
	file = open("final", 'r')
	title = file.readline()[:-1]
	subprocess.call("mv " + utaiteList[uNum].songList[sNum][:-1] + ".m4a ./m4a/" + title + ".m4a", shell=True)
	subprocess.call("mv " + utaiteList[uNum].songList[sNum][:-1] + " ./media/" + title + ".mp4", shell=True)
	apCall = "atomicparsley ./m4a/" + str(title) + ".m4a --artist \"" + str(utaiteList[uNum].name) + "\" --title \"" + str(title) + "\" --overWrite"
	print apCall
	subprocess.call(apCall,shell=True)
#}
