from flask import Flask

app=Flask(__name__)
@app.route("/home")
def index():
    return "hello"
    return "Hello"
@app.route("/contact")
def contact():
    return "contact 787856851656"
@app.route("/error")
def error():
    return "GEt out"
if(__name__=="__main__"):
    app.run()

