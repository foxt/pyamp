import math
def updateBitrate(stat,client,root,w,getImage):
    try: 
        if str(root.lastbr) != stat["bitrate"]:
            # update bitrate
            br = int(stat["bitrate"])
            root.lastbr = br
            thousand = False
            if br > 1000: br = br / 10;thousand = True
            hundreds = math.floor(br / 100)
            tens = math.floor((br - (hundreds * 100)) / 10)
            ones = math.floor(br - ((hundreds * 100) + (tens * 10)))
            if br > 99:
                w.itemconfig(root.bitrate1,image=getImage("TEXT",str(hundreds),(hundreds * 5),6,(hundreds * 5) + 5,12))
            if br > 9:
                w.itemconfig(root.bitrate2,image=getImage("TEXT",str(tens),(tens * 5),6,(tens * 5) + 5,12))
            
            if thousand == True:
                w.itemconfig(root.bitrate3,image=getImage("TEXT","H",35,0,40,6))
            else:
                w.itemconfig(root.bitrate3,image=getImage("TEXT",str(ones),(ones * 5),6,(ones * 5) + 5,12))

            ## update kbps
            kbps = math.floor(int(stat["audio"].split(':')[0]) / 1000)
            tens = math.floor(kbps / 10)
            ones = math.floor(kbps - (tens * 10))
            if br > 9:
                w.itemconfig(root.khz1,image=getImage("TEXT",str(tens),(tens * 5),6,(tens * 5) + 5,12))
            w.itemconfig(root.khz2,image=getImage("TEXT",str(ones),(ones * 5),6,(ones * 5) + 5,12))
    except Exception as err:
        print(err)