import asyncio
from playwright.async_api import async_playwright
import os

async def run():
    if not os.path.exists('/home/jules/verification'):
        os.makedirs('/home/jules/verification')

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('http://localhost:8000')

        # Wait for connection (checking for text in #statusText)
        await page.wait_for_function('document.getElementById("statusText").innerText === "Connected to backend"')

        # Capture initial state
        await page.screenshot(path='/home/jules/verification/initial.png')

        # Click on Settings tab
        await page.click('#tab-settings')
        await asyncio.sleep(0.5) # Wait for fade animation
        await page.screenshot(path='/home/jules/verification/settings.png')

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
