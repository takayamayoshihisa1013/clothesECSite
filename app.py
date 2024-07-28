import time
import base64
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import japanize_matplotlib
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, session, redirect, url_for
# import requests
import mysql.connector

# でコード要員
import urllib.parse

# ファイルの場所指定要員
import os
# 時間取得要員
from datetime import datetime, timedelta

import glob

import random

# グラフを出す
import matplotlib
matplotlib.use('Agg')

# gmailAPI
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from email.mime.text import MIMEText



app = Flask(__name__)
app.secret_key = 'hew'


# ログイン状況初期値


# acount = ""
# log = ""
# account_detail = ""


# if login == 1:
#     userName =

def database_connection():
    dbname = "ecdatabase"

    conn = mysql.connector.connect(
        user='root',
        password='',
        host='localhost',
        database=dbname
    )

    cur = conn.cursor()

    return conn, cur


def loginProcess(login):

    a = ""
    last_a = ""

    if "userName" in session:
        # info = "<a href='/account'>アカウント情報</a>"
        acount = f"<p>{session['userName']}さん</p>"
        log = "Log Out"
        account_detail = """<ul class="account">
                    <form action="">
                        <div>
                            <li class="list1"><a href="/registration">出品</a></li>
                            <li class="list2"><a href="/salesManagement">売上管理</a></li>
                        </div>
                        <div>
                            <li class="list1"><a href="/favorite">お気に入り商品</a></li>
                            <li class="list2"><a href="/kart">カート・購入履歴</a></li>
                        </div>
                    </form>
                </ul>"""
        print(login)

        if session["id"] == "1":
            a += "<a href='/site_administrator'>"
            last_a += "</a>"
            print("1です")

    else:
        # info = "<a><s>アカウント情報</s></a>"
        acount = ""
        log = "Log In"
        account_detail = ""
        print(login)
        
    
    footer_tag = """
        <footer>
        <div class="footer-box">
            <div class="category">
                <h2>カテゴリー</h2>
                <form action="/result">
                <div class="category-top">
                    

                        <ul class="category-box">
                            <h3>メンズ</h3>
                            <li><button type="submit" name="keyWord" value="men t-shirt" class="footer_button">t-shirt</button></li>
                            <li><button type="submit" name="keyWord" value="men shirt" class="footer_button">shirt</button></li>
                            <li><button type="submit" name="keyWord" value="men jacket" class="footer_button">jacket</button></li>
                            <li><button type="submit" name="keyWord" value="men pants" class="footer_button">pants</button></li>
                            <li><button type="submit" name="keyWord" value="men underwear" class="footer_button">underwear</button></li>
                        </ul>
                        <ul class="category-box">
                            <h3>レディース</h3>
                            <li><button type="submit" name="keyWord" value="woman t-shirt" class="footer_button">t-shirt</button></li>
                            <li><button type="submit" name="keyWord" value="woman shirt" class="footer_button">shirt</button></li>
                            <li><button type="submit" name="keyWord" value="woman jacket" class="footer_button">jacket</button></li>
                            <li><button type="submit" name="keyWord" value="woman pants" class="footer_button">pants</button></li>
                            <li><button type="submit" name="keyWord" value="woman skirt" class="footer_button">skirt</button></li>
                            <li><button type="submit" name="keyWord" value="woman underwear" class="footer_button">underwear</button></li>
                        </ul>
                        <ul class="category-box">
                            <h3>キッズ</h3>
                            <li><button type="submit" name="keyWord" value="kids t-shirt" class="footer_button">t-shirt</button></li>
                            <li><button type="submit" name="keyWord" value="kids shirt" class="footer_button">shirt</button></li>
                            <li><button type="submit" name="keyWord" value="kids jacket" class="footer_button">jacket</button></li>
                            <li><button type="submit" name="keyWord" value="kids pants" class="footer_button">pants</button></li>
                            <li><button type="submit" name="keyWord" value="kids skirt" class="footer_button">skirt</button></li>
                            <li><button type="submit" name="keyWord" value="kids underwear" class="footer_button">underwear</button></li>
                        </ul>
                    
                    </div>
                </form>
            </div>
            <div class="snsbox">
                <h2>公式SNS</h2>
                <ul class="footer-sns">
                    <li class="footer-instagram"><a href=""><i class="fab fa-instagram"></i></a></li>
                    <li class="footer-twitter"><a href=""><i class="fab fa-twitter"></i></a></li>
                    <li class="footer-line"><a href=""><i class="fab fa-line"></i></a></li>
                    <li class="footer-tiktok"><a href=""><i class="fab fa-tiktok"></i></a></li>
                </ul>
            </div>
            <div class="toppage">
                <!-- <a href="" id="page-top"><img src="/static/images/logo/neteru.png"></a> -->
                <a href="#page-top" id="scroll-to-top"><img src="static/images/logo/neteru.png" id="scroll_top_button"></a>
            </div>
        </div>
        <small>© 2023 SHEEP Inc. All Rights Reserved.</small>
    </footer>
    """ 
    
    session["last_page"] = request.path + "?" + request.query_string.decode("utf-8")

    print(session)
    return acount, log, account_detail, a, last_a, footer_tag


# ホーム
@app.route("/")
def index():

    # print(userName)

    now = datetime.now().date()

    # データベース読み込み

    dbname = "ecdatabase"

    conn = mysql.connector.connect(
        user='root',
        password='',
        host='localhost',
        database=dbname
    )

    cur = conn.cursor()

    cur.execute("""
                INSERT INTO siteCounter(date, visitCount) VALUE (%s, 1)
                ON DUPLICATE KEY UPDATE visitCount = visitCount + 1
                """, (now,))

    conn.commit()

    # 一番最初のスライドショー
    cur.execute("""
                SELECT clothesImage.img1, clothes.id
                FROM clothes
                JOIN clothesImage ON clothes.id = clothesImage.clothesId
                ORDER BY buyCounter DESC
                LIMIT 30;
                """)

    slideClothes = cur.fetchall()

    slideClothesData = ""
    slideCounter = 0
    for row in slideClothes:
        if slideCounter == 39:
            print()
            slideClothesData += f"<div class='s_img last'><img src='{row[0]}' alt='' class='div_img'><button type='submit' class='submit' name='submit' value='submit{row[1]}'></button></div>"
        else:
            slideClothesData += f"<div class='s_img'><img src='{row[0]}' alt='' class='div_img'><button type='submit' class='submit' name='submit' value='submit{row[1]}'></button></div>"

        slideCounter += 1
        print(slideCounter)

    # jacketのスライドショー
    cur.execute("""
                
                SELECT clothesImage.img1, clothes.id
                FROM clothes
                JOIN clothesImage ON clothes.id = clothesImage.clothesId 
                JOIN clothesDetail ON clothes.id = clothesDetail.clothesId 
                WHERE clothesDetail.type = 'jacket' ORDER BY RAND() LIMIT 10;
                
                """)

    slideJacket = cur.fetchall()

    jacketTopList = ""
    for row in slideJacket:
        print(row)

        jacketTopList += f"<div class='s_img'><img src='{row[0]}' alt=''  class='div_img'><button type='submit' class='submit' name='submit' value='submit{row[1]}'></button></div>"

    # shirtのスライドショー
    cur.execute("""
                SELECT clothesImage.img1, clothes.id
                FROM clothes
                JOIN clothesImage ON clothes.id = clothesImage.clothesId 
                JOIN clothesDetail ON clothes.id = clothesDetail.clothesId 
                WHERE clothesDetail.type = 'shirt' ORDER BY RAND() LIMIT 10;
                """)

    slideShirt = cur.fetchall()

    shirtTopList = ""
    for row in slideShirt:
        print(row)

        shirtTopList += f"<div class='s_img'><img src='{row[0]}' alt=''  class='div_img'><button type='submit' class='submit' name='submit' value='submit{row[1]}'></button></div>"

    # t-shirtのスライドショー
    cur.execute("""
                
                SELECT clothesImage.img1, clothes.id
                FROM clothes
                JOIN clothesImage ON clothes.id = clothesImage.clothesId
                JOIN clothesDetail ON clothes.id = clothesDetail.clothesId 
                WHERE clothesDetail.type = 't-shirt' ORDER BY RAND() LIMIT 10;
                
                """)

    slideT_shirt = cur.fetchall()

    t_shirtTopList = ""
    for row in slideT_shirt:
        print(row)

        t_shirtTopList += f"<div class='s_img'><img src='{row[0]}' alt=''  class='div_img'><button type='submit' class='submit' name='submit' value='submit{row[1]}'></button></div>"

    # pantsのスライドショー
    cur.execute("""
                
                SELECT clothesImage.img1, clothes.id
                FROM clothes
                JOIN clothesImage ON clothes.id = clothesImage.clothesId
                JOIN clothesDetail ON clothes.id = clothesDetail.clothesId 
                WHERE clothesDetail.type = 'pants' ORDER BY RAND() LIMIT 10;
                
                """)

    slidePants = cur.fetchall()

    pantsTopList = ""
    for row in slidePants:
        print(row)

        pantsTopList += f"<div class='s_img'><img src='{row[0]}' alt=''  class='div_img'><button type='submit' class='submit' name='submit' value='submit{row[1]}'></button></div>"

    # skirtのスライドショー
    cur.execute("""
                
                SELECT clothesImage.img1, clothes.id
                FROM clothes
                JOIN clothesImage ON clothes.id = clothesImage.clothesId
                JOIN clothesDetail ON clothes.id = clothesDetail.clothesId 
                WHERE clothesDetail.type = 'skirt' ORDER BY RAND() LIMIT 10;
                
                """)

    slideSkirt = cur.fetchall()

    skirtTopList = ""
    for row in slideSkirt:
        print(row)

        skirtTopList += f"<div class='s_img'><img src='{row[0]}' alt=''  class='div_img'><button type='submit' class='submit' name='submit' value='submit{row[1]}'>></button></div>"

    # underwearのスライドショー
    cur.execute("""
                
                SELECT clothesImage.img1, clothes.id
                FROM clothes
                JOIN clothesImage ON clothes.id = clothesImage.clothesId
                JOIN clothesDetail ON clothes.id = clothesDetail.clothesId
                WHERE clothesDetail.type = 'underwear' ORDER BY RAND() LIMIT 10;
                """)

    slideUnderwear = cur.fetchall()

    underwearTopList = ""
    for row in slideUnderwear:
        print(row)

        underwearTopList += f"<div class='s_img'><img src='{row[0]}' alt='' class='div_img'><button type='submit' class='submit' name='submit' value='submit{row[1]}'></button></div>"

    # if login == "in":
    # # info = "<a href='/account'>アカウント情報</a>"
    #     acount = f"<p>{userName}さん</p>"
    #     log = "Log Out"
    #     account_detail = """<ul class="account">
    #                 <form action="/account">
    #                     <div>
    #                         <li class="list1">アカウント情報<button class="submit" type="submit"></button></li>
    #                         <li class="list2">出品・売上管理<button class="submit" type="submit"></button></li>
    #                     </div>
    #                     <div>
    #                         <li class="list1">お気に入り商品<button class="submit" type="submit"></button></li>
    #                         <li class="list2">購買履歴<button class="submit" type="submit"></button></li>
    #                     </div>
    #                 </form>
    #             </ul>"""
    #     print(login)
    # else:
    # # info = "<a><s>アカウント情報</s></a>"
    #     acount = ""
    #     log = "Log In"
    #     account_detail = ""
    #     print(login)
    
    
    
    cur.execute("""
                SELECT date, topPageText,  featureImg, id,pageShow
                FROM feature
                """)
    
    feature_data = cur.fetchall()
    
    new_slider = ""
    for data in feature_data:
        
        if data[4] == "show":
            
            new_slider += f"""
                        <div class="feature">
                            
                                <div class="newsSlider_img">

                                    <img src="static/images/feature/{data[2]}" alt="">

                                </div>
                                <div class="news_detail">
                                    <h4>{data[0]}</h4>
                                    <p>{data[1]}</p>
                                </div>
                            <button type="submit" name="feature" value="{data[3]}" class="submit">
                        </div>
                    """
    
    
    
    

    common_header = loginProcess(login)

    print(len(slideClothes))
    
    
    cur.execute("""
                SELECT clothes.clothesName,
                clothes.productText, 
                clothes.price,
                clothesImage.img1,
                clothes.id
                FROM clothes
                JOIN clothesDetail ON clothes.id = clothesDetail.clothesId
                JOIN clothesImage ON clothesImage.clothesId = clothes.id
                ORDER BY clothes.id DESC
                LIMIT 10
                """)
    
    new_product_data = cur.fetchall()
    
    new_product_tag = ""
    product = ""
    i = 0
    for data in new_product_data:
        print()
        
        if len(data[0]) >= 20:
        
            clothes_name = data[0][:20] + "..."
        else:
            clothes_name = data[0]
            
        if len(data[1]) >= 200:
            clothes_text = data[1][:200] + "..."
            
        else:
            clothes_text = data[1]
        clothes_price = data[2]
        img = data[3]
        
        id = data[4]
        
        
        
        
        if i == 0:
            if len(data[0]) >= 40:
        
                clothes_name = data[0][:40] + "..."
            else:
                clothes_name = data[0]
            new_product_tag += f"""
                <div class="product_top">
                    <div class="top_img">
                        <img src="{img}" alt="">
                    </div>
                    <div class="title_text">
                        <h2>{clothes_name}</h2>
                        <p>{clothes_text}</p>
                    </div>
                    <div class="price">
                        <h2 style="color:red">￥{clothes_price}</h2>
                    </div>
                    <button type="submit" class="submit" name="submit" value="submit{id}"></button>
                </div>
            """
        elif i  == 1 or i == 4 or i == 7:
            product += f"""
                <div class="row">
                
                    <div class="frame">
                        <div class="img">
                            <img src="{img}" alt="">
                        </div>
                        <div class="title">
                            <h3>{clothes_name}</h3>
                        </div>
                        <div class="price">
                            <h3 style="color:red">￥{clothes_price}</h3>
                        </div>
                        <button type="submit" class="submit" name="submit" value="submit{id}"></button>
                    </div>
                
            """
        elif i == 3 or i == 6 or i == 9:
            product += f"""
                    <div class="frame">
                        <div class="img">
                            <img src="{img}" alt="">
                        </div>
                        <div class="title">
                            <h3>{clothes_name}</h3>
                        </div>
                        <div class="price">
                            <h3 style="color:red">￥{clothes_price}</h3>
                        </div>
                        <button type="submit" class="submit" name="submit" value="submit{id}"></button>
                    </div>
                </div>
            """
        else:
            product += f"""
                
                    
                        <div class="frame">
                            <div class="img">
                                <img src="{img}" alt="">
                            </div>
                            <div class="title">
                                <h3>{clothes_name}</h3>
                            </div>
                            <div class="price">
                                <h3 style="color:red">￥{clothes_price}</h3>
                            </div>
                            <button type="submit" class="submit" name="submit" value="{id}"></button>
                        </div>
                    
                
            """
        
        
        i += 1
    
    
    

    cur.close()

    # print(slideClothesData)
    print(common_header)
    # print(session["id"])

    return render_template("./page/index.html", acount=common_header[0], log=common_header[1], slideClothesData=slideClothesData, jacketTopList=jacketTopList, t_shirtTopList=t_shirtTopList, shirtTopList=shirtTopList, pantsTopList=pantsTopList, skirtTopList=skirtTopList, underwearTopList=underwearTopList, account_detail=common_header[2], a=common_header[3], a_last=common_header[4], new_slider = new_slider, footer_tag = common_header[5], new_product_tag = new_product_tag, product = product)


