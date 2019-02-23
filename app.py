from flask import Flask,render_template

app=Flask(__name__)
@app.route("/home")
def index():
    return render_template("index.html") 
@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/error")
def error():
    return "Get out"
if(__name__=="__main__"):
    app.run(debug=True)

