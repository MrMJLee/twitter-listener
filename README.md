* First component of Twitter Analytics Application *

           --- Listener component ---

This module contains a “Tweepy” library which supports for accessing the Tweeter API and a CPickle library for serializing and de-serializing any python objects.
 
This “Listner.py” connects to the Twitter and opens up a connection to the AWS messaging queue service called SQS by providing any required credential information. After those connections are succeeded, this module fetches the Twitter social feeds as objects and serialize those objects into character streams before they are saved into the messaging queue service (SQS). Running this program will get social feeds from Twitter in stream, stopping this program will stop listening feeds from Twitter.
