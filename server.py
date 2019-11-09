from flask import Flask, render_template, request
from chatbot import getResponse

app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/message", methods=['POST'])
def test():
    return getResponse(request.form['message'])

if __name__ == "__main__":
    app.run()