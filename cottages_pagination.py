from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.cottages.com/search?sort=priceasc&page=1&adult=2&child=0&infant=0&pets=0&nights=7&range=3&accommodationType=cottages&start=13-02-2023&regionId=21667&regionName=England&destinationURL=%2Fengland")

    