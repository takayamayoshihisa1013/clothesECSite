import mysql.connector
import json
import random

conn = mysql.connector.connect(
    user="root",
    password="",
    host="localhost",
    database="ecdatabase"
)

cur = conn.cursor()

# import random

# # cur.execute("DROP TABLE customerinfo")

# # cur.execute("""
# #         CREATE TABLE IF NOT EXISTS customerInfo (
# #         id INT AUTO_INCREMENT PRIMARY KEY,
# #         lastName VARCHAR(255),
# #         firstName VARCHAR(255),
# #         email VARCHAR(255),
# #         pass VARCHAR(255)
# #     )
# #     """)


# # cur.execute(f"INSERT INTO customerInfo (lastName,firstName,email,pass) values('高山','慶久','rurariyudayo@gmail.com','20031013y')")


# cur.execute("DROP TABLE clothestype")


# cur.execute("""
#             CREATE TABLE IF NOT EXISTS favorite (
#             id INT AUTO_INCREMENT PRIMARY KEY,
#             clothesId INT,
#             userId INT,
#             FOREIGN KEY (clothesID) REFERENCES clothes (id),
#             FOREIGN KEY (userId) REFERENCES customerInfo (id)
#             )
#             """)


# # 服のサイズ
cur.execute("DROP TABLE clothes_size")


cur.execute("""
            SELECT id FROM clothes;
            """)

clothesId =  cur.fetchall()


cur.execute("""
            CREATE TABLE IF NOT EXISTS clothes_size (
            id INT AUTO_INCREMENT UNIQUE KEY,
            S INT,
            M INT,
            L INT,
            clothesId INT,
            PRIMARY KEY (clothesId),
            FOREIGN KEY (clothesId) REFERENCES clothes (id)
            )
            """)


print(clothesId)

for row in clothesId:
    print(row[0])
    ran = random.randint(140, 170)
    cur.execute(f"INSERT INTO clothes_size (S, M, L, clothesId) values ({ran}, {ran + 10}, {ran + 20}, {row[0]})")


# # cur.executemany(f"INSERT INTO ")

# cur.execute("""
#             SELECT id, type FROM clothes;
#             """)

# clothesData = cur.fetchall()

# for row in clothesData:

#     print(clothesData)
#     if row[1] == "pants":
#         text = """オーセンティックなディテールを残しながらも、
#                 センタークリースやフロントホックなどキレイめな要素を取り入れた上品なカズボン。
#                 素材には、丈夫で柔らかく、ハリ感とコシ感も兼ね備えたデニム生地を採用しました。
#                 製品完成後に洗いをかけ、
#                 ポケットや脇のラインのステッチ周りに陰影を出すことでヴィンテージ感のある、
#                 小慣れた表情に仕上げています。
#             """
#         cur.execute(f"""
#                     UPDATE clothes SET productText = '{text}' WHERE id = {row[0]}
#                     """)

#     if row[1] == "jacket":
#         text =  """
#                 従来のジャケットよりもルーズなドロップショルダーのシルエットで、ゆったりとラフに着こなしていただけます。
#                 大きめの身幅とアームホールで、厚手のスウェットやニットを着込んでももたつかないデザイン。
#                 アウトドアブランドらしいこだわりの詰まったファッション製も機能性も高いハイネックブルゾンです。
#                 レジャーやキャンプなどのアウトドアはもちろん、タウンユースにもOKな幅広く活躍するデイリーな1枚。
#                 大きめサイズもご用意しており、、年齢を問わずに着用が可能なので、ギフトやプレゼントにもおすすめです。
#                 """
#         cur.execute(f"""
#                     UPDATE clothes SET productText = '{text}' WHERE id = {row[0]}
#                     """)

#     if row[1] == "shirt":
#         text = """
#             ドロップショルダーとワイドなシルエットがアクセントになったリラックスシルエットのレギュラーカラーシャツ。
#             ドレープ感のある素材に、着回しを考慮したシンプルなデザインで、気品の漂う、抜け感のあるスタイリングを演出します。
#             またボタンには貝ボタンを使用することにより高級感あふれる上品な仕上がりに。
#             1枚ではもちろん、ジャケットなどとのレイヤードスタイルにも活躍し、
#             デニムやカーゴパンツ、スウェットパンツなどカジュアルな合わせはもちろん、
#             ワイドなボトムスやスラックスなどきれいめやモードなテイストにもマッチします。
#             テイストやシーズンを問わず長くご愛用いただけるloose basicな表情のアイテムです
#             """
#         cur.execute(f"""
#                     UPDATE clothes SET productText = '{text}' WHERE id = {row[0]}
#                     """)

#     if row[1] == "skirt":
#         text = """
#             裾に向かって自然に広がるシルエットと、
#             歩くたびに揺れるプリーツで女性らしさアップ。
#             ハイウエストデザインで腰回りがスッキリ見え、
#             後ろはゴム仕様で、ストレスなく着用可能。
#             本体同生地の付属ベルト付きなので、体に合わせてウエスト調整できます。
#             裏地付きで保温性があり、柔らかな肌触りもポイントです。
#             シンプルなトップスと合わせるだけで主役級コーデが完成する
#             万能なスカートです。
#             """
#         cur.execute(f"""
#                     UPDATE clothes SET productText = '{text}' WHERE id = {row[0]}
#                     """)

