# 🎮 Dota 2 Meta-Analyzer: High-Performance ETL Pipeline

### 📌 Overview
Este proyecto es un pipeline de **Ingeniería de Datos (ETL)** diseñado para extraer, transformar y analizar métricas de rendimiento en entornos competitivos de alta carga de datos. El sistema automatiza el consumo de APIs, normaliza estructuras complejas y persiste la información en una base de datos relacional para análisis avanzado de tendencias.



### 🛠️ Tech Stack
* **Lenguaje:** Python 3.9+ (Pandas, SQLAlchemy, Requests)
* **Base de Datos:** PostgreSQL 14 (Modelo Relacional Normalizado)
* **Análisis:** Series de tiempo mediante Medias Móviles (SMA)
* **Infraestructura:** Entorno virtualizado (venv) en arquitectura Apple Silicon M1

### 🧪 Análisis Técnico: Media Móvil (SMA)
El sistema implementa una **Media Móvil Simple** sobre la métrica de KDA para identificar la estabilidad del rendimiento y detectar picos o degradaciones tras sesiones prolongadas:

$$SMA = \frac{KDA_t + KDA_{t-1} + \dots + KDA_{t-4}}{5}$$

### 📁 Estructura del Proyecto
* `src/`: Módulos de extracción (API), transformación (Data Cleaning) y carga (SQL).
* `sql/`: Scripts de definición de esquemas (DDL).
* `main.py`: Orquestador central del flujo ETL.

---
*Desarrollado por Kevin Gomez - Estudiante de Ingeniería de Sistemas (Ulima).*