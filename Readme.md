# Funcionamiento
python src/main.py

## ETL

#### Extract
En la etapa de extracción, se recuperan los datos de ventas de archivos de Excel que contienen información sobre las transacciones realizadas en diferentes meses. Se utiliza la biblioteca pandas para leer estos archivos y convertirlos en un DataFrame de pandas, lo que permite manipular fácilmente los datos en Python.

#### Transform
Durante la etapa de transformación, se aplica una conversión simple, pero efectiva, al campo `sale_amount`, con la finalidad de convertirlo de un decimal (float) a un entero para una mejor precisión.

#### Load
En la etapa de carga, los datos transformados se insertan en la base de datos mediante la función `isnert_data()` que proviene de `src/database/operations.py`, la cual se encarga de insertar de manera masiva los datos en la base de datos, mediante la espera del `commit()` de la base de datos evitamos insertar la data en caso de algún error.

#### Load sqlite db

# Guía de instalación de la aplicación

## Clonar el repositorio
Primero, clona el repositorio de GitHub:

```sh
git clone https://github.com/Alejandro-Echavarria/challenge.git
cd challenge
```

## Crear y activar el entorno virtual
Para mantener las dependencias del proyecto aisladas, crea un entorno virtual llamado myenv.

#### Crear el entorno virtual
```sh
python -m venv myenv
```

#### Activar entorno virtual en Windows
```sh
myenv\Scripts\activate
```

#### Activar entorno virtual en macOS y Linux
```sh
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

## Desactivar el entorno virtual
Cuando hayas terminado de trabajar en el proyecto, puedes desactivar el entorno virtual:

```sh
deactivate
```