from playwright.sync_api import sync_playwright
from parsel import Selector
from urllib.parse import urljoin

import pandas as pd

from time import sleep

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto('https://uk.trustpilot.com/review/www.which.co.uk')
    page.locator("//*[@id='onetrust-accept-btn-handler']").click()
    page.screenshot(full_page=True, path="test.png")

    parsed = []
    reviews = page.locator("//div[@class='styles_cardWrapper__LcCPA styles_show__HUXRb styles_reviewCard__9HxJJ']")
    for review in reviews.element_handles():
        parsed.append({
            'header':review.query_selector('h2').inner_text(),
            'text':review.query_selector('p').inner_text(),
            'date_of_experience':review.query_selector("time").inner_text(),
            'rating':review.query_selector('img').get_attribute('alt')

            })
        
        for comment in parsed:
            print(comment)

    print(parsed)

    pd.DataFrame(parsed).to_csv('test.csv')
    # sleep(5)

