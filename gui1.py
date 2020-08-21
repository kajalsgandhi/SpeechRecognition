from tkinter import *
import os.path
import sys
import pygame
import speech_recognition as sr
import webbrowser as wb

root=Tk()
root.title("Speech Recognition")
root.geometry("1100x800")
frame= Frame(root,width=1000,height=600)
output=Text(frame,width=600,height=400,bg="azure")
output.place(x=250,y=50)

def playsong():
    try:
        s1=songlist.curselection()
        filename1=songlist.get(s1)
        pygame.mixer.init()
        pygame.mixer.music.load(filename1)
        pygame.mixer.music.play()
    except:
        print("Invalid")
def getoutput(self):
    try:
        s=songlist.curselection()
        filename2=songlist.get(s)
        r = sr.Recognizer()
        with sr.AudioFile(filename2) as source:
            audio = r.record(source)
            text=r.recognize_google(audio)
        output.insert(END,"You said:{}"+str(text)+"\n")
        if text[0:3]=="add":
            p = text[4:6]
            q = text[11:13]
            a = int(p)
            b = int(q)
            s = a + b
            output.insert(END,"\nThe addition is:"+str(s)+"\n")
        elif text[0]=="h":
            output.insert(END,"\n"+text+"\n")
        elif text[0]=="p":
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            wb.get(chrome_path).open(text)
        else:
            p = text.upper()
            output.insert(END,"\n"+p+"\n")
    except sr.UnknownValueError:
        print("Sorry could not recognize what you said")
    except sr.RequestError :
        print ("could not get the results ")

show=Button(frame,text="OK")
show.place(x=200,y=100)
show.bind("<Button-1>",getoutput)
songlist=Listbox(frame,width=20,height=5)
songlist.place(x=50,y=50)
playbutton=Button(frame,text="Play",command=playsong)
playbutton.place(x=200,y=50)
creditlabel=Label(frame,text="Developed by:")
creditlabel.place(x=20,y=225)
namelabel=Label(frame,text="26-Purnima Chhabria")
namelabel1=Label(frame,text="40-Kajal Gandhi")
namelabel.place(x=20,y=250)
namelabel1.place(x=20,y=275)
titlelabel=Label(frame,text="Mini-Project on Speech Recognition")
titlelabel.place(x=550,y=25)
frame.pack()
cdir=os.getcwd()
slist=os.listdir(cdir)
for i in slist:
    if i.endswith(".wav"):
        songlist.insert(END,i)

root.mainloop()
