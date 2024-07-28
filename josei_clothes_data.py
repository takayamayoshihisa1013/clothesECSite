import json

import mysql.connector

import pprint

dbname = "ecdatabase"

conn = mysql.connector.connect(
            user='root',
            password='',
            host='localhost',
            database=dbname
        )

cur = conn.cursor()

with open("./clothesdb.json", mode="r", encoding="utf-8") as f:
    # JSONファイルからPythonオブジェクトを取得
    clothes_data = json.load(f)

# clothes_dataはリストなので、一件ずつ処理が可能
for item in clothes_data:
    # ここで各アイテムに対する処理を行う
    # print(item)
    for key, value in item.items():
        print(key)
    # pprint(item)
    





# cur.execute("""
#             UPDATE clothes
#             SET 
#             """)
