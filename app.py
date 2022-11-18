from bs4 import BeautifulSoup
from flask import Flask, render_template, request, jsonify
from bson.objectid import ObjectId

app = Flask(__name__)
from pymongo import MongoClient
import requests # requests 라이브러리 설치 필요


client = MongoClient('mongodb+srv://test:sparta@cluster0.1iypvdi.mongodb.net/?retryWrites=true&w=majority')
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


# 팀원 한명 한명 페이지
@app.route('/member_1')
def joo():
    return render_template('member_1.html')



@app.route('/member_2')
def jun():
    return render_template('member_2.html')

@app.route("/member_2", methods=["POST"])
def post_guest_list2():
    name_receive = request.form['name_give']
    message_receive = request.form['message_give']

    doc = {
        'name': name_receive,
        'message': message_receive
    }
    db.member_2.insert_one(doc)

    return jsonify({'msg': '기록 완료!'})



@app.route('/member_3')
def park():
    return render_template('member_3.html')


@app.route('/member_4')
def lee():
    return render_template('member_4.html')

@app.route('/member_5')
def jung():
    return render_template('member_5.html')

# 팀원 한명 한명 페이지

# 팀 약속 페이지
@app.route('/promise')
def promise():
    return render_template('promise.html')


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
            db.TaechoBlog.insert_one(doc)




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

# @app.route("/api/boards/<member_id>", methods=["POST", "GET"])
@app.route("/api/boards/<member_id>", methods=["POST"])
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

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
