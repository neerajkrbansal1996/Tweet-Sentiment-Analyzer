import os
from flask import Flask, request, render_template, jsonify
from twitter import TwitterClient

app = Flask(__name__)
api = TwitterClient('@neerajkrbansal')

@app.route('/')
def index():
	return render_template("home.html")

@app.route('/tweets')
def tweets():
        query = request.args.get('query')
        api.set_query(query)

        tweets = api.get_tweets()
        return jsonify({'data': tweets, 'count': len(tweets)})

port = int(os.environ.get('PORT', 5000))
app.run(host="0.0.0.0", port=port, debug=True)
