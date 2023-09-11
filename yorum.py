from selenium import webdriver
from selenium.webdriver.common.by import By

service = webdriver.chrome.service.Service('./chromedriver.exe')
service.start()
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get('https://www.baristeksin.com.tr')
yazi = driver.find_element(By.ID,'main').find_element(By.TAG_NAME,'h2').click()

yorum_metni = "Merhaba bu bir bot yorumudur."
epostaniz = "iletisim@baristeksin.com.tr"
isim = "Barış Teksin"
site = "https://www.baristeksin.com.tr"
driver.find_element(By.ID,'comment').send_keys(yorum_metni)
driver.find_element(By.ID,'author').send_keys(isim)
driver.find_element(By.ID,'email').send_keys(epostaniz)
driver.find_element(By.ID,'url').send_keys(site)
driver.find_element(By.ID,'submit').click()

input("Çıkmak için bir tuşa basın...")