import json
import urllib.error
import urllib.request

from flask import Flask, render_template, jsonify, request, abort
import requests
import pymysql
app = Flask(__name__)

conn = pymysql.connect(
    host="koctankdbcluster.cmctwgljftes.us-east-1.rds.amazonaws.com",  # endpoint link
    port=3306,  # 3306
    user="admin",  # admin
    password="welcome123",  # adminadmin
    db="koctank",  # test,
    connect_timeout=5,
    charset='utf8mb4'

)

#Table Creation
# cursor=conn.cursor()
# create_table="""
# create table Details (name varchar(200),email varchar(200),comment varchar(200),gender varchar(20) )
#
# """
# cursor.execute(create_table)
#
# def insert_details(name,email,comment,gender):
#     cur=conn.cursor()
#     cur.execute("INSERT INTO Details (name,email,comment,gender) VALUES (%s,%s,%s,%s)", (name,email,comment,gender))
#     conn.commit()
#
# def get_details():
#     cur=conn.cursor()
#     cur.execute("SELECT *  FROM Details")
#     details = cur.fetchall()
#     return details

## RDS MySQL 연결
# import db as db_mysql
# database = db_mysql.DB()
# try:
#     doc = urllib.request.urlopen("http://169.254.169.254/latest/dynamic/instance-identity/document", timeout=1).read()
# except urllib.error.URLError:
#     doc = None
#
# if doc:
#     app.config['REGION'] = json.loads(doc)['availabilityZone']
# else:
#     app.config['REGION'] = "unknown region"

## HTML을 주는 부분
@app.route('/')
def home():
    # database.query("SHOW TABLES")
    return render_template('index.html')

@app.route('/men')
def men():
    return render_template('men.html')

@app.route('/women')
def women():
    return render_template('women.html')

@app.route('/memo', methods=['GET'])
def listing():
    # articles = list(db.articles.find({}, {'_id': False}))
    # return jsonify({'all_articles': articles})
    return jsonify({'msg':'이것은 GET 요청입니다'})

## API 역할을 하는 부분
@app.route('/memo', methods=['POST'])
def saving():
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']

    # url = 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=171539'

    print(url_receive, comment_receive)
    return jsonify({'msg':'이것은 Post 요청입니다'})

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)