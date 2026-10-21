# Archivo: etl/pipeline.py
"""Mini pipeline ETL: CSV -> limpieza -> PostgreSQL"""

from pathlib import Path
from src.extract import read_csv
from src.transform import clean_rows
from src.load import load_to_db, wait_db

if __name__ == '__main__':
    print("=" * 50)
    print("Pipeline ETL iniciado")
    print("=" * 50)

    wait_db()

    # EXTRACT
    print("\nExtrayendo datos del CSV...")
    BASE_DIR = Path(__file__).resolve().parent.parent # raíz de mi-pipeline-docker/

    ruta_datos_raw = BASE_DIR / "data" /  "ventas_raw.csv"
    datos_crudos = read_csv(ruta_datos_raw)
    print(f"   Filas leídas: {len(datos_crudos)}")

    # TRANSFORM
    print("\nLimpiando y transformando...")
    datos_limpios = []

    for fila in datos_crudos:
        limpia = clean_rows(fila)

        if limpia:
            datos_limpios.append(limpia)

    print(f"   Filas válidas: {len(datos_limpios)}/{len(datos_crudos)}")
            
    # LOAD
    print("\nCargando en PostgreSQL...")
    insertadas = load_to_db(datos_limpios)
    print(f"   Filas insertadas: {insertadas}")

    print("\n[OK] Pipeline completado exitosamente!")
    print("=" * 50)
