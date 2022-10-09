from playwright.sync_api import sync_playwright
from parsel import Selector
from urllib.parse import urljoin

import pandas as pd

from time import sleep

with sync_playwright() as p:
    # initialise browser instance
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()


    # go to page, accept cookies, take screenshot
    page.goto('https://uk.trustpilot.com/review/www.which.co.uk')
    page.locator("//*[@id='onetrust-accept-btn-handler']").click()
    page.screenshot(full_page=True, path="test.png")

    # Next Page element
    next_page = page.query_selector("//div[@class='styles_pagination__6VmQv']//a[@aria-label='Next page']/span").inner_text()

    parsed = []
    df_list = []
    while next_page:
        reviews = page.locator("//div[@class='styles_cardWrapper__LcCPA styles_show__HUXRb styles_reviewCard__9HxJJ']")
        for review in reviews.element_handles():
            parsed.append({
                'header':review.query_selector('h2').inner_text(),
                'text':review.query_selector('p').inner_text(),
                'date_of_experience':review.query_selector("time").inner_text(),
                'rating':review.query_selector('img').get_attribute('alt')

                })
        if next_page:
            page.locator("//div[@class='styles_pagination__6VmQv']//a[@aria-label='Next page']/span").click()
        else:
            pass
            
        for comment in parsed:
            print(comment)
df = pd.DataFrame(parsed)
print(df)
    # # print(parsed)
    
    #     df_list.append(parsed)
    #     # print(df_list)
    # for i in df_list:
    #     df_i = pd.DataFrame(i)
    #     print(df_i)
    # # sleep(5)

