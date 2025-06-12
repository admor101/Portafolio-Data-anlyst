# Portafolio-Data-anlyst

Este repositorio contiene proyectos de ejemplo para un portafolio como data analyst.

## Proyecto: Agricultural Exports Scraper

Este proyecto descarga un conjunto de datos de exportaciones agrícolas de un repositorio público, 
realiza un análisis sencillo y genera un gráfico con los estados con mayor nivel de exportaciones.

### Requisitos

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

### Ejecución

```bash
python scripts/ag_exports_pipeline.py
```

Al ejecutarse se descargará el CSV original en `data/ag_exports.csv` y se creará una imagen `data/top10_total_exports.png` con los 10 estados con mayor nivel de exportaciones.
