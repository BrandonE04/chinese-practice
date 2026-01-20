from flask import Flask, render_template, request
from chatbot import queryChatBot

app = Flask(__name__)

context = ["你好"]

@app.route("/", methods = ['POST', 'GET'])
def homepage():
    response = queryChatBot(context[-1])
    print(response)

    if response[0:5] == "ERROR":
        error = response.text
    else:
        response = response.splitlines()
        context.append(response[0])
        return render_template("index.html", characters=response[0], pinyin=response[1],
            english=response[2], context=context, contextLength=len(context))

@app.route("/sendChat", methods = ['POST', 'GET'])
def sendChat():
    userMessage = request.form['userMessage']
    context.append(userMessage)

    return homepage()   

if __name__ == '__main__':
    app.run(debug=True)