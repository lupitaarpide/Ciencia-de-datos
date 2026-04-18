# Semana 4: Consolidado

## 1. Actividad 3

---
## 2. Ejercicios complementarios

---

#### Ejercicio 1: Normalización Min-Max
La fórmula de normalización Min-Max es:

```
X_normalized = (X - X_min) / (X_max - X_min)
```

Dados los datos: [10, 20, 30, 40, 50]

1. Aplicar Min-Max normalization manualmente
2. Verificar que el resultado esté entre 0 y 1
3. Implementar en Python

__Resultado:__
1. Identificar valores: (Xmin = 10, Xmax = 50)
2. Aplicar fórmula: Xnorm = (X - 10) / (50 - 10) = (X - 10) / 40
3. Tabla de resultados:
| X  | Cálculo    | Resultado |
| -- | ---------- | --------- |
| 10 | (10-10)/40 | 0.00      |
| 20 | 10/40      | 0.25      |
| 30 | 20/40      | 0.50      |
| 40 | 30/40      | 0.75      |
| 50 | 40/40      | 1.00      |

4. Script de Python:

```python
import numpy as np

datos = np.array([10, 20, 30, 40, 50])

X_min = datos.min()
X_max = datos.max()

normalized = (datos - X_min) / (X_max - X_min)

print(normalized)
```

#### Ejercicio 2: Estandarización (Z-Score)
La fórmula de estandarización es:

```
Z = (X - μ) / σ
```

Donde μ = media y σ = desviación estándar

Dados los datos: [2, 4, 4, 4, 5, 5, 7, 9]

1. Calcular la media
2. Calcular la desviación estándar
3. Estandarizar cada valor
4. Verificar que la media sea ~0 y std sea ~1

__Resultado:__
1. Media = 40/8 = 5
2. Desviación Estandar: $(2−5)2=9  (4−5)2=1  (4−5)2=1  (4−5)2=1  (5−5)2=0  (5−5)2=0  (7−5)2=4  (9−5)2=16$ y luego: $\sqrt{(X-5)/2}$
3. Z-Score: z = $(X - 5)/2$ 
4. Script de Python:
```python
import numpy as np

datos = np.array([2, 4, 4, 4, 5, 5, 7, 9])

mean = datos.mean()
std = datos.std()

z = (datos - mean) / std

print("Media:", mean)
print("Std:", std)
print("Z:", z)
print("Media Z:", z.mean())
print("Std Z:", z.std())
```


#### Ejercicio 3: Comparación de Técnicas
```python
import numpy as np

datos = np.array([100, 200, 300, 400, 500]).reshape(-1, 1)

# Aplicar:
# 1. MinMaxScaler de sklearn
# 2. StandardScaler de sklearn
# Comparar resultados
```

__Resultado:__
```python
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import numpy as np

datos = np.array([100, 200, 300, 400, 500]).reshape(-1,1)

minmax = MinMaxScaler()
standard = StandardScaler()

print("MinMax:\n", minmax.fit_transform(datos))
print("Standard:\n", standard.fit_transform(datos))
```

#### Ejercicio 4: Identificación de Valores Faltantes
```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, np.nan],
    'C': [1, 2, 3, 4, 5]
})

# Ejercicios:
# 1. Identificar valores faltantes con isnull()
# 2. Contar valores faltantes por columna
# 3. Calcular porcentaje de valores faltantes
# 4. Mostrar solo filas con valores faltantes
```

__Resultado:__
```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, np.nan],
    'C': [1, 2, 3, 4, 5]
})

print(df.isnull())
print(df.isnull().sum())
print(df.isnull().mean()*100)
print(df[df.isnull().any(axis=1)])
```

---

#### Ejercicio 5: Estrategias de Imputación
```python
# Para el mismo DataFrame, aplicar:
# 1. Eliminar filas con valores faltantes
# 2. Eliminar columnas con valores faltantes
# 3. Imputar con la media
# 4. Imputar con la mediana
# 5. Imputar con forward fill
# 6. Imputar con backward fill
```

