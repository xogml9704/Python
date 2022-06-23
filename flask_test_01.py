from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def index():
    return 'random : <strong>'+str(random.random())+'</strong>'
    # retrun 값 안에는 문자열 값만 가능

@app.route('/create/')
def create():
    return 'Create'

@app.route('/read/1/')
def read():
    return 'Read 1'

app.run(port=5000, debug=True)

# @app.route('/페이지 이름')
# def 페이지 이름():
#     return '페이지 내용'
# (/페이지 이름을 입력하면 밑에 함수를 응대해서 출력하라.)

# @app.route('/read/<id>/') <> id를 주면 <> 이후의 파라미터로 들어간다.
# def read(id):
#     print(id)
#     return 'Read ' + id

