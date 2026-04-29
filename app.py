from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def status():
    node_name = socket.gethostname()
    return f"<h1>bharath is checking again</h1><p>Running on: {node_name}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
