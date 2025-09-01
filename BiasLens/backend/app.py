from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

news = [
    {"id": 1, "title": "Government launches new policy", "category": "Politics"},
    {"id": 2, "title": "Football team wins championship", "category": "Sports"},
    {"id": 3, "title": "Breakthrough in AI research", "category": "Technology"},
    {"id": 4, "title": "Celebrity donates to charity", "category": "Entertainment"},
    {"id": 5, "title": "Stock market reaches new high", "category": "Finance"}
]

recommendations = [
    {"id": 1, "title": "Movie: AI Future", "genre": "Sci-Fi", "sponsored": False},
    {"id": 2, "title": "Movie: Romance Saga", "genre": "Romance", "sponsored": True},
    {"id": 3, "title": "Movie: War Tactics", "genre": "Action", "sponsored": False},
    {"id": 4, "title": "Movie: Comedy Nights", "genre": "Comedy", "sponsored": False},
]

@app.route('/news/biased')
def get_biased_news():
    return jsonify([n for n in news if n["category"] in ["Politics","Finance"]])

@app.route('/news/neutral')
def get_neutral_news():
    return jsonify(news)

@app.route('/recommendations/biased')
def get_biased_recommendations():
    return jsonify([r for r in recommendations if r["sponsored"] or r["genre"]=="Romance"])

@app.route('/recommendations/neutral')
def get_neutral_recommendations():
    return jsonify(recommendations)

@app.route('/bias-score')
def get_bias_score():
    biased = len([r for r in recommendations if r["sponsored"]])
    score = (biased / len(recommendations)) * 100
    return jsonify({"bias_score": score})

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(debug=True)








