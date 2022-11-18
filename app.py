from flask import Flask, render_template, request, jsonify, url_for

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://dadaqq1009:z10091214@cluster0.ooefn7z.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

# index 페이지
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/goals')
def goals():
    return render_template('goals.html')

#---------------------------
#---------------------------
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
#---------------------------
#---------------------------

# 팀 약속 페이지
@app.route('/promise')
def promise():
    return render_template('promise.html')

# 블로그 페이지
@app.route('/blog')
def blog():
    return render_template('blog.html')

# 방명록 페이지
@app.route('/board')
def board():
    return render_template('board.html')

# @app.route("/api/boards/<member_id>", methods=["POST", "GET"])
@app.route("/api/boards/<member_id>", methods=["POST", "GET"])
def api_boards(member_id):
    if request.method == "POST":
        name_receive = request.form['name_give']
        message_receive = request.form['message_give']

        doc = {
            'name': name_receive,
            'message': message_receive
        }
        col_name = 'member_' + member_id
        db[col_name].insert_one(doc)
        return jsonify({'msg': '기록 완료!'})
    else:
        col_name = 'member_' + member_id
        guest_list = list(db[col_name].find({}, {'_id': False}))
        return jsonify({'guests': guest_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port = 5000, debug = True)
