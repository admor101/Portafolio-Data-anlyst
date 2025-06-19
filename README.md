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

## Proyecto: Agente Conversacional y Automatización para Servicio al Cliente

En la carpeta `AgenteServicioCliente` se encuentra un prototipo de agente de inteligencia artificial que combina capacidades de RAG, visión artificial y automatización condicional. El proyecto está dividido en tres módulos independientes:

1. Agente conversacional basado en RAG (`module1_rag`)
2. Automatización por reconocimiento visual (`module2_dashboard_auto`)
3. Generador de descripciones de dashboards (`module3_description`)

Consulte el archivo `AgenteServicioCliente/README.md` para más detalles de instalación y uso.
