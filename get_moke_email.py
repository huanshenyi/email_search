from get_info import GetInfo
from pyppeteer import launch
import asyncio


async def main(firstname, lastname, domin):
        browser = await launch()
        page = await browser.newPage()
        await page.setUserAgent(
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            ' (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299')
        await page.goto("http://metricsparrow.com/toolkit/email-permutator/")
        await page.type('input#firstName', firstname)
        await page.type('input#lastName', lastname)
        await page.type('input#domain1', domin)
        await page.click('button#permutateBtn')
        await asyncio.sleep(2)
        textarea = await page.xpath("//textarea[@id='finalResult']")
        emailList = await (await textarea[0].getProperty("textContent")).jsonValue()
        await browser.close()
        return emailList

firstname, lastname, domin = GetInfo.info()
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(main(firstname, lastname, domin))
loop.run_until_complete(task)
mokeEmails = task.result()
mokeEmails = mokeEmails.split("\n")
mokeEmails = [x.strip() for x in mokeEmails]
mokeEmails = [x for x in mokeEmails if x != '']


if __name__ == "__main__":
    firstname, lastname, domin = GetInfo.info()
    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(main(firstname, lastname, domin))
    loop.run_until_complete(task)
    mokeEmails = task.result()
    mokeEmails = mokeEmails.split("\n")
    mokeEmails = [x.strip() for x in mokeEmails]
    mokeEmails = [x for x in mokeEmails if x != '']
