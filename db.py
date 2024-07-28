import mysql.connector

import glob

import pprint

import random

import datetime

import os

import json









# データベースに接続
conn = mysql.connector.connect(
    user='root',
    password='',
    host='localhost',
    database='ecdatabase'
)
cur = conn.cursor()

# cur.execute("DROP TABLE clothes")

# cur.execute("DROP TABLE material")

# cur.execute("DROP TABLE clothesType")



# cur.execute("DROP TABLE customerInfo")



create_table_query = """
        CREATE TABLE IF NOT EXISTS customerInfo (
        id INT AUTO_INCREMENT PRIMARY KEY,
        lastName VARCHAR(255),
        firstName VARCHAR(255),
        email VARCHAR(255),
        pass VARCHAR(255)
    )
    """
cur.execute(create_table_query)

cur.execute(f"INSERT INTO customerInfo (lastName,firstName,email,pass) values('高山','慶久','rurariyudayo@gmail.com','20031013y')")


cur.execute("""
    CREATE TABLE IF NOT EXISTS clothesType (
        type VARCHAR(255) PRIMARY KEY
    )
""")

data = [("t-shirt",), ("shirt",), ("jacket",), ("skirt",), ("pants",), ("underwear",)]

cur.executemany("""
    INSERT INTO clothesType (type) VALUES (%s)
""", data)

# テーブル作成
cur.execute("""
    CREATE TABLE IF NOT EXISTS material (
        material VARCHAR(255) PRIMARY KEY
    )
""")

# 素材のデータを挿入
material_data = [
    ("綿",),
    ("麻",),
    ("毛",),
    ("化学繊維",),
    ("絹",)
]

cur.executemany("INSERT INTO material (material) VALUES (%s)", material_data)

# コミットして変更を保存
conn.commit()




# データベースを先に開いておく
conn = mysql.connector.connect(
    user='root',
    password='',
    host='localhost',
    database='ecdatabase'
)
cur = conn.cursor()










# jsonファイルの読みだし
jsonFiles = glob.glob("./スクレイピング/*")

di = []
for files in jsonFiles:
    print(files)
    with open(files, "r", encoding="utf-8") as f:
        
        # print((json.load(f)).values())
        jsonli = json.load(f)
        di.append(jsonli)
        # print(di)


# jsonファイルの商品のタイトルが入ったリストを作る（重複も消す）
# とりあえずそのまま説明文全てをぶち込む
ex = []
for i in range(len(di)):
    for j in range(len(di[i])):
        # print(di[i][j]['asizebaseplus1'])
        ex.append(di[i][j]['asizebaseplus1'])

# 重複を消す
# ex = list(set(ex))
# print(ex)


# ダウンロードされている商品の画像一覧のリストを作る
clothesli = []
dw_files = glob.glob("./static/images/clothes/**/*")
# 画像ファイルから画像を取り出す
for imgFile in dw_files:
    clothesli.append(os.path.basename(imgFile))

# それをリストに入れる
# for i in range(len(clothesli)):
#     print(clothesli[i])

count = 0
appendCount = 0
countTrue = 0
exImg = []
img2Count = 0
img3Count = 0
img4Count = 0
img5Count = 0
img6Count = 0
img7Count = 0
img8Count = 0

existCounter = 0

