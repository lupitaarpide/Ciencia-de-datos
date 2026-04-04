# Actividad 2.4: Modelado de Datos NoSQL
Descripción: Diseña un modelo de datos para un caso específico.

## Instrucciones:

- Elige un caso: "Sistema de biblioteca digital"
- Diseña la estructura de documentos necesaria
- Crea al menos 5 colecciones con relaciones
- Define los campos y tipos de datos
- Justifica tu diseño
- Carpeta de entrega: Semana2/Actividades/Actividad2.4/
--- 

## Sistema de gestion de una frutería

### Creacion de colecciones

#### 1- Productos
```json
{
  "_id": ObjectId("..."),
  "nombre": "Manzana",
  "categoria": "Frutas",
  "precio_por_unidad": 15.00,
  "unidad_medida": "kg",
  "stock_actual": 45.5,
  "detalles": {
    "origen": "Chihuahua",
    "temporada": "Otoño-Invierno",
    "organico": true
  }
}
```

#### 2- Inventario
```json
{
  "_id": ObjectId("..."),
  "id_producto": ObjectId("..."),
  "fecha_ingreso": ISODate("2026-04-01T08:00:00Z"),
  "fecha_caducidad_estimada": ISODate("2026-04-10T00:00:00Z"),
  "proveedor": "Vendedor de frutas",
  "estado": "maduro"
}
```

#### 3- Clientes
```json
{
  "_id": ObjectId("..."),
  "nombre": "Ximena",
  "telefono": "4421234567",
  "direccion_entrega": "Colonia Centro, Querétaro",
  "puntos_lealtad": 120,
  "preferencias": ["Frutos rojos", "Cítricos"]
}
```

#### 4- Ventas
```json
{
  "_id": ObjectId("..."),
  "id_cliente": ObjectId("..."),
  "fecha_venta": ISODate("2026-04-03T14:30:00Z"),
  "articulos": [
    { "nombre": "Plátano", "cantidad": 1.5, "subtotal": 30.00 },
    { "nombre": "Aguacate", "cantidad": 0.8, "subtotal": 65.00 }
  ],
  "total": 95.00,
  "metodo_pago": "Efectivo"
}
```

#### 5- Ofertas
```json
{
  "_id": ObjectId("..."),
  "titulo": "Martes de Cítricos",
  "descuento_porcentaje": 15,
  "productos_aplicables": [ObjectId("..."), ObjectId("...")],
  "activo": true
}
```

### Justificación
Decidí usar MongoDB (NoSQL) para este ejemplo porque me di cuenta de que una frutería no es tan "rígida" como una tabla de Excel. Estas fueron mis razones:

- __1. Flexibilidad de Productos__: A diferencia de una tabla rígida, aquí puedo registrar productos por kilo (manzanas), por pieza (piñas) o por manojo (cilantro) en una misma 
colección sin complicaciones.

- __2. Rapidez en Ventas__: Al guardar la lista de productos comprados directamente dentro del ticket de venta (documento embebido), el sistema no tiene que buscar en varias tablas. 
Esto hace que cobrar sea mucho más rápido.

- __3. Control de Frescura__: Creé una colección de lotes para saber qué fruta llegó primero. Así el sistema me ayuda a vender lo más antiguo antes de que se eche a perder, 
reduciendo el desperdicio.

- __4. Enfoque en el Cliente__: Puedo guardar los gustos de mis clientes frecuentes en su perfil de forma sencilla. Si llega su fruta favorita, el sistema me permite identificarlos 
rápido para darles un mejor servicio.

<br>

Para mí es un modelo simple y flexible, totalmente funcional para una frutería, ya que se adapta a los cambios de inventario que estas tienen al día a día 