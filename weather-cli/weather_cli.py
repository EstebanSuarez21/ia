#!/usr/bin/env python3
"""
Weather CLI - Script para consultar el clima actual de cualquier ciudad.

Este módulo proporciona una interfaz de línea de comandos simple para obtener
información del clima actual usando la API de OpenWeatherMap. Soporta ciudades
con caracteres especiales y maneja errores comunes de forma elegante.

El script requiere una API key de OpenWeatherMap configurada como variable de
entorno y muestra la información en un formato claro y legible.

Ejemplo de uso:
    $ ./weather_cli.py
    Ingresa el nombre de la ciudad: Madrid
    Ciudad: Madrid
    Temperatura: 22°C
    Clima: Soleado

Requisitos:
    - API key de OpenWeatherMap en archivo .env
    - Conexión a internet
    - Python 3.10+

Author: Weather CLI Team
Created: November 12, 2025
License: MIT
"""
import os
import sys
import requests
from dotenv import load_dotenv

# URL base de la API de OpenWeatherMap para consultas del clima actual
API_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_api_key():
    """
    Obtiene y valida la API key de OpenWeatherMap desde variables de entorno.

    Lee la variable OPENWEATHER_API_KEY del archivo .env y verifica que exista.
    Si no se encuentra la API key, termina el programa con un mensaje de error.

    Returns:
        str: API key válida de OpenWeatherMap.

    Raises:
        SystemExit: Si la API key no está configurada en las variables de entorno.

    Example:
        >>> api_key = get_api_key()
        >>> print(len(api_key))  # Debería mostrar ~32 caracteres
        32

    Note:
        Esta función termina el programa si no encuentra la API key, por lo que
        no es necesario manejar el caso de retorno None.
    """
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        print("[ERROR] Falta la API key. Define OPENWEATHER_API_KEY en tu archivo .env.")
        sys.exit(1)
    return api_key


def get_city():
    """
    Solicita al usuario ingresar el nombre de una ciudad por consola.

    Muestra un prompt pidiendo al usuario que ingrese el nombre de la ciudad
    y valida que no esté vacío. Soporta nombres con caracteres especiales
    y acentos (ej: "São Paulo", "México").

    Returns:
        str: Nombre de la ciudad ingresado por el usuario, sin espacios extra.

    Raises:
        SystemExit: Si el usuario ingresa una cadena vacía o solo espacios.

    Example:
        >>> # Simular entrada del usuario "Madrid"
        >>> city = get_city()  # Usuario escribe "Madrid"
        >>> print(city)
        Madrid

    Note:
        La función aplica .strip() para remover espacios al inicio y final,
        pero preserva espacios internos en nombres como "Buenos Aires".
    """
    city = input("Ingresa el nombre de la ciudad: ").strip()
    if not city:
        print("[ERROR] Debes ingresar un nombre de ciudad.")
        sys.exit(1)
    return city


def fetch_weather(city, api_key):
    """
    Consulta el clima actual de una ciudad usando la API de OpenWeatherMap.

    Realiza una petición HTTP GET a la API de OpenWeatherMap para obtener
    los datos meteorológicos actuales de la ciudad especificada. Maneja
    diferentes tipos de errores de forma específica.

    Args:
        city (str): Nombre de la ciudad a consultar. Puede contener
            caracteres especiales y acentos. Ejemplos: "Madrid",
            "São Paulo", "México".
        api_key (str): API key válida de OpenWeatherMap para
            autenticación.

    Returns:
        dict: Datos JSON del clima actual con estructura de OpenWeatherMap,
            incluyendo temperatura, humedad, descripción, etc.

    Raises:
        SystemExit: En los siguientes casos:
            - API key inválida o no autorizada (401)
            - Ciudad no encontrada (404)
            - Error de red o timeout
            - Cualquier otro error HTTP

    Example:
        >>> data = fetch_weather("Madrid", "tu_api_key")
        >>> print(data['name'])
        Madrid
        >>> print(data['main']['temp'])
        22.5

    Note:
        La función usa timeout=10 segundos para evitar bloqueos indefinidos.
        Los parámetros 'units=metric' y 'lang=es' están configurados para
        obtener temperaturas en Celsius y descripciones en español.
    """
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
        "lang": "es"
    }
    try:
        response = requests.get(API_URL, params=params, timeout=10)
        # Verificar errores específicos de la API de OpenWeatherMap
        if response.status_code == 401:
            print("[ERROR] API key inválida o no autorizada.")
            sys.exit(1)
        if response.status_code == 404:
            print(f"[ERROR] Ciudad '{city}' no encontrada.")
            sys.exit(1)
        # Lanzar excepción para otros códigos de error HTTP (500, 503, etc.)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Error de red o conexión: {e}")
        sys.exit(1)


def print_weather(data):
    """
    Formatea e imprime la información del clima en un formato legible.

    Extrae los datos relevantes del JSON de respuesta de OpenWeatherMap
    y los presenta en el formato específico requerido: Ciudad, Temperatura
    en Celsius y descripción del clima con la primera letra en mayúscula.

    Args:
        data (dict): Diccionario JSON con los datos del clima obtenidos
            de la API de OpenWeatherMap. Debe contener las claves 'name',
            'main' (con 'temp') y 'weather' (lista con 'description').

    Returns:
        None: Imprime directamente en la consola, no retorna ningún valor.

    Example:
        >>> weather_data = {
        ...     "name": "Madrid",
        ...     "main": {"temp": 22.5},
        ...     "weather": [{"description": "soleado"}]
        ... }
        >>> print_weather(weather_data)
        Ciudad: Madrid
        Temperatura: 22.5°C
        Clima: Soleado

    Note:
        La función usa .get() con valores por defecto ("-") para evitar
        errores si faltan claves en la respuesta de la API. La descripción
        del clima se capitaliza para mejor presentación.
    """
    city = data.get("name", "-")
    temp = data.get("main", {}).get("temp", "-")
    weather = data.get("weather", [{}])[0].get("description", "-")
    # Formato de salida específico requerido
    print(f"Ciudad: {city}")
    print(f"Temperatura: {temp}°C")
    print(f"Clima: {weather.capitalize()}")


def main():
    """
    Función principal que coordina la ejecución completa del programa.

    Orquesta el flujo completo de la aplicación:
    1. Carga las variables de entorno desde el archivo .env
    2. Obtiene y valida la API key de OpenWeatherMap
    3. Solicita al usuario el nombre de la ciudad
    4. Realiza la consulta a la API del clima
    5. Muestra los resultados en formato legible

    El programa puede terminar en cualquier paso si hay errores (API key
    faltante, ciudad no encontrada, problemas de red, etc.).

    Returns:
        None: Función de coordinación que no retorna valores.

    Raises:
        SystemExit: Puede terminar el programa por diversos errores:
            - API key no configurada
            - Entrada vacía del usuario
            - Ciudad no encontrada
            - API key inválida
            - Problemas de conexión a internet

    Example:
        $ python weather_cli.py
        Ingresa el nombre de la ciudad: Barcelona
        Ciudad: Barcelona
        Temperatura: 18°C
        Clima: Nublado

    Note:
        Esta función actúa como punto de entrada principal cuando el script
        se ejecuta directamente. No requiere parámetros y maneja todos
        los errores terminando el programa con mensajes explicativos.
    """
    load_dotenv()
    api_key = get_api_key()
    city = get_city()
    data = fetch_weather(city, api_key)
    print_weather(data)


if __name__ == "__main__":
    main()