for i in range(len(di)):
    for j in range(len(di[i])):
        
        # ランダムな値段をつける
        ran = random.randint(500, 10000)
        
        # 時間も入れる
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        
        # print(di[i][j]['asizebaseplus1'])
        # print(di[i][j]['画像URL'][36:])
        # print(j)
        # jsonファイルの商品説明
        json_ex = di[i][j]['asizebaseplus1']
        count += 1
        # jsonファイルの画像URLの共通部分を無くしたもの
        json_imgUrl = di[i][j]['画像URL'][36:]
        
        # json_exが空白じゃなかった場合
        if json_ex != "":
            
            # exImgの要素数が0じゃなかった場合
            if len(exImg) != 0:
                
                for k in range(len(exImg)):
                    # print(k)
                    # すでに入っていた時の処理
                    if json_ex in exImg[k].values():
                        # print("もう入っている")
                        countTrue += 1
                        
                        # すでに同じURLの写真がひっていないかの調査
                        if json_imgUrl not in exImg[k].values():
                            if exImg[k]["imgUrl2"] == "":
                                exImg[k]["imgUrl2"] = json_imgUrl
                                img2Count += 1
                            elif exImg[k]["imgUrl3"] == "":
                                exImg[k]["imgUrl3"] = json_imgUrl
                                img3Count += 1
                            elif exImg[k]["imgUrl4"] == "":
                                exImg[k]["imgUrl4"] = json_imgUrl
                                img4Count += 1
                            elif exImg[k]["imgUrl5"] == "":
                                exImg[k]["imgUrl5"] = json_imgUrl
                                img5Count += 1
                            elif exImg[k]["imgUrl6"] == "":
                                exImg[k]["imgUrl6"] = json_imgUrl
                                img6Count += 1
                            elif exImg[k]["imgUrl7"] == "":
                                exImg[k]["imgUrl7"] = json_imgUrl
                                img7Count += 1
                            elif exImg[k]["imgUrl8"] == "":
                                exImg[k]["imgUrl8"] = json_imgUrl
                                img8Count += 1
                            break
                        else:
                            existCounter += 1
                            break
                        
                    # 入ってなかった時の処理
                    if k == len(exImg) - 1:
                        oneColumn = {"productTitle":json_ex, "imgUrl1":json_imgUrl, "imgUrl2":"", "imgUrl3":"", "imgUrl4":"", "imgUrl5":"", "imgUrl6":"", "imgUrl7":"", "imgUrl8":"", "price":ran, "date":date}
                        exImg.append(oneColumn)
                        # print("ss")
                        appendCount += 1
                        
                    
            # exImgの中に何も入ってなかった場合
            else:
                # 一番最初の処理
                oneColumn = {"productTitle":json_ex, "imgUrl1":json_imgUrl, "imgUrl2":"", "imgUrl3":"", "imgUrl4":"", "imgUrl5":"", "imgUrl6":"", "imgUrl7":"", "imgUrl8":"", "price":ran, "date":date}
                exImg.append(oneColumn)
                # print(oneColumn)
                # print(exImg)
                appendCount += 1
                
        else:
            print("空白やねん")
            






print(f"回った回数：{count}")
print(f"diの要素数：{len(di[0]) + len(di[1]) + len(di[2]) + len(di[3]) + len(di[4]) + len(di[5]) + len(di[6])}")
print(f"exImgの要素数：{len(exImg)}")
print(f"重複なしのexのタイトル数：{len(list(set(ex)))}")
print(f"存在しなくて追加された要素の数：{appendCount}")
print(f"すでに同じ商品タイトルがあった数：{countTrue}")
print(f"存在して追加されなかった画像の数：{existCounter}")
print(f"商品タイトルが同じで色違いだったやつ：{img2Count + img3Count + img4Count + img5Count + img6Count + img7Count + img8Count}")
print(f"di0:{len(di[0])}")
print(f"di1:{len(di[1])}")
print(f"di2:{len(di[2])}")
print(f"di3:{len(di[3])}")
print(f"di4:{len(di[4])}")
print(f"di5:{len(di[5])}")
print(f"di6:{len(di[6])}")








# ooooo
cur.execute("""
        CREATE TABLE IF NOT EXISTS clothes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        clothesName VARCHAR(255),
        price INT,
        image1 VARCHAR(255),
        image2 VARCHAR(255),
        image3 VARCHAR(255),
        image4 VARCHAR(255),
        image5 VARCHAR(255),
        image6 VARCHAR(255),
        image7 VARCHAR(255),
        image8 VARCHAR(255),
        color1 VARCHAR(255),
        color2 VARCHAR(255),
        color3 VARCHAR(255),
        color4 VARCHAR(255),
        color5 VARCHAR(255),
        color6 VARCHAR(255),
        color7 VARCHAR(255),
        color8 VARCHAR(255),
        tag1 VARCHAR(255),
        tag2 VARCHAR(255),
        tag3 VARCHAR(255),
        tag4 VARCHAR(255),
        tag5 VARCHAR(255),
        stock INT,
        review DECIMAL(10, 2),
        date TEXT,
        clickCounter INT,
        buyCounter INT,
        productText TEXT,
        sex VARCHAR(255),
        type VARCHAR(255),
        userid INT,
        material VARCHAR(255),
        FOREIGN KEY (type) REFERENCES clothesType (type),
        FOREIGN KEY (userid) REFERENCES customerInfo (id),
        FOREIGN KEY (material) REFERENCES material (material)
    )
    """)


