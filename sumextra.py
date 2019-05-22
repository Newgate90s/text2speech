import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *

window = tk.TK()
window.title("Read-O-Tron")
window.geometry('700x600')
window.config(background='blue')
style = ttk.Style(window)
style.configure('lefttab.TNotebook', tabposition='wn')
tab_control = ttk.Notebook(window, style='lefttab.TNotebook')
tab_main = ttk.Frame(tab_control)
tab_control.add(tab_main, text='Mission Control')

label_summarize = Label(tab_main, text="\nHi, I am Read-A-Tron. Let me read your text outload to you.\n", pady=5)

label_summarize.grid(column=0, row=0)
tab_control.pack(expand=1, fill='both')

def erase_inout():
    entry.delete('1.0', END)

def erase_output():
    output_display.delete('1.0', END)

def speak_it():
    import pyttsx3
    engine = pyttsx3.init()
    en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speed\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    engine.setProperty('voice', en_voice_id)
    engine.say('Hello,This is my voice.')
    rate = engine.getProperty('rate')
    engine.setProperty('rate')
    engine.setProperty('rate', rate - 50)
    engine.say('I am going to read the following text to you.')
    text_format = entry.get('1.0', tk.END)
    engine.say(text_format)

    print_voice_list(engine)

    engine.runAndWait()

def print_voice_list(engine):
    voices = engine.getProperty('voices')
    voices_list = []
    for voice in voices:
        print("Voice:")
        print(" - ID: %s" % voice.id)
        print(" - Name: %s" % voice.name)
        print(" - Languages: %s" % voice.languages)
        print(" - Gender: %s" % voice.gender)
        print(" - Age: %s" % voice.age)
        voice_current = ""
        voice_current = voice_current + "\nVoice:\n"
        voice_current = voice_current, "\n - ID: ", voice.id
        voice_current = voice_current, "\n - Name:", voice.name
        voice_current = voice_current, "\n - Languages: ", voice.languages
        voice_current = voice_current, "\n - Gender: ", voice.gender
        voice_current = voice_current, "\n - Age: ", voice.age
        voice_list.append(voice_current)
        print(voice_list)
    output_display.insert(tk.END, "test")