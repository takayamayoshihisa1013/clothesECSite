from flask import Flask, render_template, request
# import requests
import sqlite3
# でコード要員
import urllib.parse


app = Flask(__name__)




# ログイン状況初期値
login = "out"

userName = ""



    
    
    




# if login == 1:
#     userName = 






# データベース作成
# dbname = "customer.db"
    
# conn = sqlite3.connect(dbname)

# cur  = conn.cursor()

# cur.execute(
#     "CREATE TABLE customerInfo(id INTEGER PRIMARY KEY AUTOINCREMENT, lastName STRING, firstName STRING, email STRING, pass STRING, favorite STRING, cart STRING, buyLog STRING)"
# )

# conn.commit()



# データベース処理
# def db(which):
    
        













@app.route("/")
def index():
    
    # print(userName)
    
    if login == "on":
        acount = "<a href='./login'><button class='acount'>アカウントにログイン</button></a>"
    else:
        acount = f"<p>{userName}さん、ようこそ！</p><a href='/login'><button>別のアカウントでログインする</button></a>"
    
    
    return render_template("index.html", acount=acount)




# ログイン初回アクセス
@app.route("/login")
def login():
    print("ログインしたいよ")
    
    return render_template("login.html")



# ログイン可否
@app.route("/login", methods=["POST"])
def loginCheck():
    
    print("ろぐいんできたよ")
    # js初期値
    script = ""
    
    # 入力されたメールアドレス
    inputEmail = request.form["mail"]
    # 入力されたパスワード
    inputPass = request.form["pass"]
    # print(userName)
    
    
    
    
    # データベースの情報と照合
    
    dbname = "customer.db"
    
    conn = sqlite3.connect(dbname)
    
    cur = conn.cursor()
    
    # データを取り出すクエリを実行
    cur.execute("select pass, email, lastName from customerInfo;")
    # データを取る
    data = cur.fetchall()
    # 1列ごとに全てのデータを取る
    for row in data:
        print(row[0],row[1])
        
        
        # 照合
        if row[0] == inputPass and row[1] == inputEmail:
            # 照合完了
            print("一致するデータがあったよ！")
            
            
            # ログイン状態にする
            global login
            global userName
            
            login = "in"
            userName = row[2]
            
            script = "<script src='./../static/js/login.js'></script>"
            error = ""
        
        else:
            print("一致するデータがなかったよ...")
            script = ""
            error = "<h3>メールアドレス、又はパスワードが違います</h3>"
    
    # dbEmail = 
    
    
    
    
    
    
    
    
    
    
    
    
    
    return render_template("login.html",script = script, error = error)


# @app.route("/check",methods=["POST"])
# def check():
#     print("ゲットしたよ")
    
#     # global userName
    
#     # ユーザーの名前
#     userName = request.form["username"]
#     # デコード
#     userName = urllib.parse.unquote(userName)
#     print(userName)
    
    
    
    
    
    
    
    
#     # SQL作成
#     # データベース名
#     # dbname = "UserAcount.db"
#     # conn = sqlite3.connect(dbname)
    
#     # # カーソル作成
#     # cur = conn.cursor()
    
    
    
    
    
    
#     return render_template("check.html")





# サインアップページ初回アクセス
@app.route("/signup")
def signup():
    print("サインアップしたいよ")
    
    
    return render_template("signup.html")
    
    
    

# サインアップ可否
@app.route("/signup", methods=["POST"])
def signupCheck():
    
    
    # ユーザー名
    lastName = urllib.parse.unquote(request.form["lastName"])
    firstName = urllib.parse.unquote(request.form["firstName"])
    print(lastName + firstName)
    # メアド
    email = request.form["email"]
    # パス1
    pass1 = request.form["pass1"]
    # パス2
    pass2 = request.form["pass2"]
    
    # 照合 & メールアドレスがすでにないかの確認
    
    dbname = "customer.db"
    
    conn = sqlite3.connect(dbname)
    
        # カーソル
    cur  = conn.cursor()
    
    cur.execute("select email from customerInfo;")
    
    emailData = cur.fetchall()
    
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
            

    print(emailError)
    
    if pass1 == pass2 and emailError == "":
        # JS追加
        script = "<script src='./../static/js/signup.js'></script>"
        # えらーなにもなし
        passError = ""
        
        
        OKtext = f"<h2>登録完了しました。</h2><h3>ようこそ{lastName}{firstName}さん!</h3><h4>10秒後にログインページに移動します。</h4>"
        
        
        # 登録処理
        
        
        # データベースの名前
        dbname = "customer.db"
    
        conn = sqlite3.connect(dbname)
    
        # カーソル
        cur  = conn.cursor()
    
        # データベースに追加する
        cur.execute(f"INSERT INTO customerInfo (lastName,firstName,email,pass,favorite,cart,buyLog) values('{lastName}','{firstName}','{email}','{pass1}',NULL,NULL,NULL)")
    
    
        # "CREATE TABLE customerInfo(id INTEGER PRIMARY KEY AUTOINCREMENT, lastName STRING, firstName STRING, email NONE, pass STRING)"
        conn.commit()
        conn.close()
        
        print("サインアップできたよ")
    
    else:
        OKtext = ""
        passError = "パスワードが一致しません又は入力されたメールアドレスはすでに登録されています"
        script = ""
    
    
    
    
    
    
    
    
    
    
        
        
        
        
        
        
    
    
    
    return render_template("signup.html", passError = passError, script = script,
                        text = OKtext, emailError = emailError)







if __name__ == "__main__":
    app.run(port=5000, threaded=True, debug=True)