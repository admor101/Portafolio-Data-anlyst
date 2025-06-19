# Agente Conversacional y Automatizacion para Servicio al Cliente

Este proyecto contiene un prototipo de agente de inteligencia artificial para asistir a equipos internos de servicio al cliente. El repositorio incluye tres modulos principales:

1. **Modulo 1: Agente Conversacional basado en RAG**
   - Indexa documentos corporativos y permite consultas interactivas usando GPT-4o mini y ChromaDB.
2. **Modulo 2: Automatizacion por reconocimiento visual**
   - Captura tableros de Power BI, analiza el contenido con GPT-4o vision y ejecuta acciones condicionales.
3. **Modulo 3: Generador de descripciones de dashboards**
   - Combina capturas de pantallas y descripciones en Excel para crear resúmenes automaticos con GPT-4 Vision.

Cada modulo cuenta con un script de ejemplo en la carpeta `modules`.

## Instalacion

Crear un entorno virtual y luego instalar las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

Copiar `.env.example` a `.env` y agregar las claves necesarias (por ejemplo `OPENAI_API_KEY`).

## Ejecucion

Ejecutar cada modulo de forma independiente. Por ejemplo:

```bash
python modules/module1_rag/rag_agent.py
```

Los detalles de cada modulo se encuentran comentados en sus scripts correspondientes.
