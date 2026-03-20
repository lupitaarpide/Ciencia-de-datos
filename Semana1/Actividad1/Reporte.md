# Ciencia de datos
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### Guadalupe Teresa Arpide Duran / Al07148800 
# Actividad 1: 
## Descripción: 
### La actividad consiste en la elaboración de un reporte basado en el análisis de un caso práctico, en el cual se aplicarán los conceptos de ciencia de datos, Big Data, arquitecturas de almacenamiento de datos y bases de datos NoSQL.
## Objetivo: 
### Aplicar los conocimientos y habilidades adquiridas para resolver problemas reales con un enfoque práctico y eficiente.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## 1. Perfiles de ciencia de datos

Para la mejora de DeportivaMX en el manejo de sus datos, se necesita contar con un equipo:

1.- Cientifico de datos.
El analizará la información y buscará patrones o tendencia, un ejemplo de ello es que podra identificar que productos se venden más o qué prefieren los clientes. Esto ayudará a tomar mejores decisiones.

2.- Ingeniero de datos.
Será el encargadode crear y mantener la infraestructura donde se guardaran los datos, su rol será muy importante porque asegurará que la información se almacene correctamente y esté disponible cuando se necesite.

3.- Analista de datos.
Se enfocará en interpretar la información y presentarla de forma clara, en gráficas o incluso reportes, así facilitará que la empresa entienda lo que está pasando y se pueda actuar en ese momento.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## 2. Las 5 V

DeportivaMX con las cinco V del Big Data:

* Volumen: La empresa genera muchos datos, como ventas, información de clientes y productos.

* Velocidad: Los datos se generan rápidamente, ya que las compras se hacen en línea en tiempo real.

* Variedad: Diferentes tipos de datos, algunos estructurados como ventas y otros no estructurados como comentarios.

* Veracidad: Los datos se deben limpiar y revisar, para que sean los correctos.

* Valor: Es importante que los datos sirvan para tomar decisiones, así serviran para mejorar ventas o conocer mejor a los clientes.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## 3. Arquitectura de almacenamiento

En el caso de DeportivaMX, es importante contar con una buena forma de almacenar los datos debido a su crecimiento. Se recomienda usar almacenamiento en la nube, ya que permite guardar grandes cantidades de información sin necesidad de tener equipos físicos costosos. También es recomendable usar una base de datos NoSQL como MongoDB, porque permite manejar datos no estructurados y es más flexible y esto es más de uitilidad porque se manejan varios tipos de información.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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









