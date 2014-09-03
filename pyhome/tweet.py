
import twitter

# Python API on: http://mike.verdone.ca/twitter/
# (easy install twitter)

# settings on
# https://apps.twitter.com

# recipe on: http://wilsonericn.wordpress.com/2011/08/22/tweeting-in-python-the-easy-way/

# API key + secret
CON_KEY = "i4kH9Ntwpsuw7ElThGdqVqlMw"
CON_SEC = "Iqa9o4xruQHnrX2DF8q9zIieEryLFOgdhsN3qSumT1jP4mBev4"

# Access token + secret 
TOK_KEY = "61298929-8Yps2pcC5o8kE8BblP8kOmttrUJTKo6rmulxAtHZr"
TOK_SEC = "uxXSaoOE0wEuJGIRZIoui5AR7TBoXuj1LOgVLJ2l46s9G"

def send_tweet(message):
    my_auth = twitter.OAuth(TOK_KEY, TOK_SEC, CON_KEY, CON_SEC)
    twit = twitter.Twitter(auth=my_auth)
    twit.statuses.update(status=message)

