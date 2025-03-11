import tkinter as tk
from tkinter import filedialog,messagebox
import os

    
def abrir_Archivo():
    
    archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    return archivo
def CifradoCesar():
    from main import avanceCifrado
    dezplazamiento=int(avanceCifrado.get())
    caracteres=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    encriptar=abrir_Archivo()
    with open(encriptar,"r") as texto:
        lineas=[]
        
        for linea in texto:
            lineas.append(linea)
        texto=""
        for linea in lineas:
            
            for palabra in linea:
                
            
                for letra in palabra:

                    for a in caracteres:

                        if a==letra:

                            caracterposición=(caracteres.index(letra)+dezplazamiento)%len(caracteres)
                            texto=texto+caracteres[caracterposición]       
        texto=texto+"\n"

    try:
        archivo=open("cifrado.txt","x")
        archivo.writelines(texto)
        archivo.close
    

    except FileExistsError:
        os.remove("cifrado.txt")
        archivo=open("cifrado.txt","x")
        archivo.writelines(texto)
        archivo.close
    
    guardar_archivo(archivo)

def guardar_archivo(texto_cifrado): 
    archivo_guardado = filedialog.asksaveasfilename(
        defaultextension=".txt", 
        filetypes=[("Archivos de texto", "*.txt")]
    )
    
    if archivo_guardado:  
        try:
            with open(archivo_guardado, "w", encoding="utf-8") as archivo:
                archivo.write(texto_cifrado)
            messagebox.showinfo("Éxito", f"Archivo guardado como: {archivo_guardado}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")