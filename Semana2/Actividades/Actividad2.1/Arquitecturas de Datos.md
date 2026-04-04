# Actividad 2.1: Arquitecturaas de Datos

## 1. ¿Qué son los Data Warehouses y Data Lakes?

- __Data Warehouse__: Es un sistema que agrega datos de diversas fuentes (como bases de datos operativas o sistemas transaccionales) en un único repositorio central y coherente.
- __Data Lake__: Es un repositorio diseñado para almacenar grandes volúmenes de datos sin procesar (en bruto), generalmente utilizando almacenamiento de objetos en la nube de bajo costo.

## 2. Características de cada uno

### - Data Warehouse
- __Datos estructurados__: Está optimizado principalmente para datos que tienen un formato definido.
- __Proceso ETL__: Tradicionalmente, los datos se limpian, organizan y transforman antes de ser cargados en el almacén (esquema en escritura).
- __Uso empresarial__: Se utiliza para iniciativas de business intelligence (BI), informes, paneles y análisis de datos históricos por parte de usuarios comerciales.
- __Costo y rendimiento__: Ofrecen un rendimiento sólido para consultas complejas, pero tienen costos más altos y menos flexibilidad para manejar datos masivos sin procesar.

### - Data Lake
- __Diversidad de formatos__: Permite la ingesta de datos estructurados, semiestructurados y no estructurados (como texto libre, imágenes, videos y registros de IoT).
- __Esquema en lectura__: Los datos se ingieren en su estado original y no se transforman hasta que se necesitan para un análisis específico.
- __Ciencia de datos e IA__: Son ideales para el machine learning, la ciencia de datos y la analítica de big data, ya que estas tareas requieren acceso a grandes conjuntos de datos diversos y detallados.
- __Escalabilidad__: Son altamente escalables y más rentables que los almacenes tradicionales para el almacenamiento multipropósito a gran escala.

## 3. ¿Qué es un Data Mart?

Un Data Mart es un subconjunto de un almacén de datos (data warehouse) que se centra específicamente en una línea de negocio, un departamento o un área temática en particular.
Lo que hace es facilitarle a los trabajadores de ciertas áreas de negocio el acceso a los datos necesarios para realizar sus tareas.

## 4. Diagrama sobre las diferencias entre ellos.
![Diagrama](./Diagrama_Act2.1.png)

## Referencias
- https://www.ibm.com/mx-es/think/topics/data-mart
- https://www.ibm.com/mx-es/think/topics/data-warehouse
- https://www.ibm.com/mx-es/think/topics/data-lake