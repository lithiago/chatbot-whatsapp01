import ollama
from flask import Flask, request, abort
from langchain.chat_models import ChatOllama



PROMPT_TEMPLATE = ""
app =  Flask(__name__)



@app.route("/webhook", methods=["POST"])
def webhook():
    if request.method == "POST":
        print(request.json)
        return "sucess", 200
    else:
        abort(400)


