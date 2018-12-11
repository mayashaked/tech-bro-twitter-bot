import sys
sys.path.append('/Users/maya/code')

from TwitterFollowBot import TwitterBot 
import markov
import time

my_bot = TwitterBot()

things_to_tweet = markov.do_it()

for tweet in things_to_tweet:
	my_bot.send_tweet(tweet)
	time.sleep(60*3)