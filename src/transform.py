

from datetime import datetime

def clean_rows(fila: dict):
    """Limpia y valida una fila. Retorna None si no es válida"""

    # Validar cantidad
    try:
        cantidad = int(fila['cantidad'])

        if cantidad < 0:
            print(f"  [AVISO]  Fila {fila['id']}: cantidad inválida ({cantidad})")
            return None
    except (ValueError, TypeError):
        print(f"  [AVISO]  Fila {fila['id']}: cantidad vacía o no numérica")
        return None
    
    # Validar cliente
    cliente = fila.get('cliente', '').strip() or 'Desconocido'

    # Normalizar fecha (soportar YYYY-MM-DD y DD/MM/YYYY)
    fecha_raw = fila['fecha'].strip()

    try:
        formato_fecha = '%d/%m/%Y' if '/' in fecha_raw else '%Y-%m-%d'
        fecha = datetime.strptime(fecha_raw, formato_fecha)
    except ValueError:
        print(f"  [AVISO]  Fila {fila['id']}: fecha inválida ({fecha_raw})")
        return None

    # Validat precio
    try:
        precio = float(fila['precio_unitario'])

        if precio <= 0:
            print(f"  [AVISO]  Fila {fila['id']}: precio inválido ({precio})")
            return None
    except (ValueError, TypeError):
        print(f"  [AVISO]  Fila {fila['id']}: precio vacío o no numérico")
        return None
    
    total = cantidad  * precio

    return {
        "producto": fila['producto'].strip(),
        'cantidad': cantidad,
        'precio_unitario': precio,
        'total': round(total, 2),
        'fecha': fecha,
        'cliente': cliente,
        'ciudad': fila['ciudad'].strip()
    }