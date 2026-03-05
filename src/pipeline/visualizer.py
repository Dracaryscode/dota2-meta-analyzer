import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import logging

def generate_report():
    logging.info("📈 Generando reporte visual de rendimiento...")
    try:
        engine = create_engine('postgresql://nexus@localhost:5432/dota2_meta')
        query = "SELECT hero_name, AVG(kda) as avg_kda FROM matches GROUP BY hero_name ORDER BY avg_kda DESC LIMIT 10"
        df = pd.read_sql(query, engine)

        plt.figure(figsize=(10, 6))
        plt.barh(df['hero_name'], df['avg_kda'], color='#3498db')
        plt.title('Rendimiento Técnico por Héroe (Top 10)')
        plt.xlabel('Promedio de KDA')
        plt.gca().invert_yaxis()
        
        plt.savefig('reporte_rendimiento.png')
        plt.close() # Importante: cierra el plot para no bloquear el pipeline
        logging.info("✅ Reporte 'reporte_rendimiento.png' exportado con éxito.")
        return True
    except Exception as e:
        logging.error(f"❌ Error en Visualización: {e}")
        return False