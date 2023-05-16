import tkinter as tk
from tkinter import messagebox, simpledialog, ttk, filedialog
from Datos import Datos












class AgendaGUI:

  

    def __init__(self, root):
        self.root = root
        
        self.agenda = Datos
        
        self.create_widgets()
        self.create_widgets_Participantes()
        
    def create_widgets(self):
        """
        Crea los widgets necesarios para la interfaz gráfica.
        """


        

        # Agenda



        # Frame base que contiene todos los inputs
        self.Base_Frame = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        self.Base_Frame.pack(side=tk.LEFT, padx=20, pady=20, fill="y")





        # Contenedor para los frames de apartados y puntos
        self.content_frame = tk.Frame(self.Base_Frame, width=400, height=600, bg="#484d67")
        self.content_frame.pack(side=tk.TOP, padx=20, pady=20)

        

        # Frame para la lista de apartados
        self.apartados_frame = tk.Frame(self.content_frame)
        self.apartados_frame.pack(side=tk.LEFT, pady=20, padx=20, anchor="nw")

        self.apartados_label = tk.Label(self.apartados_frame, text="Apartados:")
        self.apartados_label.pack()

        self.apartados_listbox = tk.Listbox(self.apartados_frame, width=20)
        self.apartados_listbox.pack(pady=5)

        self.apartados_listbox.bind("<<ListboxSelect>>", self.select_apartado)

        # Frame para los botones del apartado
        self.apartados_buttons_frame = tk.Frame(self.apartados_frame)
        self.apartados_buttons_frame.pack(pady=5)

        self.nuevo_apartado_button = tk.Button(self.apartados_buttons_frame, text="Nuevo Apartado", command=self.nuevo_apartado)
        self.nuevo_apartado_button.pack(side=tk.LEFT, padx=5)

        self.eliminar_apartado_button = tk.Button(self.apartados_buttons_frame, text="Eliminar Apartado", command=self.eliminar_apartado)
        self.eliminar_apartado_button.pack(side=tk.LEFT, padx=5)

        # Frame para la lista de puntos
        self.puntos_frame = tk.Frame(self.content_frame)
        self.puntos_frame.pack(side=tk.LEFT, pady=20, padx=20, anchor="ne")

        self.puntos_label = tk.Label(self.puntos_frame, text="Puntos:")
        self.puntos_label.pack()

        self.puntos_listbox = tk.Listbox(self.puntos_frame, width=20)
        self.puntos_listbox.pack(pady=5)

        self.puntos_listbox.bind("<<ListboxSelect>>", self.select_punto)

        # Frame para los botones del punto
        self.puntos_buttons_frame = tk.Frame(self.puntos_frame)
        self.puntos_buttons_frame.pack(pady=5)

        self.nuevo_punto_button = tk.Button(self.puntos_buttons_frame, text="Nuevo Punto", command=self.nuevo_punto)
        self.nuevo_punto_button.pack(side=tk.LEFT, padx=5)

        self.eliminar_punto_button = tk.Button(self.puntos_buttons_frame, text="Eliminar Punto", command=self.eliminar_punto)
        self.eliminar_punto_button.pack(side=tk.LEFT, padx=5)




        # Botones para guardar proyecto
        self.buttons_frame_Parti = tk.Frame(self.root)
        self.buttons_frame_Parti.pack(side=tk.RIGHT ,pady=5, anchor="ne")

        self.nuevo_participante_button = tk.Button(self.buttons_frame_Parti, text="Guardar proyecto",command=self.guardar_proyecto)
        self.nuevo_participante_button.pack(side=tk.LEFT, padx=5, anchor="ne")



        # Botones para abir proyecti


        self.nuevo_participante_button = tk.Button(self.buttons_frame_Parti, text="Abrir proyecto", command=self.Abrir_Proyecto)
        self.nuevo_participante_button.pack(side=tk.LEFT, padx=5, anchor="ne")





        


    def guardar_proyecto(self):
        file_name = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_name:
            with open(file_name, mode='w') as archivo:
                archivo.write(str(self.agenda))
        print('Archivo guardado correctamente')

    
    def Abrir_Proyecto(self):
        file_name = filedialog.askopenfilename(defaultextension=".txt")
        if file_name:
            with open(file_name, mode='r') as archivo:
                contenido = archivo.read()
            
            
           # Convertir el contenido del archivo en un diccionario de Python
            datos_temporales = eval(contenido)
            

            Datos.clear()
            # Actualizar el diccionario de datos contenido en el archivo "Datos"
            Datos.update(datos_temporales)
            print('Archivo cargado correctamente')

            

            # Llamar a las funciones actualizadora en AgendaGUI para actualizar los datos de la agenda
            self.actualizar_apartados()
            self.actualizar_puntos()
            self.actualizar_participante()


        
    def nuevo_apartado(self):
        """
        Abre un diálogo para agregar un nuevo apartado a la lista de apartados.
        """
        apartado = simpledialog.askstring("Nuevo Apartado", "Ingrese el nombre del apartado:")
        if apartado:
            self.agenda[apartado] = []
            self.actualizar_apartados()
    
    def eliminar_apartado(self):
        """
        Elimina el apartado seleccionado de la lista de apartados.
        """
        index = self.apartados_listbox.curselection()
        if index:
            apartado = self.apartados_listbox.get(index)
            confirmacion = messagebox.askyesno("Eliminar Apartado", f"¿Está seguro que desea eliminar el apartado '{apartado}'?")
            if confirmacion:
                del self.agenda[apartado]
                self.actualizar_apartados()
                self.actualizar_puntos()
    
    def nuevo_punto(self):
        """
        Agrega un nuevo punto a la lista del apartado correspondiente.
        """
        apartado_index = self.apartados_listbox.curselection()
        if apartado_index:
            apartado = self.apartados_listbox.get(apartado_index)
            punto = simpledialog.askstring("Nuevo Punto", f"Ingrese el nombre del punto para el apartado '{apartado}':")
            if punto:
                self.agenda[apartado].append(punto)
                self.actualizar_puntos()
    
    def eliminar_punto(self):
        """
        Elimina el punto seleccionado de la lista de puntos.
        """
        apartado_index = self.apartados_listbox.curselection()
        punto_index = self.puntos_listbox.curselection()
        if apartado_index and punto_index:
            apartado = self.apartados_listbox.get(apartado_index)
            punto = self.puntos_listbox.get(punto_index)
            confirmacion = messagebox.askyesno("Eliminar Punto", f"¿Está seguro que desea eliminar el punto '{punto}' del apartado '{apartado}'?")
            if confirmacion:
                self.agenda[apartado].remove(punto)
                self.actualizar_puntos()
    
    def select_apartado(self, event):
        """
        Método que se ejecuta cuando se selecciona un apartado en la lista de apartados. 
        Actualiza los puntos relacionados con el apartado seleccionado.
        """
        self.actualizar_puntos()
    
    def select_punto(self, event):
        """
        Método que se ejecuta cuando se selecciona un punto en la lista de puntos.
        """
        pass
    
    def actualizar_apartados(self):
        """
        Método que actualiza la lista de apartados con los nombres de los apartados de la agenda,
        excluyendo las primeras 2 llave.
        """
        self.apartados_listbox.delete(0, tk.END)
        llaves = list(self.agenda.keys())[2:]
        for apartado in llaves:
            self.apartados_listbox.insert(tk.END, apartado)

    
    def actualizar_puntos(self):
        """
        Método que actualiza la lista de puntos con los puntos relacionados con el apartado seleccionado.
        """
        self.puntos_listbox.delete(0, tk.END)
        apartado_index = self.apartados_listbox.curselection()
        if apartado_index:
            apartado = self.apartados_listbox.get(apartado_index)
            for punto in self.agenda[apartado]:
                self.puntos_listbox.insert(tk.END, punto)






    #-------------------------------Participantes---------------------------------------------------


        
    def create_widgets_Participantes(self):
        """
        Crea los widgets necesarios para la interfaz gráfica.
        """

       
        # Contenedor para los frames de los participantes
        self.content_frame_Participantes = tk.Frame(self.Base_Frame, width=400, height=600, bg="#484d67")
        self.content_frame_Participantes.pack(side=tk.BOTTOM, padx=20, pady=20)


        # Frame para la lista de participantes
        self.participantes_frame = tk.Frame(self.content_frame_Participantes)
        self.participantes_frame.pack(side=tk.LEFT, padx=20, pady=20)

        self.participantes_label = tk.Label(self.participantes_frame, text="Participantes:")
        self.participantes_label.pack()

        self.participantes_listbox = tk.Listbox(self.participantes_frame, width=20)
        self.participantes_listbox.pack(pady=5)

        self.participantes_listbox.bind("<<ListboxSelect>>", self.select_participante)

        # Botones para gestionar los participantes
        self.buttons_frame_Parti = tk.Frame(self.participantes_frame)
        self.buttons_frame_Parti.pack(pady=5)

        self.nuevo_participante_button = tk.Button(self.buttons_frame_Parti, text="Nuevo participante", command=self.nuevo_participante)
        self.nuevo_participante_button.pack(side=tk.LEFT, padx=5)

        self.eliminar_participante_button = tk.Button(self.buttons_frame_Parti, text="Eliminar participante", command=self.eliminar_participante)
        self.eliminar_participante_button.pack(side=tk.LEFT, padx=5)


        

        

                
        

        
    def nuevo_participante(self):
        """
        Abre un diálogo para agregar un nuevo participante a la lista de participantes.
        """
        participante = simpledialog.askstring("Nuevo participante", "Ingrese el nombre del participante:")
        if participante:
            self.agenda['Participantes'].append(participante)
            self.actualizar_participante()
    
    def eliminar_participante(self):
        """
        Elimina el participante seleccionado de la lista de apartados.
        """
        indexParti = self.participantes_listbox.curselection()
        if indexParti:
            participante = self.participantes_listbox.get(indexParti)
            confirmacion = messagebox.askyesno("Eliminar participante", f"¿Está seguro que desea eliminar el participante '{participante}'?")
            if confirmacion:
                del self.agenda[participante]
                
    
    
    def select_participante(self, event):
        """
        Método que se ejecuta cuando se selecciona un apartado en la lista de apartados. 
        Actualiza los puntos relacionados con el apartado seleccionado.
        """
        self.actualizar_participante()
    
    
    
    
    
    
    def actualizar_participante(self):
        """
        Método que actualiza la lista de participantes.
        """
        self.participantes_listbox.delete(0, tk.END)
        participantes_index = self.participantes_listbox.curselection()
        for participante in self.agenda['Participantes']:
                self.participantes_listbox.insert(tk.END, participante)
                








#Si se ejecuta este archivó inicializa correctamente el codigo
if __name__ == "__main__":
    root = tk.Tk()
    appAgenda = AgendaGUI(root)
    root.mainloop()

    

    

