from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    app_name = os.getenv("APP_NAME", "SWE40006 Task 4.3")
    environment = os.getenv("APP_ENV", "Development")

    return f"""
    <h1>{app_name}</h1>
    <h2>Docker Container Deployment</h2>
    <p>Student: Md Fahemul Islam</p>
    <p>Environment: {environment}</p>
    <p>Task 4.3 application is running successfully.</p>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)