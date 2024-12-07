from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Testing CICD !! with Jenkins ☁️☁️☁️"

if __name__ == "__main__":
    app.run(port=9696)