# ログイン初回アクセス
@app.route("/login")
def login():
    print("ログインしたいよ")

    miss = "not_miss"
    
    return render_template("./userInfo/login.html", miss = miss)


# ログイン可否
@app.route("/login", methods=["POST"])
def loginCheck():

    print("ろぐいんするよ")
    # js初期値
    script = ""

    # 入力されたメールアドレス
    inputEmail = request.form["mail"]
    # 入力されたパスワード
    inputPass = request.form["pass"]
    # print(userName)

    # データベースの情報と照合

    dbname = "ecdatabase"

    conn = mysql.connector.connect(
        user='root',
        password='',
        host='localhost',
        database=dbname
    )

    cur = conn.cursor()

    # データを取り出すクエリを実行
    cur.execute("""
                SELECT COUNT(*), id, lastName, firstName
                FROM customerInfo
                WHERE email = %s AND pass = %s
                """, (inputEmail, inputPass))
    # データを取る
    data = cur.fetchone()
    print(data)
    # 1列ごとに全てのデータを取る
    
    
    

        # 照合
    if data[0] != 0:
            # 照合完了
        print("一致するデータがあったよ！")

        # # ログイン状態にする
        # global login
        # # global userName
        # global id

        # login = "in"
        session['userName'] = data[2] + data[3]
        session['id'] = str(data[1])   # 整数を文字列に変換
        print(session['id'])
        print(id)

        now = datetime.now()
        cur.execute("""
        UPDATE customerInfo
        SET last_login = %s
        WHERE id = %s
        """, (now, session["id"]))

        conn.commit()
        script = "<script src='static/js/login.js'></script>"
        error = ""
        
        

    else:
        print("一致するデータがなかったよ...")
        script = ""
        error = "<h3>メールアドレス、又はパスワードが違います</h3>"
        miss = "miss"
        
        return render_template("userInfo/login.html", script=script, error=error, miss = miss)
            
    return redirect(session["last_page"])
    
    
@app.route("/signup_mail", methods=["GET","POST"])
def signup_mail():
    
    if request.method == "GET":
        tag = """
        <article class="before">
            <h3>登録に使用するメールアドレスを入力してください。</h3>
            <form action="/signup_mail" method="post">
                <input type="email" name="email">
                <button type="submit">送信</button>
            </form>
        </article>
        """
    
    if request.method == "POST":
        email = request.form.get("email")
        print(email)
        try:
            def message_base64_encode(message):
                return base64.urlsafe_b64encode(message.as_bytes()).decode()

            def main(email):
                scopes = ["https://mail.google.com/"]
                creds = Credentials.from_authorized_user_file("./json/token.json", scopes)
                service = build("gmail", "v1", credentials=creds)
                message = MIMEText("SHEEP登録用ページ：http://127.0.0.1:5000/signup\n身に覚えがない場合はアクセスをしないでください。")
                # 宛先
                message["To"] = email
                message["From"] = "SHEEP公式 <rurariyudayo@gmail.com>"
                message["Subject"] = "SHEEP登録用ページURL"
                raw = {"raw": message_base64_encode(message)}
                service.users().messages().send(
                    userId = "me",
                    body=raw
                ).execute()
            main(email)
                
            print("成功")
            tag = """
            <article class="after">
                <div>
                    <img src="static/images/logo/e-mail-send_icon_1148.png">
                </div>
                <h1>入力したメールアドレスをご確認ください。</h1>
                <h3>もし受信トレイに見当たらなかった場合は迷惑メールに含まれている可能性があります。</h3>
                <h3>登録してからのページ遷移をおすすめします</h3>
                <form action="/login">
                    <button type="submit">ログインする</button>
                </form>
            </article>
            """
            
            
        except:
            tag = "エラーが発生しました。"
        
        
            
        
    return render_template("./userInfo/signup_mail.html", tag = tag)


# サインアップページ初回アクセス
@app.route("/signup")
def signup():
    print("サインアップしたいよ")

    return render_template("./userInfo/signup.html")


# サインアップ可否
@app.route("/signup", methods=["POST"])
def signupCheck():

    # ユーザー名
    lastName = urllib.parse.unquote(request.form["lastName"])
    firstName = urllib.parse.unquote(request.form["firstName"])
    print(lastName + firstName)
    print(request.form)
    # メアド
    email = request.form["email"]
    # パス1
    pass1 = request.form["pass1"]
    # パス2
    pass2 = request.form["pass2"]
    
    post_code = request.form["post_code"]
    
    
    city = request.form["prefecture"] + request.form["city"] + request.form["town"] + request.form["address"] 

    # 照合 & メールアドレスがすでにないかの確認

    dbname = "ecdatabase"

    conn = mysql.connector.connect(
        user='root',
        password='',
        host='localhost',
        database=dbname
    )

    # カーソル
    cur = conn.cursor()

    # テーブルが存在しない場合、テーブルを作成
    create_table_query = """
        CREATE TABLE IF NOT EXISTS customerInfo (
        id INT AUTO_INCREMENT PRIMARY KEY,
        lastName VARCHAR(255),
        firstName VARCHAR(255),
        email VARCHAR(255),
        pass VARCHAR(255),
        last_login datetime,
        postCode char(7),
        city varchar(255)
    )
    """
    cur.execute(create_table_query)

    # emailデータを取得
    cur.execute("SELECT email FROM customerInfo")
    emailData = cur.fetchall()

    # MySQL接続を閉じる
    cur.close()
    conn.close()

    emailError = ""

    for row in emailData:
        print(row[0])
        if row[0] == email:

            emailError = "そのメールアドレスは登録されています"
            print("そのメールアドレスは登録されています")
            print("break")
            break

        else:
            emailError = ""
            print("重複ないよ！")
            print(row[0], email)

    print(emailError)

    if pass1 == pass2 and emailError == "":
        # JS追加
        script = "<script src='static/js/signup.js'></script>"
        # えらーなにもなし
        passError = ""
        OKtext = f"""<article class="two"><h2>登録完了しました。</h2><h4>ようこそ{lastName}{firstName}さん!</h3><h4>10秒後にログインページに移動します。</h4></article>"""

        # 登録処理

        # データベースの名前
        dbname = "ecdatabase"

        conn = mysql.connector.connect(
            user='root',
            password='',
            host='localhost',
            database=dbname
        )

        # カーソル
        cur = conn.cursor()

        # データベースに追加する
        cur.execute(
            f"INSERT INTO customerInfo (lastName,firstName,email,pass,postCode,city) values('{lastName}','{firstName}','{email}','{pass1}', '{post_code}','{city}')")

        # "CREATE TABLE customerInfo(id INTEGER PRIMARY KEY AUTOINCREMENT, lastName STRING, firstName STRING, email NONE, pass STRING)"
        conn.commit()
        cur.close()
        conn.close()

        print("サインアップできたよ")

    else:
        OKtext = ""
        passError = "パスワードが一致しない、又は入力されたメールアドレスはすでに登録されています"
        script = ""

    return render_template("./userInfo/signup.html", passError=passError, script=script,
                           text=OKtext, emailError=emailError)


# アカウントページ
@app.route("/account", methods=["GET"])
def account():
    common_header = loginProcess(login)
    # print(userName)

    dbname = "ecdatabase"

    conn = mysql.connector.connect(
        user='root',
        password='',
        host='localhost',
        database=dbname
    )
    cur = conn.cursor()

    global id
    # global userName
    # userName = userName

    cur.execute(f"""
                SELECT id, email, lastname, firstname from customerInfo WHERE id = {id};
                """)

    userEmail = cur.fetchone()

    print(userEmail)
    # print("aa")

    print(id)
    return render_template("./userInfo/account.html", acount=common_header[0], log=common_header[1], account_detail=common_header[2], id=id, userEmail=userEmail[1], userName=userName)


