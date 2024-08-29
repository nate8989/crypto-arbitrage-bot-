from flask import Blueprint, render_template, jsonify
from .bot import run_bot

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/api/execute_arbitrage', methods=['POST'])
def execute_arbitrage():
    run_bot()
    return jsonify({"status": "Arbitrage Executed"})
