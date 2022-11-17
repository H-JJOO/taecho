from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://dadaqq1009:z10091214@cluster0.ooefn7z.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


import requests
from bs4 import BeautifulSoup

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

# @app.route("/member_1", methods=["POST"])
# def post_guest_list1():
#
#     name_receive = request.form['name_give']
#     message_receive = request.form['message_give']
#
#     doc = {
#         'name': name_receive,
#         'message': message_receive
#     }
#     db.member_1.insert_one(doc)
#
#     return jsonify({'msg': '기록 완료!'})

@app.route('/member_2')
def jun():
    return render_template('member_2.html')

# @app.route("/member_2", methods=["POST"])
# def post_guest_list2():
#
#     name_receive = request.form['name_give']
#     message_receive = request.form['message_give']
#
#     doc = {
#         'name': name_receive,
#         'message': message_receive
#     }
#     db.member_2.insert_one(doc)
#
#     return jsonify({'msg': '기록 완료!'})

@app.route('/member_3')
def park():
    return render_template('member_3.html')

# @app.route("/member_3", methods=["POST"])
# def post_guest_list3():
#
#     name_receive = request.form['name_give']
#     message_receive = request.form['message_give']
#
#     doc = {
#         'name': name_receive,
#         'message': message_receive
#     }
#     db.member_3.insert_one(doc)
#
#     return jsonify({'msg': '기록 완료!'})

@app.route('/member_4')
def lee():
    return render_template('member_4.html')


# @app.route("/member_4", methods=["POST"])
# def post_guest_list4():
#
#     name_receive = request.form['name_give']
#     message_receive = request.form['message_give']
#
#     doc = {
#         'name': name_receive,
#         'message': message_receive
#     }
#     db.member_4.insert_one(doc)
#
#     return jsonify({'msg': '기록 완료!'})


@app.route('/member_5')
def jung():
    return render_template('member_5.html')

# @app.route("/member_5", methods=["POST"])
# def post_guest_list5():
#
#     name_receive = request.form['name_give']
#     message_receive = request.form['message_give']
#
#     doc = {
#         'name': name_receive,
#         'message': message_receive
#     }
#     db.member_5.insert_one(doc)
#
#     return jsonify({'msg': '기록 완료!'})
# 팀원 한명 한명 페이지

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

# @app.route("/board_1", methods=["GET"])
# def get_guest_list1():
#     guest_list1 = list(db.member_1.find({}, {'_id': False}))
#     return jsonify({'guests1': guest_list1})
#
# @app.route("/board_2", methods=["GET"])
# def get_guest_list2():
#     guest_list2 = list(db.member_2.find({}, {'_id': False}))
#     return jsonify({'guests2': guest_list2})
#
# @app.route("/board_3", methods=["GET"])
# def get_guest_list3():
#     guest_list3 = list(db.member_3.find({}, {'_id': False}))
#     return jsonify({'guests3': guest_list3})
#
# @app.route("/board_4", methods=["GET"])
# def get_guest_list4():
#     guest_list4 = list(db.member_4.find({}, {'_id': False}))
#     return jsonify({'guests4': guest_list4})
#
#
# @app.route("/board_5", methods=["GET"])
# def get_guest_list5():
#     guest_list5 = list(db.member_5.find({}, {'_id': False}))
#     return jsonify({'guests5': guest_list5})






if __name__ == '__main__':
    app.run('0.0.0.0', port = 5000, debug = True)
