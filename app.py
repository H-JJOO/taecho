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
@app.route('/introduce/joo')
def joo():
    return render_template('joo.html')

@app.route('/introduce/jun')
def jun():
    return render_template('jun.html')

@app.route('/introduce/jung')
def jung():
    return render_template('jung.html')

@app.route('/introduce/lee')
def lee():
    return render_template('lee.html')

@app.route('/introduce/park')
def park():
    return render_template('park.html')
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
