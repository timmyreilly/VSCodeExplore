#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

# twitter client
import tweepy

#tokens
from tokens import *

# database interface
import sqlite3
conn = sqlite3.connect('tweets.db')
curs = conn.cursor()

class StreamWatcherHandler(tweepy.StreamListener):
    """ Handles all incoming tweets as discrete tweet objects.
    """

    def on_status(self, status):
        """Called when status (tweet) object received.

        See the following link for more information:
        https://github.com/tweepy/tweepy/blob/master/tweepy/models.py
        """
        try:
            tid = status.id_str
            usr = status.author.screen_name.strip()
            txt = status.text.strip()
            in_reply_to = status.in_reply_to_status_id
            coord = status.coordinates
            src = status.source.strip()
            cat = status.created_at

            # Now that we have our tweet information, let's stow it away in our 
            # sqlite database
            curs.execute("insert into tweets (tid, username, created_at, content, reply_to, coordinates, source) values(?, ?, ?, ?, ?, ?, ?)", (tid, usr, cat, txt, in_reply_to, coord, src))
            conn.commit()
        except Exception as e:
            # Most errors we're going to see relate to the handling of UTF-8 messages (sorry)
            print(e)

    def on_error(self, status_code):
       print('An error has occured! Status code = %s' % status_code)
       return True

def main():
    # establish stream
    consumer_key = CONSUMER_KEY
    consumer_secret = CONSUMER_SECRET
    auth1 = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)

    access_token = ACCESS_TOKEN_SECRET
    access_token_secret = ACCESS_TOKEN_SECRET
    auth1.set_access_token(access_token, access_token_secret)

    print "Establishing stream...",
    stream = tweepy.Stream(auth1, StreamWatcherHandler(), timeout=None)
    print "Done"

    # Start pulling our sample streaming API from Twitter to be handled by StreamWatcherHandler
    stream.sample()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print "Disconnecting from database... ",
        conn.commit()
        conn.close()
        print "Done"