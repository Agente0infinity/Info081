import tkinter as tk
from tkinter import filedialog, messagebox

def abrir_archivo():
    return filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])

def cifrado_cesar():
    caracteres = "abcdefghijklmnopqrstuvwxyz"
    
    try:
        desplazamiento = int(avanceCifrado.get())
        if desplazamiento < 1 or desplazamiento > 25:
            raise ValueError("El desplazamiento debe estar entre 1 y 25.")
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido entre 1 y 25 para el cifrado.")
        return

    ruta_archivo = abrir_archivo()
    if not ruta_archivo:
        return

    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo leer el archivo: {e}")
        return

    texto_cifrado = ""

    for linea in lineas:
        for letra in linea:
            if letra.lower() in caracteres:
                es_mayuscula = letra.isupper()
                indice = caracteres.index(letra.lower())
                nuevo_indice = (indice + desplazamiento) % 26
                nueva_letra = caracteres[nuevo_indice]
                texto_cifrado += nueva_letra.upper() if es_mayuscula else nueva_letra
            else:
                texto_cifrado += letra  
    
    guardar_archivo(texto_cifrado, "cifrado.txt")

def descifrado_cesar():
    caracteres = "abcdefghijklmnopqrstuvwxyz"
    
    try:
        desplazamiento = int(retrocesoCifrado.get())
        if desplazamiento < 1 or desplazamiento > 25:
            raise ValueError("El desplazamiento debe estar entre 1 y 25.")
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido entre 1 y 25 para el descifrado.")
        return

    ruta_archivo = abrir_archivo()
    if not ruta_archivo:
        return

    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo leer el archivo: {e}")
        return

    texto_descifrado = ""

    for linea in lineas:
        for letra in linea:
            if letra.lower() in caracteres:
                es_mayuscula = letra.isupper()
                indice = caracteres.index(letra.lower())
                nuevo_indice = (indice - desplazamiento) % 26
                nueva_letra = caracteres[nuevo_indice]
                texto_descifrado += nueva_letra.upper() if es_mayuscula else nueva_letra
            else:
                texto_descifrado += letra  
    
    guardar_archivo(texto_descifrado, "descifrado.txt")

def guardar_archivo(texto, nombre_defecto):
    archivo_guardado = filedialog.asksaveasfilename(
        defaultextension=".txt", 
        filetypes=[("Archivos de texto", "*.txt")],
        initialfile=nombre_defecto
    )
    
    if archivo_guardado:
        try:
            with open(archivo_guardado, "w", encoding="utf-8") as archivo:
                archivo.write(texto)
            messagebox.showinfo("Éxito", f"Archivo guardado como: {archivo_guardado}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")


app = tk.Tk()
app.geometry("500x200")
app.resizable(False, False)
app.title("Cifrador César")

titulo = tk.Label(app, text="Cifrador César", font=("Arial", 24))
titulo.grid(row=0, column=0, columnspan=2, pady=10)


tk.Label(app, text="Cifrar con desplazamiento:").grid(row=1, column=0, padx=5, sticky="e")
avanceCifrado = tk.Entry(app, width=5)
avanceCifrado.grid(row=1, column=1, padx=5, sticky="w")
avanceCifrado.insert(0, "3")

boton_cifrar = tk.Button(app, text="Cifrar Texto", command=cifrado_cesar)
boton_cifrar.grid(row=1, column=2, padx=10)

tk.Label(app, text="Descifrar con desplazamiento:").grid(row=2, column=0, padx=5, sticky="e")
retrocesoCifrado = tk.Entry(app, width=5)
retrocesoCifrado.grid(row=2, column=1, padx=5, sticky="w")
retrocesoCifrado.insert(0, "3")

boton_descifrar = tk.Button(app, text="Descifrar Texto", command=descifrado_cesar)
boton_descifrar.grid(row=2, column=2, padx=10)

app.mainloop()
