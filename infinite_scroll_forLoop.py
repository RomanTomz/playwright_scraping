from playwright.sync_api import sync_playwright
from time import sleep
import time
from math import ceil
import pandas as pd


start = time.time()

# url = "https://www.tui.co.uk/destinations/packages?airports%5B%5D=LCY%7CLGW%7CLHR%7CLTN%7CSEN%7CSTN%7CABZ%7CBHD%7CBFS%7CBHX%7CBOH%7CBRS%7CEXT%7CEDI%7CEMA%7CCWL%7CDSA%7CGLA%7CHUY%7CINV%7CLBA%7CLPL%7CMAN%7CNCL%7CNWI%7CSOU%7CMME&units%5B%5D=000207%3AREGION%7CFRA%3ACOUNTRY%7CGRC%3ACOUNTRY%7CITA%3ACOUNTRY%7CPRT%3ACOUNTRY%7CESP%3ACOUNTRY&when=27-05-2023&until=&flexibility=true&monthSearch=false&flexibleDays=3&flexibleMonths=&noOfAdults=2&noOfChildren=0&childrenAge=&duration=7115&searchRequestType=ins&searchType=search&sp=true&multiSelect=true&room=&isVilla=false&reqType=&sortBy=&nearByAirports=true"
url = "https://www.tui.co.uk/destinations/packages?airports%5B%5D=SOU%7CGLA%7CLGW&units%5B%5D=ITA%3ACOUNTRY%7CJEY%3ACOUNTRY%7CUSA%3ACOUNTRY&when=27-05-2023&until=&flexibility=true&monthSearch=false&flexibleDays=3&flexibleMonths=&noOfAdults=2&noOfChildren=0&childrenAge=&duration=7115&searchRequestType=ins&searchType=search&sp=true&multiSelect=true&room=&isVilla=false&reqType=&sortBy=&nearByAirports=true"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(url=url)

    page.locator("//div[@class='cmButtons']/button[@id='cmCloseBanner']").click()

    page.mouse.wheel(0,500)
    
    page.wait_for_selector("//div[@class='prime-for-push-modal-footer']/button").click()
    page.reload()

    pages = ceil(float(page.locator("//div[@class='holidayCount']/div/span").inner_text())/10)


    parsed = []
    for i in range(1, pages+1):
            # if  page_reload:
            holidays = page.locator("//div[@class='ResultListItemV2__packageInfo']")
            for holiday in holidays.element_handles():
                if holiday.query_selector('h5').inner_text() not in parsed:
                    parsed.append({
                        'holiday_name':holiday.query_selector('h5').inner_text(),
                        'location':holiday.query_selector('p').inner_text(),
                        # 'room_details':holiday.query_selector('.room details').inner_text()

                    })
                else:
                    continue
                    

            page.locator("//div[@class='UI__loadMoreResults']").click()
            sleep(1)

            page.mouse.wheel(0,100)
end = time.time()

print((end - start)/60)
print(len(parsed))
pd.DataFrame(parsed).to_csv('tui_test.csv')            


        

# print(str(page.query_selector(".UI__noMoreHolidays").inner_text()) == "No more holidays to show")

# try: grab total number from first page, divide by 10 and slap it into a for loop
# for i in range(0, n):

