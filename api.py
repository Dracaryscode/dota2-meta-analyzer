from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
import pandas as pd

app = FastAPI(title="Dota 2 API para Psicólogos")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = create_engine('postgresql://nexus@localhost:5432/dota2_meta')

@app.get("/api/rendimiento")
def obtener_rendimiento():
    # Ahora traemos TODA la información de la partida
    query = """
    SELECT * FROM matches 
    ORDER BY match_id ASC
    """
    df = pd.read_sql(query, engine)
    df = df.fillna(0) # Limpiamos los vacíos
    
    return df.to_dict(orient="records")