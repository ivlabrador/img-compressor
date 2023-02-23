from tkinter import *
import ttkbootstrap as ttk
from tkinter import messagebox
from ttkbootstrap.constants import *
from converter import Conventer
import os
#Tk Config
class WindowTk:
    converter = Conventer
    def __init__(self, window):
        # Ventana
        self.window = window
        self.window.title = "Compresor de imagenes"
        self.window.resizable(1,1)
        #self.window.wb_iconbitmap('url')

        # Menu Superior
        self.menu_bar = Menu(window)
        self.menu_bar.add_command(label='Salir', command=self.window.quit)
        #confirg menu
        self.window.config(menu=self.menu_bar)

        # Estilos
        style = ttk.Style()

        # Creacion del contenedor
        frame = ttk.LabelFrame(self.window, text='Comprimir imagenes', bootstyle='info')
        frame.grid(row=10, column=2, columnspan=3, padx=20)

        # Etiqueta Nombre
        self.etiqueta_nombre = Label(frame, text="URL de la carpeta: ")
        self.etiqueta_nombre.grid(row=3, column=3)
        # Entry Nombre
        self.directory = Entry(frame)
        self.directory.focus()
        self.directory.grid(row=3, column=4)

        # Etiqueta Directorio hacia
        self.download_folder = Label(frame, text="Carpeta de descarga: ")
        self.download_folder.grid(row=4, column=3)
        # Entry Nombre
        self.download_dir = Entry(frame)
        self.download_dir.focus()
        self.download_dir.grid(row=4, column=4)

        # Boton agregar Producto
        self.boton_agregar = ttk.Button(frame, text="Comprimir", bootstyle="primary", command=self.compress)
        self.boton_agregar.grid(row=5, columnspan=2, sticky=W + E)

    def path_validate(self):
        directory_ok = self.directory.get()
        print(directory_ok)
        return len(directory_ok) != 0

    def get_dirctory(self):
        directory = self.directory.get()
        return directory

    def get_download(self):
        download = self.download_dir.get()
        return download

    def compress(self):
        if self.path_validate():
            directory = self.get_dirctory()
            download_folder = self.get_download()
            compressor = self.converter(directory, download_folder)
            # Mensaje de Exito
            compressor.convert()
            messagebox.showinfo(message=f"Imagenes convertidas con exito", title='Imagen Compressor')
        else:
            messagebox.showwarning(message="El archivo no existe", title='Error')





# Recibe la carpeta de imagenes

if __name__ == '__main__':
    root = ttk.Window(themename="superhero")
    root.geometry("440x350")
    app = WindowTk(root)
    root.mainloop()
