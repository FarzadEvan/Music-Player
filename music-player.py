import tkinter as tkp
from tkinter.constants import ACTIVE, HORIZONTAL
import pygame
import os
from tkinter.filedialog import askdirectory




#window
window = tkp.Tk()
window.geometry("1000x800")
window.title("Music Player BY Farzad Evan")


#pygame init
pygame.init()
pygame.mixer.init()



#directory
dir = askdirectory()
os.chdir(dir)
musiclist = os.listdir(dir)

#listbox
musiclistbox = tkp.Listbox()


#insert music to list
for item in musiclist:
    if item.endswith(".mp3"):
        i = 0
        musiclistbox.insert(i,item)
        i += 1





#Functions
def playmusic():
    pygame.mixer.music.load(musiclistbox.get(tkp.ACTIVE))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(volume.get())
    musicname.set(musiclistbox.get(tkp.ACTIVE))
    

def stopmusic():
    pygame.mixer.music.stop()


def pausemusic():
    pygame.mixer.music.pause()


def unpause():
    pygame.mixer.music.unpause()


def changev(a):
    a = volume.get()
    pygame.mixer.music.set_volume(a)

def loadd():
    dir = askdirectory()
    os.chdir(dir)
    musiclist = os.listdir(dir)
    for item in musiclist:
        if item.endswith(".mp3"):
            i = 0
            musiclistbox.insert(i,item)
            i += 1


#volume
volume = tkp.Scale(window, from_= 0,to= 1, resolution= 0.01, orient=HORIZONTAL,command=changev)



#buttons
playbut = tkp.Button(window, width=10 , height= 5, text= 'Play',command=playmusic)


stopbut = tkp.Button(window, width=10 , height= 5, text ='Stop', command= stopmusic)


pausebut = tkp.Button(window, width= 10 ,height=5, text='Pause', command=pausemusic)


unpausebut = tkp.Button(window, width= 10 ,height= 5, text='Unpause', command=unpause)

loaddbut = tkp.Button(window, width=10, height= 5, text= 'Change Directory', command=loadd)


#music name
musicname = tkp.StringVar()
label = tkp.Label(window, textvariable=musicname)


#style
musiclistbox.pack()
volume.pack(fill='x')
label.pack(fill='x')
playbut.pack()
pausebut.pack()
unpausebut.pack()
stopbut.pack()
loaddbut.pack()



#loop
window.mainloop()