# App Install Guide

## Clonar el repositorio
Primero, clona el repositorio de GitHub:

```sh
git clone https://github.com/Alejandro-Echavarria/challenge.git
cd challenge
```

## Crear y activar el entorno virtual
Para mantener las dependencias del proyecto aisladas, crea un entorno virtual llamado myenv.

### En Windows
```sh
python -m venv myenv
myenv\Scripts\activate
```

### En macOS y Linux
```sh
python -m venv myenv
source myenv/bin/activate
```

## Instalar dependencias
Con el entorno virtual activado, instala las dependencias necesarias utilizando el archivo `requirements.txt`:

```sh
pip install -r requirements.txt
```

## Crear archivo .env con variables de entorno

Crear el archivo `.env`, puedes copiar y pegar el archivo `.env.exmaple` y renombrarlo, este debe contener lo siguiente:

```.env
DB_PATH='data/sqlite/'
CONNECTION_STRING='data/sqlite/challenge.sqlite3'
```

### Desactivar el entorno virtual
Cuando hayas terminado de trabajar en el proyecto, puedes desactivar el entorno virtual:

```sh
deactivate
```