import pandas as pd
import requests
import json

def process_matches():
    print("🔄 Iniciando el procesamiento de datos de partidas...")

    try:
        # Cargar el archivo JSON generado en la Fase 1
        with open('raw_matches.json', 'r') as f:
            data = json.load(f)
        
        # Crear un DataFrame a partir de los datos de las partidas
        df = pd.DataFrame(data)
        
        # Seleccionar columnas relevantes para el análisis
        columns = ['match_id', 'hero_id', 'player_slot', 'radiant_win', 'duration', 
                   'kills', 'deaths', 'assists']
        df = df[columns]

        # 3. Mapeo de Héroes (RF2) - Consumir constantes de la API
        print("🎭 Obteniendo nombres de héroes...")
        heroes_resp = requests.get("https://api.opendota.com/api/constants/heroes")
        heroes_dict = heroes_resp.json()
        
        # Crear un mapa {id: nombre}
        heroes_map = {int(k): v['localized_name'] for k, v in heroes_dict.items()}
        
        # Aplicar el mapeo
        df['hero_name'] = df['hero_id'].map(heroes_map)
        
        # 4. Cálculo de métrica básica (KDA Ratio)
        df['kda'] = (df['kills'] + df['assists']) / df['deaths'].replace(0, 1)

        # 2. ANÁLISIS DE FATIGA: Media Móvil (SMA) [cite: 5, 15]
        # Esto calcula el promedio de KDA de las últimas 5 partidas en orden cronológico.
        # Es fundamental que las partidas estén ordenadas por match_id (tiempo).
        df = df.sort_values('match_id') 
        df['kda_rolling_avg'] = df['kda'].rolling(window=5).mean()
        
        # 3. IDENTIFICACIÓN DE OUTLIERS (Rendimiento excepcional)
        # Marcamos partidas donde el KDA fue el doble que tu promedio móvil.
        df['is_peak_performance'] = df['kda'] > (df['kda_rolling_avg'] * 2)
        
        print("\n📊 Resumen de las últimas partidas:")
        print(df[['match_id', 'hero_name', 'kills', 'deaths', 'kda']].head())
        
        # Guardar para la Fase 3 (SQL)
        df.to_csv('processed_matches.csv', index=False)
        print("\n✅ Archivo 'processed_matches.csv' generado para carga en DB.")

    except Exception as e:
        print(f"❌ Error en el procesamiento: {e}")

if __name__ == "__main__":
    process_matches()