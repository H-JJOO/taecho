from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# index 페이지
@app.route('/')
def home():
    return render_template('index.html')

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
def jung():
    return render_template('member_3.html')

@app.route('/member_4')
def lee():
    return render_template('member_4.html')

@app.route('/member_5')
def park():
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

# 방명록 페이지
@app.route('/board')
def board():
    return render_template('board.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port = 5000, debug = True)
