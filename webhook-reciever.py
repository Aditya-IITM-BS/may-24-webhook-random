from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Get the JSON data from the request
    data = request.get_json()

    # Log or process the data (here, we're just printing it)
    print("Received webhook data:", data)

    # Send a response to acknowledge receipt of the webhook
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=80)