__Resultado:__
```python
# Eliminar filas
print(df.dropna())

# Eliminar columnas
print(df.dropna(axis=1))

# Media
print(df.fillna(df.mean()))

# Mediana
print(df.fillna(df.median()))

# Forward
print(df.fillna(method='ffill'))

# Backward
print(df.fillna(method='bfill'))
```

---

#### Ejercicio 6: Imputación Avanzada
```python
# Usar sklearn.impute.SimpleImputer
from sklearn.impute import SimpleImputer

# Probar diferentes estrategias:
# - mean
# - median
# - most_frequent
# - constant
```
__Resultado:__
```python
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy='mean')
print(imputer.fit_transform(df))

imputer = SimpleImputer(strategy='median')
print(imputer.fit_transform(df))

imputer = SimpleImputer(strategy='most_frequent')
print(imputer.fit_transform(df))

imputer = SimpleImputer(strategy='constant', fill_value=0)
print(imputer.fit_transform(df))
```


---

#### Ejercicio 7: Método IQR (Rango Intercuartil)
```python
datos = [10, 12, 14, 15, 16, 18, 20, 22, 25, 100]

# Calcular:
# 1. Q1 (percentil 25)
# 2. Q3 (percentil 75)
# 3. IQR = Q3 - Q1
# 4. Límite inferior = Q1 - 1.5 * IQR
# 5. Límite superior = Q3 + 1.5 * IQR
# 6. Identificar outliers
```

__Resultado:__
```python
[10,12,14,15,16,18,20,22,25,100]
```
- $Q1 ≈ 14$
- $Q3 ≈ 22$

$IQR = 22 - 14 = 8$

Límites:
$LI = 14 - 1.5(8) = 2LS = 22 + 1.5(8) = 34$

Outlier: 100



#### Ejercicio 8: Método Z-Score
```python
from scipy import stats
import numpy as np

datos = np.array([10, 12, 14, 15, 16, 18, 20, 22, 25, 100])

# Calcular Z-scores y encontrar valores donde |Z| > 3
z_scores = stats.zscore(datos)
outliers = np.where(np.abs(z_scores) > 3)
```

__Resultado:__
```python
from scipy import stats
import numpy as np

datos = np.array([10,12,14,15,16,18,20,22,25,100])

z = stats.zscore(datos)
outliers = np.where(abs(z) > 3)

print(z)
print(outliers)
```

---

#### Ejercicio 9: Manejo de Outliers
```python
# Opciones para manejar outliers:
# 1. Eliminar outliers
# 2.替换为边界值 (capping)
# 3. Transformación logarítmica
# 4. Transformación Box-Cox
# Aplicar cada método
```

__Resultado:__
```python
# eliminar
df = datos[datos < 34]

# capping
datos = np.clip(datos, None, 34)

# log
log = np.log(datos)

# boxcox
from scipy.stats import boxcox
boxcox_data, _ = boxcox(datos)
```

---

#### Ejercicio 10: Codificación de Variables Categóricas
```python
import pandas as pd

df = pd.DataFrame({
    'color': ['rojo', 'azul', 'verde', 'rojo', 'verde'],
    'talla': ['S', 'M', 'L', 'S', 'M']
})

# Aplicar:
# 1. Label Encoding
# 2. One-Hot Encoding con get_dummies
# 3. One-Hot Encoding con sklearn
```

```python
df = pd.DataFrame({
    'color': ['rojo','azul','verde','rojo','verde'],
    'talla': ['S','M','L','S','M']
})

# Label
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['color_label'] = le.fit_transform(df['color'])

# OneHot pandas
print(pd.get_dummies(df))

# OneHot sklearn
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder()
print(ohe.fit_transform(df[['color']]).toarray())
```

---

#### Ejercicio 11: Transformaciones Numéricas
```python
import numpy as np

datos = [1, 2, 3, 4, 5, 10, 20, 30]

# Aplicar:
# 1. Logaritmo natural
# 2. Raíz cuadrada
# 3. Transformación Box-Cox
# 4. Discretización (binned)
```

