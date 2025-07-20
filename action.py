import asyncio
import re
from playwright.async_api import async_playwright

# Seeds provided in the problem
SEED_INPUT = """
Seed 16
Seed 17
Seed 18
Seed 19
Seed 20
Seed 21
Seed 22
Seed 23
Seed 24
Seed 25
"""

SEEDS = re.findall(r"\d+", SEED_INPUT)
BASE_URL = "https://sanand0.github.io/tdsdata/js_table/?seed={}"

async def main():
    total_sum = 0
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        for seed in SEEDS:
            url = BASE_URL.format(seed)
            await page.goto(url)
            print(f"Scraping: {url}")

            # Get all table cells
            cells = await page.locator("table td").all_inner_texts()
            for val in cells:
                try:
                    total_sum += float(val.strip())
                except ValueError:
                    continue

        await browser.close()

    print(f"\nTotal Sum: {total_sum:.2f}")

if __name__ == "__main__":
    asyncio.run(main())
