from app import app
from flask import jsonify, request
from db_operations import take_statistic
from visitors import VisitorManager

manager = VisitorManager()


@app.route('/')

def index():
    ip = request.remote_addr
    manager.handle_visitor(ip)
    return "счетчик посещений"


@app.route('/stat')
def stat():
    return jsonify(take_statistic())
