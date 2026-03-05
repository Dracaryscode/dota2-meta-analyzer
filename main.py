import sys
from src.pipeline.extractor import fetch_dota_data
from src.pipeline.transformer import process_matches
from src.pipeline.loader import load_to_db
from src.pipeline.visualizer import generate_report

def run_pipeline():
    print("🚀 Iniciando Pipeline de Ingeniería de Datos...")
    
    # 1. Extracción
    if not fetch_dota_data():
        print("❌ Error en Extracción. Abortando pipeline.")
        sys.exit(1)
        
    # 2. Transformación
    if not process_matches():
        print("❌ Error en Transformación. Abortando pipeline.")
        sys.exit(1)
        
    # 3. Carga
    load_to_db()
    
    # 4. Visualización
    generate_report()
    
    print("✅ Pipeline ejecutado con éxito de extremo a extremo.")

if __name__ == "__main__":
    run_pipeline()