__Resultado:__
```python
import numpy as np
datos = np.array([1,2,3,4,5,10,20,30])

print(np.log(datos))
print(np.sqrt(datos))

from scipy.stats import boxcox
print(boxcox(datos)[0])

# discretización
bins = pd.cut(datos, bins=3)
print(bins)
```

---

#### Ejercicio 12: Feature Engineering
```python
# Crear nuevas features:
# 1. Ratio entre dos columnas
# 2. Diferencia entre columnas
# 3. Agregar indicadores binarios
# 4. Polynomial features
# 5. DateTime features
```

__Resultado:__
```python
df['ratio'] = df['A'] / df['B']
df['diff'] = df['A'] - df['B']
df['bin'] = (df['A'] > 2).astype(int)
```

---

#### Ejercicio 13: Comparar Escaladores
```python
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, MaxAbsScaler
import numpy as np

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

# Aplicar cada escalador y comparar resultados
# ¿Cuándo usar cada uno?
```

__Resultado:__
```python
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, MaxAbsScaler

data = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

print(MinMaxScaler().fit_transform(data))
print(StandardScaler().fit_transform(data))
print(RobustScaler().fit_transform(data))
print(MaxAbsScaler().fit_transform(data))
```

---

#### Ejercicio 14: Pipeline de Preprocesamiento
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.compose import ColumnTransformer

# Crear un pipeline completo:
# 1. Seleccionar columnas numéricas y categóricas
# 2. Aplicar transformaciones apropiadas
# 3. Combinar en un pipeline
```

__Resultado:__
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

num_cols = ['edad','ingreso']
cat_cols = ['genero']

preprocessor = ColumnTransformer([
    ('num', StandardScaler(), num_cols),
    ('cat', OneHotEncoder(), cat_cols)
])

pipeline = Pipeline([
    ('preprocessing', preprocessor)
])
```
---

## 3. Actividades Complementarias

### Actividad 4.1: Identificación de Valores Faltantes

__Descripción:__ Aprende a detectar y manejar valores faltantes.

__Instrucciones:__ Aprende a detectar y manejar valores faltantes.

1. Crear un DF con valores nulos

```python
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, 4, 5],
                  'Ingreso': [6, 7, None, 9, 10],
                  'Edad': [11, None, 13, None, 15]
                  })

print(df)
```

__Resultado:__
```
   A  Ingreso  Edad
0  1      6.0  11.0
1  2      7.0   NaN
2  3      NaN  13.0
3  4      9.0   NaN
4  5     10.0  15.0
```

---

2. Practica diferentes metodos de detección

```python
# Detectar con isnull()
print(df.isnull())
```

__Resultado:__
```
       A  Ingreso   Edad
0  False    False  False
1  False    False   True
2  False     True  False
3  False    False   True
4  False    False  False
```

```python
# Detectar con notnull()
print(df.notnull())
```

__Resultado:__
```
      A  Ingreso   Edad
0  True     True   True
1  True     True  False
2  True    False   True
3  True     True  False
4  True     True   True
```

```python
# Contar números por columna
print(df.isnull().sum())
```

__Resultado:__
```
A          0
Ingreso    1
Edad       2
dtype: int64
```

```python
# Ver completitud
df.info()
```

__Resultado:__
```
<class 'pandas.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 3 columns):
 #   Column   Non-Null Count  Dtype  
---  ------   --------------  -----  
 0   A        5 non-null      int64  
 1   Ingreso  4 non-null      float64
 2   Edad     3 non-null      float64
dtypes: float64(2), int64(1)
memory usage: 252.0 bytes
```

---

3. Investiga diferentes formas de manejo de valores nulos.


### Estrategia 1: Eliminar valores nulos (dropna())
- dropna() elimina filas que contienen valores nulos.
- Solo quedan filas 100% completas.

__Cuando usarla?__
- Cuando los valores nulos representan datos inútiles.
- Cuando el porcentaje de nulos es muy bajo (menos en ventas).
- Cuando eliminar esas filas no afecta el análisis.


