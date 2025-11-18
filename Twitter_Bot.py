from flask import Flask, request
import time as  darshil
import tweepy as sapara 
import os as ds


# Create Flask app instance
app = Flask(__name__)

CONSUMER_KEY = ds.getenv("CONSUMER_KEY")
CONSUMER_SECRET = ds.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = ds.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = ds.getenv("ACCESS_TOKEN_SECRET")

twitter = sapara.Client(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
)

@app.route('/')
def home():
    """Render homepage with tweet, delay, and retweet forms."""
    return '''
        <h1 style="text-align:center; color:darkblue;">Twitter Bot Dashboard</h1>

        <div style="text-align:center; margin-top:40px;">
            <form action ="/tweet" method = "post" style = "display : inline-block; padding:10px;">
                <input type = "text" name = "text" placeholder = "Enter Tweet here"
                       style = "width:250px; padding:5px; border:1px solid ; border-radius : 5px;">
                <input type = "number" name ="delay" placeholder = "Delay (sec)"
                       style = "width:120px; padding:5px; border : 1px solid ; border-radius : 5px; margin-left:5px;">
                <input type = "submit" value = "Tweet"
                       style = "background: red; color:white; border:none; padding:5px 10px; border-radius:5px;">
                       
            </form>
        </div>

        <div style = "text-align:center; margin-top:40px;">
            <form action = "/retweet" method = "post" style = "display:inline-block; padding:10px;">
                <input type = "text" name = "tweet_id" placeholder = "Enter Tweet ID here"
                       style = "width:250px; padding:5px; border:1px solid ; border-radius:5px;">
                <input type = "number" name ="delay" placeholder = "Delay (sec)"
                       style = "width:120px; padding:5px; border : 1px solid ; border-radius : 5px; margin-left:5px;">
                <input type = "submit" value = "Retweet"
                       style = "background:red; color:white; border:none; padding:5px 10px; border-radius:5px;">
            </form>
        </div>
    '''


# Route to handle tweeting

@app.route('/tweet', methods=['POST'])
def tweet():
    """Post tweet with optional delay"""
    text = request.form.get('text')
    delay = request.form.get('delay')

    if not text:
        return "Please enter a tweet! Go Back"

    try:
        if delay:  # check for delay
            darshil.sleep(int(delay))

        twitter.create_tweet(text=text)
        return f"Tweet posted successfully: {text} Go Back"

    except Exception as e:
        return f"Error: {e} Go Back"


@app.route('/retweet', methods=['POST'])
def retweet():
    """Retweet a tweet by its ID."""
    delay = request.form.get('delay')
    tweet_id = request.form.get('tweet_id')

    if not tweet_id:
        return "Please enter a valid Tweet ID! Go Back"

    try:
        if delay:  # check for delay in ms
            darshil.sleep(int(delay))

        twitter.retweet(tweet_id)
        return f"Retweeted Successfully (ID: {tweet_id}) Back"

    except Exception as e:
        return f"Error: {e} Go Back"


if __name__ == "__main__":
    app.run(debug=True)
