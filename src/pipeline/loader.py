import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

def load_to_db():
    print("🚀 Cargando datos a PostgreSQL...")
    
    try:
        # 1. Leer el CSV generado en la fase anterior
        df = pd.read_csv('processed_matches.csv')
        
        # 2. Conectar a PostgreSQL (Asegúrate de que tu usuario sea 'nexus' o el de tu Mac)
        # Estructura: postgresql://usuario:password@localhost:5432/nombre_db
        engine = create_engine('postgresql://nexus@localhost:5432/dota2_meta')
        
        # 3. Carga incremental (Sustituir por 'append' si quieres acumular datos)
        df.to_sql('matches', engine, if_exists='replace', index=False)
        
        print("✅ ¡Datos persistidos en la tabla 'matches' exitosamente!")

    except Exception as e:
        print(f"❌ Error al cargar en DB: {e}")

if __name__ == "__main__":
    load_to_db()