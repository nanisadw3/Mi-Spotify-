import requests

# Tu API Key de YouTube (cámbiala por la tuya)
API_KEY = "AIzaSyDfK4_1dpUR_dbzgbTx3Snnh1wsi_-wv7Q"


def buscar_video_youtube(cantante_o_cancion):
    # URL base de búsqueda
    url = "https://www.googleapis.com/youtube/v3/search"

    # Parámetros de la petición
    params = {
        "part": "snippet",
        "q": cantante_o_cancion,  # lo que busca el usuario
        "type": "video",  # solo videos
        "maxResults": 1,  # el primer resultado
        "key": API_KEY,
    }

    # Hacemos la petición GET
    response = requests.get(url, params=params)

    # Verificamos que todo salió bien
    if response.status_code != 200:
        print("Error al consultar la API:", response.status_code)
        return None

    data = response.json()

    # Si hay resultados
    if "items" in data and len(data["items"]) > 0:
        video_id = data["items"][0]["id"]["videoId"]
        titulo = data["items"][0]["snippet"]["title"]
        link = f"https://www.youtube.com/watch?v={video_id}"
        return titulo, link
    else:
        return None


# Pedimos al usuario el nombre del cantante o canción
busqueda = input("Ingresa el nombre del cantante o canción: ")

resultado = buscar_video_youtube(busqueda)

if resultado:
    titulo, link = resultado
    print(f"Video encontrado: {titulo}")
    print(f"Link listo para reproducir: {link}")
else:
    print("No se encontró ningún video.")
