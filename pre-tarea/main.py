import tkinter as tk
app=tk.Tk()
def reinicio():
        
    actualizar_texto("funacat.txt")
    inicio_aventura()

def obtenerTexto(texto):
    frase =""
    with open(texto,"r",encoding="utf8") as texto:
        frase=texto.read()

    return frase


def actualizar_texto(archivo):


    cuadro_de_texto.config(state="normal")
    cuadro_de_texto.delete("1.0",tk.END)
    cuadro_de_texto.insert("1.0",obtenerTexto(archivo))
    cuadro_de_texto.config(state="disabled")


def inicio_aventura():

    
    selector=opcion.get()

    if selector=="opcion1":

       
        boton.config(command=Funacat2)


    if selector=="opcion2":


        boton.config(command=Funacat3)

    

    
    

def Funacat2():
    actualizar_texto("funacat2.txt")
    boton.config(command=reinicio)

def Funacat3():
    
    actualizar_texto("funacat 3.txt")
    boton.config(command=Funacat3Nexo)

def Funacat3Nexo():
    selector=opcion.get()
    if selector=="opcion1":

        boton.config(command=Funacat4)


    if selector=="opcion2":

        boton.config(command=Funacat5)

def Funacat4():
    
    actualizar_texto("funacat 4.txt")
    boton.config(command=reinicio)

def Funacat5():
  
    actualizar_texto("funacat5.txt")
    boton.config(command=Funacat5Nexo)
   
def Funacat5Nexo():
    selector=opcion.get ()    
    if selector=="opcion1":

        boton.config(command=Funacat6)


    if selector=="opcion2":

        boton.config(command=Funacat7)

    
def Funacat7():
    
    actualizar_texto("funacat6.txt")
    boton.config(command=reinicio)
def Funacat6():
    actualizar_texto("funacat 7.txt")
    boton.config(command=reinicio)

app.geometry("480x480")
app.title("funacat")
app.resizable(False,False)
titulo=tk.Label(app, text= "funacat:Aventura de texto",font = ("Times New Roman",32))
opcion=tk.StringVar(value="opcion1")
titulo.pack()
contenido=obtenerTexto("funacat.txt")
A=tk.Radiobutton(app,text="A",variable=opcion, value="opcion1")
B=tk.Radiobutton(app,text="B",variable=opcion, value="opcion2")
boton=tk.Button(command=inicio_aventura,text="elige una opcion y presioname para proseguir con la aventura")
cuadro_de_texto=tk.Text(app,state="normal",height=15,width=50, wrap="word")
cuadro_de_texto.insert("1.0",contenido)
cuadro_de_texto.config(state="disabled")
cuadro_de_texto.pack()
A.pack()
B.pack()
boton.pack()
app.mainloop()




