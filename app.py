#web app
from flask import Flask, render_template,Request

app=Flask(__name__)

@app.route("/")
def index():
    return("web app")

if __name__=="__main__":
    app.run()