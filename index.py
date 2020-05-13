from tkinter import Tk, Label, Button,Canvas
from PIL import Image, ImageTk
from fillCanvas import fillCanvas
from handlers import createHandlers
from update import update
import mpd,math
client = mpd.MPDClient()
client.connect("localhost", 6600)



root = Tk()
root.overrideredirect(True)   
root.wait_visibility(root)

root.is_dragging = False
root.is_seeking  = False
root.is_adjvol   = False

root.SkinRoot = "./theme/"
root.SkinType = ".png"
root.images = {}
root.imgFile = {}

def getImageFile(name):
    if not name in root.imgFile: 
        print("Loading image",name)
        root.imgFile[name] = Image.open(root.SkinRoot + name + root.SkinType)
    return root.imgFile[name]
    

def getImage(name,rename,cx,cy,cw,ch):
    if not rename in root.images: 
        print("Cropping image",rename,"from",name)
        root.images[rename] = ImageTk.PhotoImage(getImageFile(name).crop((cx,cy,cw,ch)))
    return root.images[rename]

w = Canvas(root, width=275, height=116,highlightthickness=0)
createHandlers(client,root,w,getImage)
fillCanvas(root,w,getImage)
w.pack()

root.geometry("+2700+480")

root.lastbr = 123


def task():
    try:
        update(client,root,w,getImage)
    except Exception as err:
        print(err)
    root.after(1, task)
root.after(1, task)

root.mainloop()
