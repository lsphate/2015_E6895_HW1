#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "123190876-MCdXohJwM5CYM5BYKe8kePHpCuKdx7h5IXfweEqo"
access_token_secret = "azSEncgwY8aT4TLs48pIWfyrzGBHFuCDVHFrrrTnAjvfd"
consumer_key = "6g2YoWvXd3fmMnGSjg1U5AHp6"
consumer_secret = "Gv9QnJzGLVteG0uDyC72skmbxvkcHgFWpqzHwRXp7g73g1vdFx"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['Heineken'])