import pandas as pd
import logging
import psycopg2
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()

def load_to_db():
    logging.info("🚀 Iniciando carga incremental (Upsert) en PostgreSQL...")    
    try:
        # 1. Leer el CSV generado en la fase anterior
        df = pd.read_csv('processed_matches.csv')
        # 2. Conectar a PostgreSQL (Asegúrate de que tu usuario sea 'nexus' o el de tu Mac)
        # Estructura: postgresql://usuario:password@localhost:5432/nombre_db
        engine = create_engine('postgresql://nexus@localhost:5432/dota2_meta')
        
        # Carga a tabla temporal y Upsert manual
        with engine.begin() as conn:
            df.to_sql('temp_matches', conn, if_exists='replace', index=False) # Carga a tabla temporal
            #SQL para insertar solo lo que no existe (evita duplicados)
            upsert_query = """
                INSERT INTO matches (match_id, hero_name, kills, deaths, assists, kda, duration, radiant_win, kda_rolling_avg)
                SELECT match_id, hero_name, kills, deaths, assists, kda, duration, radiant_win, kda_rolling_avg 
                FROM temp_matches
                ON CONFLICT (match_id) DO NOTHING;
                    """
            conn.execute(text(upsert_query))
            conn.execute(text("DROP TABLE temp_matches;"))
        logging.info("✅ Carga finalizada: Base de datos actualizada sin duplicados.")
        return True
    except Exception as e:
        logging.error(f"❌ Error al cargar en DB: {e}")
        return False
if __name__ == "__main__":
    load_to_db()