# 🎮 Dota 2 Meta-Analyzer: Behavioral Data Pipeline

### 📌 Overview
Pipeline de **Ingeniería de Datos** que automatiza la extracción de métricas desde la API de OpenDota, realiza transformaciones analíticas para detectar fatiga cognitiva y persiste los resultados en una base de datos **PostgreSQL 14**.

### 🛠️ Tech Stack
- [cite_start]**Lenguaje:** Python 3.9+ (Pandas, SQLAlchemy) 
- [cite_start]**Base de Datos:** PostgreSQL 14 (Modelo Relacional) [cite: 13]
- [cite_start]**Análisis:** Series de tiempo (Medias Móviles) para métricas de KDA [cite: 15, 17]
- [cite_start]**Infraestructura:** Entorno virtualizado en macOS M1 

### 🧪 Análisis Avanzado
Para el **Neurolab**, el sistema implementa una **Media Móvil Simple (SMA)**:
$$SMA = \frac{KDA_t + KDA_{t-1} + \dots + KDA_{t-4}}{5}$$
[cite_start]Esto permite identificar patrones de degradación de rendimiento tras sesiones prolongadas de juego, simulando estudios de carga cognitiva[cite: 17, 21].

### 📁 Estructura del Proyecto
- `src/`: Lógica de extracción (API), transformación (Pandas) y carga (SQL).
- `sql/`: Esquemas de base de datos normalizados.
- `main.py`: Orquestador principal del flujo ETL.

---
[cite_start]*Desarrollado por Kevin Gomez - 8vo Ciclo Ingeniería de Sistemas (Ulima).* [cite: 1, 19]