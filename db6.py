import mysql.connector
from datetime import datetime, timedelta


conn = mysql.connector.connect(
    user="root",
    password="",
    host="localhost",
    database="ecdatabase"
)
cur = conn.cursor()


# cur.execute("""
#             ALTER TABLE siteCounter
#             ADD COLUMN dateClickCounter INT DEFAULT 0
#             """)

cur.execute("""
            UPDATE buyList
            SET 
                postCode = %s,
                city = %s
            """,
            ("1250032", "東京都葛飾区水元3-2-9"))


now = datetime.now()
one = datetime.now().date() - timedelta(days=1)
two = datetime.now().date() - timedelta(days=2)
three = datetime.now().date() - timedelta(days=3)
four = datetime.now().date() - timedelta(days=4)
five = datetime.now().date() - timedelta(days=5)

print(now,one,two,three,four,five)


# cur.execute("""
#             ALTER TABLE buyList
#             ADD COLUMN postCode char(7), 
#             ADD COLUMN city varchar(255)
#             """)

# cur.execute("""
            
#             """)




# for i in range(1, 9):
#     cur.execute(f"""
#                 UPDATE clothesImage 
#                 SET 
#                     img{i}  = REPLACE(img{i}, "./", "")
#                 WHERE img{i} LIKE './%';
#                 """)
    
# conn.commit()


# cur.execute("""
#             ALTER TABLE customerInfo
#             ADD COLUMN last_login DATETIME
#             """)


# cur.executemany("""
#             INSERT INTO customerInfo(last_login) VALUE (%s)
#             """,([now,],[now,],[now,]))
now = datetime.now()
# cur.execute("""
#             UPDATE customerInfo
#             SET last_login = %s
#             """,(now,))


# cur.executemany("INSERT INTO siteCounter(date, visitCount) VALUES(%s,%s)",
#                 ([one,300],[two,10],[three,140],[four,324],[five,54]))

# cur.execute("""
#             CREATE TABLE IF NOT EXISTS siteCounter(
#             date DATE DEFAULT CURRENT_DATE,
#             visitCount INT DEFAULT 0,
#             PRIMARY KEY(date)
#             )
#             """)

# cur.execute("""
#             CREATE TABLE IF NOT EXISTS buyList(
#                 userId INT,
#                 clothesId INT,
#                 clothesName VARCHAR(255),
#                 clothesSize CHAR(1),
#                 clothesImage VARCHAR(255),
#                 count INT,
#                 datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#                 FOREIGN KEY(userId) REFERENCES customerInfo(id),
#                 FOREIGN KEY(clothesId) REFERENCES clothes(id)
#             )
#             """)

# cur.execute("""
#             CREATE TABLE IF NOT EXISTS inquiry (
#                 inquiryId INT AUTO_INCREMENT,
#                 name VARCHAR(255),
#                 email VARCHAR(255),
#                 zipcode char(8),
#                 prefecture VARCHAR(255),
#                 city VARCHAR(255),
#                 tel INT,
#                 text VARCHAR(255),
#                 PRIMARY KEY (inquiryId)
#             )
#             """)

# cur.execute("""SELECT * FROM inquiry""")

# cur.execute("""
#             UPDATE clothes
#             SET stock = stock - %s
#             """,(10,))


# print(cur.fetchall())



conn.commit()