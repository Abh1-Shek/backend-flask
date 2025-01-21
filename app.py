from flask import Flask, request, jsonify
from textblob import TextBlob
# Initialize Flask app
app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze_sentiment():
    try:
        # Get the JSON data from the request
        data = request.get_json()
        text = data.get("text", "")

        if not text:
            return jsonify({"error": "No text provided"}), 400

        # Perform sentiment analysis
        blob = TextBlob(text)

        polarity = blob.sentiment.polarity
        results = "Neutral"
        # Determine sentiment based on polarity
        positive_confidence = (polarity + 1) / 2
        negative_confidence = 1 - positive_confidence
        results = "Positive: " + str(positive_confidence) + "Negative: " + str(negative_confidence)
        
        return jsonify({"results": results}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