@app.route("/account", methods=["POST"])
def account_post():

    dbname = "ecdatabase"

    conn = mysql.connector.connect(
        user='root',
        password='',
        host='localhost',
        database=dbname
    )
    cur = conn.cursor()

    cur.execute(f"""
                SELECT email from customerInfo;
                """)

    cur.fetchall()

    # for row in cur.fetchall():
    print("aa")
    print(id)

    clothes_name = request.form["clothes_name"]
    img1 = request.files["img1"]
    img2 = request.files["img2"]
    img3 = request.files["img3"]
    img4 = request.files["img4"]
    img5 = request.files["img5"]
    img6 = request.files["img6"]
    img7 = request.files["img7"]
    img8 = request.files["img8"]
    print(img3)

    category = request.form["category"]
    price = int(request.form["price"])
    stock = int(request.form["stock"])
    material = request.form["material"]
    productText = request.form["productText"]
    color1 = request.form["color1"]

    color2 = request.form["color2"]
    color3 = request.form["color3"]
    color4 = request.form["color4"]
    color5 = request.form["color5"]
    color6 = request.form["color6"]
    color7 = request.form["color7"]
    color8 = request.form["color8"]
    print(color4)

    img1.save(os.path.join(f'./static/images/{category}', img1.filename))

    if img2 == "<FileStorage: '' ('application/octet-stream')>":
        img2 = ""
    if img3 == "<FileStorage: '' ('application/octet-stream')>":
        img3 = ""
    if img4 == "<FileStorage: '' ('application/octet-stream')>":
        img4 = ""
    if img5 == "<FileStorage: '' ('application/octet-stream')>":
        img5 = ""
    if img6 == "<FileStorage: '' ('application/octet-stream')>":
        img6 = ""
    if img7 == "<FileStorage: '' ('application/octet-stream')>":
        img7 = ""
    if img8 == "<FileStorage: '' ('application/octet-stream')>":
        img8 = ""
    # print(img.filename)

    # print(price)
    # print(stock)
    # print(material)
    # print(datetime.datetime.now().replace(second=0, microsecond=0))
    date = str(datetime.datetime.now().replace(second=0, microsecond=0))
    # print(category)

    # テーブルの存在確認

    # 存在確認するテーブルの指定
    table_check_query = "SHOW TABLES LIKE 'clothes'"
    cur.execute(table_check_query)
    exist = cur.fetchone()

    if not exist:
        print("存在しなかったよ")
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
        stock INT,
        review DECIMAL(10, 2),
        date TEXT,
        clickCounter INT,
        buyCounter INT,
        productText TEXT,
        type VARCHAR(255),
        userid INT,
        material VARCHAR(255),
        FOREIGN KEY (type) REFERENCES clothesType (type),
        FOREIGN KEY (userid) REFERENCES customerInfo (id),
        FOREIGN KEY (material) REFERENCES material (material)
    )
    """)
    else:
        print("すでにあったよ")

    # プレースホルダーを使用して安全なSQLクエリを実行
    # 商品の追加
    cur.executemany("""
        INSERT INTO clothes (clothesName, price, image1, image2, image3, image4, image5, image6, image7, image8, color1, color2, color3, color4, color5, color6, color7, color8, stock, review, date, clickCounter, buyCounter, productText, type, userid, material) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 0, %s, 0, 0, %s, %s, %s, %s)
        """, [(clothes_name, price, f'./static/images/clothes/{category}/{img1.filename}', f'./static/images/{category}/{img2.filename}', f'./static/images/{category}/{img3.filename}', f'./static/images/{category}/{img4.filename}', f'./static/images/{category}/{img5.filename}', f'./static/images/{category}/{img6.filename}', f'./static/images/{category}/{img7.filename}', f'./static/images/{category}/{img8.filename}', color1, color2, color3, color4, color5, color6, color7, color8, stock, date, productText, category, id, material),])

    conn.commit()
    cur.close()
    conn.close()

    common_header = loginProcess(login)

    return render_template("./userInfo/account.html", acount=common_header[0], log=common_header[1], account_detail=common_header[2])


# 検索結果画面
@app.route("/result", methods=["GET"])
def result():
    search = request.args.get("keyWord")

    print(search)

    common_header = loginProcess(login)

    if search == "":
        print("キーワードなし")
        return redirect(url_for("index"))

    # 絞り込み判定
    splitSearch = search.split()

    if splitSearch[len(splitSearch) - 1] == "old":
        where = ""
        orderBy = "id ASC"
        search = session["keyWord"]

    elif splitSearch[len(splitSearch) - 1] == "new":
        where = ""
        orderBy = "id DESC"
        search = session["keyWord"]

    elif splitSearch[len(splitSearch) - 1] == "high":
        where = ""
        orderBy = "review.review DESC"
        search = session["keyWord"]

    elif splitSearch[len(splitSearch) - 1] == "low":
        where = ""
        orderBy = "review.review ASC"
        search = session["keyWord"]

    elif splitSearch[len(splitSearch) - 1] == "many":
        where = ""
        orderBy = "COUNT(review.review) DESC"
        search = session["keyWord"]

    # 初期もしくはoldだった場合
    else:
        where = ""
        orderBy = "id ASC"
        session["keyWord"] = search
        print("はじめて")

    print(splitSearch)

    dbname = "ecdatabase"

    conn = mysql.connector.connect(
        user='root',
        password='',
        host='localhost',
        database=dbname
    )

    popular_style = ""
    
    cur = conn.cursor()

    # 何も検索されなかった場合全部出す
    if search == "" or search == "productList":

        if where == "":
            pass
        else:
            where = " WHERE " + where

        if orderBy == "":
            pass
        else:
            orderBy = " ORDER BY " + orderBy

        cur.execute("""
                    SELECT  count(id)  from clothes;
                    """)

        count = cur.fetchone()[0]

        cur.execute(f"""
                    SELECT  clothesImage.img1, clothesDetail.type, clothes.clothesName, clothes.price, clothes.id  ,AVG(review.review) ,clothes.stock
                    from clothes
                    JOIN clothesImage ON clothes.id = clothesImage.clothesId
                    JOIN clothesDetail ON clothes.id = clothesDetail.clothesId
                    JOIN review ON clothes.id = review.clothesId
                    {where}
                    GROUP BY review.clothesId
                    {orderBy};
                    """)

        print(f"""
                    SELECT  clothesImage.img1, clothesDetail.type, clothes.clothesName, clothes.price, clothes.id ,review.review ,clothes.stock
                    from clothes 
                    JOIN clothesImage ON clothes.id = clothesImage.clothesId
                    JOIN clothesDetail ON clothes.id = clothesDetail.clothesId 
                    JOIN review ON clothes.id = review.clothesId
                    {where}
                    {orderBy};
                    """)

        image_data = cur.fetchall()
        # タプルになっているので外す

        imageTags = ""
        i = 0
        for row in image_data:
            # print(row[1])

            
            
            
            if len(row[2]) >= 35:
                title = str(row[2][:32]) + "..."
            else:
                title = row[2]

            price = (str(f"{row[3]:,}"))
            review = (row[5])
            
            if float(row[5]) - int(row[5]) != 0:
                print(float(row[5]) - int(row[5]), "結果")
                float_star = "★"
            
            else:
                float_star = ""
            
            
            star_span = f"""<span class="star_before" style="width: {int(row[5]) * 1.2}vw;">{"★" * int(row[5])}</span><span class="star_after" style="width: {float(float(float(row[5]) - int(row[5]) + 0.1) * 1.2)}vw;">{float_star}</span>"""

            

            # ストック
            stock = row[6]
            stock_alert = ""
            if int(stock) <= 30:
                if int(stock) == 0:
                    stock_alert = f"<p class='stock_alert'>在庫切れ</p>"
                else:
                    stock_alert = f"<p class='stock_alert'>在庫は残り{stock}点です</p>"
            else:
                pass

            if i != 0:
                if i % 5 == 0:
                    imageTags += f"<div class='row'><div class='line {row[1]}'><div class='productImg'><img src='{row[0]}' alt='' class='img'></div><div class='productTitle'><h3>{title}</h3></div><div class='priceAndReview'><div class='price'><h4>￥{price}</h4></div><div class='review'><p class='star'>{star_span}</p><p class='review'>{review}</p></div></div>{stock_alert}<button type='submit' class='submit' name='submit' value='submit{row[4]}'></button></div>"
                elif i % 5 == 4:
                    imageTags += f"<div class='line {row[1]}'><div class='productImg'><img src='{row[0]}' alt='' class='img'></div><div class='productTitle'><h3>{title}</h3></div><div class='priceAndReview'><div class='price'><h4>￥{price}</h4></div><div class='review'><p class='star'>{star_span}</p><p class='review'>{review}</p></div></div>{stock_alert}<button type='submit' class='submit' name='submit' value='submit{row[4]}'></button></div></div>"

                else:
                    imageTags += f"<div class='line {row[1]}'><div class='productImg'><img src='{row[0]}' alt='' class='img'></div><div class='productTitle'><h3>{title}</h3></div><div class='priceAndReview'><div class='price'><h4>￥{price}</h4></div><div class='review'><p class='star'>{star_span}</p><p class='review'>{review}</p></div></div>{stock_alert}<button type='submit' class='submit' name='submit' value='submit{row[4]}'></button></div>"

                if i == len(image_data) - 1:
                    imageTags += "</div></form>"

                if i % 50 == 49 and i != len(image_data) - 1:
                    imageTags += f"</form><form action='/product' method='get' id='form{int(i / 49)}' class='productForm'>"
                    print(i)

            else:
                imageTags += f"<form action='/product' method='get' id='form0' class='productForm'><div class='row'><div class='line {row[1]}'><div class='productImg'><img src='{row[0]}' alt='' class='img'></div><div class='productTitle'><h3>{title}</h3></div><div class='priceAndReview'><div class='price'><h4>￥{price}</h4></div><div class='review'><p class='star'>{star_span}</p><p class='review'>{review}</p></div></div>{stock_alert}<button type='submit' class='submit' name='submit' value='submit{row[4]}'></button></div>"
            i += 1
            print(i)

        page = (i / 49) + 1

        search = "全て"

    elif search == "popular":

        popular_style = """ popular """
        
        cur.execute("""
                    SELECT  count(*)  from clothes WHERE 0 < clickCounter ORDER BY clickCounter DESC;
                    """)

        count = cur.fetchone()[0]

        cur.execute("""
                    SELECT  clothesImage.img1, clothesDetail.type, clothes.clothesName, clothes.price, clothes.id ,AVG(review.review) ,clothes.stock
                    from clothes 
                    JOIN clothesImage ON clothes.id = clothesImage.clothesId 
                    JOIN clothesDetail ON clothes.id = clothesDetail.clothesId 
                    JOIN review ON clothes.id = review.clothesId
                    WHERE 0 < clickCounter 
                    GROUP BY review.clothesId
                    ORDER BY buyCounter DESC;
                    """)

        image_data = cur.fetchall()
        # タプルになっているので外す

        imageTags = ""
        i = 0
        for row in image_data:
            # print(row[1])

            if len(row[2]) >= 35:
                title = str(row[2][:32]) + "..."
            else:
                title = row[2]

            price = (str(f"{row[3]:,}"))
            review = (row[5])
            
            if float(row[5]) - int(row[5]) != 0:
                print(float(row[5]) - int(row[5]), "結果")
                float_star = "★"
            
            else:
                float_star = ""
            
            
            star_span = f"""<span class="star_before" style="width: {int(row[5]) * 1.2}vw;">{"★" * int(row[5])}</span><span class="star_after" style="width: {float(float(float(row[5]) - int(row[5]) + 0.1) * 1.2)}vw;">{float_star}</span>"""

            # ストック
            stock = row[6]
            stock_alert = ""
            if int(stock) <= 30:
                if int(stock) == 0:
                    stock_alert = f"<p class='stock_alert'>在庫切れ</p>"
                else:
                    stock_alert = f"<p class='stock_alert'>在庫は残り{stock}点です</p>"
            else:
                pass

            if i != 0:
                if i % 5 == 0:
                    imageTags += f"<div class='row'><div class='line {row[1]}'><div class='productImg'><img src='{row[0]}' alt='' class='img'></div><div class='productTitle'><h3>{title}</h3></div><div class='priceAndReview'><div class='price'><h4>￥{price}</h4></div><div class='review'><p class='star'>{star_span}</p><p class='reviewVal'>{review}</p></div></div>{stock_alert}<button type='submit' class='submit' name='submit' value='submit{row[4]}'></button></div>"
                elif i % 5 == 4:
                    imageTags += f"<div class='line {row[1]}'><div class='productImg'><img src='{row[0]}' alt='' class='img'></div><div class='productTitle'><h3>{title}</h3></div><div class='priceAndReview'><div class='price'><h4>￥{price}</h4></div><div class='review'><p class='star'>{star_span}</p><p class='reviewVal'>{review}</p></div></div>{stock_alert}<button type='submit' class='submit' name='submit' value='submit{row[4]}'></button></div></div>"

                else:
                    imageTags += f"<div class='line {row[1]}'><div class='productImg'><img src='{row[0]}' alt='' class='img'></div><div class='productTitle'><h3>{title}</h3></div><div class='priceAndReview'><div class='price'><h4>￥{price}</h4></div><div class='review'><p class='star'>{star_span}</p><p class='reviewVal'>{review}</p></div></div>{stock_alert}<button type='submit' class='submit' name='submit' value='submit{row[4]}'></button></div>"

                if i == len(image_data) - 1:
                    imageTags += "</div></form>"

                if i % 50 == 49 and i != len(image_data) - 1:
                    imageTags += f"</form><form action='/product' method='get' id='form{int(i / 49)}' class='productForm'>"
                    print(i)

            else:
                imageTags += f"<form action='/product' method='get' id='form0' class='productForm'><div class='row'><div class='line {row[1]}'><div class='productImg'><img src='{row[0]}' alt='' class='img'></div><div class='productTitle'><h3>{title}</h3></div><div class='priceAndReview'><div class='price'><h4>￥{price}</h4></div><div class='review'><p class='star'>{star_span}</p><p class='reviewVal'>{review}</p></div></div>{stock_alert}<button type='submit' class='submit' name='submit' value='submit{row[4]}'></button></div>"
            i += 1
            print(i)

        page = (i / 49) + 1

        search = "人気順"

    # 検索された場合

    else:

        if orderBy == "":
            pass
        else:
            orderBy = "ORDER BY " + orderBy
            print(" ORDER BY " + orderBy)
        # sqlのlike句に入れるためのやつ

        # 服のタイプを確認する用の連想配列
        clothes_type_check = {
            "jacket": ["ジャケット", "jacket"],
            "t-shirt": ["Tシャツ", "t-shirt"],
            "shirt": ["シャツ", "shirt"],
            "pants": ["ズボン", "pants"],
            "skirt": ["skirt", "スカート"],
            "underwear": ["パンツ", "下着", "underwear"],
        }

        # 性別を判断する連動配列
        gender_check = {
            "men": ["男", "男性", "メンズ", "men", "mens", "男性用"],
            "woman": ["女", "女性", "レディース", "woman", "women", "ladies", "Ladies"],
            "kids": ["キッズ", "子供", "子", "kids"],
            "unisex": ["男女", "ユニセックス", "unisex"],
        }

        like = ""

        for i in range(len(splitSearch)):
            print(like, "like")

            # うまく服のタイプの一致を作る
            # where += f"OR clothesDetail.type = {splitSearch[i]}"

            type_key = ""
            for key, clothes_type_row in clothes_type_check.items():
                if splitSearch[i] in clothes_type_row:

                    if where != "" :
                        where += " AND  "
                        print("or")
                    where += f" clothesDetail.type = '{key}'"
                    print(where)
                    type_key = splitSearch[i]

            gender_key = ""

            for key, clothes_gender_row in gender_check.items():
                if splitSearch[i] in clothes_gender_row:

                    if where != "":
                        where += " AND "
                        print("and")
                    where += f"clothesDetail.sex = '{key}'"
                    gender_key = splitSearch[i]

            if splitSearch[i] == "old" or splitSearch[i] == "new" or splitSearch[i] == "high" or splitSearch[i] == "low" or splitSearch[i] == "many":
                pass

            elif type_key != "":
                print("服のタイプが入力されていたため、pass", gender_key)
                pass

            elif gender_key != "":
                print("性別が入力されていたため、pass", gender_key)
                pass

            # whereが何もなかった場合も調べる
            elif i > 0 and like != "(":
                print(splitSearch[i], len(splitSearch))
                if like == "":
                    print()
                    like += f" ( clothesName LIKE '%{splitSearch[i]}%'"
                else:
                    like += f" AND clothesName LIKE '%{splitSearch[i]}%'"
            else:
                print(splitSearch[i], len(splitSearch))
                like += "("
                like += f" clothesName LIKE '%{splitSearch[i]}%'"
        if like != "":
            like += ")"
            if where != "":
                like += " AND "

        print(like + where)

        cur.execute(f"""
                    SELECT COUNT(*)
                    FROM clothes 
                    JOIN clothesDetail ON clothes.id = clothesDetail.clothesId
                    WHERE {like} {where};
                    """)

        count = cur.fetchone()[0]

        cur.execute(f"""
                    SELECT  clothesImage.img1, clothesDetail.type, clothes.clothesName, clothes.price, clothes.id, AVG(review.review) ,clothes.stock
                    from clothes 
                    JOIN clothesImage ON clothes.id = clothesImage.clothesId 
                    JOIN clothesDetail ON clothes.id = clothesDetail.clothesId 
                    JOIN review ON clothes.id = review.clothesId
                    WHERE {like} {where}
                    GROUP BY review.clothesId
                    {orderBy};
                    """)
        
        print(f"""
                    SELECT  clothesImage.img1, clothesDetail.type, clothes.clothesName, clothes.price, clothes.id  from clothes 
                    JOIN clothesImage ON clothes.id = clothesImage.clothesId 
                    JOIN clothesDetail ON clothes.id = clothesDetail.clothesId 
                    JOIN review ON review.clothesId = clothes.id
                    WHERE {like} {where}
                    {orderBy};
                    """)

        image_data = cur.fetchall()
        # タプルになっているので外す

        imageTags = ""
        i = 0
        for row in image_data:
            # print(row[1])

            if len(row[2]) >= 35:
                title = str(row[2][:32]) + "..."
            else:
                title = row[2]

            # なんかこれで数字を3桁区切りにできるらしい
            price = (str(f"{row[3]:,}"))

            review = (row[5])
            
            if float(row[5]) - int(row[5]) != 0:
                print(float(row[5]) - int(row[5]), "結果")
                float_star = "★"
            
            else:
                float_star = ""
            
            
            star_span = f"""<span class="star_before" style="width: {int(row[5]) * 1.2}vw;">{"★" * int(row[5])}</span><span class="star_after" style="width: {float(float(float(row[5]) - int(row[5]) + 0.1) * 1.2)}vw;">{float_star}</span>"""

            # ストック
            stock = row[6]
            stock_alert = ""
            if int(stock) <= 30:
                if int(stock) == 0:
                    stock_alert = f"<p class='stock_alert'>在庫切れ</p>"
                else:
                    stock_alert = f"<p class='stock_alert'>在庫は残り{stock}点です</p>"
            else:
                pass

            if i != 0:
                if i % 5 == 0:
                    imageTags += f"<div class='row'><div class='line {row[1]}'><div class='productImg'><img src='{row[0]}' alt='' class='img'></div><div class='productTitle'><h3>{title}</h3></div><div class='priceAndReview'><div class='price'><h4>￥{price}</h4></div><div class='review'><p class='star'>{star_span}</p><p class='reviewVal'>{review}</p></div></div>{stock_alert}<button type='submit' class='submit' name='submit' value='submit{row[4]}'></button></div>"
                elif i % 5 == 4:
                    imageTags += f"<div class='line {row[1]}'><div class='productImg'><img src='{row[0]}' alt='' class='img'></div><div class='productTitle'><h3>{title}</h3></div><div class='priceAndReview'><div class='price'><h4>￥{price}</h4></div><div class='review'><p class='star'>{star_span}</p><p class='reviewVal'>{review}</p></div></div>{stock_alert}<button type='submit' class='submit' name='submit' value='submit{row[4]}'></button></div></div>"

                else:
                    imageTags += f"<div class='line {row[1]}'><div class='productImg'><img src='{row[0]}' alt='' class='img'></div><div class='productTitle'><h3>{title}</h3></div><div class='priceAndReview'><div class='price'><h4>￥{price}</h4></div><div class='review'><p class='star'>{star_span}</p><p class='reviewVal'>{review}</p></div></div>{stock_alert}<button type='submit' class='submit' name='submit' value='submit{row[4]}'></button></div>"

                if i == len(image_data) - 1:
                    imageTags += "</div></form>"

                if i % 50 == 49 and i != len(image_data) - 1:
                    imageTags += f"</form><form action='/product' method='get' id='form{int(i / 49)}' class='productForm'>"
                    print(i)

            else:
                imageTags += f"<form action='/product' method='get' id='form0' class='productForm'><div class='row'><div class='line {row[1]}'><div class='productImg'><img src='{row[0]}' alt='' class='img'></div><div class='productTitle'><h3>{title}</h3></div><div class='priceAndReview'><div class='price'><h4>￥{price}</h4></div><div class='review'><p class='star'>{star_span}</p><p class='reviewVal'>{review}</p></div></div>{stock_alert}<button type='submit' class='submit' name='submit' value='submit{row[4]}'></button></div>"
            i += 1
            print(i)
            print(row[1])

        page = (i / 49) + 1
    session["result"] = request.path + "?" + request.query_string.decode("utf-8")

    # count = row[5]

    # print(image_data[8 - 1])

    # print(data[0][0])
    # print(data[0] == "./static/images/shirt/kumo.png")

    # print(imageTags)
    # print(search)
    print(len(image_data), "数")
    if len(image_data) == 0:
        not_found = "<h2 class ='not_found'>一致する商品が見つかりませんでした。</h2>"
    else:
        not_found = ""
    # conn.commit()
    cur.close()
    conn.close()
    # print(count[0])

    # print(splitSearch, len(splitSearch))

    # for word in splitSearch:

    #     search += word
    #     print(search)

    return render_template("./page/result.html", search_result=search, imageTags=imageTags, acount=common_header[0], log=common_header[1], account_detail=common_header[2], search=search, count=count, splitSearch=splitSearch, keyWord=session["keyWord"], not_found=not_found, footer_tag = common_header[5], popular_style = popular_style)


# 服の個別ページ
@app.route("/product", methods=["GET", "POST"])
def product():

    if request.method == "GET":
        common_header = loginProcess(login)

        # 服のidを読み取る
        submit_number = request.args.get("submit")

        if submit_number is None:
            pass
        else:
            session["last_product"] = submit_number

        print(session)

        favorite_star = ""

        dbname = "ecdatabase"

        conn = mysql.connector.connect(
            user='root',
            password='',
            host='localhost',
            database=dbname
        )

        cur = conn.cursor()

        # cur.execute("""
        #             SELECT review
        #             FROM review
        #             WHERE userId = %s AND clothesId = %s
        #             """,(session["id"],submit_number[6:]))

        # my_review = cur.fetchone()[0]
        # print(my_review)

        my_review_tag = ""

        for i in range(1, 6):

            get_review = request.args.get(f"star{i}")
            if get_review:

                submit_number = session["last_product"]

                cur.execute("""
                            INSERT INTO review (userId, clothesId, review)
                            VALUES (%s,%s,%s)
                            ON DUPLICATE KEY UPDATE review = %s
                            """, (session["id"], submit_number[6:], i, i))

                my_review_tag += f"""<input type="radio" name="star{i}" id="star{i}">
                            <label for="star{i}" class="star-label{i}" value = "{submit_number}"><i class="far fa-star"></i></label>"""

            else:
                my_review_tag += f"""<input type="radio" name="star{i}" id="star{i}">
                            <label for="star{i}" class="star-label{i}" value = "{submit_number}"><i class="far fa-star"></i></label>"""

                print(get_review, i)

        if submit_number == None:
            print("none")
            submit_number = request.args.get("favorite")

            # お気に入り登録されているかどうか
            cur.execute("""
                        SELECT 1 
                        FROM favorite
                        WHERE userId = %s AND clothesId = %s;
                        """, (session["id"], submit_number[6:]))

            result = cur.fetchone()

            if result:
                print("存在する")
                favorite_star = "<i class='far fa-heart'></i>"
                cur.execute("DELETE FROM favorite WHERE userId = %s AND clothesId = %s;",
                            (session["id"], submit_number[6:]))
            else:
                print("存在しない")
                favorite_star = "<i class='fas fa-heart'></i>"

                cur.execute("INSERT INTO favorite(userId, clothesId) VALUES (%s, %s);",
                            (session["id"], submit_number[6:]))
            conn.commit()

            # return render_template("page/product.html", submit_number = submit_number)
            # return redirect("/product")

        else:
            try:
                cur.execute("""
                            SELECT 1 
                            FROM favorite
                            WHERE userId = %s AND clothesId = %s;
                            """, (session["id"], submit_number[6:]))

                result = cur.fetchone()

                if result:
                    print("存在する")
                    favorite_star = "<i class='fas fa-heart'></i>"

                else:
                    print("存在しない")
                    favorite_star = "<i class='far fa-heart'></i>"
            except:
                return redirect("/login")

        cur.execute(f"""
                    SELECT 
                    clothes.id,
                    clothesImage.img1, clothesImage.img2, clothesImage.img3, clothesImage.img4, clothesImage.img5, clothesImage.img6, clothesImage.img7, clothesImage.img8, 
                    clothes.clothesName,
                    clothes.price,
                    clothes.productText,
                    clothesDetail.material,
                    clothes.clickCounter,
                    clothesDetail.type,
                    clothes.stock
                    FROM clothes
                    JOIN clothesImage ON clothes.id = clothesImage.clothesId
                    JOIN clothesDetail ON clothes.id = clothesDetail.clothesId
                    WHERE clothes.id = {submit_number[6:]};
                    """)

        id_list = cur.fetchone()

        # for row in id_list:
        #     if submit_number == f"submit{row[0]}":
        #         cur.execute(f"""
        #             SELECT * from clothes id = {row[0]};
        #             """)
        print(id_list)

        # 服のID取得
        clothes_id = id_list[0]
        # 服の画像
        img1 = id_list[1]
        img2 = id_list[2]
        img3 = id_list[3]
        img4 = id_list[4]
        img5 = id_list[5]
        img6 = id_list[6]
        img7 = id_list[7]
        img8 = id_list[8]

        clothes_img = id_list[1]
        # 服のタイトル
        clothes_title = id_list[9]
        # 服の値段
        clothes_price = id_list[10]

        # 商品説明
        productText = id_list[11]
        # 材質
        material = id_list[12]
        # 閲覧回数
        clickCounter = id_list[13]
        print(material)
        # カテゴリー
        category = id_list[14]

        # ストック
        stock = int(id_list[15])

        # select_count = 0

        if stock > 10:
            select_count = 10
            if stock > 30:
                stock_alert = ""
            else:
                stock_alert = f"<h3 class='stock_alert'>在庫は残り{stock}点です。</h3>"

        else:
            select_count = int(stock)
            stock_alert = f"<h3 class='stock_alert'>在庫は残り{stock}点です。</h3>"

        select_tag = ""
        for i in range(select_count):
            select_tag += f"""<option value="{i + 1}">{i + 1}</option>"""

        img_div = f"""
                    <div class='color_img'>
                    <input type='radio' id='img1' name='clothesImage' class='selectColor' value='{img1}' required checked>
                    <label for='img1'>
                    <img src='{img1}'>
                    </label>
                    </div>"""
        if img2 != f'static/images/clothes/{category}/':
            img_div += f"""
                    <div class='color_img'>
                    <input type='radio' id='img2' name='clothesImage' class='selectColor' value='{img2}'>
                    <label for='img2'>
                    <img src='{img2}'>
                    </label>
                    </div>"""
        if img3 != f'static/images/clothes/{category}/':
            img_div += f"""
                    <div class='color_img'>
                    <input type='radio' id='img3' name='clothesImage' class='selectColor' value='{img3}'>
                    <label for='img3'>
                    <img src='{img3}'>
                    </label>
                    </div>"""
        if img4 != f'static/images/clothes/{category}/':
            img_div += f"""
                    <div class='color_img'>
                    <input type='radio' id='img4' name='clothesImage' class='selectColor' value='{img4}'>
                    <label for='img4'>
                    <img src='{img4}'>
                    </label>
                    </div>"""
        if img5 != f'static/images/clothes/{category}/':
            img_div += f"""
                    <div class='color_img'>
                    <input type='radio' id='img5' name='clothesImage' class='selectColor' value='{img5}'>
                    <label for='img5'>
                    <img src='{img5}'>
                    </label>
                    </div>"""
        if img6 != f'static/images/clothes/{category}/':
            img_div += f"""
                    <div class='color_img'>
                    <input type='radio' id='img6' name='clothesImage' class='selectColor' value='{img6}'>
                    <label for='img6'>
                    <img src='{img6}'>
                    </label>
                    </div>"""
        if img7 != f'static/images/clothes/{category}/':
            img_div += f"""
                    <div class='color_img'>
                    <input type='radio' id='img7' name='clothesImage' class='selectColor' value='{img7}'>
                    <label for='img7'>
                    <img src='{img7}'>
                    </label>
                    </div>"""
        if img8 != f'static/images/clothes/{category}/':
            img_div += f"""
                    <div class='color_img'>
                    <input type='radio' id='img8' name='clothesImage' class='selectColor' value='{img8}'>
                    <label for='img8'>
                    <img src='{img8}'>
                    </label>
                    </div>"""

        # レビュー
        cur.execute(
            f"SELECT AVG(review), COUNT(*) FROM review WHERE clothesId = {submit_number[6:]} GROUP BY clothesId")
        reviewList = cur.fetchone()
        reviewAdd = 0
        # for row in reviewList:
        #     print(row[0])
        #     reviewAdd += float(row[0])

        # レビュー
        # レビューの数]
        print(reviewList)
        review = reviewList[0]
        reviewCount = reviewList[1]
        # print(review, row[1])

        # cur.execute("""
        #             SELECT
        #             """)

        now = datetime.now().date()

        # 閲覧回数+1する
        cur.execute(f"""
                        UPDATE clothes SET clickCounter = {clickCounter + 1} WHERE id = {submit_number[6:]};
                    """)

        cur.execute(f"""
                        UPDATE siteCounter SET dateClickCounter = dateClickCounter + 1 WHERE date = %s
                    """, (now,))

        conn.commit()

        cur.execute(
            f"SELECT S, M, L FROM clothes_size WHERE clothesId = {submit_number[6:]}")

        size = cur.fetchone()
        print(size[0], size[1], size[2])

        S = size[0]
        M = size[1]
        L = size[2]
        
        
        cur.execute("""
                    SELECT clothesImage.img1, clothes.id, clothesDetail.type
                    FROM clothes
                    JOIN clothesImage ON clothes.id = clothesImage.clothesId
                    JOIN clothesDetail ON clothes.id = clothesDetail.clothesId
                    WHERE clothesDetail.type = (
                        SELECT type
                        FROM clothesDetail
                        WHERE clothesId = %s
                    ) AND NOT clothesDetail.clothesId = %s
                    LIMIT 20
                    """, (submit_number[6:],submit_number[6:]))
        
        other_data = cur.fetchall()
        
        other_tag = ""
        for data in other_data:
            other_tag += f"""
                <div>
                    <img src="{data[0]}" alt=""  class="div_img">
                    <button type="submit" class="submit" name="submit" value="submit{data[1]}"></button>
                </div>
            """
        
        cur.execute("""
                    SELECT clothesImage.img1, clothes.id
                    FROM clothes
                    JOIN clothesImage ON clothes.id = clothesImage.clothesId
                    JOIN clothesDetail ON clothes.id = clothesDetail.clothesId
                    WHERE NOT clothesDetail.clothesId = %s
                    ORDER BY clothes.buyCounter DESC
                    LIMIT 20
                    """,(submit_number[6:],))
        
        other_favorite_data = cur.fetchall()
        
        other_favorite_tag = ""
        
        for data in other_favorite_data:
            other_favorite_tag += f"""
                <div>
                    <img src="{data[0]}" alt=""  class="div_img">
                    <button type="submit" class="submit" name="submit" value="submit{data[1]}"></button>
                </div>
            """
        

        conn.close()

        print(submit_number)

        print(favorite_star)

        print(now)
        
        
        
        
        

    return render_template("./page/product.html", acount=common_header[0], log=common_header[1],
                           account_detail=common_header[2], clothes_img=clothes_img,
                           clothes_price=clothes_price, clothes_title=clothes_title,
                           material=material, S=S, M=M, L=L, img_div=img_div,
                           productText=productText, clothes_id=clothes_id, review=review,
                           reviewCount=reviewCount, favorite_star=favorite_star,
                           select_tag=select_tag, stock_alert=stock_alert, my_review_tag=my_review_tag, submit_number=submit_number,
                           return_page = session["result"], color_first = img1, footer_tag = common_header[5],
                           other_tag = other_tag, other_favorite_tag = other_favorite_tag)


