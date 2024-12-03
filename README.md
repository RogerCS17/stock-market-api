# Stock-Market-API (Backend)

Este es el backend de la aplicación web de predicción bursátil. Está desarrollado con **FastAPI** y se encarga de gestionar la lógica de negocio y las interacciones con la base de datos.

## Estructura del Proyecto
- **`app/`**: Contiene los módulos principales del backend.
  - **`crud.py`**: Operaciones CRUD para interactuar con la base de datos.
  - **`database.py`**: Configuración de la conexión con la base de datos.
  - **`models.py`**: Definición de los modelos de base de datos.
  - **`routes.py`**: Define las rutas de la API.
  - **`schemas.py`**: Esquemas de validación para los datos de entrada y salida.
  - **`main.py`**: Punto de entrada de la aplicación.
- **`requirements.txt`**: Lista de dependencias necesarias para el backend.

## Requisitos
- Python 3.10 o superior.
- PostgreSQL como base de datos.
- Librerías detalladas en `requirements.txt`.

## Ejecución
1. Instala las dependencias con `pip install -r requirements.txt`.
2. Configura las credenciales de la base de datos en `database.py`.
3. Ejecuta el servidor con `uvicorn app.main:app --reload`.

## Endpoints principales
- **`POST /register`**: Registro de nuevos usuarios.
- **`POST /login`**: Autenticación de usuarios.
