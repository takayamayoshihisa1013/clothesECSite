import os
# import random
import requests
import time

import json


# フォルダの中身の画像を読み取るために必要なモジュール
import glob

with open("./スクレイピング/Amazon.co.jp _ skirt.json", "r", encoding="utf-8") as f:
    di = json.load(f)  # f はファイルオブジェクトであり、文字列ではありません

li = []
img_li = []
for i in range(len(di)):
    # print(str(di[i]["asizebaseplus1"]))
    li.append(str(di[i]["asizebaseplus1"]))
    img_li.append(str(di[i]["画像URL"])) 

print(li)






                



# print(img_li)
imgtest = []
for i in range(len(li)):
    for j in range(i):
        if li[i] == li[j] and i != j:
            imgtest.append(img_li[i])
            
# print(imgtest)

uniLi = list(set(li))





result_list = [[item for item in li if item == element] for element in uniLi]


# 各要素をキーとし、インデックスを値とした辞書を作成
index_dict = {}
for index, item in enumerate(li):
    if item not in index_dict:
        index_dict[item] = [index]
    else:
        index_dict[item].append(index)

# 辞書をリストに変換
# print(index_dict)
result_list = list(index_dict.values())

print(len(result_list))








for i in range(len(result_list)):
    for j in range(len(result_list[i])):
        if img_li[result_list[i][j]] == "":
            break
        # print(len(result_list[i]))5
        print(img_li[result_list[i][j]])
        # print()
        url = img_li[result_list[i][j]]
        
        res = requests.get(url)
        
        print(i)
        if res.status_code == 200:
            
        
            file_name = os.path.join(r"C:\hal\hew\サイト\static\images\clothes\skirt", os.path.basename(url))
            # ファイル保存
            with open(file_name, "wb") as f:
                f.write(res.content)

            print(f"画像を保存しました:{url}")
            
        
        else:
            print("保存に失敗しました")
        
        time.sleep(15)
    print(i)

# # print(len(result_list))
# print(result_list)
# print(index_dict[0])

# print(img_li[result_list[0][2]])

# print(r"C:\hal\hew\サイト\static\images\pants")

print(len(result_list))

# files = glob.glob("./static/images/clothes/shirt/*")

# # for file in files:
# #     print(file)
# print(files)