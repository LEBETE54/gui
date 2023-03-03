
import tkinter as tk


ventana = tk.Tk()


def decir_hola():
    print("¡Hola!")


def decir_adios():
    print("¡Adiós!")


boton_hola = tk.Button(ventana, text="Hola", command=decir_hola)
boton_hola.pack()


boton_adios = tk.Button(ventana, text="Adiós", command=decir_adios)
boton_adios.pack()



ventana.mainloop()
