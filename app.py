#!/bin/bash
# Install the tools the app needs
sudo apt-get update -y
sudo apt-get install -y python3-flask

# Create the app file on the server
cat <<EOF > /home/ubuntu/app.py
$(cat <<'INNER_EOF'
from flask import Flask
import socket
import datetime
app = Flask(__name__)
@app.route('/')
def status():
    node_name = socket.gethostname()
    return f"<h1>Automation is fully working!!!</h1><p>Running on: {node_name}</p>"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
INNER_EOF
)
EOF

# Start the app in the background
sudo python3 /home/ubuntu/app.py &
