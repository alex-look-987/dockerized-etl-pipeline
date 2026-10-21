import os, psycopg2, time

def wait_db(max_intentos=10):
    """Espera que PostgreSQL esté listo antes de conectar."""

    for intento in range(max_intentos):
        try:
            conn = psycopg2.connect(
                host=os.getenv("DB_HOST", "postgres"),
                port=5432,
                user=os.getenv("DB_USER", "etl_user"),
                password=os.getenv("DB_PASS", "etl_secreto"),
                database=os.getenv("DB_NAME", "ventas")
            )

            conn.close()

            print(f"[OK] PostgreSQL listo (intento {intento + 1})")

            return True
        except psycopg2.OperationalError:
            print(f"⏳ Esperando PostgreSQL... (intento {intento + 1})")
            time.sleep(2)
    raise Exception("[ERROR] PostgreSQL no respondió después de varios intentos")


def load_to_db(filas_limpias):
    """Insertar las filas limpias en PostgreSQL."""

    conn = psycopg2.connect(
        host=os.getenv("DB_HOST", "postgres"),
        port=5432,
        user=os.getenv("DB_USER", "etl_user"),
        password=os.getenv("DB_PASS", "etl_secreto"),
        database=os.getenv("DB_NAME", "ventas")
    )
    
    cursor = conn.cursor()

    for fila in filas_limpias:
        cursor.execute("""
            INSERT INTO ventas_limpias
            (producto, cantidad, precio_unitario, total, fecha, cliente, ciudad)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, 
        (
            fila['producto'], fila['cantidad'], fila['precio_unitario'],
            fila['total'], fila['fecha'], fila['cliente'], fila['ciudad']
        ))

    conn.commit()
    cursor.close()
    conn.close()

    return len(filas_limpias)

