# Extended from the BigDataStack Docker course

- [Dockerized Developement Environment](https://bigdatastack.dev/profesion/ingenieria-datos/entrenamiento/docker/proyecto-entorno-completo)

## Add-Ons to be implemented

1. UV package management
    - Create virtualenv
    - Modify Dockerfile to use uv virtualenv
2. Modularization (pipeline.py script to src/)
```bash
    └── src/
        ├── __init__.py
        ├── config.py             # rutas, variables de entorno
        ├── extract.py            # lectura de raw / fuentes
        ├── transform.py          # limpieza y validación
        ├── load.py               # carga a PostgreSQL u otra DB
        └── pipeline.py           # orquesta extract → transform → load
```
3. CookieCutter directory structure implementation
```bash
.
├── README.md
├── Makefile                  # atajos: make up, make etl, make test
├── pyproject.toml
├── requirements.txt          # (estaba escrito "requiriments.txt")
├── .env.example              # credenciales de DB, sin secretos reales
├── .gitignore
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── init-db/
│   └── schema.sql
├── data/
│   ├── raw/                  # inmutable
│   │   └── ventas_raw.csv
│   ├── interim/              # datos limpios intermedios
│   └── processed/            # listo para cargar a DB o modelar
├── notebooks/                # exploración (EDA)
├── tests/
│   └── test_pipeline.py
└── src/
```
4. Make commands