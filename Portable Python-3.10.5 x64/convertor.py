import sys
import os
import moviepy.editor as mpy
import speech_recognition as sr
from PyQt5 import QtWidgets
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.geometry('500x500')

def add_video():
    global file_path
    file_path = tk.filedialog.askopenfilename()

def convert():
    global file_path
    r = sr.Recognizer()
    #fileName = sys.argv[0]
    clip = mpy.VideoFileClip(file_path)
    audio = clip.audio
    audio.write_audiofile('audio.wav')
    with sr.AudioFile("audio.wav") as source:
        audio_data = r.record(source)
        txt = r.recognize_google(audio_data)
    label = tk.Text(root, height=50, width=200, font="Arial 8")
    label.insert("end", txt, "bold")
    label.grid(row=2, column=2)
    
    #file = open('text.txt', 'w')
    #file.write(text)
    #file.close()


label_video = tk.Label(root, text="Add a video file")
button_video = tk.Button(root, text="Browse", command=add_video)

label_convert = tk.Label(root, text="Convert video")
button_convert = tk.Button(root, text="Convert", command=convert)

label_video.grid(row=0, column=0)
button_video.grid(row=0, column=1)
label_convert.grid(row=1, column=0)
button_convert.grid(row=1, column=1)
button_convert.config(bg='green')

root.mainloop()