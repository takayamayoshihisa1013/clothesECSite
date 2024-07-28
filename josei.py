from flask import Flask, render_template
import mysql.connector
import datetime


app = Flask(__name__)


@app.route("/")
def josei():
    
    dbname = "ecdatabase"
    conn = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database=dbname
    )
    
    cur = conn.cursor()
    
    return render_template("josei/josei.html")
    

if __name__ == "__main__":
    app.run(port=5000, threaded=True, debug=True)
