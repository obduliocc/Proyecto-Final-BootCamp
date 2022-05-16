import tkinter as tk


########## VENTANA PRINCIPAL ##########

ventana = tk.Tk()
ventana.title("Proyecto Final BootCamp Código Facilito")
ventana.geometry("600x500+500+200")
ventana.minsize(width=600, height=500)
ventana.resizable(0,0)
ventana.configure(bg="lightblue")


########## FUNCIONES ##########

def convertir():

    try:
        dolares = entrada_dolares.get()
        tipo_de_cambio = entrada_tipo_cambio.get()
        resultado = float(dolares)*float(tipo_de_cambio)
        rotulo_resultado.config(text=resultado)
        entrada_dolares.config(state="disabled")
        entrada_tipo_cambio.config(state="disabled")
        boton_convertir.config(state="disabled")
            
    except ValueError:
        pass


def borrar():
    entrada_dolares.config(state="normal")
    entrada_tipo_cambio.config(state="normal")
    boton_convertir.config(state="normal")
    entrada_dolares.delete(0, tk.END)
    entrada_tipo_cambio.delete(0, tk.END)
    rotulo_resultado.config(text="")



########## ROTULO DEL TITULO ##########

rotulo_titulo = tk.Label(ventana, 
	text="CONVERSOR DIVISAS",
    bg="lightblue", fg="black",
    font= "consolas 30 bold",
    relief = tk.GROOVE, bd=2,
    padx=10, pady=10)
rotulo_titulo.pack(padx=20, pady=20)


########## CUADRO PRIMERO ##########

cuadro1 = tk.Frame(ventana,
    bg="lightblue")

rotulo_dolares = tk.Label(cuadro1,
    text="DOLARES:      ",
    bg="lightblue",
    font="consolas 18 bold",
    width=15,
    anchor=tk.W)
rotulo_dolares.pack(side=tk.LEFT, padx=10, pady=10)

entrada_dolares = tk.Entry(cuadro1,
    bg="white", fg="black",
    font="consolas 18 bold",
    relief=tk.SUNKEN,
    width=10,
    justify=tk.RIGHT,
    state="normal")
entrada_dolares.pack(side=tk.LEFT, padx=10, pady=10)

cuadro1.pack(pady=10)

########## CUADRO SEGUNDO ##########

cuadro2 = tk.Frame(ventana,
    bg="lightblue")

rotulo_tipo_cambio = tk.Label(cuadro2,
    text="TIPO DE CAMBIO:",
    bg="lightblue",
    font="consolas 18 bold",
    width=15,
    anchor=tk.W)
rotulo_tipo_cambio.pack(side=tk.LEFT, padx=10, pady=10)

entrada_tipo_cambio = tk.Entry(cuadro2,
    bg="white", fg="black",
    font="consolas 18 bold",
    relief=tk.SUNKEN,
    width=10,
    justify=tk.RIGHT,
    state="normal")
entrada_tipo_cambio.pack(side=tk.LEFT, padx=10, pady=10)

cuadro2.pack(pady=10)


########## CUADRO TERCERO ##########

cuadro3 = tk.Frame(ventana,
    bg="lightblue")

rotulo_pesos_mexicanos = tk.Label(cuadro3,
    text="PESOS MX:      ",
    bg="lightblue",
    font="consolas 18 bold",
    width=15,
    anchor=tk.W)
rotulo_pesos_mexicanos.pack(side=tk.LEFT, padx=10, pady=10)

rotulo_resultado = tk.Label(cuadro3,
    text="",
    bg="lightgreen",
    font="consolas 18 bold",
    width=10,
    relief = tk.GROOVE,
    anchor=tk.E)
rotulo_resultado.pack(side=tk.LEFT, padx=10, pady=10)

cuadro3.pack(pady=10)


##### CUADRO CUARTO #####

cuadro4 = tk.Frame(ventana,
    bg="lightblue")

boton_borrar = tk.Button(cuadro4,
    text="Borrar",
    bg="grey",
    font="consolas 18 bold",
    width=10,
    command=borrar)
boton_borrar.pack(side=tk.LEFT, padx=20, pady=20)

boton_convertir = tk.Button(cuadro4,
    text="Convertir",
    bg="orange",
    font="consolas 18 bold",
    width=10,
    state="normal",
    command=convertir)
boton_convertir.pack(side=tk.LEFT, padx=20, pady=20)

cuadro4.pack(pady=10)


entrada_dolares.focus()


##### BUCLE PRINCIPAL #####

ventana.mainloop()