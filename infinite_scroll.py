from playwright.sync_api import sync_playwright
from time import sleep

# url = "https://www.tui.co.uk/destinations/packages?airports%5B%5D=LCY%7CLGW%7CLHR%7CLTN%7CSEN%7CSTN%7CABZ%7CBHD%7CBFS%7CBHX%7CBOH%7CBRS%7CEXT%7CEDI%7CEMA%7CCWL%7CDSA%7CGLA%7CHUY%7CINV%7CLBA%7CLPL%7CMAN%7CNCL%7CNWI%7CSOU%7CMME&units%5B%5D=000207%3AREGION%7CFRA%3ACOUNTRY%7CGRC%3ACOUNTRY%7CITA%3ACOUNTRY%7CPRT%3ACOUNTRY%7CESP%3ACOUNTRY&when=27-05-2023&until=&flexibility=true&monthSearch=false&flexibleDays=3&flexibleMonths=&noOfAdults=2&noOfChildren=0&childrenAge=&duration=7115&searchRequestType=ins&searchType=search&sp=true&multiSelect=true&room=&isVilla=false&reqType=&sortBy=&nearByAirports=true"
url = "https://www.tui.co.uk/destinations/packages?airports%5B%5D=SOU&units%5B%5D=JEY%3ACOUNTRY&when=27-05-2023&until=&flexibility=true&monthSearch=false&flexibleDays=3&flexibleMonths=&noOfAdults=2&noOfChildren=0&childrenAge=&duration=3115&searchRequestType=ins&searchType=search&sp=true&multiSelect=true&room=&isVilla=false&reqType=&sortBy=&nearByAirports=true#2b7bf5f285e0aab7bde34521a5c11f791e4e1fb3"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(url=url)

    page.locator("//div[@class='cmButtons']/button[@id='cmCloseBanner']").click()

    page.mouse.wheel(0,500)
    
    page.wait_for_selector("//div[@class='prime-for-push-modal-footer']/button").click()
    page.reload()

    page_reload = page.locator("//div[@class='UI__loadMoreResults']/div/img[@class='UI__preloader']")
    end_pagination = page.locator("//div[@class='UI__loadMoreResults']/span[@class='UI__noMoreHolidays']")

    parsed = []
    while page_reload: 
        try:
            # if  page_reload:
            holidays = page.locator("//div[@class='ResultListItemV2__packageInfo']")
            for holiday in holidays.element_handles():
                parsed.append({
                    'holiday_name':holiday.query_selector('h5').inner_text(),
                    'location':holiday.query_selector('p').inner_text(),
                    # 'room_details':holiday.query_selector('.room details').inner_text()

                })

            page.locator("//div[@class='UI__loadMoreResults']").click()
            page.mouse.wheel(0,100)
            sleep(0.5)
            
            # else:
            #     print(parsed)
            #     break 
            
            if page.locator("//div[@class='UI__loadMoreResults']/span[@class='UI__noMoreHolidays']"):
                print('success')
                continue

        except:
            print (page.locator("//div[@class='UI__loadMoreResults']/span[@class='UI__noMoreHolidays']").inner_text())

            print(parsed)
            break
        

# print(str(page.query_selector(".UI__noMoreHolidays").inner_text()) == "No more holidays to show")
    sleep(5)

# try: grab total number from first page, divide by 10 and slap it into a for loop
# for i in range(0, n):

