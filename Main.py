import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from AgendaYParticipantes import AgendaGUI
from Datos import Datos





class main:
    def __init__(self, root):

        self.root = root
        self.root.title("TextToSpeech") #Nombre del programa
        
        root.config(bg="#1f1f1f")


        agenda = AgendaGUI(root)
        
        




root = tk.Tk()
main(root)
root.mainloop()
print(Datos)