### Estrategia 2: fillna()
- Sustituye nulos por valores definidos

__Cuando usarla?__
- Cuando existe un valor lógico por defecto.
- Variables categóricas:
- - "Desconocido" o "No especificado"
- Variables numéricas donde 0 tiene sentido:
- - Numero de compras -> 0 si no hay compras


### Estrategia 3: Imputación con promedio:
- Pandas ignora nulos automáticamente.

__Cuando usarla?__
- Cuando hay variables numéricas continuas
- Cuando los datos faltan de forma aleatoria.

4. Aplica al menos 3:


```python
# Estrategia 1
df_drop = df.dropna()
print(df_drop)
```

__Resultado:__
```
   A  Ingreso  Edad
0  1      6.0  11.0
4  5     10.0  15.0
```


```python
# Estrategia 2
df_fill = df.fillna({
    'Nombre': 'Desconocido',
    'Edad': 0,
    'Ingreso': 0
})

print(df_fill)
```

__Resultado:__
```
   A  Ingreso  Edad
0  1      6.0  11.0
1  2      7.0   0.0
2  3      0.0  13.0
3  4      9.0   0.0
4  5     10.0  15.0
```

```python
# Estrategia 3
df_mean = df.copy()

media_edad = df_mean['Edad'].mean()
media_ingreso = df_mean['Ingreso'].mean()

df_mean['Edad'] = df_mean['Edad'].fillna(media_edad)
df_mean['Ingreso'] = df_mean['Ingreso'].fillna(media_ingreso)

print(df_mean)
```

__Resultado:__
```
   A  Ingreso  Edad
0  1      6.0  11.0
1  2      7.0  13.0
2  3      8.0  13.0
3  4      9.0  13.0
4  5     10.0  15.0
```

---

