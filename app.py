from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "Version 1: Hello from Python Docker Application!"
@app.route("/about")
def about():
    return "About: This Flask application is running in Docker."
@app.route("/contact")
def contact():
    return "Contact: DevOps Practical Demo"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

