📦 Proyecto clientes – FastAPI + Poetry

Este servicio forma parte del monorepo y proporciona un CRUD de clientes utilizando FastAPI, Poetry y Uvicorn.

🚀 Requisitos previos

* Python 3.12
* Poetry instalado
* PyCharm (opcional pero recomendado)

🛠️ Instalación del proyecto

1. Clonar el repositorio

```
git clone <url-del-repo>
cd clientes
```
2. Instalar dependencias con Poetry

```
poetry install
``` 

3. Activar el entorno virtual (opcional)

```
poetry shell
``` 

Poetry crea el entorno virtual en:

```
C:\Users\<usuario>\AppData\Local\pypoetry\Cache\virtualenvs\
``` 

▶️ Ejecutar el servidor FastAPI

Puerto por defecto (8000)
```
poetry run uvicorn app.main:app --reload
``` 

Puerto personalizado (ej. 8001)
```
poetry run uvicorn app.main:app --reload --port 8001
``` 

Acceso a la API:

Documentación Swagger: http://127.0.0.1:8001/docs
ReDoc: http://127.0.0.1:8001/redoc

🧪 Ejecutar tests
```
poetry run pytest
``` 

🧩 Configuración en PyCharm

1.- Abrir PyCharm → Open → seleccionar carpeta clientes
2.- Ir a:
```
File → Settings → Python → Interpreter
```


3.- Seleccionar Existing Interpreter
Elegir el ejecutable:
```
...\pypoetry\Cache\virtualenvs\clientes-xxxx\Scripts\python.exe
```

4.- Crear un “Run Configuration”:

* Add → Python
* Module name: uvicorn
* Parameters:

```
app.main:app --reload --port 8001
```
Working directory: carpeta raíz clientes

📁 Estructura recomendada del proyecto

```
clientes/
│
├── app/
│   ├── main.py
│   ├── __init__.py
│   └── routes/
│       └── ...
│
├── pyproject.toml
├── README.md
└── ...
```

📄 Notas

* Para que PyCharm detecte los módulos correctamente, el proyecto debe abrirse directamente en la carpeta clientes.
* Para usar .venv dentro del proyecto:

```
poetry config virtualenvs.in-project true
poetry env remove python
poetry install
```