# @app.route("/favorite")
# def favorite():


@app.route("/process", methods=["POST"])
def buy():

    button_type = request.form["next"]

    common_header = loginProcess(login)

    clothes_size = request.form["clothesSize"]
    print("押した服のサイズ", clothes_size)

    clothes_img = request.form["clothesImage"]
    print("押した服の名前", clothes_img)

    clothes_count = int(request.form["count"])
    print("服の数量", clothes_count)

    dbname = "ecdatabase"

    conn = mysql.connector.connect(
        user='root',
        password='',
        host='localhost',
        database=dbname
    )

    cur = conn.cursor()

    clothes_id = button_type.split("_")[1]

    cur.execute("""
                UPDATE clothes
                SET stock = stock - %s
                WHERE id = %s
                """, (clothes_count, clothes_id))
    
    
    
    cur.execute("""
                    SELECT clothes.id, clothesImage.img1 from clothes
                    JOIN clothesImage ON clothesImage.clothesId = clothes.id
                    ORDER BY buyCounter DESC 
                    LIMIT 20;
                    """)

    descClothes = cur.fetchall()
    # この商品売れてますよのやつ
    addFavoriteList = ""
    for row in descClothes:
        # print(row)
        addFavoriteList += f"<div class='img_div'><img src='{row[1]}' alt='' class='img'><button type='submit' class='submit' name='submit' value='submit{row[0]}'></button></div>"

    cur.execute("""
                SELECT clothesImage.img1, clothes.id
                FROM clothes
                JOIN clothesImage ON clothesImage.clothesId = clothes.id
                JOIN clothesDetail ON clothesDetail.clothesId = clothes.id
                WHERE clothesDetail.type = (
                    SELECT type
                    FROM clothesDetail
                    WHERE clothesId = %s
                )
                LIMIT 20
                """, (clothes_id,))
    
    same_type = cur.fetchall()
    print(same_type)
    same_type_tag = ""
    for data in same_type:
        same_type_tag += f"""
            <div class='img_div'>
                <img src='{data[0]}' alt='' class='img'>
                <button type='submit' class='submit' name='submit' value='submit{data[1]}'></button>
            </div>
        """
    
    
    
    

    if button_type.startswith('buy_'):
        print("buy")
        print(clothes_id)
        address_check = request.form.get("address_check")
        post_code = request.form.get("post_code")
        address = request.form.get("prefecture") + request.form.get("city") + request.form.get("town") + request.form.get("address")
        print(request.form.get("prefecture"), "prefecture")
        print(request.form.get("city"), "city")
        print(request.form.get("town"), "town")
        print(request.form.get("address"), "address")
        print(post_code,"post_code", address, "address",address_check,"address_check")
        print(post_code, "post_code")
        print(address_check, "address_check")
        if address_check is None or address_check == "on":
            # お届け先が未入力の場合
            if request.form.get("prefecture") == "" or request.form.get("city") == "" or request.form.get("town") == "" or request.form.get("address") == "":
                return redirect(session["last_product"])
            else:
                # お届け先がしっかり入力している場合
                post_code = request.form.get("post_code")
                address = request.form.get("prefecture") + request.form.get("city") + request.form.get("town") + request.form.get("address")
        if address_check == "off":
            # お届け先が登録されている住所だった場合
            cur.execute("""
                        SELECT postCode, city
                        FROM customerInfo
                        WHERE id = %s
                        """, (session["id"],))
            
            post_code_data = cur.fetchone()
            print(post_code_data,"a")
            post_code = post_code_data[0]
            address = post_code_data[1]
            
        cur.execute(f"""
                    SELECT id, buyCounter, clothesName FROM clothes WHERE id = {clothes_id};
                    """)

    # print(buy_clothes_id)

        id_list = cur.fetchone()

        clothes_id = id_list[0]
        buy_counter = id_list[1]
        clothes_name = id_list[2]

        # print(id_list)

        cur.execute(f"""
                    UPDATE clothes SET
                    buyCounter = {buy_counter + clothes_count} 
                    WHERE id = {clothes_id}
                    """)

        cur.execute("""
                    INSERT INTO buyList (userId, clothesId, clothesName, clothesSize, clothesImage, count, postCode, city) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
                    """, (session["id"], clothes_id, clothes_name, clothes_size, clothes_img, clothes_count,post_code, address))

        
        conn.commit()
        conn.close()

        return render_template("page/buy.html", acount=common_header[0], log=common_header[1],
                               account_detail=common_header[2], addFavoriteList=addFavoriteList, footer_tag = common_header[5],
                               same_type_tag = same_type_tag)

    if button_type.startswith("kart_"):
        print("kart", clothes_id)

        try:
            # 服がカートに入ってなかった場合
            cur.execute("""
                        INSERT INTO kart(userId, clothesId, clothesImage, clothesSize, count) VALUES (%s,%s,%s,%s,%s)
                        """, (session["id"], clothes_id, clothes_img, clothes_size, clothes_count,))
            conn.commit()

            cur.execute("""
                        SELECT clothesName, price, id
                        FROM clothes
                        WHERE id = %s;
                        """, (clothes_id,))

            row = cur.fetchone()

            if row is not None:
                clothesName = row[0]
                price = row[1]
                # id = row[2]

                print(price)
            else:
                print(row)
                print("該当するデータがありません")

            conn.close()

            # print(price)
        except Exception as e:

            print("追加エラー")
            cur.execute("""
                        SELECT clothes.clothesName, clothes.price, kart.userId, kart.clothesId, kart.clothesImage, kart.clothesSize, kart.count
                        FROM kart
                        JOIN clothes ON clothes.id = kart.clothesId
                        WHERE kart.clothesId = %s AND kart.userId = %s AND clothesSize = %s;
                        """, (clothes_id, session["id"], clothes_size))

            exist_data = cur.fetchone()

            # print(exist_data)

            # print(e)
            if exist_data is not None:

                clothesName = exist_data[0]
                price = exist_data[1]
                data_count = int(exist_data[6])
                print("すでに")

                if clothes_count + data_count < 10:

                    cur.execute("UPDATE kart SET count = %s WHERE clothesId = %s AND userId = %s AND clothesSize = %s",
                                (clothes_count + data_count, clothes_id, session["id"], clothes_size))
                    conn.commit()

                else:
                    clothesName = "すでにカートに同じ服が10個以上入っています。一度に購入できるのは10個までです。"
                    price = ""

            else:
                clothesName = "error"
                price = "error"

            # print("")
            # else:

            print("該当するデータがありません")

        return render_template("page/kart_in.html", acount=common_header[0], log=common_header[1],
                               account_detail=common_header[2], clothes_img=clothes_img,
                               clothesName=clothesName, price=price, clothes_size=clothes_size,
                               clothes_count=clothes_count,addFavoriteList=addFavoriteList, footer_tag = common_header[5],
                               same_type_tag = same_type_tag)

    print(session)

    # print(clothes_id)

    return render_template("page/index", acount=common_header[0], log=common_header[1],
                           account_detail=common_header[2],)


