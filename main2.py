import numpy as np

# Definimos los parámetros
ciudades = ["Ciudad1", "Ciudad2", "Ciudad3"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4  # Número de semanas

# Crear una matriz 3D (ciudades, días de la semana, semanas) con temperaturas aleatorias entre 15 y 35 grados.
np.random.seed(42)  # Fijar la semilla para reproducibilidad
temperaturas = np.random.randint(15, 35, (len(ciudades), len(dias_semana), semanas))

# Calcular el promedio de temperaturas para cada ciudad por semana
for i in range(len(ciudades)):  # Recorre las ciudades
    print(f"Promedios de temperaturas para {ciudades[i]}:")
    for k in range(semanas):  # Recorre las semanas
        promedio_semana = np.mean(temperaturas[i, :, k])
        print(f"  Semana {k+1}: {promedio_semana:.2f}°C")
    print()