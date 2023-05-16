import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pydub import AudioSegment
from pydub.silence import split_on_silence
import speech_recognition as sr
from Datos import Datos
from tkinter.messagebox import showinfo



class VoiceRec:
    def __init__(self, root):
        self.root = root
        self.data = Datos
        self.textoRec = "" 
        self.create_widgets()


    def dividir(self):
        # Duración mínima de la pausa en milisegundos
        min_silence_len = 3000
        archivo_de_audio = self.ruta_grabacion_a_dividir.get("1.0", "end-1c")
        carpeta_de_segmentos = self.ruta_carpeta.get("1.0", "end-1c")
        audio_file = AudioSegment.from_wav(archivo_de_audio)

        audio_chunks = split_on_silence(
            audio_file,
            min_silence_len=min_silence_len,
            silence_thresh=-50
        )

        for i, chunk in enumerate(audio_chunks):
            print(f'Recorte numero {i} procesado')
            chunk.export(f'{carpeta_de_segmentos}/grabacion_{i}.wav', format='wav')

        messagebox.showinfo("Fin del proceso de división", f"Se han terminado de procesar el archivo de audio, puede visualizar el resultado en la carpeta: {carpeta_de_segmentos}")

    def dialogo_grabacion(self):
        # Creamos el diálogo de selección de archivo
        filename = filedialog.askopenfilename()
        # Si el usuario selecciona un archivo, mostramos la ruta en un label
        if filename:
            self.ruta_grabacion_a_dividir.delete("1.0", "end")
            self.ruta_grabacion_a_dividir.insert("1.0", filename)

    def dialogo_carpeta(self):
        # Creamos el diálogo de selección de carpeta
        directory = filedialog.askdirectory()
        # Si el usuario selecciona una carpeta, mostramos la ruta en un label
        if directory:
            self.ruta_carpeta.delete("1.0", "end")
            self.ruta_carpeta.insert("1.0", directory)

    def dialogo_grabacion_reconocer(self):
        # Creamos el diálogo de selección de archivo
        self.filename = filedialog.askopenfilename()
        # Si el usuario selecciona un archivo, mostramos la ruta en un label
        if self.filename:
            self.ruta_grabacion_a_reconocer.delete("1.0", "end")
            self.ruta_grabacion_a_reconocer.insert("1.0", self.filename)

     
    def reconocer_texto(self):
        archivo_a_reconocer = self.ruta_grabacion_a_reconocer.get("1.0", "end-1c")
        r = sr.Recognizer()
        with sr.AudioFile(archivo_a_reconocer) as source:
            audio_data = r.record(source)
        text = r.recognize_google(audio_data, language='es-ES')  #Texto reconocido
        self.resultado.delete("1.0", "end")
        self.resultado.insert("1.0", text)
        print(text)
        self.textoRec = text

    def asignar_agenda(self):
            ruta_archi = self.filename

            if ruta_archi in [ruta[4] for ruta in self.data['Registro']]:
                    
                    # Mostrar ventana de error
                    root = tk.Tk()
                    root.geometry('250x150')
                    root.resizable(False, False)
                    root.title('Error')

                    label = tk.Label(root, text="El archivo ya se reconoció", padx=20, pady=20)
                    label.pack()

                    def cerrar_ventana():
                        root.destroy()

                    boton_aceptar = tk.Button(root, text="Aceptar", command=cerrar_ventana)
                    boton_aceptar.pack(pady=10)

                    root.mainloop()
                    return
            else:
                
                root = tk.Tk()
                root.geometry('500x250')
                root.resizable(False, False)
                root.title('Asignar punto de la agenda')

                label1 = ttk.Label(root, text="Seleccione el participante:")
                label1.pack(fill=tk.X, padx=5, pady=5)

                selected_participant = tk.StringVar()
                option_cb1 = ttk.Combobox(root, textvariable=selected_participant)
                option_cb1['values'] = self.data['Participantes']
                option_cb1['state'] = 'readonly'
                option_cb1.pack(fill=tk.X, padx=5, pady=5)

                label2 = ttk.Label(root, text="Seleccione el apartado de la agenda:")
                label2.pack(fill=tk.X, padx=5, pady=5)

                selected_topic = tk.StringVar()
                option_cb2 = ttk.Combobox(root, textvariable=selected_topic)
                option_cb2["values"] = list(self.data.keys())[2:]
                option_cb2['state'] = 'readonly'
                option_cb2.pack(fill=tk.X, padx=5, pady=5)

                label3 = ttk.Label(root, text="Seleccione el punto de la agenda:")
                label3.pack(fill=tk.X, padx=5, pady=5)

                selected_point = tk.StringVar()
                option_cb3 = ttk.Combobox(root, textvariable=selected_point)
                option_cb3['state'] = 'readonly'
                option_cb3.pack(fill=tk.X, padx=5, pady=5)

                # Variables que almacenarán los valores seleccionados
                participante_seleccionado = ""
                apartado_seleccionado = ""
                punto_seleccionado = ""

                def update_point_options(event):
                    nonlocal apartado_seleccionado  # Declaramos la variable apartado_seleccionado como no local
                    selected_topic = option_cb2.get()
                    apartado_seleccionado = selected_topic  # Actualizamos el valor de la variable apartado_seleccionado
                    if selected_topic in self.data:
                        option_cb3['values'] = self.data[selected_topic]
                    else:
                        option_cb3['values'] = []

                def guardar_seleccion():
                    nonlocal participante_seleccionado, apartado_seleccionado, punto_seleccionado
                    participante_seleccionado = option_cb1.get()
                    punto_seleccionado = option_cb3.get()


                    registro = [participante_seleccionado, apartado_seleccionado, punto_seleccionado, self.textoRec, self.filename]
                    Datos['Registro'].append(registro)
                    root.destroy() # Cierra la ventana

                option_cb2.bind('<<ComboboxSelected>>', update_point_options)

                # Botón para guardar la selección
                btn_guardar = ttk.Button(root, text="Guardar selección", command=guardar_seleccion)
                btn_guardar.pack(pady=10)


                root.mainloop()



        






        



    def create_widgets(self):


        # Frame base que contiene todos los inputs
        self.Base_Frame = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        self.Base_Frame.pack(side=tk.LEFT, padx=20, pady=20, fill="y")
        
        # Contenedor para los frames de los participantes
        self.content_frame_Participantes = tk.Frame(self.Base_Frame, width=400, height=600, bg="#484d67")
        self.content_frame_Participantes.pack(side=tk.LEFT, padx=20, pady=20)



        # Agregamos un botón para abrir el selector de archivo para la grabación a subdividir
        button = tk.Button(self.content_frame_Participantes, text="Abrir archivo de audio", command=self.dialogo_grabacion)
        button.place(x=0, y=0, width=500, height=30)

        # Agregamos una caja de texto para determinar la ruta del archivo de la grabación a subdividir
        self.ruta_grabacion_a_dividir = tk.Text(self.content_frame_Participantes, height=3, width=48)
        self.ruta_grabacion_a_dividir.insert("1.0", "Inserte el archivo con la sesion completa para ser segmentada...")
        self.ruta_grabacion_a_dividir.place(x=8, y=40)

        # Agregamos un botón para abrir el selector de la carpeta
        button = tk.Button(self.content_frame_Participantes, text="Abrir carpeta con segmentos", command=self.dialogo_carpeta)
        button.place(x=0, y=120, width=500, height=30)

        # Agregamos una caja de texto para determinar la ruta del archivo de la grabación a subdividir
        self.ruta_carpeta = tk.Text( self.content_frame_Participantes, height=3, width=48)
        self.ruta_carpeta.insert("1.0", "Inserte la carpeta con los segmentos...")
        self.ruta_carpeta.place(x=8, y=160)

        # Agregamos un botón para abrir el selector del archivo ya cortado a ser reconocido por SpeechRecognition
        button = tk.Button(self.content_frame_Participantes, text="Abrir el archivo a reconocer", command=self.dialogo_grabacion_reconocer)
        button.place(x=0, y=240, width=500, height=30)

        # Agregamos una caja de texto para determinar la ruta del archivo de la grabación a subdividir
        self.ruta_grabacion_a_reconocer = tk.Text(self.content_frame_Participantes, height=3, width=48)
        self.ruta_grabacion_a_reconocer.insert("1.0", "Ingrese el archivo a reconocer...")
        self.ruta_grabacion_a_reconocer.place(x=8, y=270)

        # Agregamos un botón para iniciar la división del audio
        button = tk.Button(self.content_frame_Participantes, text="Iniciar división del archivo", command=self.dividir)
        button.place(x=0, y=310, width=500, height=30)

        # Agregamos un botón para iniciar el reconocimiento del texto
        button = tk.Button(self.content_frame_Participantes, text="Iniciar el reconocimiento del texto", command=self.reconocer_texto)
        button.place(x=0, y=340, width=500, height=30)

        # Agregamos una caja de texto para mostrar el resultado del reconocimiento de texto
        self.resultado = tk.Text(self.content_frame_Participantes, height=6, width=48, bg="lightgreen")
        self.resultado.place(x=8, y=380)



        #-----Asignaciones---------------------------------------------


         # Agregamos un botón para iniciar las asignaciones a la agenda en base al texto
        button = tk.Button(self.content_frame_Participantes, text="Asiganr", command=self.asignar_agenda)
        button.place(x=100, y=550, width=200, height=30)






#Si se ejecuta este archivó inicializa correctamente el codigo
if __name__ == "__main__":
    root = tk.Tk()
    appAgenda = VoiceRec(root)
    root.mainloop()
