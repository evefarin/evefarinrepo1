from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



serv_obj = Service("C:\drivers\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Electronics").click()
#links=driver.find_elements(By.TAG_NAME, "a")
links=driver.find_elements(By.XPATH, "//a")
print("No. of links", len(links))


for link in links:
    print(link.text)