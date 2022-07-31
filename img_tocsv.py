#インポート
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

#chromedriverのパスを指定
chrome_path = r"C:\Users\Takekawa Takumi\chromedriver.exe"

driver = webdriver.Chrome(chrome_path)

#yahoom画像検索画面のパスを指定
url ="https://search.yahoo.co.jp/image"
driver.get(url)

sleep(3)

#検索キーワードとして「ドラゴンフルーツ」を指定
query="ドラゴンフルーツ"

#yahoom画像検索画面の検索バーにキーワードを入力して、送信する
search_box = driver.find_element(By.CLASS_NAME,"SearchBox__searchInput")
search_box.send_keys(query)
search_box.submit()

sleep(3)

#検索結果画面でのスクロールの高さを指定
height = 1000

#スクロールが3000を超えるまで、スクロール値に100を追加する
while height < 3000:
    driver.execute_script("window.scrollTo(0,{});".format(height))
    height += 100
    sleep(1)

#検索結果画面にある要素を複数指定
elements = driver.find_elements(By.CLASS_NAME,"sw-Thumbnail--tile")

d_list = []

#画像のsrc属性、href属性、alt属性をそれぞれ取得して、辞書dに格納するのをループで回す。その際nameはファイル名用に格納。
for i, element in enumerate(elements, start=1):
    name=f"{query}_{i}"
    yahoo_img_url = element.find_element(By.TAG_NAME,"img").get_attribute("src")
    raw_url = element.find_element(By.CLASS_NAME,"sw-ThumbnailGrid__details").get_attribute("href")
    title = element.find_element(By.TAG_NAME,"img").get_attribute("alt") 

    d={
        "filename": name,
        "raw_url": raw_url,
        "yahoo_img_url": yahoo_img_url,
        "title": title
    }

    d_list.append(d)
    sleep(2)

#配列d_listをcsvファイルに出力する準備をしてから、出力
df = pd.DataFrame(d_list)
df.to_csv("image_urls_dragonfruits.csv")

#webdriverを閉じる
driver.quit()
