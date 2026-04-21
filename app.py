from flask import Flask, request, abort

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    # Se você definiu methods=["POST"], o Flask já barra outras 
    # requisições automaticamente, então o "if" é opcional aqui.
    print(request.json)
    return "success", 200

# ADICIONE ISTO:
if __name__ == "__main__":
    app.run(port=5000)