# Weather CLI 🌤️

Script de línea de comandos en Python para consultar el clima actual de cualquier ciudad del mundo usando la API de OpenWeatherMap.

## � Descripción

Weather CLI es una herramienta simple y eficiente que permite obtener información meteorológica actualizada de cualquier ciudad mediante la consola. El script está diseñado para ser fácil de usar, robusto en el manejo de errores y soporta ciudades con caracteres especiales y acentos.

**Características principales:**
- 🌍 Soporte para ciudades internacionales con caracteres especiales
- 🌡️ Temperatura mostrada en grados Celsius
- 📝 Formato de salida claro y consistente
- ⚠️ Manejo robusto de errores (ciudad no encontrada, problemas de red, API key inválida)
- 🔐 Configuración segura de API key mediante variables de entorno
- ✅ Tests automáticos incluidos
- 🚀 Ejecutable directo con shebang para sistemas Unix

## 🛠️ Características

- ✨ **Interfaz CLI simple**: Solo ingresa el nombre de la ciudad
- 🚀 **Respuesta rápida**: Consulta directa a OpenWeatherMap API
- 📦 **Sin dependencias pesadas**: Usa solo librerías estándar + requests
- 🔍 **Búsqueda inteligente**: Soporta "São Paulo", "México", "New York"
- 🌡️ **Información clara**: Ciudad, temperatura y descripción del clima
- ⚡ **Validación previa**: Verifica API key antes de hacer consultas
- 🛡️ **Manejo de errores**: Mensajes claros para cada tipo de problema
- 📊 **Testing completo**: Suite de tests automáticos con pytest

## 📋 Requisitos Previos

