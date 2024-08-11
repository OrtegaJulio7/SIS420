# Importación de librerías necesarias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generar datos de estatura y peso controlados
np.random.seed(42)  # Fijamos una semilla para asegurar la reproducibilidad de los resultados
estaturas = np.random.uniform(1.4, 2.0, 100)  # Generamos 100 estaturas aleatorias entre 1.4m y 2.0m
pesos = []  # Lista para almacenar los pesos generados

# Bucle para generar pesos aleatorios controlados según la estatura
for estatura in estaturas:
    # Calcular el peso mínimo y máximo usando el IMC saludable (18.5 a 24.9)
    peso_min = 18.5 * (estatura ** 2)  # Peso mínimo según IMC de 18.5
    peso_max = 24.9 * (estatura  ** 2)  # Peso máximo según IMC de 24.9
    # Generar un peso aleatorio entre el peso mínimo y máximo calculado
    peso = np.random.uniform(peso_min, peso_max)
    pesos.append(peso)  # Añadir el peso a la lista de pesos

# Crear un DataFrame con los datos de estatura y peso
data = pd.DataFrame({
    'Estatura (m)': estaturas,
    'Peso (kg)': pesos
})

# Calcular la pendiente (m) y la intersección (b) de la recta y = mx + b
x = data['Estatura (m)']
y = data['Peso (kg)']
m = np.sum((x - np.mean(x)) * (y - np.mean(y))) / np.sum((x - np.mean(x)) ** 2)
b = np.mean(y) - m * np.mean(x)

# Crear los valores de y basados en la fórmula de la recta
y_line = m * x + b

# Visualización de los datos generados y la recta ajustada
plt.scatter(data['Estatura (m)'], data['Peso (kg)'], color='blue', label='Datos')
plt.plot(x, y_line, color='red', label='Línea ajustada')
plt.title('Ajuste de curva')
plt.xlabel('Estatura (m)')
plt.ylabel('Peso (kg)')
plt.legend()
plt.show()