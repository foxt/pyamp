def fillCanvas(root,w,getImage):
    #Window Chrome
    root.bg = w.create_image(0,0,image=getImage("MAIN","bg",0,0,275,116),anchor="nw")
    root.titlebar = w.create_image(0,0,image=getImage("TITLEBAR","titlebar",27,0,303,14),disabledimage=getImage("TITLEBAR","disabled_titlebar",27,16,303,29),anchor="nw")

    #Clutterbar + Time Remaining
    root.clutter = w.create_image(12,24,image=getImage("TITLEBAR","clutterbar",305,2,312,40),anchor="nw")

    getImage("PLAYPAUS","pause",9,0,18,9)
    getImage("PLAYPAUS","stop",18,0,27,9)
    root.status = w.create_image(30,28,image=getImage("PLAYPAUS","play",0,0,9,9),anchor="nw")

    root.elapsed1 = w.create_image(48,26,image=getImage("NUMBERS","big_0",0,0,9,13),anchor="nw")
    root.elapsed2 = w.create_image(60,26,image=getImage("NUMBERS","big_1",9,0,18,13),anchor="nw")
    root.elapsed3 = w.create_image(78,26,image=getImage("NUMBERS","big_3",18,0,27,13),anchor="nw")
    root.elapsed4 = w.create_image(90,26,image=getImage("NUMBERS","big_4",27,0,36,13),anchor="nw")

    # Mono/Stereo
    root.mono = w.create_image(210,41,image=getImage("MONOSTER","mono_active",29,0,57,11),disabledimage=getImage("MONOSTER","mono_inactive",29,12,57,24),anchor="nw",state="disabled")
    root.stereo = w.create_image(239,41,image=getImage("MONOSTER","stereo_active",0,0,28,11),disabledimage=getImage("MONOSTER","stereo_inactive",0,12,28,24),anchor="nw")

    # Transport Controls
    root.prev = w.create_image(16,88,image=getImage("CBUTTONS","prev_released",0,0,23,18),anchor="nw")
    root.play = w.create_image(39,88,image=getImage("CBUTTONS","play_released",23,0,46,18),anchor="nw")
    root.pause = w.create_image(62,88,image=getImage("CBUTTONS","pause_released",46,0,68,18),anchor="nw")
    root.stop = w.create_image(85,88,image=getImage("CBUTTONS","stop_released",69,0,91,18),anchor="nw")
    root.next = w.create_image(108,88,image=getImage("CBUTTONS","next_released",92,0,114,18),anchor="nw")
    #root.open = w.create_image(136,89,image=getImage("CBUTTONS","eject_released",114,0,136,16),disabledimage=getImage("CBUTTONS","eject_pushed",114,16,136,32),anchor="nw")
    getImage("SHUFREP","shuffle_on_released",29,30,75,45)
    getImage("SHUFREP","repeat_on_released",0,30,28,45)
    root.shuffle = w.create_image(165,90,image=getImage("SHUFREP","shuffle_off_released",29,0,75,15),anchor="nw")
    root.repeat = w.create_image(210,90,image=getImage("SHUFREP","repeat_off_released",0,0,28,15),anchor="nw")

    # Elapsed Bar (x ranges from 16 to 236)
    root.progbox = w.create_image(16,72,image=getImage("POSBAR","elapsed",248,0,277,10),anchor="nw")

    # Volume bar (goes from 107 to 158)
    root.volbar = w.create_image(107,57,image=getImage("VOLUME","volbar0",0,0,68,14),anchor="nw")
    root.volnub = w.create_image(107,58,image=getImage("VOLUME","volnub",15,422,29,433),anchor="nw")

    # Bitrate + SampleDepth
    root.bitrate1 = w.create_image(111,43,image=getImage("TEXT","A",0,0,5,6),anchor="nw")
    root.bitrate2 = w.create_image(116,43,image=getImage("TEXT","A",0,0,5,6),anchor="nw")
    root.bitrate3 = w.create_image(121,43,image=getImage("TEXT","A",0,0,5,6),anchor="nw")

    root.khz1 = w.create_image(156,43,image=getImage("TEXT","A",0,0,5,6),anchor="nw")
    root.khz2 = w.create_image(161,43,image=getImage("TEXT","A",0,0,5,6),anchor="nw")

    # Song title
    root.songtitlecharacters = []
    for x in range(30):
        root.songtitlecharacters.append(w.create_image(113 + (x * 5),27,image=getImage("TEXT","A",0,0,5,6),anchor="nw"))