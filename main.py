from flask import Flask

app = Flask(__name__)

@app.route("/health")
def hello():
    return "I'm alive!"

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port=80)