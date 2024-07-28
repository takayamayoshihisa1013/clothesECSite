import mysql.connector



conn = mysql.connector.connect(
    user="root",
    password="",
    host="localhost",
    database="ecdatabase"
)

cur = conn.cursor()

# cur.execute("DROP TABLE kart")


# cur.execute("""
#             CREATE TABLE IF NOT EXISTS clickCounter (
#                 userId INT,
#                 clothesId INT,
#                 date DATE DEFAULT CURRENT_DATE,
#                 PRIMARY KEY(userId, clothesId),
#                 FOREIGN KEY (userId) REFERENCES customerInfo(id),
#                 FOREIGN KEY (clothesId) REFERENCES clothes(id) 
#             )
#             """)


# cur.execute("""
#             CREATE TABLE IF NOT EXISTS favorite(
#                 userId INT,
#                 clothesId INT,
#                 PRIMARY KEY(userId, clothesId),
#                 FOREIGN KEY(userId) REFERENCES customerInfo(id),
#                 FOREIGN KEY(clothesId) REFERENCES clothes(id)
#             )
#             """)

cur.execute("""
            CREATE TABLE IF NOT EXISTS kart(
                userId INT,
                clothesId INT,
                clothesImage VARCHAR(256),
                clothesSize CHAR(1),
                count INT,
                datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY(userId, clothesId, clothesSize),
                FOREIGN KEY(userId) REFERENCES customerInfo(id),
                FOREIGN KEY(clothesId) REFERENCES clothes(id)
            )
            """)

# cur.execute("""
#             CREATE TABLE IF NOT EXISTS buyList (
                
#             )
#             """)

# cur.execute("""
#             SELECT  clothesImage.img1, clothesDetail.type, clothes.clothesName, clothes.price, clothes.id, review.review 
#                     from clothes 
#                     JOIN clothesImage ON clothes.id = clothesImage.clothesId 
#                     JOIN clothesDetail ON clothes.id = clothesDetail.clothesId 
#                     JOIN review ON clothes.id = review.clothesId
#                     ORDER BY clothes.id ASC
#                     ;""")

# data = cur.fetchall()
# for row in data:
#     print(row)

conn.commit()
conn.close()