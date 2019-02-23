from flask import Flask

app=Flask(__name__)
@app.route("/home")
def index():
    return "<h2>hello</h2><h3> hi</h3>"
@app.route("/contact")
def contact():
    return "contact  64668  5464687658 787856851656"
@app.route("/error")
def error():
    return "Get out"
if(__name__=="__main__"):
    app.run(debug=True)

