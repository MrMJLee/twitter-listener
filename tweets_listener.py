from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from boto.sqs.message import Message
import cPickle
import urllib3

urllib3.disable_warnings()
consumer_key = "<Your tweeter consumer Key>"
consumer_secret ="<Your tweeter secret key>"
access_token = "<Your tweeter access token>"
access_token_secret = "<Your tweeter secret token>"

ACCESS_KEY = "<Your AWS access Key>"
SECRET_KEY ="<Your AWS secret Key>"

import boto.sqs
conn= boto.sqs.connect_to_region('us-west-2',aws_access_key_id= ACCESS_KEY,
                                 aws_secret_access_key= SECRET_KEY)

q = conn.get_all_queues()

class StdOutListener(StreamListener):
    def on_data(self,data):
        #print data
        msg=cPickle.dumps(data)
        m = Message()
        m.set_body(msg)
        status = q[0].write(m)
        return True
    def on_error(self,status):
        print status

if __name__ == '__main__':
    keywords = ['Korea']
    print "Listnening....tweets....."
    l = StdOutListener()
    auth = OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    stream = Stream(auth,l)
    stream.filter(track=keywords)

