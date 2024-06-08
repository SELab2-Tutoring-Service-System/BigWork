from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from collections import defaultdict
import datetime
from tea_register_ import tea_register
from stu_register_ import stu_register
from tea_login_ import tea_login
from stu_login_ import stu_login
from stu_search_ import stu_search
from tea_record_ import tea_record
from tea_search_ import tea_search
import logging

app = Flask(__name__)
CORS(app)

route_counter = defaultdict(int)
ip_counter = defaultdict(int)
traffic_stats = {'upload': 0, 'download': 0}

# 定义一个装饰器，用于统计路由访问次数
@app.before_request
def count_route():
    route = request.path
    ip = request.remote_addr
    route_counter[route] += 1
    ip_counter[ip] += 1


@app.route('/')
def hello_world():
    print("hello world", flush=True)
    return 'Hello, World!'


@app.route('/tea_register', methods=['POST', 'GET'] )
def tea_reg():
    print("teacher register", flush=True)
    data = request.json.get('data')
    print(data, flush=True)
    data = data.split(',')
    res = tea_register(data)
    print(res, flush=True)
    return jsonify({"res": res})


@app.route('/stu_register', methods=['POST', 'GET'] )
def stu_reg():
    print("student register", flush=True)
    data = request.json.get('data')
    print(data, flush=True)
    data = data.split(',')
    res = stu_register(data)
    print(res, flush=True)
    return jsonify({"res": res})


@app.route('/tea_login', methods=['POST', 'GET'] )
def tea_log():
    print("teacher login", flush=True)
    data = request.json.get('data')
    print(data, flush=True)
    data = data.split(',')
    res = tea_login(data)
    print(res, flush=True)
    return jsonify({"res": res})


@app.route('/stu_login', methods=['POST', 'GET'] )
def stu_log():
    print("student login", flush=True)
    data = request.json.get('data')
    print(data, flush=True)
    data = data.split(',')
    res = stu_login(data)
    print(res, flush=True)
    return jsonify({"res": res})


@app.route('/tea_record', methods=['POST'] )
def tea_rec():
    print("teacher record", flush=True)
    data = request.json.get('data')
    print(data, flush=True)
    data = data.split(',')
    res = tea_record(data)
    print(res, flush=True)
    return jsonify({"res": res})


@app.route('/stu_search', methods=['POST', 'GET'] )
def stu_sea():

    subject = request.args.get('subject')
    stage = request.args.get('stage')
    time = request.args.get('time')
    gender = request.args.get('gender')

    if gender == 'male':
        gender = "M"
    elif gender == 'female':
        gender = "F"
    else:
        gender = "ok"

    res = stu_search(subject, stage, time, gender)
    print("查询返回: ",res)

    return jsonify(res)


@app.route('/tea_search', methods=['POST', 'GET'] )
def tea_sea():

    id = request.args.get('mobile')
    res = tea_search(id)
    print("查询返回: ",res)



    return jsonify(res)


@app.route('/stats')
def stats():
    try:
        route_stats = {route: count for route, count in route_counter.items()}
        unique_ips = len(ip_counter)
        return {'route_stats': route_stats, 'unique_visitors': unique_ips}
    except:
        return {'err': "err"}


if __name__ == '__main__':
    app.debug = True
    app.logger.setLevel(logging.DEBUG)
    app.run(host='0.0.0.0', port=5000)
