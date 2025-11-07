
import csv
import requests
import os
import time
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Carga la clave de API desde una variable de entorno para mayor seguridad.
API_KEY = os.getenv("YOUTUBE_API_KEY")

def buscar_video_youtube(query):
    """
    Busca un video en YouTube y devuelve el título y el enlace del primer resultado.
    """
    # URL base de la API de búsqueda de YouTube
    url = "https://www.googleapis.com/youtube/v3/search"

    # Parámetros para la petición a la API
    params = {
        "part": "snippet",
        "q": query,          # La consulta de búsqueda (ej: "nombre cancion - artista")
        "type": "video",     # Solo buscar videos
        "maxResults": 1,     # Traer solo el primer resultado
        "key": API_KEY,
    }

    # Se realiza la petición GET a la API de YouTube
    response = requests.get(url, params=params)

    # Si la petición falla, se informa el error.
    if response.status_code != 200:
        print(f"❌ Error al consultar la API de YouTube: {response.status_code} - {response.text}")
        return None

    data = response.json()

    # Si se encontraron resultados, se extrae la información del video.
    if "items" in data and len(data["items"]) > 0:
        video_id = data["items"][0]["id"]["videoId"]
        titulo = data["items"][0]["snippet"]["title"]
        link = f"https://www.youtube.com/watch?v={video_id}"
        return titulo, link
    else:
        # Si no se encuentra nada, se devuelve None.
        return None

def procesar_canciones_favoritas():
    """
    Lee el archivo CSV de canciones favoritas y busca cada una en YouTube.
    """
    # Primero, se verifica que la clave de API de YouTube esté configurada.
    if not API_KEY:
        print("🛑 Error: La variable de entorno YOUTUBE_API_KEY no está configurada.")
        print("Por favor, configúrala con tu clave de API de YouTube antes de ejecutar.")
        return

    # Construye una ruta robusta al archivo CSV, relativa a la ubicación del script.
    script_dir = os.path.dirname(os.path.abspath(__file__))
    archivo_csv = os.path.join(script_dir, 'favoritos.csv')

    try:
        with open(archivo_csv, "r", newline="", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            canciones = list(lector)
            total_canciones = len(canciones)
            
            print(f"🎶 Encontradas {total_canciones} canciones en 'favoritos.csv'. Buscando en YouTube...")

            for i, cancion in enumerate(canciones):
                nombre = cancion["nombre"]
                artista = cancion["artista"]
                
                # Se crea una consulta de búsqueda más precisa para mejores resultados.
                consulta = f"{nombre} {artista} Official Video"
                
                print(f"\n({i+1}/{total_canciones}) Buscando: '{nombre}' de '{artista}'...")
                
                resultado = buscar_video_youtube(consulta)

                if resultado:
                    titulo_yt, link_yt = resultado
                    print(f"  ✅ Título: {titulo_yt}")
                    print(f"  📺 Link: {link_yt}")
                else:
                    print("  ❌ No se encontró un video de YouTube para esta canción.")
                
                # Se añade una pequeña pausa para no saturar la API de YouTube.
                time.sleep(1)

    except FileNotFoundError:
        print(f"🛑 Error: No se pudo encontrar el archivo '{archivo_csv}'.")
        print("Asegúrate de que el archivo 'favoritos.csv' existe en el directorio principal.")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")

if __name__ == "__main__":
    procesar_canciones_favoritas()
