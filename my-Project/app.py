
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "application": "My jenkins Pipeline with a Proper Jenkins File",
        "message": "Application is running successfully",
        "status": "OK"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "application": "Dockerized Flask Application",
        "message": "Application is running successfully",
        "status": "OK"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
