from flask import Flask, render_template, jsonify, request
from flask_mysqldb import MySQL,MySQLdb

app = Flask(__name__)

app.secret_key = "caircocoders-ednalan"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'testingdb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/postskill",methods=["POST","GET"])
def postskill():
    cursor = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        skills = request.form.getlist('skill[]')
        for value in skills:
            cur.execute("INSERT INTO skills (skillname) VALUES (%s)",[value])
            mysql.connection.commit()
        cur.close()
        msg = 'New record created successfully'
    return jsonify(msg)
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
