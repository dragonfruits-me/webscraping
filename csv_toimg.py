#インポート
import os
from time import sleep

import pandas as pd
import requests

#画像格納先フォルダ
IMAGE_DIR = "./img/"

#csvファイルの読み込み
df = pd.read_csv("image_urls_dragonfruits.csv")

#画像格納先フォルダ（img）が存在するかどうかの処理。存在しない場合、新たに作成。
if os.path.isdir(IMAGE_DIR):
    print("既に存在します。")
else:
    os.makedirs(IMAGE_DIR)

#画像の保存
for filename, yahoo_img_url in zip(df.filename, df.yahoo_img_url):
   image = requests.get(yahoo_img_url)
   with open(IMAGE_DIR + filename + ".jpg", "wb") as f:
        f.write(image.content)
   
   sleep(2)
