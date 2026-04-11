# -----------------------------
# 1. LISTAS
# -----------------------------

# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Lista original:", numeros)

# -----------------------------
# 2. DICCIONARIOS
# -----------------------------

# Diccionario con información de estudiantes
estudiantes = {
    "Emi": {"edad": 20, "promedio": 8.7},
    "Pato": {"edad": 50, "promedio": 9.1},
    "Furia": {"edad": 19, "promedio": 7.8}
}

print("\nDiccionario de estudiantes:")
for nombre, datos in estudiantes.items():
    print(f"{nombre} -> Edad: {datos['edad']}, Promedio: {datos['promedio']}")

# -----------------------------
# 3. DATAFRAMES
# -----------------------------

# Importamos pandas para trabajar con DataFrames
import pandas as pd

# Convertimos el diccionario en una tabla
df_estudiantes = pd.DataFrame([
    {"Nombre": nombre, "Edad": datos["edad"], "Promedio": datos["promedio"]}
    for nombre, datos in estudiantes.items()
])

print("\nDataFrame de estudiantes:")
print(df_estudiantes)

# Agregamos una columna nueva usando una condición
df_estudiantes["Aprobado"] = df_estudiantes["Promedio"] >= 7.0

print("\nDataFrame con columna 'Aprobado':")
print(df_estudiantes)

# -----------------------------
# 4. FUNCIONES LAMBDA
# -----------------------------

# Función lambda para duplicar un número
duplicar = lambda x: x * 2

# Aplicamos lambda a la lista de números
duplicados = list(map(duplicar, numeros))

print("\nNúmeros duplicados con lambda:")
print(duplicados)

# Otra lambda: verificar si un número es mayor que 5
mayor_que_5 = lambda x: x > 5
print("\n¿7 es mayor que 5?:", mayor_que_5(7))

# -----------------------------
# 5. MANEJO DE ERRORES
# -----------------------------

# Intentamos realizar una división controlando posibles errores
try:
    numero1 = int(input("\nIngresa un número entero: "))
    numero2 = int(input("Ingresa otro número entero: "))
    division = numero1 / numero2
    print(f"Resultado de la división: {division}")

except ValueError:
    print("Error: Bro, debes ingresar números enteros válidos.")

except ZeroDivisionError:
    print("Error: no se puede dividir entre cero, pasaste el kinder?.")

# -----------------------------
# 6. CINCO EJERCICIOS BÁSICOS
# -----------------------------

print("\n==============================")
print("EJERCICIOS DE PROGRAMACIÓN")
print("==============================")

# Ejercicio 1: Verificar si un número es positivo, negativo o cero
def clasificar_numero(n):
    if n > 0:
        return "positivo"
    elif n < 0:
        return "negativo"
    else:
        return "cero"

print("\nEjercicio 1:")
print("El número -3 es", clasificar_numero(-3))
print("El número 0 es", clasificar_numero(0))
print("El número 8 es", clasificar_numero(8))

# Ejercicio 2: Calcular el factorial de un número con while
def factorial(n):
    resultado = 1
    contador = 1
    while contador <= n:
        resultado *= contador
        contador += 1
    return resultado

print("\nEjercicio 2:")
print("Factorial de 5:", factorial(5))

# Ejercicio 3: Calcular el promedio de una lista
def calcular_promedio(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

notas = [8, 9, 7, 10, 6]
print("\nEjercicio 3:")
print("Notas:", notas)
print("Promedio:", calcular_promedio(notas))

# Ejercicio 4: Encontrar el valor máximo y mínimo
def maximo_y_minimo(lista):
    if len(lista) == 0:
        return None, None
    return max(lista), min(lista)

mayor, menor = maximo_y_minimo(numeros)
print("\nEjercicio 4:")
print("Lista:", numeros)
print("Máximo:", mayor)
print("Mínimo:", menor)

# Ejercicio 5: Contar cuántas vocales tiene una palabra
def contar_vocales(palabra):
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in palabra:
        if letra in vocales:
            contador += 1
    return contador

palabra = "programacion"
print("\nEjercicio 5:")
print(f"La palabra '{palabra}' tiene {contar_vocales(palabra)} vocales")
