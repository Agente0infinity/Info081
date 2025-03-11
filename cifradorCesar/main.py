import tkinter as tk
import eventos
from tkinter import filedialog
from eventos import CifradoCesar,abrir_Archivo,guardar_archivo
app=tk.Tk()
app.geometry("640x160")
app.resizable(False,False)
app.title("cifradorCesar")
titulo=tk.Label(app,text="          Cifrador Cesar", font=("Arial",36))
titulo.grid(row=0,column=0,padx=2)
boton_cifrar=tk.Button(text="cifrar texto",command=CifradoCesar)
avanceCifrado=tk.Entry(text="ingresa un numero de cifrado entre desde 1 a 25")
boton_descifrar=tk.Button(text="descifrar texto")
retrocesoCifrado=tk.Entry(text="ingrese el numero de desplazamiento del cifrado original")
boton_cifrar.grid(row=1,column=0)
avanceCifrado.grid(row=1,column=1)
boton_descifrar.grid(row=2,column=0)
retrocesoCifrado.grid(row=2,column=1)

app.mainloop()
