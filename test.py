# from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import sqlite3
import math
import time

import mysql.connector

# tokyo_url = "https://house.goo.ne.jp/buy/la/result.html?la=shuto&ma=tokyo&lc%5B%5D=13101&lc%5B%5D=13102&lc%5B%5D=13103&lc%5B%5D=13105&lc%5B%5D=13106&lc%5B%5D=13107&lc%5B%5D=13108&lc%5B%5D=13118&lc%5B%5D=13121&lc%5B%5D=13122&lc%5B%5D=13123&lc%5B%5D=13109&lc%5B%5D=13110&lc%5B%5D=13111&lc%5B%5D=13112&lc%5B%5D=13113&lc%5B%5D=13104&lc%5B%5D=13114&lc%5B%5D=13115&lc%5B%5D=13116&lc%5B%5D=13117&lc%5B%5D=13119&lc%5B%5D=13120&lc%5B%5D=13201&lc%5B%5D=13202&lc%5B%5D=13203&lc%5B%5D=13204&lc%5B%5D=13205&lc%5B%5D=13206&lc%5B%5D=13207&lc%5B%5D=13208&lc%5B%5D=13209&lc%5B%5D=13210&lc%5B%5D=13211&lc%5B%5D=13212&lc%5B%5D=13213&lc%5B%5D=13214&lc%5B%5D=13215&lc%5B%5D=13218&lc%5B%5D=13219&lc%5B%5D=13220&lc%5B%5D=13221&lc%5B%5D=13222&lc%5B%5D=13223&lc%5B%5D=13224&lc%5B%5D=13225&lc%5B%5D=13227&lc%5B%5D=13228&lc%5B%5D=13229&lc%5B%5D=13303&lc%5B%5D=13305&lc%5B%5D=13308&lc%5B%5D=13361&lc%5B%5D=13401&ps=80"




# # for i in range()
# tokyo_res = requests.get(tokyo_url)

# tokyo_soup = BeautifulSoup(tokyo_res.content, "html.parser")



# # すべての物件数
# all_bukken_tag = tokyo_soup.select_one(".pageing_noall .txt_red")

# print(all_bukken_tag.contents[0].replace(",", ""))

# all_bukken = all_bukken_tag.contents[0].replace(",", "")


# # ページの数
# all_page = math.ceil(int(all_bukken) / 80)
# print(all_page)

# # 1ページの最大
# onepage_all = 80

# for i in range(all_page):
    
#     tokyo_url = f"https://house.goo.ne.jp/buy/la/result.html?p={i + 1}&la=shuto&ma=tokyo&lc%5B%5D=13101&lc%5B%5D=13102&lc%5B%5D=13103&lc%5B%5D=13105&lc%5B%5D=13106&lc%5B%5D=13107&lc%5B%5D=13108&lc%5B%5D=13118&lc%5B%5D=13121&lc%5B%5D=13122&lc%5B%5D=13123&lc%5B%5D=13109&lc%5B%5D=13110&lc%5B%5D=13111&lc%5B%5D=13112&lc%5B%5D=13113&lc%5B%5D=13104&lc%5B%5D=13114&lc%5B%5D=13115&lc%5B%5D=13116&lc%5B%5D=13117&lc%5B%5D=13119&lc%5B%5D=13120&lc%5B%5D=13201&lc%5B%5D=13202&lc%5B%5D=13203&lc%5B%5D=13204&lc%5B%5D=13205&lc%5B%5D=13206&lc%5B%5D=13207&lc%5B%5D=13208&lc%5B%5D=13209&lc%5B%5D=13210&lc%5B%5D=13211&lc%5B%5D=13212&lc%5B%5D=13213&lc%5B%5D=13214&lc%5B%5D=13215&lc%5B%5D=13218&lc%5B%5D=13219&lc%5B%5D=13220&lc%5B%5D=13221&lc%5B%5D=13222&lc%5B%5D=13223&lc%5B%5D=13224&lc%5B%5D=13225&lc%5B%5D=13227&lc%5B%5D=13228&lc%5B%5D=13229&lc%5B%5D=13303&lc%5B%5D=13305&lc%5B%5D=13308&lc%5B%5D=13361&lc%5B%5D=13401&ps=80"

#     tokyo_res = requests.get(tokyo_url)
    
#     tokyo_soup = BeautifulSoup(tokyo_res.content, "html.parser")
    
    
#     tokyo_elems = tokyo_soup.select(".bukken_title a")

#     print(tokyo_elems[0].contents[0])

#     tokyo_price_elems = tokyo_soup.select(".center .txt_em")
#     print(tokyo_price_elems[0].contents[0])



#     dbname = "bukken.db"
#     conn = sqlite3.connect(dbname)


