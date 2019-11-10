from flask import Flask, session, render_template, request
import prompt
import nlp

app = Flask(__name__)
app.secret_key = b'\xf0E\x18\x0bx0\xb9y\xc6\xc9\xdaA\x8e/\xabH' # super secret

@app.route("/")
def index():
    # always create a new session (meaning clear data from old session)
    session['prompt'] = 'start'
    return render_template('webpage.html')

@app.route("/message", methods=['POST'])
def test():
    tmp = getResponse(request.form['message'])
    return(tmp)

def getResponse(user_message):
    user_in = user_message[0:-1].lower() # slice to cut out the newline character
    words = user_in.split(" ")
    choice = None
    p = prompt.get_obj(session['prompt']) # the current prompt object
    print(p.message)
    for word in words:
        choice = p.next_name(word)
        print("Choice: " + (choice or 'None'))
        if (choice is not None):
            break
    if (choice is None):
        return("Sorry, I didn't understand that. " + p.message)
    else:
        session['prompt'] = choice # p = next value based on user input
        p = prompt.get_obj(choice)
        print(p.message)
        return(p.message)

if __name__ == "__main__":
    app.run()

