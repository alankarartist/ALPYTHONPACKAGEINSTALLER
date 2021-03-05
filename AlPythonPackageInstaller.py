import subprocess
from tkinter import*
from tkinter import font
import pyttsx3

class AlPythonPackageInstaller():
    
    def __init__(self):
        root = Tk(className = " AlPythonPackageInstaller ")
        root.geometry("400x200+1500+815")
        root.config(bg="#3b74a8")
        color = '#3b74a8'

        def speak(audio):
            engine = pyttsx3.init('sapi5')
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)
            engine.say(audio)
            engine.runAndWait()

        def install():
            text.delete(1.0, END)
            package = pythonPackage.get()
            check = subprocess.getoutput('pip install ' + package)
            alreadyInstalled = 'Requirement already satisfied: ' + package
            nowInstalled = 'Successfully installed ' + package
            errorInstalling = 'ERROR: Could not find a version that satisfies the requirement ' + package
            if nowInstalled in check.split('\n')[-1]:
                text.insert(1.0, check.split('\n')[-1])
                speak('Successfully installed ' + package)
            elif alreadyInstalled in check.split('\n')[0]:
                text.insert(1.0, check.split('\n')[0])
                speak(package + 'already installed')
            elif errorInstalling in check:
                text.insert(1.0, check)
                speak('Error installing ' + package)

        appHighlightFont = font.Font(family='sans-serif', size=12, weight='bold')
        textHighlightFont = font.Font(family='LEMON MILK', size=10, weight='bold')

        #package widget
        pythonPackage = Label(root, text="Package Name")
        pythonPackage.pack()
        pythonPackage.config(bg=color,fg="white",font=textHighlightFont)
        pythonPackage= Entry(root, bg="#ffd045", fg='#ffffff', highlightbackground=color, highlightcolor=color, highlightthickness=3, bd=0,font=appHighlightFont)
        pythonPackage.pack(fill=X)

        #install button
        install = Button(root, borderwidth=0, highlightthickness=3, text="Install", command=install)
        install.config(bg=color,fg="white",font=textHighlightFont)
        install.pack(fill=X)

        text = Text(root, font="sans-serif",  relief=SUNKEN , highlightbackground=color, highlightcolor=color, highlightthickness=5, bd=0)
        text.config(bg="#ffd045", fg='#ffffff', height=2, font=appHighlightFont)
        text.pack(fill=BOTH, expand=True)

        root.mainloop()

if __name__ == "__main__":
    AlPythonPackageInstaller() 