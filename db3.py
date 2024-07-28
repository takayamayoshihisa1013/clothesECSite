import mysql.connector
import random

conn = mysql.connector.connect(
    user="root",
    password="",
    host="localhost",
    database="ecdatabase"
)

cur = conn.cursor()

# cur.execute("""
#     SELECT clothes.id, clothes.clothesName 
#     FROM clothes
# """)

# data = cur.fetchall()

# for row in data:
#     clothes_id = row[0]
#     clothes_name = row[1]

    # if "ユニセックス" in clothes_name or "男女" in clothes_name or ("男" in clothes_name and "女" in clothes_name) or ("メンズ" in clothes_name and "レディース" in clothes_name):
    #     sex = 'unisex'
    # elif "女" in clothes_name or "スカート" in clothes_name or "レディース" in clothes_name or "セクシー" in clothes_name or "嬢" in clothes_name:
    #     sex = 'woman'
    # elif "男" in clothes_name or "メンズ" in clothes_name or "mens" in clothes_name:
    #     sex = 'men'
    # else:
    #     sex_list = ['men', 'woman', 'unisex']
    #     sex = random.choice(sex_list)

    # ここで既存のレコードを更新する
    # cur.execute(f"""
    #     UPDATE clothesdetail
    #     SET sex = '{sex}'
    #     WHERE clothesId = {clothes_id}
    # """)
    
# cur.execute("DROP TABLE review")
    
cur.execute("""
            CREATE TABLE IF NOT EXISTS review (
                id INT AUTO_INCREMENT UNIQUE KEY,
                review VARCHAR(255),
                userId INT,
                clothesId INT,
                PRIMARY KEY (clothesId, userId),
                FOREIGN KEY (clothesId) REFERENCES clothes (id),
                FOREIGN KEY (userId) REFERENCES customerInfo (id)
            )
            """)



cur.execute("""
            SELECT id FROM clothes;
            """)

clothesId = cur.fetchall()

for row in clothesId:
    ran = random.randint(0,5)
    print(ran)
    cur.execute(f"INSERT INTO review (review, clothesId, userId) values ('{ran}', {row[0]}, 1)")
    

conn.commit()
