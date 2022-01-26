import random
from flask import Flask
from flask import request, jsonify
from app.visitor_manager import VisitorManager

app = Flask(__name__)
manager = VisitorManager()


@app.route('/')
def index():
    ip = request.args.get('redefine_ip', request.remote_addr)
    random_ip = request.args.get('random', False)
    if random_ip == '':
        ip = generate_ip()
    if not check_ip(ip):
        ip = generate_ip()
    manager.handle_visitor(ip)
    return "счетчик посещений"


@app.route('/stat_by_day')
def stat_by_day():
    return jsonify(manager.take_statistic(by_day=True))


@app.route('/stat_by_month')
def stat_by_month():
    return jsonify(manager.take_statistic(by_month=True))


@app.route('/stat_by_year')
def stat_by_year():
    return jsonify(manager.take_statistic(by_year=True))


def generate_ip():
    return ".".join(map(str, (random.randint(0, 255)
                              for _ in range(4))))


def check_ip(ip):
    split_ip = ip.split('.')
    if len(split_ip) != 4:
        return False
    for x in split_ip:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True
