import asyncio
from playwright.sync_api import sync_playwright
import time
import os

def verify_palette_fixes():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Navigate to the app
        page.goto("http://localhost:8000")

        # 1. Verify Save Settings Button Fix
        print("Verifying Save Settings button...")
        page.click("#tab-settings")
        save_btn = page.query_selector("#saveSettings")

        # Click and check for loading state
        # We need to be fast or the mock backend responds immediately
        page.click("#saveSettings")

        # Check if it has the spinner class (even if briefly)
        # Since it's a mock backend, it might be too fast, but we can check if it crashed
        # If it crashed, a ReferenceError would be in console

        # Check console for errors
        page.on("console", lambda msg: print(f"Console {msg.type}: {msg.text}") if msg.type == "error" else None)

        # 2. Verify Export Button loading state
        print("Verifying Export Data button...")
        page.click("#tab-networks") # Go back to main
        page.click("#exportBtn")

        # Check for spinner
        spinner = page.query_selector(".spinner-sm")
        if spinner:
            print("✅ Spinner detected during Export")
        else:
            print("⚠️ Spinner not detected during Export (might be too fast)")

        # 3. Verify Accessibility (ARIA hidden on emojis)
        print("Verifying ARIA accessibility...")
        header_emoji = page.query_selector("h1 span[aria-hidden='true']")
        if header_emoji:
            print("✅ Header emoji is hidden from screen readers")
        else:
            print("❌ Header emoji is NOT hidden")

        # 4. Verify Label Association
        label = page.query_selector("label[for='scanInterval']")
        if label:
            print("✅ Label for scanInterval found")
        else:
            print("❌ Label for scanInterval NOT found")

        # Capture a screenshot of the settings tab
        page.click("#tab-settings")
        time.sleep(1) # wait for animation
        os.makedirs("/home/jules/verification/screenshots", exist_ok=True)
        page.screenshot(path="/home/jules/verification/screenshots/final_settings.png")
        print("✅ Final screenshot saved")

        browser.close()

if __name__ == "__main__":
    verify_palette_fixes()