@app.route("/registration", methods=["GET", "POST"])
def regi():
    # common_header = loginProcess(login)

    if request.method == "POST":
        # 画像ファイルの受け取り

        UPLOAD_FOLDER = ''

        dbname = "ecdatabase"
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            database=dbname
        )

        cur = conn.cursor()
        
        try:
        
            price = request.form["price"]

            stock = request.form["stock"]

            now = datetime.now()
            formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")

            clothes_name = request.form["productName"]

            clothes_text = request.form["productDetail"]

            print(formatted_date)

            # clothesテーブルに情報を入力する
            cur.execute(f"""
                        INSERT INTO clothes (clothesName, price, stock, date, clickCounter, buyCounter, productText, userid) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                        """, (clothes_name, price, stock, formatted_date, 0, 0, clothes_text, session["id"]))

            
            

            from werkzeug.utils import secure_filename

            type = request.form["clothes_type"]

            # save_path = f"./static/images/clothes/{type}/"
            save_path = f"./static/images/clothes/{type}/"
            regi_path = f"static/images/clothes/{type}/"

            img_li = []

            for i in range(1, 9):
                clothes_image = request.files.get(f"file{i}")

                if clothes_image and clothes_image.filename != '':
                    # print(f"ファイル {i} を受け取りました。")
                    filename = secure_filename(clothes_image.filename)

                    # 保存する所
                    save_file_path = os.path.join(save_path, filename)
                    regi_file_path = os.path.join(regi_path, filename)
                    # print(f"保存するファイルパス: {save_file_path}")
                    os.makedirs(save_path, exist_ok=True)
                    clothes_image.save(save_file_path)
                    print(f"ファイル {i} を保存しました。")

                print(clothes_image.filename)
                img_li.append(clothes_image.filename)

                # cur.executemany("""
                #                 INSERT INTO clothes (clothesName, price, image1, image2, image3, image4, image5, image6, image7, image8,  stock, review, date, clickCounter, buyCounter, productText, type, userid, material)
                #                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 0, %s, 0, 0, %s, %s, %s, %s)
                #                 """, [(clothes_name, price, f'./static/images/clothes/{type}/{img_li[0]}', f'./static/images/{type}/{img_li[1]}', f'./static/images/{type}/{img_li[2]}', f'./static/images/{type}/{img_li[3]}', f'./static/images/{type}/{img_li[4]}', f'./static/images/{type}/{img_li[5]}', f'./static/images/{type}/{img_li[6]}', f'./static/images/{type}/{img_li[7]}',  stock, date, productText, category, id, material),])

            
            # clothesテーブルの最後のidを取得する
            cur.execute("""
                        SELECT id FROM clothes ORDER BY id DESC LIMIT 1;
                        """)

            last_id = cur.fetchone()[0]
            print(last_id)

            material = request.form["material"]
            print(material)
            gender = request.form["gender"]
            print(gender)

            cur.execute(f"""
                        INSERT INTO clothesdetail (clothesId, type, material, sex) 
                        VALUES (%s, %s, %s, %s)
                        """, (last_id, type, material, gender))

            cur.execute("""
                        INSERT INTO clothesimage (clothesId, img1, img2, img3, img4, img5, img6, img7, img8)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
                        """, (last_id, regi_path + img_li[0], regi_path + img_li[1], regi_path + img_li[2], regi_path + img_li[3], regi_path + img_li[4], regi_path + img_li[5], regi_path + img_li[6], regi_path + img_li[7]))

            review = "NULL"

            cur.execute("""
                        INSERT INTO review (review, userId, clothesId)
                        VALUE (%s,%s,%s)
                        """, ("0", session["id"], last_id))

            print(img_li)

            size_s = request.form["S"]
            size_m = request.form["M"]
            size_l = request.form["L"]

            cur.execute("""
                        INSERT INTO clothes_size (S, M, L, clothesId)
                        VALUE (%s,%s,%s,%s)
                        """, (size_s, size_m, size_l, last_id))

            conn.commit()
            print(save_path)
            print(img_li)

            print(clothes_name, price, stock, formatted_date, 0, 0, clothes_text, 1)
            print(last_id, regi_path + img_li[0], regi_path + img_li[1], regi_path + img_li[2], regi_path +
                img_li[3], regi_path + img_li[4], regi_path + img_li[5], regi_path + img_li[6], regi_path + img_li[7])
            print(regi_file_path + img_li[5])

            return redirect("/success")
        except:
            print("ユニーク")
            alert = """<script src="static/js/alert.js"></script>"""
            
    
    if request.method == "GET":
        alert = ""
    
    return render_template("userInfo/registration.html", alert = alert)


@app.route("/success")
def success():
    return render_template("userInfo/registration_saccess.html")


