'''
2. Defina la clase TarifaProveedor con un método calcular(totalSMS, totalMinutos,
totalGigas) que, dado la cantidad de mensajes, minutos de llamada y GB de consumo de
datos calcule el valor en pesos a pagar. El valor a retornar del método calcular debe ser
la suma de los resultados obtenidos en los métodos calcularSMS(totalSMS),
calcularMinutosDeLlamada(totalMinutos) y calcularConsumoGB(totalGigas)
Los valores por defecto de cada servicio son
● Mensajes de texto(SMS): $1
● Minuto de llamada: $15
● Gigas(GB) de internet: $20.
Además de los métodos anteriores, debe poseer un método abstracto getNombre() que
retorne el nombre del proveedor.
Luego, defina una clase hija por cada uno de los siguientes proveedores:

● Claro: que tiene un 20% extra sobre el básico total ## esto esta

● Personal: que tiene un 20% extra sobre los minutos de llamada y 50% sobre los
GB de datos.

● Movistar: tiene un 10% extra sobre los mensajes de texto, 20% sobre las
llamadas y 30% sobre los GB de datos.

Desarrolle una interfaz gráfica que permita ingresar la cantidad de SMS, minutos de
llamada, Gigas y muestre como resultado la tarifa que se obtendría con cada proveedor.



'''
from TarifaProveedor import TarifaProveedor
from Claro import Claro
from Personal import Personal
from Movistar import Movistar


#prueba = TarifaProveedor("Movistar")## es una clase abstracta por ende NO SE PUEDE CREAR UNA INSTANCIA
#print(prueba.calcular(20,12,15))

# plan1 = Claro("Claro")
# print(plan1.calcular(300,20,25))


# plan2 = Personal("Personal")
# print(plan2.calcular(300,20,25))

# plan3 = Movistar("Movistar")
# print(plan3.calcular(300,20,25))

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
#from proveedores import Claro, Personal, Movistar

class InterfazTarifas:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora de Tarifas")
        
        self.label_sms = ttk.Label(ventana, text="Cantidad de SMS:")#son paneles dodne los escribo
        self.label_sms.grid(row=0, column=0, padx=10, pady=5)
        
        self.label_minutos = ttk.Label(ventana, text="Minutos de llamada:")
        self.label_minutos.grid(row=1, column=0, padx=10, pady=5)
        
        self.label_gigas = ttk.Label(ventana, text="GB de datos:")
        self.label_gigas.grid(row=2, column=0, padx=10, pady=5)
        
        self.entry_sms = ttk.Entry(ventana)
        self.entry_sms.grid(row=0, column=1, padx=10, pady=5)## ventanas de ingreso
        
        self.entry_minutos = ttk.Entry(ventana)
        self.entry_minutos.grid(row=1, column=1, padx=10, pady=5)#ventanas de ingreso
        
        self.entry_gigas = ttk.Entry(ventana)
        self.entry_gigas.grid(row=2, column=1, padx=10, pady=5)
        
        self.boton_calcular = ttk.Button(ventana, text="Calcular Tarifas", command=self.calcular_tarifas)
        self.boton_calcular.grid(row=3, column=0, columnspan=2, padx=10, pady=10)### boton de calcular tarifas
        
        self.resultados_label = ttk.Label(ventana, text="Resultados:")
        self.resultados_label.grid(row=4, column=0, padx=10, pady=5, columnspan=2)
        
        self.resultados_text = tk.Text(ventana, height=5, width=40)
        self.resultados_text.grid(row=5, column=0, columnspan=2, padx=10, pady=5)
        
    def calcular_tarifas(self):# metodo donde dispongo todo
        try:
            cantidad_sms = int(self.entry_sms.get())# ingreso los datos
            cantidad_minutos = int(self.entry_minutos.get())
            cantidad_gigas = int(self.entry_gigas.get())
            
            claro = Claro("Claro")
            personal = Personal("Personal")#creo  la intancias de los proveedores
            movistar = Movistar("Movistar")
            
            tarifa_claro = claro.calcular(cantidad_sms, cantidad_minutos, cantidad_gigas)#asigno los resultados a variables
            tarifa_personal = personal.calcular(cantidad_sms, cantidad_minutos, cantidad_gigas)
            tarifa_movistar = movistar.calcular(cantidad_sms, cantidad_minutos, cantidad_gigas)
            
            resultado = f"Claro: ${tarifa_claro}\nPersonal: ${tarifa_personal}\nMovistar: ${tarifa_movistar}"#imprimto todo
            self.resultados_text.delete(1.0, tk.END)  # Limpiar el texto anterior
            self.resultados_text.insert(tk.END, resultado)
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos.")#unaexcepcion si ingresas valores erroneos 


if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = InterfazTarifas(ventana_principal)
    ventana_principal.mainloop()
