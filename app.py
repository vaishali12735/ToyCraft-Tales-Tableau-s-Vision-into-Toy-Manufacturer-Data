from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("welcome.html")

@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/story')
def story():
    return render_template("story.html")

if __name__ == '__main__':
    app.run(debug=True)