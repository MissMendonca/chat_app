import os
from flask import Flask, render_template, redirect

app = Flask(__name__)
messages = []

def add_message(username, message):
    messages.append(f"{username}: {message}")

def get_all_messages():
    return "<br>".join(messages)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/<username>')
def user(username):
    return f"<h1>Welcome, {username}</h1> {get_all_messages()}" 

@app.route('/<username>/<message>')
def send_message(username, message):
    add_message(username, message)
    
    return redirect('/' + username)

if __name__ == '__main__':
    app.run(host = os.environ.get('IP', '0.0.0.0'),
            port = int(os.environ.get('PORT', '5000')),
            debug = True)