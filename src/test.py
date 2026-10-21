from pathlib import Path
from extract import read_csv

def main():
    print("""
Hello from dockerized-etl-pipeline!
You're testing the main.py from src/ for the Dockerfile image!

The intended purpose of this function its to test src.extract "read_csv" function
""")


if __name__ == "__main__":
    main()
    
    # EXTRACT
    print("\nExtrayendo datos del CSV...")
    BASE_DIR = Path(__file__).resolve().parent.parent # raíz de mi-pipeline-docker/

    ruta_datos_raw = BASE_DIR / "data" / "raw" / "ventas_raw.csv"

    print(ruta_datos_raw)

    datos_crudos = read_csv(ruta_datos_raw)
    print(f"   Filas leídas: {len(datos_crudos)}")