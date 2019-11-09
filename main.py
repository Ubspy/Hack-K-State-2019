from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/request", methods=['POST'])
def test():
    return str(int(request.form['number']) + 1)

if __name__ == "__main__":
    app.run()