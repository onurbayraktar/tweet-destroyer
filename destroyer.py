import tweepy
from . import config

# Authentication to twitter
auth = tweepy.OAuthHandler(config.API_KEY, config.API_SECRET_KEY)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# Empty Array That Will Keep Id's of Tweets
tmp = []

# Function to extract the tweets
def get_tweets(username):

    try:
        api.verify_credentials()
        print("Authentication is OK!")
    except:
        print("Error occured ...")

    # Getting all the tweets of user
    cursor = tweepy.Cursor(api.user_timeline, screen_name=username)

    # Put the tweet ids to the array
    for tweet in cursor.items():
        # Appending tweets to the empty array tmp
        tmp.append(tweet.id)


if __name__ == '__main__':
    # Getting the tweet ids to the array
    get_tweets(config.YOUR_USERNAME)

    # Destroy all the tweets in array
    try:
        for tweet in tmp:
            api.destroy_status(tweet)
        print("All tweets deleted successfully..")

    except:
        print("A problem occured when deleting tweets!")
