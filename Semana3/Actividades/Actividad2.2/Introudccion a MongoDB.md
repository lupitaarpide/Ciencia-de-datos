# Actividad 2.2: Introducción a MongoDB

## Crear base de datos de prueba.
Como MongoDB Compass no funcionaba, hice todo en terminal.

Primero ejecuté el siguiente comando para abrir la terminal de mongo:

```bash
mongosh
```

Una vez dentro de mongo, ingrese el siguiente comando:
```bash
use actividad2
```

## Crear una coleccion y agregar 5 documentos de ejemplo.
```bash
db.createCollection("estudiantes")
```

```bash
db.estudiantes.insertMany([
|   { "nombre": "Emiliano", "carrera": "Software Engineering", "semestre": 3, "intereses": ["Arch Linux", "Python"] },
|   { "nombre": "Carlos", "carrera": "Software Engineering", "semestre": 2, "intereses": ["Web Design", "React"] },
|   { "nombre": "Ximena", "carrera": "Data Science", "semestre": 4, "intereses": ["Machine Learning", "R"] },
|   { "nombre": "Mateo", "carrera": "Cybersecurity", "semestre": 5, "intereses": ["Networking", "C++"] },
|   { "nombre": "Lucía", "carrera": "Software Engineering", "semestre": 1, "intereses": ["Logic", "Java"] }
| ])
```