import mysql.connector
import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import *


    # Conectarse a la base de datos
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="", 
    database="conversiones"
    )

def modificar ():
    tasa = tasa_entry.get()
    moneda1 = selected_option1.get()
    moneda2 = selected_option2.get()
    
    query = f"UPDATE tasas_cambio SET tasa_cambio = {tasa} WHERE moneda_origen = '{moneda1}' AND moneda_destino = '{moneda2}'"
    
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        messagebox.showinfo("Éxito", "Tasa de cambio modificada correctamente.")
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"No se pudo modificar la tasa de cambio: {error}")
    finally:
        cursor.close()
    cursor.close
    
# crear la ventana principal
root = Tk()
root.title("ADMINISTRADOR")
root.iconbitmap('divisa.ico')
root.geometry("340x120")

monto_label = Label(root, text="Tasa de camnio (0.0):")
tasa_entry = Entry(root)

options1 = ['MXN (PESO MEXICANO)', 'USD (DOLAR ESTADOUNIDENSE)', 'AUD (DOLAR AUSTRALIANO)', 'EUR (EURO)', 'CAD (DOLAR CANADIENSE)', 'GBP (LIBRA ESTERLINA)', 'JPY (YEN JAPONES)', 'ARS (PESO ARGENTINO)', 'CNY (YUAN CHINO)', 'RUP (RUBLO RUSO)',  '']
options2 = ['MXN (PESO MEXICANO)', 'USD (DOLAR ESTADOUNIDENSE)', 'AUD (DOLAR AUSTRALIANO)', 'EUR (EURO)', 'CAD (DOLAR CANADIENSE)', 'GBP (LIBRA ESTERLINA)', 'JPY (YEN JAPONES)', 'ARS (PESO ARGENTINO)', 'CNY (YUAN CHINO)', 'RUP (RUBLO RUSO)',  '']

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


# agregar los campos de entrada a la ventana
monto_label.grid(row=1, column=2)
tasa_entry.grid(row=1, column=3)

moneda1_label.grid(row=2, column=2)
moneda1.grid(row=2, column=3)

moneda2_label.grid(row=3, column=2)
moneda2.grid(row=3, column=3)

# agregar el botón de conversión
convertir_button = Button(root, text="Modificar", command=modificar)
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