@app.route("/salesManagement")
def admin():
    common_header = loginProcess(login)

    type_op = request.args.get("type")
    gender_op = request.args.get("gender")
    narrow_op = request.args.get("narrow")
    sales_name = request.args.get("sales_name")

    print(type_op, gender_op, narrow_op, sales_name)

    sql_where = ""
    if type_op != "None" and type_op:
        print(type_op, "noneじゃない")
        sql_where += f" AND clothesDetail.type = '{type_op}'"

    if gender_op != "None" and gender_op:
        print(gender_op, "noneじゃない")
        sql_where += f" AND clothesDetail.sex = '{gender_op}'"

    if sales_name != "" and sales_name != None and sales_name:
        print(sales_name, "noneじゃない")
        sql_where += f" AND clothes.clothesName LIKE  '%{sales_name}%'"

    if type_op and type_op != "None":
        print("noneじゃない")

    print(sql_where)

    order = ""

    if narrow_op is None or narrow_op == "buy":
        print("buy", "none")
        order += "clothes.buyCounter"
    elif narrow_op == "click":
        print("click")
        order += "clothes.clickCounter"
    elif narrow_op == "add":
        print("add")
        order += "clothes.date"
    elif narrow_op == "review":
        print("review")
        order += "review.review"
    elif narrow_op == "stock":
        print("stock")
        order += "clothes.stock"
    elif narrow_op == "sales":
        print("sales")
        order += "clothes.price * clothes.buyCounter"
    else:
        print("error")

    sort = request.args.get("sort")

    if sort:
        print(sort)
        order_sort = sort
    else:
        order_sort = "DESC"

    today = datetime.now().date()
    one_days_ago = today - timedelta(days=1)
    two_days_ago = today - timedelta(days=2)
    three_days_ago = today - timedelta(days=3)
    four_days_ago = today - timedelta(days=4)
    five_days_ago = today - timedelta(days=5)
    six_days_ago = today - timedelta(days=6)
    seven_days_ago = today - timedelta(days=7)

    # print(today)
    # print(one_days_ago)
    # print(two_days_ago)
    # print(three_days_ago)
    # print(four_days_ago)
    # print(five_days_ago)
    # print(six_days_ago)
    # print(seven_days_ago)

    # グラフの生成
    date = [seven_days_ago, six_days_ago, five_days_ago, four_days_ago,
            three_days_ago, two_days_ago, one_days_ago, today]
    frequency = [10, 20, 30, 40, 10, 60, 70, 50]

    conn, cur = database_connection()

    print(f"""
                SELECT clothes.*, clothesimage.img1,  AVG(review.review), clothesDetail.type, clothesDetail.sex
                FROM clothes
                JOIN clothesimage ON clothes.id = clothesimage.clothesId
                JOIN review ON clothes.id = review.clothesId
                JOIN clothesDetail ON clothes.id = clothesDetail.clothesId
                WHERE clothes.userId = %s {sql_where}
                GROUP BY review.clothesId
                ORDER BY buyCounter DESC;
                """)

    cur.execute(f"""
                SELECT clothes.*, clothesimage.img1,  AVG(review.review), clothesDetail.type, clothesDetail.sex
                FROM clothes
                JOIN clothesimage ON clothes.id = clothesimage.clothesId
                JOIN review ON clothes.id = review.clothesId
                JOIN clothesDetail ON clothes.id = clothesDetail.clothesId
                WHERE clothes.userId = %s {sql_where}
                GROUP BY review.clothesId
                ORDER BY {order} {order_sort};
                """, (int(session['id']),))
    # int(session['id'])
    count_data = cur.fetchall()

    # print(count_data)

    click_data = []
    buy_data = []
    name_data = []
    productList = ""
    for row in count_data:
        # 商品...省略
        if len(row[1]) >= 20:
            clothes_name = row[1][:10] + "..."
        else:
            clothes_name = row[1]

        if row[1] != 0 and len(buy_data) != 10:
            print(row[1])
            click_data.append(row[5])
            buy_data.append(row[6])

            name_data.append(clothes_name)
            print(clothes_name, row[5], row[6])

        regi_date = row[4].split(" ")[0]

        productList += f"""
            <tr>
                <td><img src='{row[9]}' alt='Product1'></td>
                <td>{clothes_name}</td>
                <td>{row[5]}</td>
                <td>{row[6]}</td>
                <td>{row[10]}</td>
                <td>{row[2]}</td>
                <td>{row[2] * row[6]}</td>
                <td>{row[3]}</td>
                <td>{regi_date}</td>
                <td>{regi_date}</td>
                <td><button type="submit" name="product_number" value="{row[0]}">在庫追加・削除</button></td>
            </tr>
        """

    conn.close()

    # print(click_data)
    # print(name_data)

    # グラフの大きさ指定
    # plt.figure(figsize=(10, 5))
    # plt.bar(date, frequency, color='skyblue')
    # plt.plot(date, frequency)
    # plt.xlabel('日付', fontname="MS Gothic")
    # plt.ylabel('回数', fontname="MS Gothic")
    # # plt.title('Matplotlibグラフ')
    # plt.legend(["閲覧","売上"], prop={"family":"MS Gothic"})
    # plt.ylim(0,100)

    plt.figure(figsize=(12, 5))
    # print(buy_data)
    # print(click_data)
    # print(name_data)
    plt.bar(name_data, buy_data, color='skyblue')
    plt.plot(name_data, click_data)
    plt.xlabel('商品名', fontname="MS Gothic", fontsize=15)
    plt.ylabel('回数', fontname="MS Gothic", fontsize=15)
    plt.xticks(rotation=15)
    plt.title('売上TOP10', fontsize=30)
    plt.legend(["閲覧", "売上"], prop={"family": "MS Gothic"})
    # plt.ylim(0,200)
    # plt.set

    # グラフをバイトデータに変換
    img_stream = io.BytesIO()
    plt.savefig(img_stream, format='png')
    img_stream.seek(0)
    plt.close()

    # バイト列をbase64エンコードするHTMLに埋め込めるURLを作成
    image_base64 = base64.b64encode(img_stream.read()).decode("utf=8")

    # print(session)

    return render_template("userInfo/salesManagement.html", acount=common_header[0], log=common_header[1],
                           account_detail=common_header[2], bar_data=image_base64, productList=productList, order=order, footer_tag = common_header[5])


@app.route("/product_management", methods=["GET", "POST"])
def product_management():

    common_header = loginProcess(login)
    conn, cur = database_connection()
    product_number = request.args.get("product_number")

    if request.method == "POST":
        product_number = request.form.get("product_number")
        rem = request.form.get("remove")
        print(rem, "button")
        if product_number != None:
            add_stock = request.form.get("add_stock")
            print(add_stock, product_number, rem)
            cur.execute("""
                        UPDATE clothes
                        SET stock = stock + %s
                        WHERE id = %s
                        """, (add_stock, product_number))

            sql = cur.lastrowid
            conn.commit()
            print(sql)
            return redirect("/salesManagement")
        elif rem != None:
            print("remove")
            cur.execute("""
                        DELETE FROM review WHERE clothesId = %s
                        """, (rem,))

            cur.execute("""
                        DELETE FROM clothesImage WHERE clothesId = %s
                        """, (rem,))

            cur.execute("""
                        DELETE FROM clothes_size WHERE clothesId = %s
                        """, (rem,))

            cur.execute("""
                        DELETE FROM clothesDetail WHERE clothesId = %s
                        """, (rem,))

            cur.execute("""
                        DELETE FROM clothes WHERE id = %s
                        """, (rem,))

            conn.commit()

            return redirect("/salesManagement")

        else:
            return redirect("/")

    cur.execute("""
                SELECT clothes.*, clothesImage.img1, AVG(review.review)
                FROM clothes
                JOIN clothesImage ON clothes.Id = clothesImage.clothesId
                JOIN review ON review.clothesId = clothes.id
                WHERE clothes.id = %s
                GROUP BY review.clothesId
                """, (product_number,))

    data = cur.fetchone()

    print(data)

    id = data[0]
    img = data[9]
    name = data[1]
    price = f"{data[2]:,}"
    click = data[5]
    buy = data[6]
    stock = data[3]
    review = data[10]

    print(session)

    return render_template("userInfo/product_management.html", img=img,
                           name=name, price=price, acount=common_header[0],
                           log=common_header[1], account_detail=common_header[2],
                           click=click, buy=buy, stock=stock, review=review,
                           clothes_id=id, footer_tag = common_header[5])


# それぞれのサイト


@app.route("/koike")
def koike():

    return render_template("koike/history.html")


@app.route("/favorite")
def haruyama():

    common_header = loginProcess(login)
    conn, cur = database_connection()

    cur.execute("""
                SELECT clothes.id, clothes.clothesName, clothes.price, clothes.stock,
                clothesImage.img1
                FROM favorite
                JOIN clothes ON clothes.id = favorite.clothesId
                JOIN clothesDetail ON clothesDetail.clothesId = clothes.id
                JOIN clothesImage ON clothes.id = clothesImage.clothesId
                WHERE favorite.userId = %s
                """, (session["id"],))

    favorite_data = cur.fetchall()

    product_count = 0
    favorite_tag = ""
    for row in favorite_data:
        print(row, "1行")
        clothes_id = row[0]
        clothes_name = row[1]
        
        if len(clothes_name) > 30:
            clothes_name = clothes_name[:30] + "..."
        
        clothes_price = row[2]
        clothes_stock = int(row[3])
        clothes_img = row[4]
        stock_tag = ""
        if clothes_stock <= 30:
            stock_tag = f"""
            <div class="stock">
                <p>在庫残り{clothes_stock}点です。</p>
            </div>
            """

        if product_count == 0 or product_count % 5 == 0:
            favorite_tag += f"""
            <form action="product" id="" class="row">
                <div class="product_frame">
                    <div class="img_div">
                        <img src="{clothes_img}" alt="">
                    </div>
                    <div class="prduct_detail_area">
                        <div class="title">
                            <h3>{clothes_name}</h3>
                        </div>
                        <div class="priceAndReview">
                            <h3 class="price">￥{clothes_price}円</h3>
                        </div>
                        {stock_tag}
                    </div>
                    <button type="submit" class="submit" name="submit" value="submit{clothes_id}"></button>
                </div>
            """
        elif product_count % 5 == 4:
            favorite_tag += f"""
            <div class="product_frame">
                    <div class="img_div">
                        <img src="{clothes_img}" alt="">
                    </div>
                    <div class="prduct_detail_area">
                        <div class="title">
                            <h3>{clothes_name}</h3>
                        </div>
                        <div class="priceAndReview">
                            <h3 class="price">￥{clothes_price}円</h3>
                        </div>
                        {stock_tag}
                    </div>
                    <button type="submit" class="submit" name="submit" value="submit{clothes_id}"></button>
                </div>
            </form>
            """
        else:
            favorite_tag += f"""
                <div class="product_frame">
                    <div class="img_div">
                        <img src="{clothes_img}" alt="">
                    </div>
                    <div class="prduct_detail_area">
                        <div class="title">
                            <h3>{clothes_name}</h3>
                        </div>
                        <div class="priceAndReview">
                            <h3 class="price">￥{clothes_price}円</h3>
                        </div>
                        {stock_tag}
                    </div>
                    <button type="submit" class="submit" name="submit" value="submit{clothes_id}"></button>
                </div>
            """
        print(product_count)
        product_count += 1

    favorite_tag += "</form>"

    print(favorite_tag)
    url = request.path + request.query_string.decode("utf-8")
    print(url)
    session["result"]  = "/favorite"

    return render_template("haruyama/favorite.html", acount=common_header[0],
                        log=common_header[1], account_detail=common_header[2], favorite_tag=favorite_tag,
                        footer_tag = common_header[5],)


@app.route("/kart")
def takeuti():

    common_header = loginProcess(login)

    conn, cur = database_connection()

    cur.execute("""
                SELECT kart.*, clothes.clothesName, clothes.stock, clothes.price, clothes.stock
                FROM kart
                JOIN clothes ON clothes.id = kart.clothesId
                WHERE kart.userId = %s
                """, (session["id"],))

    kart_data = cur.fetchall()

    kart_in_product = ""

    i = 0
    print(kart_data)
    for row in kart_data:
        print(row[6])
        clothes_id = row[1]
        clothes_img = row[2]
        clothes_size = row[3]
        clothes_count = row[4]
        clothes_name = row[6]
        clothes_stock = row[7]
        clothes_price = row[8]
        clothes_stock = row[9]

        if len(clothes_name) >= 20:
            clothes_name = clothes_name[:30] + "..."

        if clothes_stock + clothes_count >= 10:
            op_max = 10
        else:
            op_max = clothes_stock + clothes_count
        op = ""
        j = 1
        while j < op_max + 1:
            print(clothes_stock)
            if j == int(clothes_count):
                op += f"""<option value="count{j}_size{clothes_size}_id{clothes_id}" selected>{j}</option>"""
            else:
                op += f"""<option value="count{j}_size{clothes_size}_id{clothes_id}">{j}</option>"""
            print(j)
            j += 1

        kart_in_product += f"""
                        <label for="check{i}" class = "label">
                            <input type="checkbox" name="check{i}" id="check{i}" class="check_button" checked>
                            <div class="cart-item">
                                <div class="cart-item-details">
                                    <div class="cart-item-detail_img">
                                        <img src="{clothes_img}" alt="">
                                    </div>
                                    <div class="cart-item-detail">
                                        <div class="product-name">{clothes_name}</div>
                                        <div class="item-options">
                                            <div class="product-stock">在庫あり</div>
                                            <div class="product-size">サイズ: {clothes_size}</div>
                                            <select name="clothes{i}" id="" class="product-quantity quantity">
                                                {op}
                                            </select>
                                            <button class="remove-item" type="submit" value="remove_{clothes_id}_{clothes_size}" name="remove">削除</button>
                                        </div>
                                    </div>
                                    <div class="item-total-1">￥ <span class="item-total">{clothes_price}</span>円</div>
                                </div>
                            </div>
                        </label>
                    """
        i += 1

    
    
    if i == 0:
        print()
        
        kart_in_product += """<div class="cart-item no_cart">カートには何も入っていません</div>"""

    cur.execute("""
                SELECT buyList.*, clothes.price * buyList.count
                FROM buyList
                JOIN clothes ON clothes.id = buyList.clothesId
                WHERE buyList.userId = %s
                ORDER BY datetime DESC
                """, (session["id"],))

    buy_list_data = cur.fetchall()

    buy_list = ""
    date_count = ""
    for row in buy_list_data:
        # print(row)

        clothes_name = row[2]
        clothes_size = row[3]
        clothes_img = row[4]
        clothes_count = row[5]
        clothes_date = row[6].strftime("%Y-%m-%d %H:%M:%S").split(" ")[0]
        clothes_price = (str(f"{row[9]:,}"))

        # print(clothes_name)

        print(clothes_price, "price")

        if date_count != clothes_date:
            # print(clothes_date)
            buy_list += f"""<h4 class = "date">{clothes_date}</h4>"""

        date_count = clothes_date
        # print(date_count)

        if len(clothes_name) >= 20:
            clothes_name = clothes_name[:30] + "..."

        buy_list += f"""
        <div class="frame">
                <div class="img_div">
                    <img src="{clothes_img}" alt="">
                </div>
                <div class="text">
                    <h4>{clothes_name}</h4>
                    <h4>{clothes_size}</h4>
                    <h4>￥{clothes_price}</h4>
                    <h4>{clothes_count}</h4>
                </div>
            </div>
        """

    conn.close()

    return render_template("userInfo/takeuti/kart.html", product_data=kart_in_product, acount=common_header[0], log=common_header[1],
                        account_detail=common_header[2], buy_list=buy_list, footer_tag = common_header[5])


