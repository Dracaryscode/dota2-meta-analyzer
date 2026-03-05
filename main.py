import sys
from src.pipeline.extractor import fetch_dota_data
from src.pipeline.transformer import process_matches
from src.pipeline.loader import load_to_db
from src.pipeline.visualizer import generate_report
import logging
import os

# Crear carpeta de logs si no existe
os.makedirs('logs', exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - [%(filename)s] - %(message)s',
    handlers=[
        logging.FileHandler("logs/pipeline.log"), # Guarda en archivo
        logging.StreamHandler()                  # Muestra en consola (como el logging.info)
    ]
)

def run_pipeline():
    logging.info("🚀 Iniciando Pipeline de Ingeniería de Datos...")
    
    try:
        # 1. Extracción
        if not fetch_dota_data():
            logging.error("❌ Error en Extracción. Abortando.")
            sys.exit(1)
            
        # 2. Transformación
        if not process_matches():
            logging.error("❌ Error en Transformación. Abortando.")
            sys.exit(1)
            
        # 3. Carga (AHORA CON VALIDACIÓN)
        if not load_to_db():
            logging.error("❌ Error en Carga a DB. El reporte no será preciso.")
            sys.exit(1) # Esto detiene el proceso aquí
        
        # 4. Visualización
        generate_report()
        
        logging.info("✅ Pipeline ejecutado con éxito de extremo a extremo.")

    except Exception as e:
        logging.critical(f"💥 Fallo crítico: {e}")
        sys.exit(1)
        
if __name__ == "__main__":
    run_pipeline()