#     #SQLiteを操作するためのカーソルを作成
#     cur = conn.cursor()

    
#     for j in range(len(tokyo_elems)):
        
#         k = j + (onepage_all * i)
        
        
        
        
        
#         if i == 0 and j == 0:
#             # テーブルの作成
#             cur.execute(
#             "CREATE TABLE bukken(id INTEGER PRIMARY KEY AUTOINCREMENT,name STRING,price REAL)"
#             )
            
#             print("テーブル作成完了")
        
        
#         cur.execute(f"INSERT INTO bukken values({k},'{tokyo_elems[j].contents[0]}',{tokyo_price_elems[j].contents[0]})")

#         # コミットしないと登録が反映されない
#         conn.commit()
        
        
        
#     time.sleep(2)
#     print(i)


# conn.close()

# l = "田植え"

# A_url = f"https://www.athome.co.jp/tochi/tokyo/list/"
# print(A_url)

# A_res = requests.get(A_url)

# A_res.encoding = "shift_jis"

# A_soup = BeautifulSoup(A_res.content, "html.parser")

# A_elems = A_soup.select("body")

# print(A_elems)





# url = "https://www.gu-global.com/jp/ja/search?q=%E3%82%BA%E3%83%9C%E3%83%B3"

# res = requests.get(url)

# soup = BeautifulSoup(res.content, "html.parser")

# elems = soup.select_one("body")

# print(elems)

# a = "jdjdjdjd"

# b = "submit23"

# print(b[6:])


# import json
# import glob

# jsonFiles = glob.glob("./スクレイピング/*")

# di = []
# for files in jsonFiles:
#     print(files)
#     with open(files, "r", encoding="utf-8") as f:
        
#         # print((json.load(f)).values())
#         jsonli = json.load(f)
#         di.append(jsonli)


# # li = []
# for i in di:
#     # di.append(list(i.values()))
#     print()

# print(di)
# li = list(set(li))
# print(li)

# for i in range(len(li)):
#     if li[i] == "":
#         print("空伯")

# a = {"key11":"あああ"}
# print("あああ" in a.values())


# data = [(exImg[i]["productTitle"], exImg[i]["price"], f'./static/images/clothes/{category}/{exImg[i]["imgUrl1"]}', f'./static/images/clothes/{category}/{exImg[i]["imgUrl2"]}', f'./static/images/clothes/{category}/{exImg[i]["imgUrl3"]}', f'./static/images/clothes/{category}/{exImg[i]["imgUrl4"]}', f'./static/images/clothes/{category}/{exImg[i]["imgUrl5"]}', f'./static/images/clothes/{category}/{exImg[i]["imgUrl6"]}', f'./static/images/clothes/{category}/{exImg[i]["imgUrl7"]}', f'./static/images/clothes/{category}/{exImg[i]["imgUrl8"]}', "", "", "", "", "", "", "", "", "", "", "", "", "", stock, 0, date, 0, 0, "", "", category, 1, materialList[ran])]
# number_of_elements = len(data)
# print(number_of_elements)







dbname = "ecdatabase"
    
conn = mysql.connector.connect(
        user='root',
        password='',
        host='localhost',
        database=dbname
)
    
cur = conn.cursor()

clothes_type_check = {
            "jacket": ["ジャケット", "jacket"],
            "t-shirt": ["Tシャツ", "t-shirt"], 
            "shirt": ["シャツ", "shirt"], 
            "pants": ["ズボン", "pants"], 
            "skirt": ["skirt", "スカート"],
            "underwear": ["パンツ", "下着","underwear"],
        }

check_text = "スカート"



for key, row in clothes_type_check.items() :
    # print(clothes_type_check[row])
    
    # print(key, row)
    if check_text in row:
        
        print(f"{key}に入ってた")
        select_key = key
        

cur.execute(f"""
                    SELECT COUNT(*)
                    FROM clothes 
                    JOIN clothesDetail ON clothes.id = clothesDetail.clothesId
                    WHERE clothes.clothesName LIKE '%スカート%' OR clothesDetail.type = '{select_key}';
                    """)

data = cur.fetchall()

print(len(data))
# for row in data:
#     print(row[1])


# print(f"""
#                     SELECT  clothesImage.img1, clothesDetail.type, clothes.clothesName, clothes.price, clothes.id, review.review 
#                     from clothes 
#                     JOIN clothesImage ON clothes.id = clothesImage.clothesId 
#                     JOIN clothesDetail ON clothes.id = clothesDetail.clothesId 
#                     JOIN review ON clothes.id = review.clothesId
#                     WHERE clothes.clothesName LIKE '%スカート%' OR clothesDetail.type = '{key}';
#                     """)

cur.execute("""
            SELECT COUNT(type)
            FROM clothesDetail
            WHERE type = 'skirt';
            """)

s_data = cur.fetchone()

print(s_data)