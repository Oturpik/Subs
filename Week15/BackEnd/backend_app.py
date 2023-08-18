from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS

import random

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

quotes = [
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Success is not the key to happiness. Happiness is the key to success. – Albert Schweitzer",
    "The future depends on what you do today. – Mahatma Gandhi",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "Don't watch the clock; do what it does. Keep going. – Sam Levenson",
    "Innovation distinguishes between a leader and a follower. – Steve Jobs",
    "Your time is limited, don't waste it living someone else's life. – Steve Jobs",
    "The only thing standing between you and your dream is the will to try and the belief that it is actually possible. – Joel Brown",
    "Success is walking from failure to failure with no loss of enthusiasm. – Winston Churchill",
    "Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work. – Steve Jobs"
]

@app.route('/quote', methods=['GET'])
def get_random_quote():
    random_quote = random.choice(quotes)
    return jsonify({'quote': random_quote})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
