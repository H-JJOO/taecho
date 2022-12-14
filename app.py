from bs4 import BeautifulSoup
from flask import Flask, render_template, request, jsonify, url_for
from bson.objectid import ObjectId
from datetime import datetime
app = Flask(__name__)
from pymongo import MongoClient
import requests # requests 라이브러리 설치 필요

client = MongoClient('mongodb+srv://dadaqq1009:z10091214@cluster0.ooefn7z.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

# index 페이지
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/goals')
def goals():
    return render_template('goals.html')

# 팀 소개 페이지
@app.route('/introduce')
def introduce():
    return render_template('introduce.html')

# html 이름을 바꾸고 배열식으로 만들어서 만들어도됨..
# member_' + member_num + '.html'
@app.route('/<member_name>')
def introduce_members(member_name):
    if member_name == "joo":
        return render_template('member_1.html')
    if member_name == "jun":
        return render_template('member_2.html')
    if member_name == "park":
        return render_template('member_3.html')
    if member_name == "lee":
        return render_template('member_4.html')
    if member_name == "jeong":
        return render_template('member_5.html')

# 팀 약속 페이지
@app.route('/promise')
def promise():
    promise_list = objectIdDecoder(list(db.promises.find({}).limit(200)))
    return render_template('promise.html', template_promises=promise_list)

# 블로그 페이지
@app.route('/blog')
def blog():
    return render_template('blog.html')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

for i in range(1, 7):
    url = 'https://icepri3535.tistory.com/?page=' + str((i))

    data =requests.get('https://icepri3535.tistory.com/?page=' + str((i)) , headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    blogs = soup.select('#mArticle > div')

    for blog in blogs:
        a = blog.select_one('strong')
        if a is not None:
            title1 = a.text
            time1 = blog.select_one('div > span.txt_date').text
            summary1 = blog.select_one('a.link_post > p').text

            doc = {
                'title1': title1,
                'summary1': summary1,
                'time1': time1
            }
            # db.TaechoBlog.insert_one(doc)

@app.route("/blog", methods=["GET"])
def blog_get():
    blog_list = list(db.TaechoBlog.find({}, {'_id': False}))

    return jsonify({'blogs':blog_list})

# 방명록 페이지
@app.route('/board')
def board():
    return render_template('board.html')


def objectIdDecoder(list):
    results=[]
    for document in list:
        document['_id'] = str(document['_id'])
        results.append(document)
    return results

@app.route("/api/boards/<member_id>", methods=["POST", "GET", "PUT", "DELETE"])

def api_boards(member_id):
    col_name = 'member_' + member_id
    if request.method == "POST":
        name = request.form['name']
        message = request.form['message']

        doc = {
            'name': name,
            'message': message
        }
        db[col_name].insert_one(doc)
        return jsonify({'msg': '기록 완료!'})
    elif request.method == "PUT":
        board_id = request.form['id']
        message = request.form['message']
        db[col_name].update_one({'_id': ObjectId(board_id)}, {'$set': {'message': message}})
        return jsonify({'msg': '수정 완료!'})
    elif request.method == "DELETE":
        board_id = request.form['id']
        db[col_name].delete_one({'_id': ObjectId(board_id)})
        return jsonify({'msg': '삭제 완료!'})
    else:
        guest_list = objectIdDecoder(list(db[col_name].find({})))
        return jsonify({'guests': guest_list})

@app.route("/api/promises", methods=["GET", "POST", "PUT", "DELETE"])
def api_promises():
    col_name = 'promises'
    now = datetime.now()
    if request.method == "POST":
        name = request.form['name']
        content = request.form['content']
        promise_style = request.form['promise_style']
        doc = {
            "name": name,
            "content": content,
            "promiseStyle": promise_style,
            "createdAt": now
        }
        db[col_name].insert_one(doc)
        return jsonify({'msg': '약속을 새겼다!'})
    elif request.method == "PUT":
        promise_id = request.form['id']
        content = request.form['content']
        db[col_name].update_one({'_id': ObjectId(promise_id)},
                                {'$set': {'content': content, 'createdAt': now
                                          }})
        return jsonify({'msg': '약속은 바뀌는거야!'})
    elif request.method == "DELETE":
        promise_id = request.form['id']
        db[col_name].delete_one({'_id': ObjectId(promise_id)})
        return jsonify({'msg': '삭제 완료!'})
    else:
        promise_list = objectIdDecoder(list(db[col_name].find({}).sort("_id", -1).limit(200)))
        return jsonify({'promise_list': promise_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)