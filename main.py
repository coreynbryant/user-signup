from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/welcome", methods=['POST'])
def add_user():
    # look inside the request to figure out what the user typed
    username = request.form['username']
    
    return render_template('welcome.html', username = username)


@app.route("/")
def index():
    return render_template('main.html')

app.run()