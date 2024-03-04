from flask import Flask, render_template, request
from multi_instance_terminal import terminal
from threading import Thread
from txt2cmd import Text2CMD
from gpt import genCompletion
from tokens import BehaviourToken
from brain import *
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('server.html')

@app.route('/response', methods=['POST'])
def response():
    data = request.form['input_text']
    Text2CMD(data).equat()
    Brain().cmd2pw(Text2CMD.cmd_stream)
    response = f"You entered: {data}"
    return response
Thread(target=lambda: app.run(port=5000)).start()
terminal.execute()