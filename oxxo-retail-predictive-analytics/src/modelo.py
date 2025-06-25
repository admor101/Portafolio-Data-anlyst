"""Entrenamiento de modelos de probabilidad de recompra."""

from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import VectorAssembler
from pyspark.sql import DataFrame

def entrenar_modelo(df: DataFrame, features: list, label: str = 'recompra'):
    assembler = VectorAssembler(inputCols=features, outputCol='features')
    datos = assembler.transform(df)
    lr = LogisticRegression(featuresCol='features', labelCol=label)
    modelo = lr.fit(datos)
    return modelo
