"""Funciones para ingeniería de features del proyecto OXXO."""

from pyspark.sql import DataFrame
from pyspark.sql import functions as F

def agregar_features_basicos(df: DataFrame) -> DataFrame:
    """Ejemplo de función para crear columnas adicionales."""
    return df.withColumn('es_fin_de_semana', F.dayofweek('order_dow').isin([6,7]))
