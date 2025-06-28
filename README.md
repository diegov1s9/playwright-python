# Playwright Python QA

## Descripción

Este proyecto tiene como objetivo automatizar pruebas para aplicaciones web utilizando Playwright con Python. 
Permite verificar el correcto funcionamiento de la aplicación, asegurando que los casos de uso principales estén cubiertos por pruebas automatizadas.

## Instalación

1. Asegúrate de tener Python instalado.
2. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/playwright-python.git
   cd playwright-python
   ```
3. Instala las dependencias del proyecto:
   ```bash
   pip install -r requirements.txt
   ```
   Esto instalará `pytest-playwright`, `playwright`, `pytest` y cualquier otra dependencia necesaria.
4. Instala los navegadores requeridos por Playwright:
   ```bash
   playwright install
   ```

## Uso

Ejecuta los tests con:
```bash
pytest
```
O usando Playwright directamente:
```bash
playwright test
```

## Estructura del Proyecto

- `/tests`: Contiene los casos de prueba automatizados.
- `/pages`: Page Objects para la automatización.
- `requirements.txt`: Dependencias del proyecto.
- `README.md`: Este archivo.

## Contribución

1. Haz un fork del repositorio.
2. Crea una rama para tu feature o fix.
3. Haz tus cambios y realiza un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Plugins recomendados

Para mejorar la experiencia de desarrollo, se recomienda instalar los siguientes plugins en tu editor (por ejemplo, VSCode):

- **Playwright Test for VSCode**: Facilita la ejecución y depuración de tests Playwright desde el editor.
- **Python** (Microsoft): Soporte para desarrollo en Python y ejecución de pruebas con pytest.