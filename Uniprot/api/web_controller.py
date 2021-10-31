# web crawler
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# web scraper
from bs4 import BeautifulSoup

import time


class SignalP_controller:

    def __init__(self):
        self.chrome_service = Service(ChromeDriverManager().install())
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('window-size=1920,1080')
        self.options.add_argument('headless')
        # window size 설정: 'window-size=1920,1080'
        # background 실행: 'headless'
        self.driver = webdriver.Chrome(service=self.chrome_service, options=self.options)
        self.driver.implicitly_wait(5)

    def site_enter(self, get_url):
        self.driver.get(url=get_url)

    def input_seq(self, sequence):
        # iframe 위치 찾기
        self.iframe = self.driver.find_element(By.ID, "servicetabs-1")

        # 찾은 위치로 진입하고 sequence를 입력할 textarea 찾기
        self.driver.switch_to.frame(self.iframe)
        self.sequence_box = self.driver.find_element(By.NAME, "SEQPASTE")
        self.sequence_box.send_keys(sequence)

        # cookies 방해 받지 않게 scroll down
        self.driver.switch_to.default_content()
        self.driver.execute_script("window.scrollTo(0, 800)")

        # 다시 iframe으로 진입 후 button click으로 다음 페이지로 이동
        self.driver.switch_to.frame(self.iframe)
        self.driver.find_element(By.XPATH, "/html/body/form/table[2]/tbody/tr[3]/td[1]/input[3]").click()
        self.driver.find_element(By.XPATH, "/html/body/form/p[5]/input[1]").click()

        time.sleep(1)

        while True:
            time.sleep(1)
            html = self.driver.page_source
            soup = BeautifulSoup(html, "html.parser")
            html_text = soup.select('body p')[0].text

            start_num = html_text.find("1")
            end_num = html_text.find("#", start_num)
            html_text = html_text[start_num:end_num]

            if html_text != '':
                break

        return html_text

    def back_and_clear(self):
        self.driver.back()
        # time.sleep(3)
        self.driver.switch_to.frame(self.iframe)
        self.sequence_box = self.driver.find_element(By.NAME, "SEQPASTE")
        self.sequence_box.clear()
        self.driver.switch_to.default_content()
        self.driver.execute_script("window.scrollTo(0, 0)")

    def finish(self):
        self.driver.quit()