import os
import mysql.connector
import shutil

dbname = "ecdatabase"
    
conn = mysql.connector.connect(
    user='root',
    password='',
    host='localhost',
    database=dbname
)

cur = conn.cursor()

cur.execute("""
            SELECT clothesdetail.type, clothesdetail.sex, clothesimage.img1 , clothesimage.img2 ,
            clothesimage.img3 , clothesimage.img4 , clothesimage.img5 , clothesimage.img6 ,
            clothesimage.img7 , clothesimage.img8 
            FROM clothesdetail 
            JOIN clothesimage ON clothesdetail.clothesId = clothesimage.clothesId;
            """)

data = cur.fetchall()



down_path = "./static/images/clothes"
source_folder = "./static/images/clothes/hewほんもの/"

image_files = [f for f in os.listdir(source_folder) if f.endswith((".png", "jpg", "jpeg"))]

# print(image_files)

for row in data:
    # print(row[1])
    
    if row[1] != None:
        # print(row[0])
        for i in range(2, 10):
            # print(row[i])
            if "./static/images/clothes/" + row[0] + "/" != row[i]:
                # print(row[i])
                if row[0] == "jacket":
                    # print(row[i][31:])
                    source_path =  source_folder + row[i][31:]
                elif row[0] == "pants":
                    # print(row[i][30:])
                    source_path =  source_folder + row[i][30:]
                elif row[0] == "shirt":
                    # print(row[i][30:])
                    source_path =  source_folder + row[i][30:]
                elif row[0] == "skirt":
                    # print(row[i][30:])
                    source_path =  source_folder + row[i][30:]
                elif row[0] == "t-shirt":
                    # print(row[i][32:])
                    source_path =  source_folder + row[i][32:]
                elif row[0] == "underwear":
                    # print(row[i][34:])
                    source_path =  source_folder + row[i][34:]
                else:
                    print("エラー", row[i])
                
                # source_path = os.path.join()
                # print(row[i])
                print(source_path)
                if not os.path.exists(row[i]):
                    shutil.move(source_path, row[i])
                    print("保存")
                else:
                    print("無視")
                
                
                print()
                
                
                
                
                

# print(image_files)


conn.close()