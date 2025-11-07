
import csv
import os
import time
from dotenv import load_dotenv
import yt_dlp

def descargar_video(query, output_path):
    """
    Busca y descarga un video de YouTube en formato mp4.
    """
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
        'default_search': 'ytsearch',
        'no_warnings': True,
        'quiet': True, # Suprime la salida de yt-dlp, excepto los errores
        'progress_hooks': [lambda d: print_progress(d)],
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"  📥 Buscando y descargando...")
            ydl.download([query])

    except Exception as e:
        print(f"  ❌ Error al buscar o descargar el video: {e}")

def print_progress(d):
    if d['status'] == 'downloading':
        # Obtiene el nombre del archivo que se está descargando
        filename = d.get('filename', 'archivo')
        
        # Imprime el progreso en una sola línea
        print(
            f"\r  Downloading '{filename}': {d['_percent_str']} of {d['_total_bytes_str']} at {d['_speed_str']}",
            end=''
        )
    elif d['status'] == 'finished':
        # Salto de línea final al completar la descarga
        print(f"\n  ✅ Video '{d.get('filename')}' descargado con éxito.")


def procesar_canciones_favoritas():
    """
    Lee el archivo CSV de canciones favoritas, busca cada una en YouTube y la descarga.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    archivo_csv = os.path.join(script_dir, 'favoritos.csv')
    descargas_dir = os.path.join(script_dir, 'descargas')

    # Asegurarse de que el directorio de descargas existe
    if not os.path.exists(descargas_dir):
        os.makedirs(descargas_dir)

    try:
        with open(archivo_csv, "r", newline="", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            canciones = list(lector)
            total_canciones = len(canciones)
            
            print(f"🎶 Encontradas {total_canciones} canciones en 'favoritos.csv'. Buscando y descargando desde YouTube...")

            for i, cancion in enumerate(canciones):
                nombre = cancion["nombre"]
                artista = cancion["artista"]
                
                consulta = f"{nombre} {artista} Official Video"
                
                print(f"\n({i+1}/{total_canciones}) Procesando: '{nombre}' de '{artista}'...")
                
                descargar_video(consulta, descargas_dir)
                
                # Se añade una pequeña pausa para no hacer peticiones tan seguidas
                time.sleep(1)

    except FileNotFoundError:
        print(f"🛑 Error: No se pudo encontrar el archivo '{archivo_csv}'.")
        print("Asegúrate de que el archivo 'favoritos.csv' existe en el directorio principal.")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")

if __name__ == "__main__":
    procesar_canciones_favoritas()