#     if row[1] == "underwear":
#         # text = """

#         #     """
#         # cur.execute(f"""
#         #             UPDATE clothes SET productText = {text} WHERE id = {row[0]}
#         #             """)
#         pass
#     if row[1] == "t-shirt":
#         text = """
#             どんな服装にも合わせやすく、一枚でも、重ね着のインナーとしても着用できる、着回し力に優れた一品です。
#             首元はダブルステッチで伸びにくい仕様に仕上げています。
#             サイドに縫い目がない丸胴仕様で長い間着用、洗濯してもよれにくくなっています。
#             ボトムスはハーフパンツやバルーンパンツ、ワイドパンツ、ハイウエストのデニムやジョガーパンツ、ラインパンツ、
#             スカートならスリットスカートやロングスカート、ラップスカート、マキシワンピースのレイヤードと様々なスタイルに対応してくれます。
#             小物でアクセントをつけるならトレンドの巾着バッグやビニールバッグ・クリアバッグ、マクラメトート、メッシュバッグは欠かせません。
#             ノームコアなデザインなのでスポーツサンダル、スニーカーサンダルやエスパドリーユ、ミュールなどのサンダル類との相性も抜群で一枚と言わず色違いで何枚でも持っておきたいアイテムです。
#             """
#         cur.execute(f"""
#                     UPDATE clothes SET productText = '{text}' WHERE id = {row[0]}
#                     """)


# cur.execute("""
#             CREATE TABLE IF NOT EXISTS review (
#                 id INT AUTO_INCREMENT PRIMARY KEY,
#                 review VARCHAR(255),
#                 userId INT,
#                 clothesId INT,
#                 FOREIGN KEY (clothesId) REFERENCES clothes (id),
#                 FOREIGN KEY (userId) REFERENCES customerInfo (id)
#             )
#             """)


# cur.execute("""
#             SELECT id FROM clothes;
#             """)

# clothesId = cur.fetchall()

# for row in clothesId:
#     ran = round(random.uniform(0, 5),1)
#     print(ran)
#     cur.execute(f"INSERT INTO review (review, clothesId, userId) values ('{ran}', {row[0]}, 1)")


# conn.commit()
# cur.close()

# # favorite VARCHAR(255),
# # cart VARCHAR(255),
# # buyLog VARCHAR(255)



# 商品画像のテーブル作成
# cur.execute("""
#             CREATE TABLE IF NOT EXISTS clothesImage(
#             id INT AUTO_INCREMENT,
#             clothesId INT,
#             img1 VARCHAR(255),
#             img2 VARCHAR(255),
#             img3 VARCHAR(255),
#             img4 VARCHAR(255),
#             img5 VARCHAR(255),
#             img6 VARCHAR(255),
#             img7 VARCHAR(255),
#             img8 VARCHAR(255),
#             PRIMARY KEY (id, clothesId),
#             FOREIGN KEY (clothesId) REFERENCES clothes(id)
#             )
#             """)

# with open("./json/clothesdb.json", "r", encoding="utf-8") as file:
#     json_data = json.load(file)

# i = 0
# for row in json_data:
#     # print(row)
#     i += 1
#     for key, value in row.items():
#         print(value["img1"])
#         cur.execute("INSERT INTO clothesDetail(clothesId, sex, type, material) VALUES (%s,%s,%s,%s)",
#                 (i, "",value["type"], value["material"]))



# タグのテーブル作成
# cur.execute("""
#             CREATE TABLE IF NOT EXISTS tag(
#                 id INT AUTO_INCREMENT,
#                 clothesId INT,
#                 tag1 VARCHAR(255),
#                 tag2 VARCHAR(255),
#                 tag3 VARCHAR(255),
#                 tag4 VARCHAR(255),
#                 tag5 VARCHAR(255),
#                 PRIMARY KEY (id, clothesId),
#                 FOREIGN KEY(clothesId) REFERENCES clothes(id)
#             )
#             """)


# cur.execute("DROP TABLE clothesType")

# cur.execute("""
#     ALTER TABLE `clothes` DROP FOREIGN KEY `clothes_ibfk_3`;
# """)


# 服の詳細な情報のテーブル
# cur.execute("""
#             CREATE TABLE IF NOT EXISTS ClothesDetail(
#                 clothesId INT,
#                 sex VARCHAR(255),
#                 type VARCHAR(255),
#                 material VARCHAR(255),
#                 PRIMARY KEY (clothesId),
#                 FOREIGN KEY (clothesId) REFERENCES clothes(id),
#                 FOREIGN KEY (type) REFERENCES clothesType(type),
#                 FOREIGN KEY (material) REFERENCES material(material)
#             )
#             """)

# cur.execute("""
#     CREATE TABLE IF NOT EXISTS clothesType (
#         type VARCHAR(255) PRIMARY KEY
#     )
# """)

# data = [("t-shirt",), ("shirt",), ("jacket",), ("skirt",), ("pants",), ("underwear",)]

# cur.executemany("""
#     INSERT INTO clothesType (type) VALUES (%s)
# """, data)


conn.commit()
conn.close()
