# Ciencia de datos

---
### Guadalupe Teresa Arpide Duran / Al07148800 
# Actividad 1: 
## Descripción: 
 La actividad consiste en la elaboración de un reporte basado en el análisis de un caso práctico, en el cual se aplicarán los conceptos de ciencia de datos, Big Data, arquitecturas de almacenamiento de datos y bases de datos NoSQL.
## Objetivo:
Aplicar los conocimientos y habilidades adquiridas para resolver problemas reales con un enfoque práctico y eficiente.

---

## 1. Perfiles de ciencia de datos

Aplicar los conocimientos y habilidades adquiridas para resolver problemas reales con un enfoque práctico y eficiente.

Para la mejora de DeportivaMX en el manejo de sus datos, se necesita contar con un equipo:

1.- Cientifico de datos.
El analizará la información y buscará patrones o tendencia, un ejemplo de ello es que podra identificar que productos se venden más o qué prefieren los clientes. Esto ayudará a tomar mejores decisiones.

2.- Ingeniero de datos.
Será el encargadode crear y mantener la infraestructura donde se guardaran los datos, su rol será muy importante porque asegurará que la información se almacene correctamente y esté disponible cuando se necesite.

3.- Analista de datos.
Se enfocará en interpretar la información y presentarla de forma clara, en gráficas o incluso reportes, así facilitará que la empresa entienda lo que está pasando y se pueda actuar en ese momento.

---
## 2. Las 5 V

DeportivaMX con las cinco V del Big Data:

* Volumen: La empresa genera muchos datos, como ventas, información de clientes y productos.

* Velocidad: Los datos se generan rápidamente, ya que las compras se hacen en línea en tiempo real.

* Variedad: Diferentes tipos de datos, algunos estructurados como ventas y otros no estructurados como comentarios.

* Veracidad: Los datos se deben limpiar y revisar, para que sean los correctos.

* Valor: Es importante que los datos sirvan para tomar decisiones, así serviran para mejorar ventas o conocer mejor a los clientes.

---
## 3. Arquitectura de almacenamiento

En el caso de DeportivaMX, es importante contar con una buena forma de almacenar los datos debido a su crecimiento. Se recomienda usar almacenamiento en la nube, ya que permite guardar grandes cantidades de información sin necesidad de tener equipos físicos costosos. También es recomendable usar una base de datos NoSQL como MongoDB, porque permite manejar datos no estructurados y es más flexible y esto es más de uitilidad porque se manejan varios tipos de información.

---
## 4. Diseño de colecciones en JSON

CLIENTES

```json
{
  "_id": "Al07",
  "nombre": "Guadalupe Arpide",
  "correo": "lupitaarpide@gamil.com",
  "telefono": "5635362567",
  "ciudad": "CDMX",
  "fecha_registro": "2026-03-20"
}
```
PRODUCTOS
```json
{
  "_id": "Al07",
  "nombre": "Conjunto lululemon",
  "categoria": "Ropa",
  "precio": 2500,
  "stock": 10
}
```
VENTAS
```json
{
  "_id": "Al07",
  "cliente_id": "Guadalupe Arpide",
  "fecha": "2026-03-25",
  "productos": [
    {
      "producto_id": "Al07",
      "cantidad": 2,
      "precio_unitario": 2500
    }
  ],
  "total": 5000,
  "metodo_pago": "tarjeta"
}
```
COMPORTAMIENTO_USUARIO
```json
{
  "_id": "Guadalupe Arpide",
  "cliente_id": "Al07",
  "productos_vistos": ["Al07", "Al08"],
  "tiempo_en_sitio": 30
}
```
## Conclusión 
En conclusión, el uso del Big Data y la ciencia de datos es muy importante para empresas como DeportivaMX, ya que les permite manejar grandes cantidades de información y tomar mejores decisiones.

---
## Actividad 1.2: Análisis de Casos de Uso

**Descripción:** Analiza casos reales de aplicación de ciencia de datos.

**Instrucciones:**
1. Investiga 3 empresas que utilizan ciencia de datos (ej: Netflix, Amazon, Spotify)
2. Para cada empresa, identifica:
   - Qué tipo de datos recopilan
   - Qué técnicas de análisis utilizan
   - Qué problemas resuelven con los datos
3. Crea una presentación breve resumiendo tus hallazgos

---
### Empresa 1: Netflix

### Datos que recopilan:

* Historial de visualización
* Tiempo que ves cada contenido
* Búsquedas realizadas
* Calificaciones (likes/dislikes)
* Dispositivo y horario de uso ([LinkedIn][1])

### Técnicas de análisis:

* Machine Learning
* Filtrado colaborativo
* Análisis de comportamiento
* Deep Learning ([GeeksforGeeks][2])

### Problemas que resuelven:

* Recomendar contenido personalizado
* Reducir cancelaciones de usuarios
* Decidir qué series o películas producir
* Mejorar la experiencia del usuario ([GeeksforGeeks][2])

----

### Empresa 2: Amazon

### Datos que recopilan:

* Historial de compras
* Productos vistos
* Carrito y lista de deseos
* Reseñas y calificaciones
* Ubicación y preferencias de entrega ([LinkedIn][1])

### Técnicas de análisis:

* Sistemas de recomendación
* Análisis predictivo
* Big Data
* Segmentación de clientes

### Problemas que resuelven:

* Recomendar productos relevantes
* Aumentar ventas
* Optimizar logística y entregas
* Personalizar la experiencia de compra ([LinkedIn][1])

---

### Empresa 3: Spotify

### Datos que recopilan:

* Canciones escuchadas
* Listas de reproducción
* Tiempo de escucha
* Géneros musicales
* Interacciones del usuario

### Técnicas de análisis:

* Inteligencia artificial (IA)
* Procesamiento de lenguaje natural
* Sistemas de recomendación
* Análisis semántico ([Smith Hanley Associates][3])

### Problemas que resuelven:

* Crear playlists personalizadas (ej. Discover Weekly)
* Recomendar música nueva
* Mejorar la retención de usuarios
* Entender tendencias musicales ([EPAM Startups & SMBs][4])

---

# Conclusión

La ciencia de datos permite a las empresas:

* Entender mejor a sus usuarios
* Personalizar servicios
* Tomar decisiones estratégicas
* Incrementar ingresos

---

[1]: https://www.linkedin.com/pulse/how-netflix-amazon-use-data-science-predict-what-lthrc?utm_source=chatgpt.com "How Netflix and Amazon Use Data Science to Predict What You Like"
[2]: https://www.geeksforgeeks.org/how-netflix-uses-data-science/?utm_source=chatgpt.com "How Netflix Uses Data Science? - GeeksforGeeks"
[3]: https://www.smithhanley.com/2024/04/04/entertainment-industry-data-science/?utm_source=chatgpt.com "Entertainment Industry Data Science | Smith Hanley Associates"
[4]: https://startups.epam.com/blog/data-science-in-the-retail-industry?utm_source=chatgpt.com "Data Science in Retail Industry | EPAM Startups & SMBs"

---
### Actividad 1.4: Exploración de Fuentes de Datos

**Descripción:** Explora diferentes fuentes de datos disponibles.

**Instrucciones:**
1. Investiga qué es Kaggle y cómo puedes usarlo
2. Explora al menos 3 datasets públicos en Kaggle
3. Identifica qué tipo de datos contiene cada uno
4. Elige un dataset que te interese y describe:
   - Qué información contiene
   - Qué preguntas podrías responder con esos datos







