# web crawler
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# web scraper


import time


s = Service(ChromeDriverManager().install())

options = webdriver.ChromeOptions()
options.add_argument('window-size=1920,1080')
# options.add_argument("headless")

driver = webdriver.Chrome(service=s,
                          options=options)
driver.implicitly_wait(5)

driver.get(url="https://services.healthtech.dtu.dk/service.php?SignalP-4.1")
assert "SignalP" in driver.title


iframe = driver.find_element(By.ID, "servicetabs-1")
driver.switch_to.frame(iframe)


text_box = driver.find_element(By.NAME, "SEQPASTE")
# need to input sequence variable
seq = 'MWVRQVPWSF TWAVLQLSWQ SGWLLEVPNG PWRSLTFYPA WLTVSEGANA TFTCSLSNWS EDLMLNWNRL SPSNQTEKQA AFCNGLSQPV QDARFQIIQL PNRHDFHMNI LDTRRNDSGI YLCGAISLHP KAKIEESPGA ELVVTERILE TSTRYPSPSP KPEGRFQGMV IGIMSALVGI PVLLLLAWAL AVFCSTSMSE ARGAGSKDDT LKEEPSAAPV PSVAYEELDF QGREKTPELP TACVHTEYAT IVFTEGLGAS AMGRRGSADG LQGPRPPRHE DGHCSWPL'
seq.strip()
text_box.send_keys(seq)
driver.switch_to.default_content()

driver.execute_script("window.scrollTo(0, 800)")

driver.switch_to.frame(iframe)
driver.find_element(By.XPATH, "/html/body/form/table[2]/tbody/tr[3]/td[1]/input[3]").click()
driver.find_element(By.XPATH, "/html/body/form/p[5]/input[1]").click()
driver.switch_to.default_content()

address = driver.current_url

print(type(address))

driver.quit()