# ooooo
# 必要なモジュールをインポート
import random

materialList = ["化学繊維","毛","絹","綿","麻"]

for i in range(len(exImg)):
    if i < 263:
        category = "jacket"
    elif i >= 263 and i < 527:
        category = "shirt"
    elif i >= 527 and i < 778:
        category = "skirt"
    elif i >= 778 and i < 1015:
        category = "t-shirt"
    elif i >= 1015 and i < 1155:
        category = "underwear"
    elif i >= 1155 and i < 1350:
        category = "pants"
    elif i >= 1350 :
        category = "underwear"

    stock = random.randint(1, 20)
    ran = random.randint(0, 4)  # 0から4の間でランダムな値を取得

    # productTextを空の文字列で初期化
    productText = ""

    # data = [exImg[i]["productTitle"], exImg[i]["price"], f'./static/images/clothes/{category}/{exImg[i]["imgUrl1"]}', f'./static/images/clothes/{category}/{exImg[i]["imgUrl2"]}', f'./static/images/clothes/{category}/{exImg[i]["imgUrl3"]}', f'./static/images/clothes/{category}/{exImg[i]["imgUrl4"]}', f'./static/images/clothes/{category}/{exImg[i]["imgUrl5"]}', f'./static/images/clothes/{category}/{exImg[i]["imgUrl6"]}', f'./static/images/clothes/{category}/{exImg[i]["imgUrl7"]}', f'./static/images/clothes/{category}/{exImg[i]["imgUrl8"]}', "", "", "", "", "", "", "", "", "", "", "", "", "", stock, 0, date, 0, 0, "", "", category, 1, materialList[ran]]
    # number_of_elements = len(data)
    # print(number_of_elements)

    # SQLクエリを実行
    # cur.executemany("""
    #     INSERT INTO clothes (clothesName, price) 
    #     VALUES (%s, %s,)
    #     """, [(exImg[i]["productTitle"], 1)]
    # )
    
    cur.executemany("""
        INSERT INTO clothes (clothesName, price, image1, image2, image3, image4, image5, image6, image7, image8, color1, color2, color3, color4, color5, color6, color7, color8, tag1, tag2, tag3, tag4, tag5, stock, review, date, clickCounter, buyCounter, productText, sex, type, userid, material) 
        VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, [(exImg[i]["productTitle"], exImg[i]["price"],  f'./static/images/clothes/{category}/{exImg[i]["imgUrl1"]}',  f'./static/images/clothes/{category}/{exImg[i]["imgUrl2"]}',  f'./static/images/clothes/{category}/{exImg[i]["imgUrl3"]}',  f'./static/images/clothes/{category}/{exImg[i]["imgUrl4"]}',  f'./static/images/clothes/{category}/{exImg[i]["imgUrl5"]}',  f'./static/images/clothes/{category}/{exImg[i]["imgUrl6"]}', f'./static/images/clothes/{category}/{exImg[i]["imgUrl7"]}',  f'./static/images/clothes/{category}/{exImg[i]["imgUrl8"]}', "", "", "", "", "", "", "", "", "", "", "", "", "", stock, 0, date, 0, 0, productText, "", category, 1, materialList[ran])]

    )


# clothesName, price, image1, image2, image3, image4, image5, image6, image7, image8, color1, color2, color3, color4, color5, color6, color7, color8, tag1, tag2, tag3, tag4, tag5, stock, review, date, clickCounter, buyCounter, productText, sex, type, userid, material
# %s, 0, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 0, 0, %s, 0, 0, %s, %s, %s, 1, %s )
# [(exImg[i]["productTitle"], exImg[i]["price"],  f'./static/images/clothes/{category}/{exImg[i]["imgUrl1"]}',  f'./static/images/clothes/{category}/{exImg[i]["imgUrl2"]}',  f'./static/images/clothes/{category}/{exImg[i]["imgUrl3"]}',  f'./static/images/clothes/{category}/{exImg[i]["imgUrl4"]}',  f'./static/images/clothes/{category}/{exImg[i]["imgUrl5"]}',  f'./static/images/clothes/{category}/{exImg[i]["imgUrl6"]}', f'./static/images/clothes/{category}/{exImg[i]["imgUrl7"]}',  f'./static/images/clothes/{category}/{exImg[i]["imgUrl8"]}', "", "", "", "", "", "", "", "", "", "", "", "", "", stock, 0, date, 0, 0, productText, "", category, 1, materialList[ran])









    # 後で商品説明と素材を入れなければいけない
        # """, [(exImg[i]["productTitle"], exImg[i]["price"],  f'./static/images/clothes/{category}/{exImg[i]["imgUrl1"]}',  f'./static/images/clothes/{category}/{exImg[i]["imgUrl2"]}',  f'./static/images/clothes/{category}/{exImg[i]["imgUrl3"]}',  f'./static/images/clothes/{category}/{exImg[i]["imgUrl4"]}',  f'./static/images/clothes/{category}/{exImg[i]["imgUrl5"]}',  f'./static/images/clothes/{category}/{exImg[i]["imgUrl6"]}', f'./static/images/clothes/{category}/{exImg[i]["imgUrl7"]}',  f'./static/images/clothes/{category}/{exImg[i]["imgUrl8"]}', "", "", "", "", "", "", "", "", stock, date, productText, category, id, material),])