@app.route("/buy_process", methods=["POST"])
def buy_process():

    common_header = loginProcess(login)

    dbname = "ecdatabase"

    conn = mysql.connector.connect(
        user='root',
        password='',
        host='localhost',
        database=dbname
    )

    cur = conn.cursor()

    remove = request.form.get("remove")

    if remove is not None:
        print(remove)
        remove_data = remove.split("_")
        remove_id = remove_data[1]
        remove_size = remove_data[2]
        print(remove_data)
        print(remove_id, remove_size)

        cur.execute("""
                    SELECT *
                    FROM kart
                    WHERE  clothesId = %s AND userId = %s AND clothesSize = %s
                    """, (remove_id, session["id"], remove_size))

        remove_kart_table_data = cur.fetchone()

        # 返す商品数
        print(remove_kart_table_data[4], "removekartdata")

        cur.execute("""
                    UPDATE clothes
                    SET stock = stock + %s
                    WHERE id = %s
                    """, (remove_kart_table_data[4], remove_id))

        cur.execute("""
                    DELETE FROM kart 
                    WHERE clothesId = %s AND userId = %s AND clothesSize = %s
                    """, (remove_id, session["id"], remove_size))

        conn.commit()

        return redirect(url_for("takeuti"))
    
    contains_clothes_key = any('clothes' in key for key in request.form)

    if contains_clothes_key:
        print("'clothes' を含むキーが存在します。")
    else:
        print("'clothes' を含むキーは存在しません。")
        return redirect("/kart")
        
    address_check = request.form.get("address_check")
    post_code = request.form.get("post_code")
    address = request.form.get("prefecture") + request.form.get("city") + request.form.get("town") + request.form.get("address")
    print(request.form.get("prefecture"), "prefecture")
    print(request.form.get("city"), "city")
    print(request.form.get("town"), "town")
    print(request.form.get("address"), "address")
    print(post_code,"post_code", address, "address",address_check,"address_check")
    print(post_code, "post_code")
    print(address_check, "address_check")
    if address_check is None or address_check == "on":
        # お届け先が未入力の場合
        if request.form.get("prefecture") == "" or request.form.get("city") == "" or request.form.get("town") == "" or request.form.get("address") == "":
            return redirect(session["last_product"])
        else:
            # お届け先がしっかり入力している場合
            post_code = request.form.get("post_code")
            address = request.form.get("prefecture") + request.form.get("city") + request.form.get("town") + request.form.get("address")
    if address_check == "off":
        # お届け先が登録されている住所だった場合
        cur.execute("""
                    SELECT postCode, city
                    FROM customerInfo
                    WHERE id = %s
                    """, (session["id"],))
        
        post_code_data = cur.fetchone()
        print(post_code_data,"a")
        post_code = post_code_data[0]
        address = post_code_data[1]
    
    
    

    # カートの中の商品数
    cur.execute("""
                SELECT COUNT(*)
                FROM kart
                WHERE userId = %s
                """, (session["id"],))

    all_count = int(cur.fetchone()[0])

    # print(all_count, "データベースの要素数")

    # カートの情報をすべて出す
    cur.execute("""
                SELECT kart.clothesId, kart.userId, kart.clothesSize, clothes.clothesName, kart.clothesImage , kart.count            
                FROM kart
                JOIN clothes ON clothes.id = kart.clothesId
                WHERE kart.userId = %s
                """, (session["id"],))

    kart_in_data = cur.fetchall()
    

    # clothes{i}のやつ
    for i in range(all_count):
        print(i)
        # カートの中身と一致するものを探す
        for row in kart_in_data:

            # リクエストデータの中身
            data = request.form[f"clothes{i}"].split("_")
            print(data, "data")
            count = int(data[0][5:])
            size = data[1][4:]
            id = int(data[2][2:])

            # カートのテーブルの中の名前
            name = row[3]
            # カートのテーブルの画像
            image = row[4]

            # カートテーブルの商品の個数
            kart_data_count = row[5]

            # print(f"clothes{i}")

            # print(data,"買った服のデータ")
            # カートテーブルの中身
            # print(kart_in_data)
            # print(count,id, row[0], session["id"], row[1], size, row[2])

            if count != 0 and id == int(row[0]) and int(session["id"]) == int(row[1]) and size == row[2] and f"check{i}" in request.form:

                # データの取り出し
                # print(count,"個数")
                # print(size,"サイズ")
                # print(id,"ID")
                # check = request.form[f"check2"]

                add_count = count - kart_data_count

                # print(add_count, "dou")

                cur.execute("""
                            UPDATE clothes
                            SET stock = stock - %s
                            """, (add_count,))

                # 購買履歴に登録
                cur.execute("INSERT INTO buyList(userId, clothesId, clothesName, clothesSize, clothesImage, count, postCode, city) VALUE(%s,%s,%s,%s,%s,%s,%s,%s)",
                            (session["id"], id, name, size, image, count, post_code, address))

                # カートから削除
                cur.execute("DELETE FROM kart WHERE userId = %s AND clothesId = %s AND clothesSize = %s",
                            (session["id"], id, size))

                conn.commit()

                # return render_template("page/buy.html", acount=common_header[0], log = common_header[1],
                #             account_detail = common_header[2],)
                # return redirect("/buy")

    # data = request.form[f"clothes{i}"]
    # print(data)

    # print(kart_in_data)
    
    
    cur.execute("""
                    SELECT clothes.id, clothesImage.img1 from clothes
                    JOIN clothesImage ON clothesImage.clothesId = clothes.id
                    ORDER BY buyCounter DESC 
                    LIMIT 20;
                    """)

    descClothes = cur.fetchall()
    # この商品売れてますよのやつ
    addFavoriteList = ""
    for row in descClothes:
        # print(row)
        addFavoriteList += f"<div class='img_div'><img src='{row[1]}' alt='' class='img'><button type='submit' class='submit' name='submit' value='submit{row[0]}'></button></div>"

    cur.execute("""
                SELECT clothesImage.img1, clothes.id
                FROM clothes
                JOIN clothesImage ON clothesImage.clothesId = clothes.id
                JOIN clothesDetail ON clothesDetail.clothesId = clothes.id
                LIMIT 20
                """)
    
    same_type = cur.fetchall()
    print(same_type)
    same_type_tag = ""
    for data in same_type:
        same_type_tag += f"""
            <div class='img_div'>
                <img src='{data[0]}' alt='' class='img'>
                <button type='submit' class='submit' name='submit' value='submit{data[1]}'></button>
            </div>
        """
    
    conn.close()

    # print(request.form)
    print(request.form)
    
    

    # return redirect("/kart")
    return render_template("page/buy.html", acount=common_header[0], log=common_header[1],
                        account_detail=common_header[2], footer_tag = common_header[5],
                        addFavoriteList=addFavoriteList)


@app.route("/inquiry", methods=["GET", "POST"])
def huzita():
    common_header = loginProcess(login)

    print(session, "セッションの確認")

    if "id" not in session:
        print("ログインされてません")
        return redirect("/login")

    if request.method == "POST":
        # 名前
        name = request.form.get("name")
        # メールアドレス
        email = request.form.get("email")
        # 郵便番号
        zipcode = request.form.get("zipcode")
        # 都道府県
        prefecture = request.form.get("prefecture")
        # 市区町村
        city = request.form.get("city")
        # 電話番号
        tel = request.form.get("tel")
        # お問い合わせ内容
        text = request.form.get("textarea")

        if text is None:
            print("textがNoneでした。")
            return redirect("/inquiry")

        print(name)
        print(email)
        print(zipcode)
        print(prefecture)
        print(city)
        print(tel)
        print(text)

        print(filter(str.isdigit, tel))

        common_header = loginProcess(login)

        dbname = "ecdatabase"

        conn = mysql.connector.connect(
            user='root',
            password='',
            host='localhost',
            database=dbname
        )

        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS inquiry (
                inquiryId INT AUTO_INCREMENT,
                name VARCHAR(255),
                email VARCHAR(255),
                zipcode VARCHAR(255),
                prefecture VARCHAR(255),
                city VARCHAR(255),
                tel VARCHAR(255),
                text VARCHAR(255),
                PRIMARY KEY (inquiryId)
            )
            """)

        cur.execute("INSERT INTO inquiry(name, email, zipcode, prefecture, city, tel, text) VALUES(%s,%s,%s,%s,%s,%s,%s)",
                    (name, email, zipcode, prefecture, city, tel, text))

        conn.commit()
        conn.close()

        return redirect("/inquiry")

    return render_template("huzita/inquiry.html", account=common_header[0], log=common_header[1],
                        account_detail=common_header[2], footer_tag = common_header[5])


@app.route("/josei", methods=["GET", "POST"])
def josei():
    if request.method == "POST":
        # フォームがPOSTリクエストで送信された場合の処理を追加する
        # フォームデータを取得して処理する
        print("post")

        clothesName = request.form["clothesName"]
        gender = request.form["gender"]
        type = request.form["type"]
        clothesText = request.form["clothesText"]

        # clothesImage1 - clothesImage8 はファイルなので request.files を使って取得する

        save_path = f"./static/images/clothes/{type}/"

        # clothesImage1 = request.files["clothesImage1"]
        # clothesImage2 = request.files["clothesImage2"]
        # clothesImage3 = request.files["clothesImage3"]
        # clothesImage4 = request.files["clothesImage4"]
        # clothesImage5 = request.files["clothesImage5"]
        # clothesImage6 = request.files["clothesImage6"]
        # clothesImage7 = request.files["clothesImage7"]
        # clothesImage8 = request.files["clothesImage8"]

        print(clothesName)
        print(gender)
        print(type)
        print(clothesText)
        print(save_path)
        # print(clothesImage1)
        # print(clothesImage2)
        # print(clothesImage3)
        # print(clothesImage4)
        # print(clothesImage5)
        # print(clothesImage6)
        # print(clothesImage7)
        # print(clothesImage8)

        dbname = "ecdatabase"
        conn = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            database=dbname
        )

        cur = conn.cursor()

        from werkzeug.utils import secure_filename

        img_li = []

        for i in range(1, 9):
            clothes_image = request.files.get(f"clothesImage{i}")

            if clothes_image and clothes_image.filename != '':
                print(f"ファイル {i} を受け取りました。")
                filename = secure_filename(clothes_image.filename)

                # 保存する所
                save_file_path = os.path.join(save_path, filename)
                print(f"保存するファイルパス: {save_file_path}")
                clothes_image.save(save_file_path)
                print(f"ファイル {i} を保存しました。")

            print(clothes_image.filename)
            img_li.append(clothes_image.filename)

            # cur.executemany("""
            #             INSERT INTO clothes (clothesName, price, image1, image2, image3, image4, image5, image6, image7, image8, color1, color2, color3, color4, color5, color6, color7, color8, stock, review, date, clickCounter, buyCounter, productText, type, userid, material)
            #             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 0, %s, 0, 0, %s, %s, %s, %s)
            #             """, [(clothes_name, price, f'./static/images/clothes/{category}/{img1.filename}', f'./static/images/{category}/{img2.filename}', f'./static/images/{category}/{img3.filename}', f'./static/images/{category}/{img4.filename}', f'./static/images/{category}/{img5.filename}', f'./static/images/{category}/{img6.filename}', f'./static/images/{category}/{img7.filename}', f'./static/images/{category}/{img8.filename}', color1, color2, color3, color4, color5, color6, color7, color8, stock, date, productText, category, id, material),])

        price = random.randint(1999, 50000)

        stock = random.randint(10, 100)

        now = datetime.datetime.now()
        formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")

        print(formatted_date)

        # clothesテーブルに情報を入力する
        cur.execute(f"""
                    INSERT INTO clothes (clothesName, price, stock, date, clickCounter, buyCounter, productText, userid) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    """, (clothesName, price, stock, formatted_date, 0, 0, clothesText, 1))

        # clothesテーブルの最後のidを取得する
        cur.execute("""
                    SELECT id FROM clothes ORDER BY id DESC LIMIT 1;
                    """)

        last_id = cur.fetchone()[0]
        print(last_id)

        material_li = ["化学繊維", "毛", "絹", "綿", "麻"]

        material_ran = random.randint(0, 4)
        cur.execute(f"""
                    INSERT INTO clothesdetail (clothesId, type, material, sex) 
                    VALUES (%s, %s, %s, %s)
                    """, (last_id, type, material_li[material_ran], gender))

        cur.execute("""
                    INSERT INTO clothesimage (clothesId, img1, img2, img3, img4, img5, img6, img7, img8)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """, (last_id, save_path + img_li[0], save_path + img_li[1], save_path + img_li[2], save_path + img_li[3], save_path + img_li[4], save_path + img_li[5], save_path + img_li[6], save_path + img_li[7]))

        review_ran = random.randint(0, 5)

        cur.execute("""
                    INSERT INTO review (review, userId, clothesId)
                    VALUE (%s,%s,%s)
                    """, (review_ran, 1, last_id))

        print(img_li)

        size_ran = random.randint(140, 170)

        cur.execute("""
                    INSERT INTO clothes_size (S, M, L, clothesId)
                    VALUE (%s,%s,%s,%s)
                    """, (size_ran, size_ran + 10, size_ran + 20, last_id))

        conn.commit()

    return render_template("josei/josei.html")


# 管理者ページ

