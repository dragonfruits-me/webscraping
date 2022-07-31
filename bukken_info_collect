#インポート
from time import sleep
from bs4 import BeautifulSoup
import requests
import pandas as pd

#物件情報を格納するリストを用意
d_list = []

#1～2ページの物件情報を取得
for i in range(1,3):
    
    #スクレイピング先のurlへリクエストを投げる
    url = "https://suumo.jp/chintai/tokyo/sc_shinjuku/?page={}"
    target_url = url.format(i) 
    res = requests.get(target_url)
    
    sleep(1)
    
    #BeautifulSouppオブジェクトを生成し、物件情報の要素一覧を取得
    soup = BeautifulSoup(res.text)
    contents = soup.find_all("div",class_="cassetteitem")

    #一つ一つの物件情報のキー情報を取得する
    for content in contents:
        detail = content.find("div",class_="cassetteitem-detail")
        table= content.find("table",class_="cassetteitem_other")
        title = detail.find("div", class_="cassetteitem_content-title").text
        address = detail.find("li", class_="cassetteitem_detail-col1").text
        access = detail.find("li", class_="cassetteitem_detail-col2").text
        age = detail.find("li", class_="cassetteitem_detail-col3").text

        #一つ一つの物件の細かいプラン情報を取得する
        tr_tags = table.find_all("tr",class_="js-cassette_link")
        for tr_tag in tr_tags:
            floor, price, first_fee, capacity = tr_tag.find_all("td")[2:6]
            fee, management_fee = price.find_all("li")
            deposit, gratuity = first_fee.find_all("li")
            madori, menseki = capacity.find_all("li")

            #辞書に物件情報を格納する
            d = {
                "title":title,
                "address":address,
                "access":access,
                "age":age,
                "floor":floor.text,
                "fee":fee.text,
                "management_fee":management_fee.text,
                "deposit":deposit.text,
                "gratuity":gratuity.text,
                "madori":madori.text,
                "menseki":menseki.text
            }

             #辞書の情報をリストに追加
            d_list.append(d)

 #物件情報をcsvファイルに出力する準備をして、出力
df = pd.DataFrame(d_list)
df.to_csv("bukken_info.csv",index=None,encoding="utf-8-sig")