# pprint.pprint(exImg)
# print()
# print(exImg[0]["productTitle"])

cur.execute("""
            SELECT id, type FROM clothes;
            """)

clothesData = cur.fetchall()

for row in clothesData:

    print(clothesData)
    if row[1] == "pants":
        text = """オーセンティックなディテールを残しながらも、
                センタークリースやフロントホックなどキレイめな要素を取り入れた上品なカズボン。
                素材には、丈夫で柔らかく、ハリ感とコシ感も兼ね備えたデニム生地を採用しました。
                製品完成後に洗いをかけ、
                ポケットや脇のラインのステッチ周りに陰影を出すことでヴィンテージ感のある、
                小慣れた表情に仕上げています。
            """
        cur.execute(f"""
                    UPDATE clothes SET productText = '{text}' WHERE id = {row[0]}
                    """)
        
    if row[1] == "jacket":
        text =  """
                従来のジャケットよりもルーズなドロップショルダーのシルエットで、ゆったりとラフに着こなしていただけます。
                大きめの身幅とアームホールで、厚手のスウェットやニットを着込んでももたつかないデザイン。
                アウトドアブランドらしいこだわりの詰まったファッション製も機能性も高いハイネックブルゾンです。
                レジャーやキャンプなどのアウトドアはもちろん、タウンユースにもOKな幅広く活躍するデイリーな1枚。
                大きめサイズもご用意しており、、年齢を問わずに着用が可能なので、ギフトやプレゼントにもおすすめです。
                """
        cur.execute(f"""
                    UPDATE clothes SET productText = '{text}' WHERE id = {row[0]}
                    """)
        
    if row[1] == "shirt":
        text = """
            ドロップショルダーとワイドなシルエットがアクセントになったリラックスシルエットのレギュラーカラーシャツ。
            ドレープ感のある素材に、着回しを考慮したシンプルなデザインで、気品の漂う、抜け感のあるスタイリングを演出します。
            またボタンには貝ボタンを使用することにより高級感あふれる上品な仕上がりに。
            1枚ではもちろん、ジャケットなどとのレイヤードスタイルにも活躍し、
            デニムやカーゴパンツ、スウェットパンツなどカジュアルな合わせはもちろん、
            ワイドなボトムスやスラックスなどきれいめやモードなテイストにもマッチします。
            テイストやシーズンを問わず長くご愛用いただけるloose basicな表情のアイテムです
            """
        cur.execute(f"""
                    UPDATE clothes SET productText = '{text}' WHERE id = {row[0]}
                    """)
        
    if row[1] == "skirt":
        text = """
            裾に向かって自然に広がるシルエットと、
            歩くたびに揺れるプリーツで女性らしさアップ。
            ハイウエストデザインで腰回りがスッキリ見え、
            後ろはゴム仕様で、ストレスなく着用可能。
            本体同生地の付属ベルト付きなので、体に合わせてウエスト調整できます。
            裏地付きで保温性があり、柔らかな肌触りもポイントです。
            シンプルなトップスと合わせるだけで主役級コーデが完成する
            万能なスカートです。
            """
        cur.execute(f"""
                    UPDATE clothes SET productText = '{text}' WHERE id = {row[0]}
                    """)
        
    if row[1] == "underwear":
        # text = """

        #     """
        # cur.execute(f"""
        #             UPDATE clothes SET productText = {text} WHERE id = {row[0]}
        #             """)
        pass
    if row[1] == "t-shirt":
        text = """
            どんな服装にも合わせやすく、一枚でも、重ね着のインナーとしても着用できる、着回し力に優れた一品です。
            首元はダブルステッチで伸びにくい仕様に仕上げています。
            サイドに縫い目がない丸胴仕様で長い間着用、洗濯してもよれにくくなっています。
            ボトムスはハーフパンツやバルーンパンツ、ワイドパンツ、ハイウエストのデニムやジョガーパンツ、ラインパンツ、
            スカートならスリットスカートやロングスカート、ラップスカート、マキシワンピースのレイヤードと様々なスタイルに対応してくれます。
            小物でアクセントをつけるならトレンドの巾着バッグやビニールバッグ・クリアバッグ、マクラメトート、メッシュバッグは欠かせません。
            ノームコアなデザインなのでスポーツサンダル、スニーカーサンダルやエスパドリーユ、ミュールなどのサンダル類との相性も抜群で一枚と言わず色違いで何枚でも持っておきたいアイテムです。
            """
        cur.execute(f"""
                    UPDATE clothes SET productText = '{text}' WHERE id = {row[0]}
                    """)



