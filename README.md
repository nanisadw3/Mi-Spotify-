# Mi Spotify

Este proyecto contiene una serie de scripts de Python para interactuar con datos de canciones, buscar videos en YouTube y descargarlos.

## Características

- **`app.py`**: Lee una lista de canciones desde `favoritos.csv`, busca cada una en YouTube usando la API de YouTube y muestra el título y el enlace del video.
- **`descargas.py`**: Lee la misma lista de `favoritos.csv`, busca cada canción en YouTube y descarga el video en formato MP4 a la carpeta `descargas/`. Este script utiliza `yt-dlp` para buscar y descargar, por lo que no requiere una clave de API de YouTube.
- **`spotify.py` y `youtuve.py`**: Scripts adicionales (actualmente sin implementación completa).

## Archivo `favoritos.csv`

Este archivo CSV contiene la lista de canciones a procesar. Debe tener las siguientes columnas:

- `nombre`: El nombre de la canción.
- `artista`: El artista de la canción.

Ejemplo:
```csv
nombre,artista
"she's all i wanna be","Tate McRae"
"Crazy","One Zero"
```

## Configuración y Uso

Sigue estos pasos para configurar y ejecutar el proyecto:

### 1. Clonar el Repositorio (si es necesario)

```bash
git clone https://github.com/nanisadw3/Mi-Spotify-.git
cd Mi-Spotify-
```

### 2. Crear y Activar un Entorno Virtual

Es una buena práctica usar un entorno virtual para gestionar las dependencias del proyecto.

```bash
# Crear el entorno virtual
python3 -m venv venv

# Activar el entorno virtual
source venv/bin/activate
```

### 3. Instalar Dependencias

Instala las librerías de Python necesarias:

```bash
pip install -r requirements.txt
```
*(Nota: Se necesita crear un archivo `requirements.txt`)*

### 4. Configurar Variables de Entorno (Opcional)

El script `app.py` requiere una clave de API de YouTube. Crea un archivo llamado `.env` en la raíz del proyecto y añade tu clave:

```
YOUTUBE_API_KEY=tu_clave_de_api_aqui
```

El script `descargas.py` no necesita esta clave.

### 5. Ejecutar los Scripts

Asegúrate de que tu entorno virtual esté activado.

- **Para buscar y mostrar los enlaces de los videos:**
  ```bash
  python app.py
  ```

- **Para descargar los videos:**
  ```bash
  python descargas.py
  ```

### 6. Desactivar el Entorno Virtual

Cuando hayas terminado, puedes desactivar el entorno virtual:

```bash
deactivate
```
