"""Ejemplo de automatizacion condicional usando GPT-4o vision."""

import base64
from io import BytesIO
from pathlib import Path

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import openai


def capture_dashboard(url: str) -> bytes:
    """Abre la URL con Selenium y devuelve una captura de pantalla en bytes."""
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        png = driver.get_screenshot_as_png()
        return png
    finally:
        driver.quit()


def analyze_image(image_bytes: bytes, prompt: str) -> str:
    """Envía la imagen a GPT-4o vision y devuelve la respuesta."""
    encoded = base64.b64encode(image_bytes).decode("utf-8")
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": f"data:image/png;base64,{encoded}"},
            ]}
        ],
    )
    return response.choices[0].message["content"]


def main():
    load_dotenv()
    dashboard_url = "https://example.com/powerbi"
    screenshot = capture_dashboard(dashboard_url)
    result = analyze_image(screenshot, "Describe el estado del tablero y si hay agentes sin grupo")
    print(result)


if __name__ == "__main__":
    main()
