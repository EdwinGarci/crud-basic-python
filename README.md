# API REST con Python Flask

## Descripción
Este proyecto es una API REST construida con Python Flask. A continuación, se detallan las herramientas y tecnologías usadas en el proyecto.

* Python 3.9+
* MySQL
* Flask 2.0+
* PyMySQL

## Instalación
Pasos para instalar y configurar el proyecto en tu entorno local.

1. Clona el repositorio:
```bash
git clone https://github.com/EdwinGarci/crud-basic-python.git
```

2. Crea un entorno virtual y actívalo:
```bash
python -m venv venv
# En Windows
venv\Scripts\activate
# En macOS/Linux
source venv/bin/activate
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

4. Crea un archivo `.env` en la raíz del proyecto y copia las variables de entorno que estan en el `.env.template`:
```
MYSQL_DB_HOST=localhost
MYSQL_DB_USER=tu_usuario
MYSQL_DB_PASSWORD=tu_contraseña
MYSQL_DB_NAME=nombre_db
```

5. Ejecuta el script de base de datos (si existe):
```bash
mysql -u tu_usuario -p tu_base_de_datos < src/database/schema.sql
```

6. Inicia la aplicación:
```bash
python run.py
```

## Estructura del Proyecto
```
proyecto/
    ├── src/
    │   ├── routes/
    │   │   ├── IndexRoutes.py
    │   │   └── ProductRoutes.py
    │   ├── models/
    │   │   └── ProductModel.py
    │   ├── services/
    │   │   └── ProductService.py
    │   ├── database/
    │   │    └── db_mysql.py
    │   └── __init__.py
    ├── .env
    ├── requirements.txt
    └── index.py
    └── config.py
```

## Decisiones de Diseño
- Se implementó una arquitectura en capas (rutas, servicios, modelos)
- Se utilizaron querys para las operaciones de base de datos
- Se implementaron validaciones y manejo de errores
- La estructura CRUD fue implementada para manejar productos

## Endpoints
- GET /products - Obtiene todos los productos
- GET /products/{id} - Obtiene un producto por ID
- POST /products - Crea un nuevo producto
- PUT /products/{id} - Actualiza un producto
- DELETE /products/{id} - Elimina un producto