### Actividad 4.2:  
[Actividad4.2] (https://github.com/lupitaarpide/Ciencia-de-datos/blob/main/Semana4/Actividades/Actividad4.2/Actividad4.2.ipynb)  
Me dió flojera poner la actividad 4.2 en el consolidado pq ya la había puesto y no hizo el push y ya no pude recuperarla
---

### Actividad 4.3: Transformación de Datos

__Descripción:__ Practica transformaciones comunes de datos.

__Instrucciones:__
1. Con un dataset, realiza las siguientes transformaciones:
    - Normalización de datos (Min-Max)
    - Estandarización (Z-score)
    - Codificación de variables categóricas (One-Hot Encoding)
    - Creación de variables derivadas

```python
import pandas as pd

df = pd.DataFrame({
    'Edad': [20, 25, 30, 35, 40],
    'Ingreso': [8000, 12000, 15000, 20000, 22000],
    'Ciudad': ['QRO', 'CDMX', 'GDL', 'QRO', 'CDMX']
})

print(df)
```

__Resultado:__
```
   Edad  Ingreso Ciudad
0    20     8000    QRO
1    25    12000   CDMX
2    30    15000    GDL
3    35    20000    QRO
4    40    22000   CDMX
```

---

## Normalización de datos (Min - Max)

```python
df_norm = df.copy()


df_norm['Edad'] = (df['Edad'] - df['Edad'].min()) / (df['Edad'].max() - df['Edad'].min())
df_norm['Ingreso'] = (df['Ingreso'] - df['Ingreso'].min()) / (df['Ingreso'].max() - df['Ingreso'].min())

print(df_norm)
```

__Resultado:__
```
   Edad   Ingreso Ciudad
0  0.00  0.000000    QRO
1  0.25  0.285714   CDMX
2  0.50  0.500000    GDL
3  0.75  0.857143    QRO
4  1.00  1.000000   CDMX
```


#### Explicación:
Técnica sencilla utilizada en análisis de datos y machine learning para ajustar los valores numéricos de un conjunto de datos a una escala común, usualmente entre 0 y 1

__Cuándo utilizar:__
- Cuando el algoritmo requiere que todas las características estén exactamente en la misma escala
- Algoritmos Basados en Distancia
- Cuando se quiere mantener la forma de la distribución original

__Cuándo no utilizar:__
- Si tus datos tienen valores atípicos severos, Min-Max los comprimirá en un rango muy pequeño
- Si el modelo funciona mejor con una distribución gaussiana, la estandarización suele ser preferible.

---

### Estandarización (Z-Score)


```python
df_zscr = df.copy()

df_zscr['Edad'] = (df['Edad'] - df['Edad'].mean()) / df['Edad'].std()
df_zscr['Ingreso'] = (df['Ingreso'] - df['Ingreso'].mean()) / df['Ingreso'].std()

print(df_zscr)
```


__Resultado:__
```
       Edad   Ingreso Ciudad
0 -1.264911 -1.292096    QRO
1 -0.632456 -0.593666   CDMX
2  0.000000 -0.069843    GDL
3  0.632456  0.803195    QRO
4  1.264911  1.152410   CDMX
```


### Explicación:
Técnica estadística que transforma datos brutos en una escala común con media 0 y desviación estándar 1

__Cuando utilizar:__
- Comparación de escalas distintas.
- Detección de valores atípicos.
- Distribuciones Normales.

__Cuando no utilizar:__
- Datos no normales con outliers fuertes.
- Datos dispersos.

---

### One-Hot Encoding

```python
df_ohe = pd.get_dummies(df, columns=['Ciudad'])

print(df_ohe)
```


__Resultado:__
```
   Edad  Ingreso  Ciudad_CDMX  Ciudad_GDL  Ciudad_QRO
0    20     8000        False       False        True
1    25    12000         True       False       False
2    30    15000        False        True       False
3    35    20000        False       False        True
4    40    22000         True       False       False
```


### Explicación:
Técnica para convertir variables categóricas (texto) en formato numérico binario (0s y 1s) para modelos de Machine Learning

__Cuando utilizar:__
- Variables Categóricas Nominales.
- Baja Cardinalidad.

__Cuando no utilizar:__
- Alta Cardinalidad.
- Variables Ordinales.

---

### Creación de variables derivadas:

```python
df_der = df.copy()

# Ejemplo 1: Ingreso por edad
df_der['Ingreso_por_edad'] = df['Ingreso'] / df['Edad']

# Ejemplo 2: Categorizar edad
df_der['Grupo_edad'] = pd.cut(df['Edad'], bins=[0, 25, 35, 50], labels=['Joven', 'Adulto', 'Mayor'])

print(df_der)
```


__Resultado:__
```
   Edad  Ingreso Ciudad  Ingreso_por_edad Grupo_edad
0    20     8000    QRO        400.000000      Joven
1    25    12000   CDMX        480.000000      Joven
2    30    15000    GDL        500.000000     Adulto
3    35    20000    QRO        571.428571     Adulto
4    40    22000   CDMX        550.000000      Mayor
```


### Explicación:
Proceso de generar nuevas variables a partir de la manipulación, cálculo o combinación de variables existentes en un conjunto de datos.

__Cuando utilizar:__
- Para combinar categorías.
- Para convertir datos de fecha y hora.
- Para realizar cálculos complejos.

__Cuando no utilizar:__
- Alta correlación con otras variables.
- Complejidad y sobreajuste.
- Alto costo de procesamiento.

---

## 4. Resumen de Aprendizaje
- Normalización Min-Max: escala los datos entre 0 y 1.
- Estandarización (Z-score): transforma datos a media 0 y desviación estándar 1.
- Identificación de valores nulos con `isnull()` y `notnull()`.
- Manejo de valores faltantes
- Uso de `SimpleImputer` para automatizar imputación.
- Detección de outliers
- Manejo de outliers
- Codificación de variables categóricas
- Transformaciones numéricas
- Creación de nuevas variables (ratios, diferencias, categorías)
- Comparación de escaladores
- Uso de pipelines para automatizar el preprocesamiento de datos.
- Importancia del preprocesamiento para mejorar el rendimiento de modelos.
---

## 5. Dudas o Preguntas
Ninguna profe.
