
import tkinter as tk
from PIL import Image, ImageTk

ventana = tk.Tk()
path = Image.open("C:\\Users\Biblioteca\Downloads\icono\instalg.png")
icono = ImageTk.PhotoImage(path)
ventana.iconphoto(True, icono)

ventana.title("Tecnar APP")

ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla =ventana.winfo_screenheight()

ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}")
ventana.resizable(True, True)
ventana.config(bg="light blue")


etiqueta = tk.Label(ventana, text="¡Hello Bro!", bg="white", fg="black", font=("Times New Roman", 16), width=20, height=2, anchor="center")
etiqueta.pack()


def cambiar_texto():
    etiqueta.config(text="¡Hello Man!")

etiqueta = tk.Label(ventana, text="Holis Señor")
etiqueta.pack()

boton1 = tk.Button(ventana, text="Change", command=cambiar_texto)
boton1.pack()

boton2 = tk.Button(ventana, text="Botón 2", bg="blue", fg="white", font=("Arial", 12))
boton2.pack()

boton3 = tk.Button(ventana, text="Deshabilitado", state="disabled")
boton3.pack()

marco1 = tk.Frame(ventana, width=200, height=100, bd=2, relief="solid")
marco1.pack()

etiqueta1 = tk.Label(marco1, text="Marco 1")
etiqueta1.pack()
etiqueta3 = tk.Label(marco1, text="Marco 1")
etiqueta3.pack()

marco2 = tk.Frame(ventana, width=200, height=100, bd=2, relief="raised")
marco2.pack()

etiqueta2 = tk.Label(marco2, text="Marco 2")
etiqueta2.pack()

def obtener_seleccion():
    seleccionados = cuadro_lista.curselection()
    for index in seleccionados:
        elemento = cuadro_lista.get(index)
        print("Elemento seleccionado:", elemento)


cuadro_lista = tk.Listbox(ventana, width=30, selectmode="multiple")
cuadro_lista.pack()

elementos = ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4"]

for elemento in elementos:
    cuadro_lista.insert(tk.END, elemento)

boton = tk.Button(ventana, text="Obtener", command=obtener_seleccion)
boton.pack()

ventana.mainloop()



