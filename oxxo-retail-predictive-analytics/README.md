# OXXO Retail Predictive Analytics

Este proyecto simula un caso de ciencia de datos para el sector retail tomando como referencia los datos de Instacart. El objetivo principal es entender y predecir el comportamiento de compra de los clientes para proponer promociones personalizadas.

## Estructura del proyecto

```
oxxo-retail-predictive-analytics/
│
├── data/                             # CSVs originales Instacart
├── notebooks/
│   ├── 01_ingesta_datos.ipynb
│   ├── 02_exploracion_analitica.ipynb
│   ├── 03_segmentacion_clientes.ipynb
│   ├── 04_modelo_recompra_clientes.ipynb
│   ├── 05_scoring_pipeline.ipynb
│
├── src/                              # Funciones de soporte Python
│   ├── features.py
│   ├── modelo.py
│
├── outputs/
│   ├── modelos_ml/
│   ├── tablas_resultado/
│
├── dashboard/                        # Power BI (opcional)
│
├── README.md                         # Explicación ejecutiva
├── requirements.txt                  # Dependencias
```

## Objetivos

1. Comprender los patrones de compra de los clientes.
2. Segmentar a los compradores según su comportamiento.
3. Predecir la probabilidad de recompra y la siguiente compra.
4. Recomendar acciones promocionales basadas en las predicciones.

## Flujo de trabajo

1. **Ingesta y limpieza**: Lectura de archivos CSV con PySpark, validación de datos y creación de tablas integradas.
2. **Exploración**: Análisis exploratorio con SQL/PySpark para detectar tendencias y clientes activos o inactivos.
3. **Segmentación**: Cálculo de métricas RFM y clustering con K-means para definir perfiles de clientes.
4. **Modelado**: Entrenamiento de un modelo de clasificación binaria para predecir la probabilidad de recompra.
5. **Scoring y Deploy**: Registro y despliegue de modelos con MLflow, así como generación de resultados en tablas.
6. **Visualización**: Creación de paneles de control (opcional) en Power BI o en las visualizaciones de Databricks.

## Indicadores de éxito

- AUC del modelo superior a 0.75.
- Al menos tres segmentos de clientes diferenciados y accionables.
- Pipeline reproducible y fácil de seguir.

## Uso rápido

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Explorar el notebook de ingesta:

```bash
jupyter notebook notebooks/01_ingesta_datos.ipynb
```

Este repositorio forma parte de un portafolio de proyectos de ciencia de datos enfocados en retail.
