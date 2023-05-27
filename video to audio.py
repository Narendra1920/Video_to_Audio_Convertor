#importing modules
import moviepy.editor
from tkinter.filedialog import *
from tkinter import *

window=Tk()

window.geometry("300x100")
window.title("My_Personal_Converter")

Label(window, text="Choose a File ").pack()

def browse():
    global video
    video = askopenfilename()
    video = moviepy.editor.VideoFileClip(video)
    pathlab.config(text=video)#configure method

def save():
    audio = video.audio#convert to audio
    audio.write_audiofile("sample.wav")#save as audio
    Label(window, text="Video Converted into Audio and Saved Successfully",bg='red', font=('Calibri 15')).pack()# a lable
    

pathlab = Label(window)
pathlab.pack()
#creating buttons
Button(window,text='browse',command=browse).pack()
Button(window,text='SAVE',command=save).pack()

window.mainloop()