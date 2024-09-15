# Función para calcular la temperatura promedio de cada ciudad durante un periodo de semanas
def calcular_temperatura_promedio(temperaturas):
    """
    Calcula la temperatura promedio de cada ciudad durante un periodo de tiempo.

    Parámetros:
    temperaturas (dict): Un diccionario donde las llaves son los nombres de las ciudades y los valores son listas 
                         de temperaturas semanales.

    Retorna:
    dict: Un diccionario donde las llaves son las ciudades y los valores son las temperaturas promedio.
    """
    promedios = {}

    # Recorrer cada ciudad en el diccionario de temperaturas
    for ciudad, temps in temperaturas.items():
        # Calcular la temperatura promedio para la ciudad
        promedio_ciudad = sum(temps) / len(temps)
        # Almacenar el promedio en el diccionario
        promedios[ciudad] = promedio_ciudad

    return promedios


# Ejemplo de uso con datos de temperaturas de 3 ciudades durante 4 semanas
temperaturas = {
    "Ciudad A": [30, 32, 29, 31],  # Temperaturas durante 4 semanas para Ciudad A
    "Ciudad B": [25, 26, 24, 27],  # Temperaturas durante 4 semanas para Ciudad B
    "Ciudad C": [20, 19, 21, 22]   # Temperaturas durante 4 semanas para Ciudad C
}

# Llamada a la función
promedios = calcular_temperatura_promedio(temperaturas)

# Imprimir el resultado
for ciudad, promedio in promedios.items():
    print(f"El promedio de temperaturas de {ciudad} es: {promedio:.2f}°C")