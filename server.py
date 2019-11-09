from flask import Flask, render_template, request
import prompt

p = prompt.prompt_list('start')
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('webpage.html')

@app.route("/message", methods=['POST'])
def test():
    tmp = getResponse(request.form['message'])
    print(tmp)
    return tmp

def getResponse(message):
    global p
    user_in = message.lower()
    words = user_in.split(" ")
    choice = None
    for word in words:
        choice = p.next(word)
        if choice is not None:
            break
    if choice is None:
        return("Sorry, I didn't understand that.")
    else:
        p = prompt.prompt_list(choice) # p = next value based on user input
        return(p.message)

if __name__ == "__main__":
    app.run()
