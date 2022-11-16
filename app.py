from flask import Flask, render_template, request, jsonify

app = Flask(__name__)



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

@app.route('/member_2')
def jun():
    return render_template('member_2.html')

@app.route('/member_3')
def park():
    return render_template('member_3.html')

@app.route('/member_4')
def lee():
    return render_template('member_4.html')


@app.route("/member_4", methods=["POST"])
def web_board_post():
    name_receive = request.form['name_give']
    message_receive = request.form['message_give']

    doc = {
        'name': name_receive,
        'message': message_receive
    }
    db.SetColorData.insert_one(doc)

    return jsonify({'msg': '기록 완료!'})


@app.route('/member_5')
def jung():
    return render_template('member_5.html')

# @app.route('/member_5')
# def jung_set_color_post():
#     backgroundColor_receive = request.form["backgroundColor_give"]
#     textColor_receive       = request.form["textColor_give"]
#     boxColor_receive        = request.form["boxColor_give"]

#     doc = {
#         'backgroundColor': backgroundColor_receive,
#         'textColor': textColor_receive,
#         'boxColor': boxColor_receive
#     }

#     db.member_5.insert_one(doc)
#     return render_template({'msg':'Color change!'})




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


if __name__ == '__main__':
    app.run('0.0.0.0', port = 5000, debug = True)
