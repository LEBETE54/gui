import tkinter as tk

# Definir la función que se llamará al hacer clic en cada botón
def on_button_click(shape):
    print(f'Se ha hecho clic en el botón {shape}')

# Crear la ventana principal de la aplicación y ajustar su tamaño
root = tk.Tk()
root.geometry('400x300')

# Crear botones para cada forma geométrica y ajustar su tamaño
square_button = tk.Button(root, text='Cuadrado', command=lambda: on_button_click('Cuadrado'))
square_button.config(height=5, width=15)

rectangle_button = tk.Button(root, text='Rectángulo', command=lambda: on_button_click('Rectángulo'))
rectangle_button.config(height=5, width=15)

triangle_button = tk.Button(root, text='Triángulo', command=lambda: on_button_click('Triángulo'))
triangle_button.config(height=5, width=15)

hexagon_button = tk.Button(root, text='Hexágono', command=lambda: on_button_click('Hexágono'))
hexagon_button.config(height=5, width=15)

# Colocar los botones en la ventana principal
square_button.pack(side=tk.LEFT, padx=10, pady=10)
rectangle_button.pack(side=tk.LEFT, padx=10, pady=10)
triangle_button.pack(side=tk.LEFT, padx=10, pady=10)
hexagon_button.pack(side=tk.LEFT, padx=10, pady=10)

# Iniciar el bucle de eventos principal de la aplicación
root.mainloop()

import tkinter as tk
import tkinter.simpledialog as sd

# Definir las funciones que se llamarán al hacer clic en cada botón
def on_square_button_click():
    square_side = sd.askfloat('Cuadrado', 'Ingresa la medida del lado:')
    if square_side is not None:
        print(f'Se ha hecho clic en el botón Cuadrado y se ingresó la medida del lado: {square_side}')

def on_rectangle_button_click():
    rectangle_height = sd.askfloat('Rectángulo', 'Ingresa la medida de la altura:')
    rectangle_width = sd.askfloat('Rectángulo', 'Ingresa la medida de la anchura:')
    if rectangle_height is not None and rectangle_width is not None:
        print(f'Se ha hecho clic en el botón Rectángulo y se ingresó la medida de la altura: {rectangle_height} y la medida de la anchura: {rectangle_width}')

def on_triangle_button_click():
    triangle_base = sd.askfloat('Triángulo', 'Ingresa la medida de la base:')
    triangle_height = sd.askfloat('Triángulo', 'Ingresa la medida de la altura:')
    if triangle_base is not None and triangle_height is not None:
        print(f'Se ha hecho clic en el botón Triángulo y se ingresó la medida de la base: {triangle_base} y la medida de la altura: {triangle_height}')

def on_hexagon_button_click():
    hexagon_side = sd.askfloat('Hexágono', 'Ingresa la medida del lado:')
    if hexagon_side is not None:
        print(f'Se ha hecho clic en el botón Hexágono y se ingresó la medida del lado: {hexagon_side}')

# Crear la ventana principal de la aplicación y ajustar su tamaño
root = tk.Tk()
root.geometry('400x300')

# Crear botones para cada forma geométrica y ajustar su tamaño
square_button = tk.Button(root, text='Cuadrado', command=on_square_button_click)
square_button.config(height=5, width=15)

rectangle_button = tk.Button(root, text='Rectángulo', command=on_rectangle_button_click)
rectangle_button.config(height=5, width=15)

triangle_button = tk.Button(root, text='Triángulo', command=on_triangle_button_click)
triangle_button.config(height=5, width=15)

hexagon_button = tk.Button(root, text='Hexágono', command=on_hexagon_button_click)
hexagon_button.config(height=5, width=15)

# Colocar los botones en la ventana principal
square_button.pack(side=tk.LEFT, padx=10, pady=10)
rectangle_button.pack(side=tk.LEFT, padx=10, pady=10)
triangle_button.pack(side=tk.LEFT, padx=10, pady=10)
hexagon_button.pack(side=tk.LEFT, padx=10, pady=10)

# Iniciar el bucle de eventos principal de la aplicación
root.mainloop()
