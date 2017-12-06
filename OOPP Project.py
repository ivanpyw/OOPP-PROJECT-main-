from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template("index.html")

@app.route('/contact/')
def contact():
    return render_template("contact.html")

@app.route('/elements/')
def elements():
    return render_template("elements.html")

@app.route('/index/')
def index():
    return render_template("index.html")

@app.route('/services/')
def services():
    return render_template("services.html")

@app.route('/left-sidebar/')
def left_sidebar():
    return render_template("left-sidebar.html")

@app.route('/right-sidebar/')
def right_sidebar():
    return render_template("right-sidebar.html")



if __name__ == '__main__':
    app.run(debug=True)
