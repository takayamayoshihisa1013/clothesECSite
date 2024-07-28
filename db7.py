import mysql.connector
from datetime import datetime, timedelta


conn = mysql.connector.connect(
    user="root",
    password="",
    host="localhost",
    database="ecdatabase"
)
cur = conn.cursor()



cur.execute("""
            CREATE TABLE IF NOT EXISTS feature(
                id INT AUTO_INCREMENT,
                date DATE DEFAULT CURRENT_DATE,
                topPageText VARCHAR(255),
                pageName VARCHAR(255),
                featureImg VARCHAR(255),
                featureFileName VARCHAR(255),
                pageShow CHAR(4) DEFAULT 'hide',
                PRIMARY KEY(id)
            )
            """)

# cur.execute("INSERT INTO feature(featureUrl,topPageText,featureImg,featureFileName) VALUES (%s,%s,%s,%s)",
#             ("feature1", "この冬人気だった服を集めました！。この冬流行りに乗ってみませんか？", "static/images/feature/9aeefcb6d9a01f4ef528e5a717c9adbb.webp","feature1"))


conn.commit()
