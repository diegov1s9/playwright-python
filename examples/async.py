import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        # Ejecuta el navegador en modo no headless (visualizar el navegador).
        # browser = await p.chromium.launch(headless=False)
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        # Navegar a una página
        await page.goto('https://playwright.dev/')
        
        # Tomar una captura de pantalla
        await page.screenshot(path='screenshots/example.png')
        
        # Cerrar el navegador
        await browser.close()

asyncio.run(main())