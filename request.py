import requests
import json
import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import *

# Obtener la dirección IP del servidor
server_ip = simpledialog.askstring(
    "Dirección IP del servidor", "Ingrese la dirección IP del servidor:")
if server_ip is None:
    # Si el usuario cancela el diálogo, salir del programa
    exit()

# Crear el método para la conversión
def convertir():
    monto = monto_entry.get()
    moneda1 = selected_option1.get()
    moneda2 = selected_option2.get()

    # Construir la URL completa del servidor
    # 5000 se cambiaria por "server_port"
    url = f"http://{server_ip}:5000/convertir/{monto}/{moneda1}/{moneda2}"
    # Hacer la solicitud al servidor
    try:
        response = requests.get(url)
        data = json.loads(response.text)

        if 'error' in data:
            # Si se recibió un mensaje de error, mostrarlo en un messagebox
            messagebox.showerror('Error', data['error'])
        else:
            # Si se recibieron los datos de la conversión, mostrarlos en un messagebox
            cantidad = data['cantidad']
            de_moneda = data['moneda_origen']
            a_moneda = data['moneda_destino']
            cantidad_convertida = data['cantidad_convertida']
            messagebox.showinfo(
                'Resultado', f"{cantidad} {de_moneda} equivale a {cantidad_convertida} {a_moneda}")
    except Exception as e:
        messagebox.showerror('Error', f"Ha ocurrido un error: {str(e)}")


# crear la ventana principal
root = Tk()
root.title("Conversión de Monedas")
root.iconbitmap('divisa.ico')
root.geometry("340x120")

monto_label = Label(root, text="Monto (0.0):")
monto_entry = Entry(root)

options1 = ['MXN (PESO MEXICANO)', 'USD (DOLAR ESTADOUNIDENSE)', 'AUD (DOALR AUSTRALIANO)', 'EUR (EURO)', 'CAD (DOLAR CANADIENSE)', 'GBP (LIBRA ESTERLINA)', 'JPY (YEN JAPONES)', 'ARS (PESO ARGENTINO)', 'CNY (YUAN CHINO)', 'RUP (RUBLO RUSO)',  '']
options2 = ['MXN (PESO MEXICANO)', 'USD (DOLAR ESTADOUNIDENSE)', 'AUD (DOALR AUSTRALIANO)', 'EUR (EURO)', 'CAD (DOLAR CANADIENSE)', 'GBP (LIBRA ESTERLINA)', 'JPY (YEN JAPONES)', 'ARS (PESO ARGENTINO)', 'CNY (YUAN CHINO)', 'RUP (RUBLO RUSO)',  '']

selected_option1 = tk.StringVar()
selected_option2 = tk.StringVar()
selected_option1_or = tk.StringVar()
selected_option2_or = tk.StringVar()

def get_short_option(option):
    return option[:3]

moneda1_label = Label(root, text="Moneda origen:")
moneda1 = tk.OptionMenu(root, selected_option1, *options1, command=lambda option: selected_option1.set(get_short_option(option)))

moneda2_label = Label(root, text="Moneda destino:")
moneda2 = tk.OptionMenu(root, selected_option2, *options2, command=lambda option: selected_option2.set(get_short_option(option)))



def intercambiar_opciones():
     # Obtenemos las opciones seleccionadas actualmente
    opcion_1 = selected_option1_or.get()
    opcion_2 = selected_option2_or.get()

    # Obtenemos el índice de las opciones seleccionadas actualmente
    index_opcion_1 = options1.index(opcion_1)
    index_opcion_2 = options2.index(opcion_2)

    # Intercambiamos las opciones
    selected_option1.set(options2[index_opcion_2])
    selected_option2.set(options1[index_opcion_1])

intercambiar_btn = tk.Button(root, text="Intercambiar", command=intercambiar_opciones)
intercambiar_btn.grid(row=2, column=1, pady=10)

# agregar los campos de entrada a la ventana
monto_label.grid(row=1, column=2)
monto_entry.grid(row=1, column=3)

moneda1_label.grid(row=2, column=2)
moneda1.grid(row=2, column=3)

moneda2_label.grid(row=3, column=2)
moneda2.grid(row=3, column=3)

# agregar el botón de conversión
convertir_button = Button(root, text="Convertir", command=convertir)
convertir_button.grid(row=4, column=2, columnspan=2)

# Centrar ventana en la pantalla
root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# ejecutar la ventana
root.mainloop()