# 服のサイズ
cur.execute("DROP TABLE clothes_size")



cur.execute("""
            SELECT id FROM clothes;
            """)

clothesId =  cur.fetchall()


cur.execute("""
            CREATE TABLE IF NOT EXISTS clothes_size (
            id INT AUTO_INCREMENT PRIMARY KEY,
            S INT,
            M INT,
            L INT,
            clothesId INT,
            FOREIGN KEY (clothesId) REFERENCES clothes (id)
            )
            """)








print(clothesId)

for row in clothesId:
    print(row[0])
    ran = random.randint(140, 170)
    cur.execute(f"INSERT INTO clothes_size (S, M, L, clothesId) values ({ran}, {ran + 10}, {ran + 20}, {row[0]})")
    


cur.execute("""
            CREATE TABLE IF NOT EXISTS favorite (
            id INT AUTO_INCREMENT PRIMARY KEY,
            clothesId INT,
            userId INT,
            FOREIGN KEY (clothesID) REFERENCES clothes (id),
            FOREIGN KEY (userId) REFERENCES customerInfo (id)
            )
            """)



# 服のサイズ
cur.execute("DROP TABLE clothes_size")



cur.execute("""
            SELECT id FROM clothes;
            """)

clothesId =  cur.fetchall()


cur.execute("""
            CREATE TABLE IF NOT EXISTS clothes_size (
            id INT AUTO_INCREMENT PRIMARY KEY,
            S INT,
            M INT,
            L INT,
            clothesId INT,
            FOREIGN KEY (clothesId) REFERENCES clothes (id)
            )
            """)








print(clothesId)

for row in clothesId:
    print(row[0])
    ran = random.randint(140, 170)
    cur.execute(f"INSERT INTO clothes_size (S, M, L, clothesId) values ({ran}, {ran + 10}, {ran + 20}, {row[0]})")
    










cur.execute("""
            SELECT id, type FROM clothes;
            """)

clothesData = cur.fetchall()

