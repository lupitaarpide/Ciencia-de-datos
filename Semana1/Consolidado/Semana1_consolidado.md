# Ejercicios Complementarios - Semana 1

## Temas Cubiertos
- **T1**: Fundamentos de ciencia de datos
- **T2**: Big Data

## Prerrequisitos Recomendados
- **Matemáticas**: Conceptos básicos de álgebra, escalas y volúmenes
- **Lógica**: Pensamiento computacional básico

---

## Ejercicios de Matemáticas y Álgebra Básica

### Ejercicio 1: Operaciones Algebraicas Básicas
Resolver las siguientes operaciones:

```
a) 3x + 5 = 17      → x = ?
3x = 17 - 5
3x = 12
x = 4

b) 2y - 8 = 22      → y = ?
2y = 22 + 8
2y = 30
y = 15

c) 4z + 3 = 3z + 10 → z = ?
4z - 3z = 10 - 3
z = 7

d) 5(x + 2) = 35    → x = ?
x + 2 = 7
x = 5

```

**Solución:**
- a) x = 4
- b) y = 15
- c) z = 7
- d) x = 5

### Ejercicio 2: Funciones Lineales
Dada la función f(x) = 2x + 3:

- Calcular f(0), f(1), f(5), f(10)
- f(0)= 3
- f(1)= 5
- f(5)= 13
- f(10)= 23
- 
- Graficar la función e identificar la pendiente y ordenada al origen


### Ejercicio 3: Escalas y Volúmenes (Big Data)
Expresar en notación científica:

| Cantidad                    | Notación Científica |
| --------------------------- | ------------------- |
| 1,000,000 bytes             | 1*10⁶               |
| 1,000,000,000 registros     | 1*10⁹               |
| 1,000,000,000,000 bytes     | 1*10¹²              |

**Referencias:**
- 10³ = 1,000 (Kilo)
- 10⁶ = 1,000,000 (Mega)
- 10⁹ = 1,000,000,000 (Giga)
- 10¹² = 1,000,000,000,000 (Tera)
- 10¹⁵ = 1,000,000,000,000,000 (Peta)
- 10¹⁸ = 1,000,000,000,000,000,000 (Exa)

---

## Ejercicios de Lógica Computacional

### Ejercicio 4: Diagramas de Flujo
Diseñar un algoritmo simple para:
1. Determinar si un número es par o impar
```
   flowchart TD
    A[Inicio] --> B[Ingresar número]
    B --> C{¿Número % 2 == 0?}
    C -->|Sí| D[Es par]
    C -->|No| E[Es impar]
    D --> F[Fin]
    E --> F
``` 
   
3. Calcular el promedio de 3 números
```    
   flowchart TD
    A[Inicio] --> B[Ingresar n1]
    B --> C[Ingresar n2]
    C --> D[Ingresar n3]
    D --> E[Suma = n1 + n2 + n3]
    E --> F[Promedio = Suma / 3]
    F --> G[Mostrar promedio]
    G --> H[Fin]
``` 

5. Encontrar el mayor de 4 números
```
   flowchart TD
    A[Inicio] --> B[Ingresar n1, n2, n3, n4]
    B --> C[Mayor = n1]
    C --> D{¿n2 > Mayor?}
    D -->|Sí| E[Mayor = n2]
    D -->|No| F[Continuar]
    E --> G
    F --> G
    G --> H{¿n3 > Mayor?}
    H -->|Sí| I[Mayor = n3]
    H -->|No| J[Continuar]
    I --> K
    J --> K
    K --> L{¿n4 > Mayor?}
    L -->|Sí| M[Mayor = n4]
    L -->|No| N[Continuar]
    M --> O
    N --> O
    O --> P[Mostrar Mayor]
    P --> Q[Fin]
```

### Ejercicio 5: Pseudocódigo
Escribir pseudocódigo para:
1. Calcular el factorial de un número
```
Leer n
factorial = 1
Para i desde 1 hasta n:
    factorial = factorial * i
Mostrar factorial
```
2. Buscar un elemento en una lista
```
Leer lista
Leer elemento
Para cada valor en lista:
    Si valor == elemento:
        Mostrar "Encontrado"
        Terminar
Mostrar "No encontrado"
```
3. Ordenar una lista de números
```
Leer lista
Para i desde 0 hasta longitud:
    Para j desde 0 hasta longitud-1:
        Si lista[j] > lista[j+1]:
            Intercambiar
Mostrar lista ordenada
```


### Ejercicio 6: Operaciones Booleanas
Evaluar las siguientes expresiones:

```python
a = True
b = False
c = True

# Evaluar:
print(a and b)      # False
print(a or b)      # True
print(not b)       # True
print(a and c)     # True
print((a or b) and c)  # True
```

---

## Ejercicios de Investigación

### Ejercicio 7: Historia de la Ciencia de Datos
Investigar y responder:
1. ¿Quién es considerada la primera científica de datos?

La primera científica de datos es considerada Ada Lovelace, ya que fue la primera en escribir un algoritmo.

2. ¿Qué es el "Data Science Venn Diagram" de Drew Conway?

Muestra que la ciencia de datos se compone de:

* Programación (hacking skills)

* Matemáticas y estadística

* Conocimiento del dominio
  
3. Menciona 3 herramientas modernas de Big Data

* Hadoop

* Spark

* Google BigQuery

### Ejercicio 8: Aplicaciones de Big Data
Investigar un caso de uso real de Big Data en:
- Salud
  Se usa para analizar enfermedades y mejorar diagnósticos.
- Finanzas
  Detección de fraudes en transacciones bancarias.
- Redes sociales
  Recomendación de contenido.
- Deportes
  Análisis de rendimiento de jugadores y estrategias de juego.
  
