# Changelog

Todos los cambios notables de este proyecto se documentan en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
y este proyecto sigue [Versionado Semántico](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Agregado
- Documentación completa con docstrings detallados
- README.md profesional con guías paso a paso
- Ejemplos de uso con ciudades internacionales
- Sección de troubleshooting en documentación

### Mejorado
- Comentarios explicativos en código complejo
- Documentación de API y parámetros
- Formato de presentación de resultados

## [1.0.0] - 2025-11-12

### Agregado
- **Funcionalidad inicial**: Script CLI para consultar clima actual
- **Soporte OpenWeatherMap**: Integración con API de OpenWeatherMap
- **Configuración segura**: Variables de entorno para API key (.env)
- **Manejo de errores**: Validación de API key, ciudad no encontrada, errores de red
- **Caracteres especiales**: Soporte para ciudades con acentos y espacios
- **Formato específico**: Salida en formato "Ciudad: X / Temperatura: Y°C / Clima: Z"
- **Tests automáticos**: Suite completa con pytest y requests-mock
  - Test para endpoint válido
  - Test para ciudad inexistente
  - Test para errores de red simulados
  - Test para validación de API key
  - Test para validación de entrada del usuario
- **Linting**: Configuración flake8 para calidad de código
- **Ejecutable Unix**: Shebang para ejecución directa en Linux/macOS
- **Documentación base**: README.md con instrucciones básicas

### Características técnicas
- **Python**: Soporte para Python 3.10.12+
- **Dependencias**: requests, python-dotenv, pytest, requests-mock, flake8
- **Timeout**: Configuración de 10 segundos para requests HTTP
- **Idioma**: Respuestas en español (lang=es)
- **Unidades**: Temperaturas en Celsius (units=metric)
- **Validación**: Input no vacío y API key requerida

### Estructura del proyecto
- `weather_cli.py`: Script principal ejecutable
- `requirements.txt`: Gestión de dependencias
- `test_weather_cli.py`: Tests automáticos completos
- `.env.example`: Template de configuración
- `.gitignore`: Archivos ignorados (incluye .env)
- `README.md`: Documentación de usuario

### Decisiones de diseño
- **Salida inmediata**: El script termina en caso de error (sys.exit)
- **Validación previa**: API key se verifica antes de solicitar ciudad
- **Formato fijo**: Salida consistente independiente de la respuesta de API
- **URLs encoding**: Soporte automático para caracteres especiales en nombres