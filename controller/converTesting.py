def convertAndTag(uNum, sNum, utaiteList = []):
#{
#       avconvCall = "avconv -i " + utaiteList[uNum].songList[sNum][:-1] + " -vn -c:a alac " + utaiteList[uNum].songList[sNum][:-1] + ".m4a"
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
        return title
#}