@app.route("/site_administrator")
def site_administrator():

    common_header = loginProcess(login)

    # サイト訪問者数グラフ

    now = datetime.now().date()
    one = datetime.now().date() - timedelta(days=1)
    two = datetime.now().date() - timedelta(days=2)
    three = datetime.now().date() - timedelta(days=3)
    four = datetime.now().date() - timedelta(days=4)
    five = datetime.now().date() - timedelta(days=5)
    six = datetime.now().date() - timedelta(days=6)

    # print(now, one, two, three, four,five,six)
    date_exist_list = [now, one, two, three, four, five, six]

    conn, cur = database_connection()

    cur.execute("""
                SELECT *
                FROM  siteCounter
                WHERE date = %s OR date = %s OR date = %s OR date = %s OR date = %s OR date = %s OR date = %s
                """, (now, one, two, three, four, five, six))

    counter_data = cur.fetchall()

    # print(date_list[0][0])

    date_list = []
    visit_count = []

    for row in counter_data:
        # print(row[0])

        date_list.append(str(row[0]))
        visit_count.append(row[1])

    print(date_list)
    print(visit_count)

    plt.bar(date_list, visit_count)

    plt.xlabel("日付")
    plt.ylabel("訪問数")
    plt.title("アクセス数")
    plt.xticks(rotation=15)
    access_img = io.BytesIO()
    plt.savefig(access_img, format="png")
    access_img.seek(0)
    plt.close()

    access_img = base64.b64encode(access_img.getvalue()).decode()




    # サイト全体の商品のクリック回数と買うに至った数

    cur.execute("""
                SELECT siteCounter.date, siteCounter.dateClickCounter, SUM(buyList.count), siteCounter.visitCount
                FROM siteCounter
                LEFT JOIN buyList ON siteCounter.date = DATE(buyList.datetime)
                WHERE siteCounter.date = %s OR date = %s OR date = %s OR date = %s OR date = %s OR date = %s OR date = %s
                GROUP BY DATE(siteCounter.date)
                """, (now, one, two, three, four, five, six))

    site_click_counter = cur.fetchall()

    print(site_click_counter)

    site_date_graph = []

    site_click_count_graph = []

    site_buy_count_graph = []

    
    site_buy_count_graph_tag = ""
    for row in site_click_counter:
        print(row)

        site_date_graph.append(str(row[0]))
        site_click_count_graph.append(row[1])
        access_num = row[2]
        if row[2] is None:
            site_buy_count_graph.append(0)
            buy_num = 0
            
        else:
            site_buy_count_graph.append(row[2])
            
        # テーブルを作る
        
        
    cur.execute("""
                SELECT siteCounter.date, siteCounter.dateClickCounter, SUM(buyList.count), siteCounter.visitCount
                FROM siteCounter
                LEFT JOIN buyList ON siteCounter.date = DATE(buyList.datetime)
                WHERE siteCounter.date = %s OR date = %s OR date = %s OR date = %s OR date = %s OR date = %s OR date = %s
                GROUP BY DATE(siteCounter.date)
                ORDER BY  DATE(siteCounter.date) DESC
                """, (now, one, two, three, four, five, six))
    
    site_buy_count_graph_tag_li = cur.fetchall()
    
    for row in site_buy_count_graph_tag_li:
        site_buy_count_graph_tag += f"""<tr><td>{str(row[0])}</td><td>{row[1]}</td><td>{row[3]}</td><td>{buy_num}</td></tr>"""
    
        

    plt.bar(site_date_graph, site_buy_count_graph, label="購入された数")
    plt.plot(site_date_graph, site_click_count_graph,
            color='skyblue', label="クリックされた数")

    plt.xlabel("日付")
    plt.ylabel("回数")
    plt.title("商品のクリック数・購入数")
    plt.legend()
    plt.xticks(rotation=15)
    site_data_img = io.BytesIO()
    plt.savefig(site_data_img, format="png")
    site_data_img.seek(0)
    plt.close()

    site_data_img = base64.b64encode(site_data_img.getvalue()).decode()
    
    
    # テーブルを作る
    
    
    
    
    

    # コンバージョン率

    cur.execute("""
                    SELECT SUM((clothes.price * 0.2) * buyList.count), siteCounter.date, clothes.price, SUM(buyList.count), siteCounter.visitCount, COUNT(DATE(buyList.datetime)), COUNT(DISTINCT buyList.userId)
                    FROM buyList
                    JOIN clothes ON clothes.id = buyList.clothesId
                    RIGHT JOIN siteCounter ON DATE(buyList.datetime) = siteCounter.date
                    GROUP BY siteCounter.date
                    ORDER BY siteCounter.date DESC
                    """)

    buy_data = cur.fetchall()

    date_count = 0
    benefit_dag = ""
    con_date = []
    con_con = []
    con_earnings = []
    con_visit = []
    con_buyCount = []
    for row in buy_data:
        print(row)
        benefit_date = row[1]
        benefit_sum = row[0]
        benefit_visit = row[4]

        if row[3] is None:
            benefit_productCount = 0
        else:
            benefit_productCount = row[3]

        benefit_buyCount = row[5]
        benefit_userCount = row[6]

        if benefit_sum is None:
            benefit_sum = 0

        print(benefit_buyCount, "count")

        benefit_dag += f"""<tr><td>{benefit_date}</td><td>{benefit_sum}</td><td>{benefit_visit}</td><td>{benefit_productCount}</td><td>{round((benefit_productCount / benefit_visit) * 100, 1)}%</td></tr>"""
        print(benefit_date, "benefitdate")

        if date_count < 7:
            print()
            con_date.append(benefit_date)
            con_con.append(
                round((benefit_productCount / benefit_visit) * 100, 1))
            con_earnings.append(benefit_sum)
            con_visit.append(benefit_visit)
            con_buyCount.append(benefit_productCount)

        date_count += 1

    print(benefit_dag)
    # {1000 / benefit_visit} サイトに訪問した人の数
    # {1000 / benefit_userCount} ログインして買った人（ID識別）の数

    # plt.bar(con_date, con_visit, label = "訪問者数")
    plt.bar(con_date, con_buyCount, label="購入された数")
    plt.plot(con_date, con_con, color='skyblue', label="コンバージョン率")

    plt.xlabel("日付")
    plt.ylabel("回数・％")
    plt.title("売上個数・コンバージョン率")
    plt.legend()
    plt.xticks(rotation=15)
    con_img = io.BytesIO()
    plt.savefig(con_img, format="png")
    con_img.seek(0)
    plt.close()

    con_img = base64.b64encode(con_img.getvalue()).decode()

    plt.bar(con_date, con_earnings, label="売上")

    plt.xlabel("日付")
    plt.ylabel("売上金額")
    plt.title("売上")
    plt.legend()
    plt.xticks(rotation=15)
    earnings_img = io.BytesIO()
    plt.savefig(earnings_img, format="png")
    earnings_img.seek(0)
    plt.close()

    earnings_img = base64.b64encode(earnings_img.getvalue()).decode()

    cur.execute("""
                SELECT *
                FROM customerInfo
                """)

    user_data = cur.fetchall()

    user_data_table = ""
    for user in user_data:
        print(user)
        user_id = user[0]
        user_name = user[1] + user[2]
        user_email = user[3]
        user_pass = user[4]
        user_lastLog = str(user[5])

        user_data_table += f"<tr><td>{user_name}</td><td>{user_email}</td><td>{user_pass}</td><td>{user_lastLog}</td><td><form action='/user_delete' method='post'><button type='submit' value='{user_id}' name='delete_user_id'>削除</button></form></td></tr>"

    cur.execute("""
                SELECT *
                FROM inquiry
                """)

    inquiry_data = cur.fetchall()

    print(inquiry_data)
    inquiry_tag = ""
    for inquiry in inquiry_data:
        print(inquiry)

        inquiry_name = inquiry[1]
        inquiry_email = inquiry[2]
        inquiry_prefecture = inquiry[4]
        inquiry_city = inquiry[5]
        inquiry_text = inquiry[7]

        inquiry_tag += f"""

        <div class="inquiry_div">
            <div class="inquiry_detail">
                <p>名前：{inquiry_name}さん</p>
                <p>都道府県：{inquiry_prefecture}{inquiry_city}在住</p>
                <p>email:{inquiry_email}</p>
            </div>
            <div class="inquiry_text">
                <p>{inquiry_text}</p>
            </div>
        </div>
        """

    cur.execute("""
                SELECT clothes.userid,
                clothesImage.img1, 
                clothes.clothesName, 
                clothes.clickCounter, 
                clothes.buyCounter,
                clothes.price,
                AVG(review.review),
                clothes.id
                FROM clothes
                JOIN clothesImage ON clothes.id = clothesImage.clothesId
                JOIN review ON review.clothesId = clothes.id
                GROUP BY review.clothesId
                """)

    product_data = cur.fetchall()

    product_table_tag = ""
    for row in product_data:
        print(row)
        pro_id = row[0]
        pro_user_id = row[0]
        pro_img = row[1]
        pro_name = row[2]

        if len(pro_name) >= 40:
            pro_name = pro_name[:40] + "..."

        pro_click = row[3]
        pro_buy = row[4]
        pro_price = row[5]
        review = row[6]
        product_table_tag += f"""<tr><td><img src='{pro_img}'></td><td>{pro_user_id}</td><td>{pro_name}</td><td>{pro_buy}</td><td>{pro_price}</td><td>{review}</td><td><form action="/product_management"><button type"submit" name="product_number" value="{pro_id}">詳細</button></form></td></tr>"""
    
    display = ""
    
    cur.execute("""
                SELECT id, pageName, pageShow
                FROM feature
                """)
    
    feature_data = cur.fetchall()
    
    feature_tag = ""
    for data in feature_data:
        
        
        if data[2] == "show":
            feature_tag += f"""<tr><td>{data[0]}</td><td>{data[1]}</td><td>
                <input type="radio" name="feature{data[0]}" id="show{data[0]}" checked value="show">
                <label for="show{data[0]}">show</label>
                <input type="radio" name="feature{data[0]}" id="hide{data[0]}" value="hide">
                <label for="hide{data[0]}">hide</label></td></tr>"""
        
        else:
            feature_tag += f"""<tr><td>{data[0]}</td><td>{data[1]}</td><td>
                <input type="radio" name="feature{data[0]}" id="show{data[0]}" checked value="show">
                <label for="show{data[0]}">show</label>
                <input type="radio" name="feature{data[0]}" id="hide{data[0]}" checked  value="hide">
                <label for="hide{data[0]}">hide</label></td></tr>"""


    return render_template("/userinfo/site_administrator.html", access_img=access_img, benefit_dag=benefit_dag, site_data_img=site_data_img, account=common_header[0], log=common_header[1],
                        account_detail=common_header[2], user_data_table=user_data_table, inquiry_tag=inquiry_tag, con_img=con_img, earnings_img=earnings_img, product_table_tag=product_table_tag,
                        display = display, site_buy_count_graph_tag = site_buy_count_graph_tag, feature_tag = feature_tag, footer_tag = common_header[5])


@app.route("/user_delete", methods=["POST"])
def user_delete():
    common_header = loginProcess(login)
    conn, cur = database_connection()
    
    delete_user_id = request.form.get("delete_user_id")
    
    print(delete_user_id)
    
    cur.execute("""
                DELETE FROM customerInfo
                WHERE id = %s
                """, (delete_user_id,))
    
    conn.commit()
    
    return redirect("/site_administrator")



@app.route("/pass_change", methods = ["POST", "GET"])
def pass_change():
    error_tag = ""
    
    if request.method == "POST":
        conn, cur = database_connection()

        email = request.form.get("email")
        
        print(email)
        
        cur.execute("""
                    SELECT COUNT(*), id
                    FROM customerInfo
                    WHERE email = %s
                    """, (email,))
        
        email_data = cur.fetchone()
        
        print(email_data, "email")
        print(email_data[1])
        
        if email_data[0] == 1:
            try:
                def message_base64_encode(message):
                    return base64.urlsafe_b64encode(message.as_bytes()).decode()

                error_tag = ""
                def main(email):
                    scopes = ["https://mail.google.com/"]
                    creds = Credentials.from_authorized_user_file("./json/token.json", scopes)
                    service = build("gmail", "v1", credentials=creds)
                    message = MIMEText("お客様からパスワードの変更を確認しました。\nSHEEPパスワード変更ページ：http://127.0.0.1:5000//pass_change_process\n身に覚えがない場合はアクセスをしないでください。")
                    # 宛先
                    message["To"] = email
                    message["From"] = "SHEEP公式 <SHEEP@gmail.com>"
                    message["Subject"] = "SHEEPパスワード変更URL"
                    raw = {"raw": message_base64_encode(message)}
                    service.users().messages().send(
                        userId = "me",
                        body=raw
                    ).execute()
                main(email)
                session["change_pass_id"] = email_data[1]
            except Exception as e:
                print(e)
                error_tag = "エラー"
                
        elif email_data[0] == 0:
            error_tag = "メールアドレスが間違えています。"
        else:
            print("a")
            error_tag = "エラー"
    else:
        pass
    
    
    
    return render_template("/userinfo/pass_change.html", error_tag = error_tag)
    

@app.route("/pass_change_process", methods = ["GET", "POST"])
def pass_change_process():
    
    if "change_pass_id" in session:
        print("ある")
    else: 
        print("ないので不正")
        return redirect("/")
    
    error_tag = ""
    if request.method == "POST":
        pass_change1 = request.form.get("pass1")
        pass_change2 = request.form.get("pass2")
        print(pass_change1)
        print(pass_change2)
        
    
        if pass_change1 == pass_change2:
            conn, cur = database_connection()
            
            cur.execute("""
                        UPDATE customerInfo
                        SET pass = %s
                        WHERE id = %s
                        """, (pass_change1, session["change_pass_id"]))
            print(session["change_pass_id"])
            conn.commit()
            session.pop("change_pass_id", None)
            
            return redirect("/login")
        else:
            error_tag = "パスワードが異なっています"
    else:
        pass
        
    
    return render_template("/userinfo/pass_change_process.html", error_tag = error_tag)


@app.route("/feature_setting", methods=["POST"])
def feature():
    print()
    
    conn, cur = database_connection()
    
    file_name = request.form.get("filename")
    feature_text = request.form.get("new_feature_text")
    page_name = request.form.get("page_name")
    feature_file = request.files["file"]
    feature_img = request.files["feature_img"]
    
    extension = os.path.splitext(feature_file.filename)[1]
    
    print(file_name,  feature_text, feature_file)
    print(extension, "extension")
    
    
    app.config['UPLOAD_FOLDER'] = 'templates/feature'
    feature_img_path = os.path.join('static', "images", 'feature')
    feature_file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name + extension))
    feature_img.save(os.path.join(app.root_path,feature_img_path,feature_img.filename))
    
    cur.execute("INSERT INTO feature(topPageText,featureImg,featureFileName,pageName) VALUES (%s,%s,%s,%s)",
            ( feature_text, feature_img.filename, file_name + extension, page_name))

    conn.commit()
    # return redirect("/site_administrator")
    return extension

@app.route("/feature")
def feature1():
    print()
    
    conn, cur = database_connection()
    common_header = loginProcess(login)
    
    page_num = request.args.get("feature")
    
    cur.execute("""
                SELECT featureFileName, featureImg, pageName
                FROM feature
                WHERE id = %s
                """, ( page_num,))
    
    page = cur.fetchone()
    
    # return page
    return render_template(f"feature/{page[0]}", top_img = page[1], page_name = page[2], account=common_header[0], log=common_header[1],
                        account_detail=common_header[2], footer_tag = common_header[5])

@app.route("/show_or_hide", methods=["POST"])
def show_or_hide():
    
    conn, cur = database_connection()

    cur.execute("""
                SELECT id
                FROM feature
                """)
    
    feature_data = cur.fetchall()
    
    for data in feature_data:
        print(data)
        check = request.form.get(f"feature{data[0]}")
        print(check)
        
        cur.execute("""
                    UPDATE feature
                    SET pageShow = %s
                    WHERE id = %s
                    """, (check, data[0]))
        
        conn.commit()
        # idで調べてshowかhideか見極めるボタンをつける
    
    return redirect("/site_administrator")
    

if __name__ == "__main__":
    app.run(port=5000, threaded=True, debug=True)