for row in clothesData:

    print(clothesData)
    if row[1] == "pants":
        text = """オーセンティックなディテールを残しながらも、
                センタークリースやフロントホックなどキレイめな要素を取り入れた上品なカズボン。
                素材には、丈夫で柔らかく、ハリ感とコシ感も兼ね備えたデニム生地を採用しました。
                製品完成後に洗いをかけ、
                ポケットや脇のラインのステッチ周りに陰影を出すことでヴィンテージ感のある、
                小慣れた表情に仕上げています。
            """
        cur.execute(f"""
                    UPDATE clothes SET productText = '{text}' WHERE id = {row[0]}
                    """)
        
    if row[1] == "jacket":
        text =  """
                従来のジャケットよりもルーズなドロップショルダーのシルエットで、ゆったりとラフに着こなしていただけます。
                大きめの身幅とアームホールで、厚手のスウェットやニットを着込んでももたつかないデザイン。
                アウトドアブランドらしいこだわりの詰まったファッション製も機能性も高いハイネックブルゾンです。
                レジャーやキャンプなどのアウトドアはもちろん、タウンユースにもOKな幅広く活躍するデイリーな1枚。
                大きめサイズもご用意しており、、年齢を問わずに着用が可能なので、ギフトやプレゼントにもおすすめです。
                """
        cur.execute(f"""
                    UPDATE clothes SET productText = '{text}' WHERE id = {row[0]}
                    """)
        
    if row[1] == "shirt":
        text = """
            ドロップショルダーとワイドなシルエットがアクセントになったリラックスシルエットのレギュラーカラーシャツ。
            ドレープ感のある素材に、着回しを考慮したシンプルなデザインで、気品の漂う、抜け感のあるスタイリングを演出します。
            またボタンには貝ボタンを使用することにより高級感あふれる上品な仕上がりに。
            1枚ではもちろん、ジャケットなどとのレイヤードスタイルにも活躍し、
            デニムやカーゴパンツ、スウェットパンツなどカジュアルな合わせはもちろん、
            ワイドなボトムスやスラックスなどきれいめやモードなテイストにもマッチします。
            テイストやシーズンを問わず長くご愛用いただけるloose basicな表情のアイテムです
            """
        cur.execute(f"""
                    UPDATE clothes SET productText = '{text}' WHERE id = {row[0]}
                    """)
        
    if row[1] == "skirt":
        text = """
            裾に向かって自然に広がるシルエットと、
            歩くたびに揺れるプリーツで女性らしさアップ。
            ハイウエストデザインで腰回りがスッキリ見え、
            後ろはゴム仕様で、ストレスなく着用可能。
            本体同生地の付属ベルト付きなので、体に合わせてウエスト調整できます。
            裏地付きで保温性があり、柔らかな肌触りもポイントです。
            シンプルなトップスと合わせるだけで主役級コーデが完成する
            万能なスカートです。
            """
        cur.execute(f"""
                    UPDATE clothes SET productText = '{text}' WHERE id = {row[0]}
                    """)
        
    if row[1] == "underwear":
        # text = """

        #     """
        # cur.execute(f"""
        #             UPDATE clothes SET productText = {text} WHERE id = {row[0]}
        #             """)
        pass
    if row[1] == "t-shirt":
        text = """
            どんな服装にも合わせやすく、一枚でも、重ね着のインナーとしても着用できる、着回し力に優れた一品です。
            首元はダブルステッチで伸びにくい仕様に仕上げています。
            サイドに縫い目がない丸胴仕様で長い間着用、洗濯してもよれにくくなっています。
            ボトムスはハーフパンツやバルーンパンツ、ワイドパンツ、ハイウエストのデニムやジョガーパンツ、ラインパンツ、
            スカートならスリットスカートやロングスカート、ラップスカート、マキシワンピースのレイヤードと様々なスタイルに対応してくれます。
            小物でアクセントをつけるならトレンドの巾着バッグやビニールバッグ・クリアバッグ、マクラメトート、メッシュバッグは欠かせません。
            ノームコアなデザインなのでスポーツサンダル、スニーカーサンダルやエスパドリーユ、ミュールなどのサンダル類との相性も抜群で一枚と言わず色違いで何枚でも持っておきたいアイテムです。
            """
        cur.execute(f"""
                    UPDATE clothes SET productText = '{text}' WHERE id = {row[0]}
                    """)





cur.execute("""
            CREATE TABLE IF NOT EXISTS review (
                id INT AUTO_INCREMENT PRIMARY KEY,
                review VARCHAR(255),
                userId INT,
                clothesId INT,
                FOREIGN KEY (clothesId) REFERENCES clothes (id),
                FOREIGN KEY (userId) REFERENCES customerInfo (id)
            )
            """)



cur.execute("""
            SELECT id FROM clothes;
            """)

clothesId = cur.fetchall()

for row in clothesId:
    ran = round(random.uniform(0, 5),1)
    print(ran)
    cur.execute(f"INSERT INTO review (review, clothesId, userId) values ('{ran}', {row[0]}, 1)")
    



# コミットして変更を保存
conn.commit()

# 接続を閉じる
conn.close()


# for i in range(len(exImg)):

# pprint.pprint(exImg)


# blank_counter = 0
# for i in range(len(exImg)):
#     # print(exImg[i])
#     # print(exImg[i]["imgUrl1"])
    
#     if exImg[i]["imgUrl1"] == "":
#         blank_counter += 1
    

# print(blank_counter)
    