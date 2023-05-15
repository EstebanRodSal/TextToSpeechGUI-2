import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from AgendaYParticipantes import AgendaGUI
from Datos import Datos
from VoiceRectkinter import VoiceRec




class main:
    def __init__(self, root):

        self.root = root
        self.root.title("TextToSpeech") #Nombre del programa
        
        root.config(bg="#1f1f1f")


        agenda = AgendaGUI(root)
        reconocimiento = VoiceRec(root)

        
    """
    def reconocimiento(self):

        # Frame base que contiene todos los inputs
        self.Base_Frame = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        self.Base_Frame.pack(side=tk.RIGHT, padx=20, pady=20)


        #Frame para los botones
        self.btn_buttons_frame = tk.Frame(self.Base_Frame)
        self.btn_buttons_frame.pack(pady=5)

        self.nuevo_punto_button = tk.Button(self.btn_buttons_frame, text="Reconocimiento", command=self.abrir_reconocimiento)
        self.nuevo_punto_button.pack(side=tk.LEFT, padx=5)    
        

    def abrir_reconocimiento(self):
        import VoiceRectkinter as VR
    """




root = tk.Tk()
main(root)
root.mainloop()
print(Datos)
