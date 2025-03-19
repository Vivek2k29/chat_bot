from flask import Flask, request, jsonify
from chatbot import get_chat_response

app = Flask(__name__)


@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_query = data.get("query")

    if not user_query:
        return jsonify({"error": "Query is required"}), 400

    response = get_chat_response(user_query)
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)