- **Python**: 3.10.12 o superior
- **API Key**: Cuenta gratuita en [OpenWeatherMap](https://openweathermap.org/api)
- **Internet**: Conexión activa para consultas a la API
- **Sistema**: Linux, macOS o Windows con Python

## 🚀 Instalación

### Paso 1: Clonar el proyecto
```bash
git clone <repository-url>
cd weather-cli
```

### Paso 2: Instalar dependencias
```bash
pip install -r requirements.txt
```

### Paso 3: Configurar API key
```bash
# Copiar archivo de ejemplo
cp .env.example .env

# Editar .env y agregar tu API key
# OPENWEATHER_API_KEY=tu_api_key_de_openweathermap
```

### Paso 4: Hacer ejecutable (Linux/macOS)
```bash
chmod +x weather_cli.py
```

## 🔑 Configuración de API Key

1. **Crear cuenta gratuita:**
   - Ve a [OpenWeatherMap](https://openweathermap.org/api)
   - Regístrate con tu email
   - Confirma tu cuenta

2. **Obtener API Key:**
   - Inicia sesión en tu cuenta
   - Ve a "API Keys" en tu dashboard
   - Copia tu API key (32 caracteres alfanuméricos)

3. **Configurar en .env:**
   ```bash
   OPENWEATHER_API_KEY=abc123def456ghi789jkl012mno345pq
   ```

**⚠️ Importante:**
- Nunca hardcodees la API key en el código
- Mantén tu archivo `.env` privado (ya está en .gitignore)
- La API gratuita permite 1,000 consultas/mes

## 🖥️ Uso

### Ejecución básica
```bash
./weather_cli.py
```

### Ejemplo de uso completo
```bash
$ ./weather_cli.py
Ingresa el nombre de la ciudad: Madrid
Ciudad: Madrid
Temperatura: 22°C
Clima: Soleado
```

### Ejemplos con ciudades internacionales
```bash
# Ciudad con acentos
$ ./weather_cli.py
Ingresa el nombre de la ciudad: São Paulo
Ciudad: São Paulo
Temperatura: 28°C
Clima: Parcialmente nublado

# Ciudad con espacios
$ ./weather_cli.py
Ingresa el nombre de la ciudad: Buenos Aires
Ciudad: Buenos Aires
Temperatura: 15°C
Clima: Lluvia ligera

# Ciudad con caracteres especiales
$ ./weather_cli.py
Ingresa el nombre de la ciudad: München
Ciudad: Munich
Temperatura: 8°C
Clima: Nublado
```

## 🧪 Testing

### Ejecutar todos los tests
```bash
pytest
```

### Ejecutar con información detallada
```bash
pytest -v
```

### Ver cobertura de tests
```bash
pytest --cov=weather_cli
```

### Tests incluidos
- ✅ **Validación de API key**: Presencia y manejo de ausencia
- ✅ **Consulta exitosa**: Ciudad válida con respuesta correcta
- ✅ **Ciudad no encontrada**: Manejo de error 404
- ✅ **API key inválida**: Manejo de error 401
- ✅ **Errores de red**: Timeout y problemas de conexión
- ✅ **Formato de salida**: Verificación del formato correcto
- ✅ **Validación de entrada**: Input vacío o solo espacios

## 📝 Linting y Calidad de Código

### Verificar estilo con flake8
```bash
flake8 weather_cli.py test_weather_cli.py
```

### Configuración de calidad
- **Estándar**: PEP 8 (Python)
- **Linter**: flake8
- **Docstrings**: Formato Google/NumPy
- **Comentarios**: Explicaciones claras y necesarias

## 🔧 Estructura del Proyecto

```
weather-cli/
├── weather_cli.py          # Script principal ejecutable
├── .env.example           # Template para configuración
├── .env                   # Tu configuración (no versionado)
├── requirements.txt       # Dependencias del proyecto
├── test_weather_cli.py    # Tests automáticos
├── README.md              # Documentación (este archivo)
└── .gitignore             # Archivos ignorados por git
```

## 🌐 API de OpenWeatherMap

### Endpoint utilizado
```
GET https://api.openweathermap.org/data/2.5/weather
```

### Parámetros de consulta
- `q`: Nombre de la ciudad (ej: "Madrid", "São Paulo")
- `appid`: Tu API key de OpenWeatherMap
- `units=metric`: Temperatura en Celsius
- `lang=es`: Descripción en español

### Ejemplo de respuesta
```json
{
  "name": "Madrid",
  "main": {
    "temp": 22.5,
    "humidity": 65
  },
  "weather": [
    {
      "description": "soleado"
    }
  ]
}
```

## ⚠️ Solución de Problemas

### Error: "Falta la API key"
```bash
[ERROR] Falta la API key. Define OPENWEATHER_API_KEY en tu archivo .env.
```
**Solución:**
1. Verifica que existe el archivo `.env`
2. Asegúrate de que contiene `OPENWEATHER_API_KEY=tu_api_key`
3. Reinicia el script

### Error: "API key inválida"
```bash
[ERROR] API key inválida o no autorizada.
```
**Solución:**
1. Verifica que copiaste correctamente la API key
2. Asegúrate de que tu cuenta en OpenWeatherMap esté activada
3. Espera unos minutos (las API keys nuevas pueden tardar en activarse)

### Error: "Ciudad no encontrada"
```bash
[ERROR] Ciudad 'CiudadInventada' no encontrada.
```
**Solución:**
1. Verifica la ortografía del nombre de la ciudad
2. Prueba con el nombre en inglés: "Madrid" vs "Madrid"
3. Para ciudades pequeñas, incluye el país: "Springfield, US"

### Error: "Error de red o conexión"
```bash
[ERROR] Error de red o conexión: ConnectionTimeout
```
**Solución:**
1. Verifica tu conexión a internet
2. Revisa que no haya firewall bloqueando el acceso
3. Espera un momento y vuelve a intentar

### Error: "Permission denied" (Linux/macOS)
```bash
bash: ./weather_cli.py: Permission denied
```
**Solución:**
```bash
chmod +x weather_cli.py
```

## 🛠️ Tecnologías Utilizadas

- **[Python 3.10+](https://python.org)** - Lenguaje de programación principal
- **[requests](https://docs.python-requests.org/)** - Cliente HTTP para consumir API
- **[python-dotenv](https://pypi.org/project/python-dotenv/)** - Gestión de variables de entorno
- **[pytest](https://pytest.org/)** - Framework de testing
- **[requests-mock](https://pypi.org/project/requests-mock/)** - Mocking para tests HTTP
- **[flake8](https://flake8.pycqa.org/)** - Linter para calidad de código
- **[OpenWeatherMap API](https://openweathermap.org/api)** - Servicio de datos meteorológicos

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## 👥 Contribuir

1. **Fork** el proyecto
2. Crea una **rama feature** (`git checkout -b feature/nueva-funcionalidad`)
3. **Commit** tus cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. **Push** a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un **Pull Request**

### Pautas de contribución
- Mantén el código simple y legible
- Agrega tests para nueva funcionalidad
- Asegúrate de que todos los tests pasen
- Sigue el estilo PEP 8
- Actualiza la documentación si es necesario

## 📞 Soporte y Contacto

- **Issues**: Reporta bugs en [GitHub Issues]
- **Documentación**: Lee este README y los comentarios en el código
- **API**: Consulta [OpenWeatherMap Docs](https://openweathermap.org/api)

---

**¡Disfruta consultando el clima desde tu terminal! 🌦️**
