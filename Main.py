import tkinter as tk
from tkinter import messagebox, simpledialog
from AgendaYParticipantes import AgendaGUI,ParticipantesGUI
from Datos import Datos





class main:
    def __init__(self, root):

        self.root = root
        self.root.title("TextToSpeech") #Nombre del programa
        
        root.config(bg="skyblue")


        agenda = AgendaGUI(root)
        participantes = ParticipantesGUI(root)
        




root = tk.Tk()
main(root)
root.mainloop()
print(Datos)
