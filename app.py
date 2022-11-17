from flask import Flask, render_template, request, jsonify
from bson.objectid import ObjectId
from datetime import datetime
app = Flask(__name__)
from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.1iypvdi.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


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


@app.route("/blog", methods=["GET"])
def blog_get():
    blog_list = list(db.TaechoBlog.find({}, {'_id': False}))
    return jsonify({'blog': blog_list})





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
        content = request.form['promise']
        promise_style = request.form['promise_style']
        doc = {
            "name": name,
            "promise": content,
            "promiseStyle": promise_style,
            "createdAt": now
        }
        db[col_name].insert_one(doc)
        return jsonify({'msg': '약속을 새겼다!'})
    elif request.method == "PUT":
        promise_id = request.form['id']
        content = request.form['promise']
        db[col_name].update_one({'_id': ObjectId(promise_id)},
                                {'$set': {'promise': content, 'createdAt': now
                                          }})
        return jsonify({'msg': '약속은 바뀌는거야!'})
    elif request.method == "DELETE":
        promise_id = request.form['id']
        db[col_name].delete_one({'_id': ObjectId(promise_id)})
        return jsonify({'msg': '삭제 완료!'})
    else:
        promise_list = objectIdDecoder(list(db[col_name].find({}).limit(200)))
        return jsonify({'promise_list': promise_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
