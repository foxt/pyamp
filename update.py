import math
from updateBitrate import updateBitrate
from setText import setText
def update(client,root,w,getImage):
    stat = client.status()
    print(stat)
    try: 
        elapsed = float(stat["elapsed"]) / float(stat["duration"])
        root.songlen = float(stat["duration"])
        root.progboxPos = int(16 + ( 220 * elapsed))
        w.moveto(root.progbox,int(16 + ( 220 * elapsed)),72)
    except Exception as err:
        print(13,err)

    try: 
        vol = float(stat["volume"]) / 100
        root.volnubPos = int(107 + ( 51 * vol))
        w.moveto(root.volnub,int(107 + ( 51 * vol)),58)
        segment = int(vol * 27)
        w.itemconfig(root.volbar,image=getImage("VOLUME","volbar"+str(segment),0,segment * 15,68,(segment * 15) + 14))
    except Exception as err:
        print(22,err)

    try: 
        elapsed = float(stat["elapsed"])
        mins = math.floor(elapsed / 60)
        secs = elapsed % 60

        w.itemconfig(root.elapsed1, image=getImage("NUMBERS","big_" + str(math.floor(mins / 10)),math.floor(mins / 10) * 9,0,(math.floor(mins / 10) + 1) * 9 ,13),anchor="nw")
        w.itemconfig(root.elapsed2, image=getImage("NUMBERS","big_" + str(math.floor(mins % 10)),math.floor(mins % 10) * 9,0,(math.floor(mins % 10) + 1) * 9 ,13),anchor="nw")

        w.itemconfig(root.elapsed3,image=getImage("NUMBERS","big_" + str(math.floor(secs / 10)),math.floor(secs / 10) * 9,0,(math.floor(secs / 10) + 1) * 9 ,13),anchor="nw")
        w.itemconfig(root.elapsed4,image=getImage("NUMBERS","big_" + str(math.floor(secs % 10)),math.floor(secs % 10) * 9,0,(math.floor(secs % 10) + 1) * 9 ,13),anchor="nw")

    except Exception as e:
        print(36,e)

    try: 
        w.itemconfig(root.shuffle, image=getImage("SHUFREP","shuffle_" + ('on' if stat["random"] == '1' else 'off') + "_released",29,0,75,15),anchor="nw")
        w.itemconfig(root.repeat, image=getImage("SHUFREP","repeat_" + ('on' if stat["repeat"] == '1' else 'off') + "_released",29,0,75,15),anchor="nw")
    except Exception as e:
        print(42,e)
    
    try:
        w.itemconfig(root.status,image=getImage("PLAYPAUS",stat["state"],18,0,27,9),anchor="nw")
    except Exception as e:
        print(47,e)

    updateBitrate(stat,client,root,w,getImage)
    try:
        song = client.currentsong()
        print(song)
        dur = int(song["time"])
        dur = str(math.floor(dur/60)) + ":" + str(dur%60)
        setText(song["pos"] + ". " + song["artist"] + " - " + song["title"] + " (" + dur + ")" ,root,w,getImage)
    except Exception as err:
        print(55,err)
    try: 
        w.itemconfig(root.mono,state="disabled")
        w.itemconfig(root.stereo,state="disabled")
        if stat["audio"].split(':')[2] == "1":
            w.itemconfig(root.mono,state="normal")
        elif stat["audio"].split(":")[2] == "2":
            w.itemconfig(root.stereo,state="normal")
            
    except Exception as err:
        print(65,err)