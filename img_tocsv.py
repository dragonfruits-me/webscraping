from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd


chrome_path = r"C:\Users\Takekawa Takumi\2022725hayatasu\chromedriver.exe"


driver = webdriver.Chrome(chrome_path)

url ="https://search.yahoo.co.jp/image"
driver.get(url)

sleep(3)

query="プログラミング"

# search_box = driver.find_element_by_class_name("SearchBox__searchInput")
# search_box = driver.find_element_by_class("SearchBox__searchInput")
search_box = driver.find_element(By.CLASS_NAME,"SearchBox__searchInput")
search_box.send_keys(query)
search_box.submit()



sleep(3)
height = 1000


while height < 3000:
    driver.execute_script("window.scrollTo(0,{});".format(height))
    height += 100
    sleep(1)

elements = driver.find_elements(By.CLASS_NAME,"sw-Thumbnail--tile")

d_list = []

for i, element in enumerate(elements, start=1):
    name=f"{query}_{i}"
    yahoo_img_url = element.find_element(By.TAG_NAME,"img").get_attribute("src")
    raw_url = element.find_element(By.CLASS_NAME,"sw-ThumbnailGrid__details").get_attribute("href")
    title = element.find_element(By.TAG_NAME,"img").get_attribute("alt") 

    d={
        "filenqame": name,
        "raw_url": raw_url,
        "yahoo_img_url": yahoo_img_url,
        "title": title
    }

    d_list.append(d)
    sleep(2)


df = pd.DataFrame(d_list)
df.to_csv("image_urls_2018.csv")

driver.quit()