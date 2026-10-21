import csv

def read_csv(filepath):
    """Leer el CSV crudo."""
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        return list(reader)
