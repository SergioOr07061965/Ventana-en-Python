from tkinter import *

ventana_pricipal = Tk()
ventana_pricipal.title("Identificate")
ventana_pricipal.minsize(width=300, height=400)
ventana_pricipal.config(padx=35, pady=35)

etiqueta1 = Label(text='Escribe un nombre de usuario', font=("Arial", 14))
etiqueta1.grid(column=0,row=1)

caja_texto1 = Entry(width=20, font=("Arial", 14))
caja_texto1.grid(column=0, row=2)

etiqueta2 = Label(text='Escribe tu contraseña', font=("Arial", 14))
etiqueta2.grid(column=0,row=3)

caja_texto2 = Entry(width=20, font=("Arial", 14), show="*")
caja_texto2.grid(column=0, row=4)

boton1 = Button(text="Aceptar", font=("Arial", 14))
boton1.grid(column=0, row=6)



ventana_pricipal.mainloop()