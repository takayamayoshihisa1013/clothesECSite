import json
import mysql.connector

# データベース接続
conn = mysql.connector.connect(
    user='root',
    password='',
    host='localhost',
    database='ecdatabase'
)
cur = conn.cursor()

cur.execute("""
            SELECT * FROM clothes;
            """)

clothesList = cur.fetchall()

# print(clothesList)


# from decimal import Decimal

# def decimal_default(obj):
#     if isinstance(obj, Decimal):
#         return float(obj)
#     raise TypeError

# data_list = []
# for i, clothes in enumerate(clothesList, start=1):
#     clothes_data = {
#         "id": clothes[0],
#         "title": clothes[1],
#         "price": clothes[2],
#         "img1": clothes[3],
#         "img2": clothes[4],
#         "img3": clothes[5],
#         "img4": clothes[6],
#         "img5": clothes[7],
#         "img6": clothes[8],
#         "img7": clothes[9],
#         "img8": clothes[10],
#         "color1": clothes[11],
#         "color2": clothes[12],
#         "color3": clothes[13],
#         "color4": clothes[14],
#         "color5": clothes[15],
#         "color6": clothes[16],
#         "color7": clothes[17],
#         "color8": clothes[18],
#         "tag1": clothes[19],
#         "tag2": clothes[20],
#         "tag3": clothes[21],
#         "tag4": clothes[22],
#         "tag5": clothes[23],
#         "stock": clothes[24],
#         "review": clothes[25],
#         "date": clothes[26],
#         "clickCounter": clothes[27],
#         "buyCounter": clothes[28],
#         "productText": clothes[29],
#         "sex": clothes[30],
#         "type": clothes[31],
#         "userId": clothes[32],
#         "material": clothes[33]
#     }
#     data_list.append({"clothes" + str(i): clothes_data})

# data = json.dumps(data_list, default=decimal_default, ensure_ascii=False)

# with open("./json/clothesdb.json", mode="w", encoding="utf-8") as file:
#     file.write(data)
    
# # print(i)
    

with open("./json/clothesdb.json", mode="r", encoding="utf-8") as file:
    json_file = json.load(file)
    # for line in file:
    #     data = json.loads(line)
    #     print(data)

# #     # exist_data.update(new_data)

# print(json_file[0])
# for row in json_file:
#     print(row)

# forループでimg1の値を取り出す
for item in json_file:  # clothes_data内の各要素（辞書）に対して
    for key, value in item.items():  # 辞書内のキーと値を取得
        img1_value = value["img1"]  # "img1" の値を取得する
        print(value,img1_value)  # img1の値を表示








