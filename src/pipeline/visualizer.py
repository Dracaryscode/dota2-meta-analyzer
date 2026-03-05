import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

def generate_report():
    print("📈 Extrayendo datos de SQL para el reporte...")
    # Conexión nativa a tu base de datos local
    engine = create_engine('postgresql://nexus@localhost:5432/dota2_meta')
    
    # Query de agregación: Rendimiento por Héroe
    query = """
    SELECT hero_name, AVG(kda) as avg_kda, COUNT(*) as games_played
    FROM matches 
    GROUP BY hero_name 
    HAVING COUNT(*) >= 1
    ORDER BY avg_kda DESC 
    LIMIT 10
    """
    df = pd.read_sql(query, engine)

    # Crear el gráfico de barras horizontales
    plt.figure(figsize=(12, 7))
    bars = plt.barh(df['hero_name'], df['avg_kda'], color='#3498db')
    plt.xlabel('Promedio de KDA (Kills + Assists / Deaths)')
    plt.title('Top 10 Héroes con Mejor Rendimiento Cognitivo/Técnico')
    plt.gca().invert_yaxis() # Los mejores arriba
    
    # Añadir etiquetas de valor en las barras
    for bar in bars:
        plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2, 
                 f'{bar.get_width():.2f}', va='center')

    plt.tight_layout()
    plt.savefig('reporte_rendimiento.png')
    print("✅ Gráfico 'reporte_rendimiento.png' generado. ¡Listo para la reunión!")
    plt.show()

if __name__ == "__main__":
    generate_report()