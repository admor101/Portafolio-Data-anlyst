"""Genera descripciones de dashboards usando GPT-4 Vision."""

from pathlib import Path
import base64

import pandas as pd
import openai
from PIL import Image
from dotenv import load_dotenv


def image_to_base64(path: Path) -> str:
    with open(path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")
    return encoded


def summarize(row) -> str:
    image_b64 = image_to_base64(Path(row["imagen"]))
    prompt = f"Resumen del dashboard: {row['descripcion']}"
    response = openai.ChatCompletion.create(
        model="gpt-4-vision-preview",
        messages=[
            {"role": "user", "content": [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": f"data:image/png;base64,{image_b64}"},
            ]}
        ],
    )
    return response.choices[0].message["content"]


def main():
    load_dotenv()
    df = pd.read_excel("dashboards.xlsx")
    df["resumen"] = df.apply(summarize, axis=1)
    df.to_excel("dashboards_con_resumen.xlsx", index=False)


if __name__ == "__main__":
    main()
