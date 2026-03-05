import requests
import json
import os
from dotenv import load_dotenv
import logging
import os

# Cargar variables de entorno (Estándar de Seguridad)
load_dotenv()
PLAYER_ID = os.getenv("PLAYER_ID")

def fetch_dota_data():
    if not PLAYER_ID:
        logging.info("❌ Error: No se encontró PLAYER_ID en el archivo .env")
        return False # Retorna False para indicar fallo en la extracción

    url = f"https://api.opendota.com/api/players/{PLAYER_ID}/matches?limit=50"
    
    logging.info(f"📡 Conectando con OpenDota para el jugador {PLAYER_ID}...")
    
    try:
        # Petición a la API
        response = requests.get(url, timeout=10)
        response.raise_for_status() # Lanza error si la respuesta es fallida
        
        matches = response.json()
        
        # Guardar el entregable de la Fase 1
        with open('raw_matches.json', 'w') as f:
            json.dump(matches, f, indent=4)
            
        logging.info(f"✅ Fase 1 Completada: Se generó 'raw_matches.json' con {len(matches)} partidas.")
        return True # Retorna True para indicar éxito en la extracción
    
    except requests.exceptions.RequestException as e:
        logging.error(f"❌ Error durante la implementación (Fase 1): {e}")
        return False # Retorna False para indicar fallo en la extracción
if __name__ == "__main__":
    fetch_dota_data()