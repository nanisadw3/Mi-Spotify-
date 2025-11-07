import requests
import csv
import os

token = "BQD4rcaqo1M_jHse8J0abI_sWH4_inxWtYMaFXg4JEctGCGa2pILUJbJzPd_YqNuAVvDW6J7InzBiK5N7A9KlhZB8rMSUPN_8KTvnWOI7gowW3Hh_oSLzgaiusOfoah8ErcO6eM6rh0z4pNbsGJ2EQyWmhK1BEj5s5y9ZIC9IsYLnVQGzPny_0LN_BFZgMz-4ylkPIMkp1zIfzh-zQuEpy3ZmKABMB6urN8BT6uTgbTMISrRIjKq7CUQycR_pTlPbRn5"
url = "https://api.spotify.com/v1/me/tracks"
headers = {"Authorization": f"Bearer {token}"}

all_songs = []
limit = 50
offset = 0

while True:
    params = {"limit": limit, "offset": offset}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print("Error:", response.status_code, response.text)
        break

    data = response.json()
    items = data["items"]
    if not items:
        break

    for item in items:
        track = item["track"]
        all_songs.append(
            {
                "nombre": track["name"],
                "artista": ", ".join([a["name"] for a in track["artists"]]),
                "album": track["album"]["name"],
                "url": track["external_urls"]["spotify"],
            }
        )

    offset += limit
    if offset >= data["total"]:
        break

# Construye una ruta robusta al archivo CSV, relativa a la ubicación del script.
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'favoritos.csv')

# Guardar a CSV
with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["nombre", "artista", "album", "url"])
    writer.writeheader()
    writer.writerows(all_songs)
    f.flush()
    os.fsync(f.fileno())

print(f"✅ {len(all_songs)} canciones guardadas en 'favoritos.csv'")
