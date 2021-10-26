# github.com/echtr
from flask import Flask, render_template, request, url_for
import json
import sqlite3 as sql

def add(nick, message):
    vt = sql.connect("database.db")
    c = vt.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS msgs (nick, message)""")
    c.execute(f"""INSERT INTO msgs(nick, message) VALUES("{nick}", "{message}")""")
    vt.commit()
    vt.close()
def rd():
    vt = sql.connect("database.db")
    c = vt.cursor()
    c.execute("SELECT * FROM msgs")
    _data= c.fetchall()
    vt.close()
    last_data = ""
    for i in _data:
        last_data = last_data + f"<li> {i[0]} > {i[1]}</li>"
    return last_data
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/post_message", methods=["GET","POST"])
def post_message():
    _data=[]
    if request.method == "POST":
        try:
            _data.append(request.form["nick"])
            _data.append(request.form["message"])
            add(_data[0], _data[1])
        except Exception as e:
            print(e)
        return json.dumps({"success":True}), 200, {"ContentType":"application/json"} 

@app.route("/get_datas", methods = ["GET", "POST"])
def get_datas():
    if request.method == "GET":
        try:
            rd()
        except Exception as e:
            print(e)
    return json.dumps(rd()), 200, {"ContentType":"application/json"}    

if __name__ == "__main__":
    app.run(debug=True)