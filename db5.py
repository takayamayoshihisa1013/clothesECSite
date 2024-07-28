import mysql.connector


conn = mysql.connector.connect(
    user="root",
    password="",
    host="localhost",
    database="ecdatabase"
)

cur = conn.cursor()

cur.execute("""
            SELECT clothes.id, clothes.clothesName, clothesDetail.sex 
            FROM clothesdetail 
            JOIN clothes ON clothes.id = clothesDetail.clothesId
            WHERE sex IS NULL;
            """)

data = cur.fetchall()
# print(data)


i = 0
for row in data:
    if ("メンズ" in row[1] and "レディース" in row[1]) or ("男" in row[1] and "女" in row[1]) or  "ユニセックス" in row[1] or "unisex" in row[1] or "Unisex" in row[1] :
        # print(row[1])
        i += 1
        # cur.execute("UPDATE clothesDetail SET sex = %s WHERE clothesId = %s", ("unisex", row[0]))
        pass
    
    elif "男" in row[1] or "メンズ" in row[1] :
        # print(row[1])
        i += 1
        # cur.execute("UPDATE clothesDetail SET sex = %s WHERE clothesId = %s", ("men", row[0]))
        
        pass
    
    elif "女" in row[1] or "レディース" in row[1] or "婦"in row[1] or "スカート" in row[1] or "嬢" in row[1] or "セクシー" in row[1]:
        # print(row[1])
        i += 1
        # cur.execute("UPDATE clothesDetail SET sex = %s WHERE clothesId = %s", ("woman", row[0]))
        
        pass
    else:
        print(row[0],row[1])
        # i += 1

print(len(data))
print(i)

# conn.commit()
# for row in data:
#     if 

conn.close()