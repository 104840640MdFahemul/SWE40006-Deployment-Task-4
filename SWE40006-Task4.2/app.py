from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>SWE40006 - Task 4.2</h1>
    <h2>Dockerized Python Flask Application</h2>
    <p>Student: Md Fahemul Islam</p>
    <p>Container deployment is working successfully.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)