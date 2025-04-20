# Imports Flask and module request
from flask import Flask, request

# Creates an instance of Flask for the web application 
app = Flask(__name__)

# Route for endpoint /info
@app.route("/info", methods=["GET"])
def info():
    return {
        "message": "An example of an API using Flask"
        }

# Route for endpoint /message 
@app.route("/message", methods=["POST"])
def message():
    data = request.json
    message = data.get("message", "")
    return {
        "respond": f"Got your message: {message}"
        }

if __name__ == "__main__":
    app.run(debug=True)