# from get_moke_email import mokeEmails # ['den@bell-face.com', 'shouitsu@bell-face.com', 'denshouitsu@bell-face.com']


import requests
import re
import time

email_list = []


class PostApi(object):
    def __init__(self):
        self.url = "http://tool.chacuo.net/mailverify"
        self.headers = {
                    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
                    'accept': "*/*",
                    'accept-encoding': "gzip, deflate",
                    'cookie': "__cfduid=d047079299edcbac2362a05a51724b3d11562738434; bdshare_firstime=1562738454047; BAIDU_SSP_lcr=http://www.baidu.com/link?url=tgJFlKi8NzummevHmKAaNpwPQrf_XLESlNZZ8F96GDqBOEfY9TKchIaYVhRkWmRm&wd=&eqid=a5a801c600011a87000000065d355c38; Hm_lvt_ef483ae9c0f4f800aefdf407e35a21b3=1562738452,1563778246; Hm_lpvt_ef483ae9c0f4f800aefdf407e35a21b3=1563778569",
                    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
                    'referer': "http://tool.chacuo.net/mailverify",
                    'pragma': "no-cache",
                    'origin': "http://tool.chacuo.net",
                    'host': "tool.chacuo.net",
                    'cache-control': "no-cache",
                    'postman-token': "9eb5aae4-614c-da3b-9e67-05e1ed864f82"
                    }

    def send(self, email):
        payload = f"------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"data\"\r\n\r\n{email}\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"type\"\r\n\r\nverify\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"arg\"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        response = requests.post(self.url, verify=False, data=payload, headers=self.headers)
        ans = response.json()
        dr = re.compile(r'<[^>]+>', re.S)
        ans = str(ans["data"])
        ans = dr.sub("", ans)
        ans = ans[2:6]
        if ans == "验证成功":
            ans = "メールアドレス存在します"
        else:
            ans = "メールアドレス存在しません"
        nowTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return {"date": nowTime, "name": email, "address": ans}


if __name__ == "__main__":
    pass
    # for email in mokeEmails:
    #     p = PostApi()
    #     ans = p.send(email)
    #     email_list.append(ans)
    #     time.sleep(5)
    # print(email_list)































# import asyncio
#
# from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# ans_list = []
# import time
# import os
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
#
#
# class SearchEmail(object):
#     def __init__(self):
#         # desired_capabilities = DesiredCapabilities.CHROME  # 修改页面加载策略
#         # desired_capabilities["pageLoadStrategy"] = "none"
#         self.driverPath = os.path.abspath(os.path.join(os.getcwd()))+"/chromedriver"
#         self.options = webdriver.ChromeOptions()
#         prefs = {"profile.managed_default_content_settings.images": 2}
#         self.options.add_experimental_option("prefs", prefs)
#         # # headlessで動かすために必要なオプション
#         # self.options.add_argument("--headless")
#         # self.options.add_argument("--disable-gpu")
#         # self.options.add_argument("--window-size=1280x1696")
#         # self.options.add_argument("--disable-application-cache")
#         # self.options.add_argument("--disable-infobars")
#         # self.options.add_argument("--no-sandbox")
#         # self.options.add_argument("--hide-scrollbars")
#         # self.options.add_argument("--enable-logging")
#         # self.options.add_argument("--log-level=0")
#         # self.options.add_argument("--single-process")
#         # self.options.add_argument("--ignore-certificate-errors")
#         # self.options.add_argument("--homedir=/tmp")
#         self.driver = webdriver.Chrome(executable_path=self.driverPath, chrome_options=self.options)
#
#     def search(self):
#         self.driver.get("http://tool.chacuo.net/mailverify")
#         WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='converts']")))
#         inputE = self.driver.find_element_by_id("converts")
#         inputE.send_keys("306581901111d.com")
#         wait = WebDriverWait(self.driver, 10)
#         wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='检测邮箱真实性']")))
#         btn = self.driver.find_element_by_xpath("//input[@value='检测邮箱真实性']")
#         btn.click()
#         time.sleep(10)
#         wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='convertd']/h3")))
#         ans = self.driver.find_element_by_xpath("//*[@id='convertd']/h3").text
#         self.driver.quit()
#         print(ans)
#
#
# if __name__ == "__main__":
#     g = SearchEmail()
#     g.search()
#
#         # self.task_content = []
# # from pyppeteer import launch
# # for email in mokeEmails:
# #     async def main():
# #         browser = await launch({'headless': False, 'args': ['--no-sandbox'], 'dumpio': True})
# #         page = await browser.newPage()
# #         await page.setUserAgent(
# #             'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
# #             ' (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299')
# #         await page.goto("http://tool.chacuo.net/mailverify", timeout=100000)
# #         await asyncio.sleep(3)
# #         await page.type('input#converts', email)
# #         await page.click("input.inline-block")
# #         await asyncio.sleep(10)
# #         text = await page.xpath("//*[@id='convertd']/h3")
# #         ans = await (await text[0].getProperty("textContent")).jsonValue()
# #         await browser.close()
# #         print(ans)
# #         if ans == "验证成功！":
# #             ans = "メール見つかりました"
# #         else:
# #             ans = "メール存在しません"
# #         return {"email": email, "status": ans}
# #     loop = asyncio.get_event_loop()
# #     task = asyncio.ensure_future(main())
# #     loop.run_until_complete(task)
# #
# #     ans_list.append(task.result())
# # print(ans_list)
#
