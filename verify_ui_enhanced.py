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

        await page.wait_for_function('document.getElementById("statusText").innerText === "Connected to backend"')

        # Check if stop button has title
        stop_btn_title = await page.get_attribute('#stopBtn', 'title')
        print(f"Stop button title: {stop_btn_title}")

        # Click Export Data and capture loading state
        await page.click('#exportBtn')
        # We need to be fast or the mock backend responds immediately.
        # Since it is local, it might be very fast.
        await page.screenshot(path='/home/jules/verification/export_loading.png')

        # Check labels in settings
        await page.click('#tab-settings')
        scan_label_for = await page.get_attribute('label[for="scanInterval"]', 'for')
        backend_label_for = await page.get_attribute('label[for="backendUrl"]', 'for')
        print(f"Scan label for: {scan_label_for}")
        print(f"Backend label for: {backend_label_for}")

        await page.screenshot(path='/home/jules/verification/settings_labels.png')

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
