from update import update
def createHandlers(client,root,w,getImage):
    def mousedown(event):
        print("clicked at", event.x, event.y)
        if event.x > 16 and event.y > 88 and event.x < 39 and event.y < 106:
            # Previous Button
            w.itemconfig(root.prev,image=getImage("CBUTTONS","prev_pushed",0,18,23,36))
            client.previous()
        elif event.x > 39 and event.y > 88 and event.x < 62 and event.y < 106:
            # Play Button
            client.pause(0)
            w.itemconfig(root.play,image=getImage("CBUTTONS","play_pushed",23,18,46,36))
            
        elif event.x > 62 and event.y > 88 and event.x < 84 and event.y < 106:
            # Pause Button
            w.itemconfig(root.pause,image=getImage("CBUTTONS","pause_pushed",46,18,68,36))
            client.pause(1)
        elif event.x > 84 and event.y > 88 and event.x < 106 and event.y < 106:
            # Stop Button
            w.itemconfig(root.stop,image=getImage("CBUTTONS","stop_pushed",69,18,92,36))
            client.stop()
        elif event.x > 106 and event.y > 88 and event.x < 129 and event.y < 106:
            # Next Button
            w.itemconfig(root.next,image=getImage("CBUTTONS","next_pushed",92,18,114,36))
            client.next()
        elif event.x > 165 and event.y > 90 and event.x < 210 and event.y < 104:
            client.random(int(not bool(int(client.status()["random"]))))
        elif event.x > 211 and event.y > 90 and event.x < 238 and event.y < 104:
            client.repeat(int(not bool(int(client.status()["repeat"]))))
        elif event.x > root.progboxPos and event.y > 72 and event.x < root.progboxPos + 30 and event.y < 82:
            root.dragOffset =[root.winfo_pointerx() - root.progboxPos,root.winfo_pointery() - 72]
            root.is_seeking = True
            w.itemconfig(root.progbox,image=getImage("POSBAR","elapsed_pushed",277,0,307,10))
        elif event.x > root.volnubPos and event.y > 58 and event.x < root.volnubPos + 14 and event.y < 69:
            print("nub")
            root.dragOffset =[root.winfo_pointerx() - root.volnubPos,root.winfo_pointery() - 58]
            root.is_adjvol = True
            w.itemconfig(root.volnub,image=getImage("VOLUME","volnubDown",15,422,29,433))
        else:
            root.dragOffset = [event.x,event.y]
            root.is_dragging = True
        

    def mousemove(event):
        if root.is_dragging == True:
            root.geometry("+" + str(root.winfo_pointerx() - root.dragOffset[0]) + "+" + str(root.winfo_pointery() - root.dragOffset[1]))
        elif root.is_seeking == True:
            pos = min(max(root.winfo_pointerx() - root.dragOffset[0],16),232)
            client.seekcur(((pos - 16) / 220) * root.songlen)
            #if pos < 16:
                #client.previous()
            update(client,root,w,getImage)
            w.moveto(root.progbox, pos,72)
        elif root.is_adjvol == True:
            pos = min(max(root.winfo_pointerx() - root.dragOffset[0],107),158)
            client.setvol(int(((pos - 107) / 51) * 100))
            update(client,root,w,getImage)
            w.moveto(root.volnub, pos,58)


    def mouseup(event):
        w.itemconfig(root.prev,image=getImage("CBUTTONS","prev_released",0,0,23,18))
        w.itemconfig(root.play,image=getImage("CBUTTONS","play_released",23,0,46,18))
        w.itemconfig(root.pause,image=getImage("CBUTTONS","pause_released",46,0,66,18))
        w.itemconfig(root.stop,image=getImage("CBUTTONS","stop_released",70,0,92,18))
        w.itemconfig(root.next,image=getImage("CBUTTONS","next_released",92,0,114,18))
        w.itemconfig(root.progbox,image=getImage("POSBAR","elapsed",248,0,277,10))
        w.itemconfig(root.volnub,image=getImage("VOLUME","volnub",0,422,14,433))
        root.is_seeking  = False
        root.is_dragging = False
        


    w.bind("<Button-1>",mousedown)
    w.bind("<B1-Motion>",mousemove)
    w.bind("<ButtonRelease-1>",mouseup)
