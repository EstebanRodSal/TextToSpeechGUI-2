import tkinter as tk
from AgendaYParticipantes import AgendaGUI
from Datos import Datos
from VoiceRectkinter import VoiceRec



class main:
    def __init__(self, root):

        self.root = root
        self.root.title("TextToSpeech") #Nombre del programa
        
        root.config(bg="#1f1f1f")

        agenda = AgendaGUI(root)
        reconocimiento = VoiceRec(root) #Si se llenan los inputs de la agenda entonces se llama el proceso siguiente





root = tk.Tk()
main(root)
root.mainloop()
print(Datos)
