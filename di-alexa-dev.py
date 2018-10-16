import nltk
#from twython import Twython
from twarc import Twarc
from collections import Counter
from string import *
import json
import simplejson
import re
import fileinput
import collections
import time
import logging
import requests
print("""\
                     

d8888b. d888888b         .d8b.  db      d88888b db    db  .d8b.  
88  `8D   `88'          d8' `8b 88      88'     `8b  d8' d8' `8b 
88   88    88           88ooo88 88      88ooooo  `8bd8'  88ooo88 
88   88    88    C8888D 88~~~88 88      88~~~~~  .dPYb.  88~~~88 
88  .8D   .88.          88   88 88booo. 88.     .8P  Y8. 88   88 
Y8888D' Y888888P        YP   YP Y88888P Y88888P YP    YP YP   YP 
                                                                 
                                                                 

By @AKRoLLA47
""")




def total(self):

	for (sum) in count1+count2+count3+count4+count5+count6+count7+count8:
		return total





def bagOfWords(tweets):
    wordsList = []
    for (words, dialect) in tweets:
      wordsList.extend(words)
    return wordsList

def wordFeatures(wordList):
    wordList = nltk.FreqDist(wordList)
    wordFeatures = wordList.keys()
    return wordFeatures

def getFeatures(doc):
    docWords = set(doc)
    feat = {}
    for word in wordFeatures:
        feat['contains(%s)' % word] = (word in docWords)
    return feat

def read_tweets(fname, t_type):
    tweets = []
    f = open(fname, 'r')
    line = f.readline()
    while line != '':
        tweets.append([line, t_type])
        line = f.readline()
    f.close()
    return tweets










dr1 = read_tweets('dr1.txt', 'New England')

dr2 = read_tweets('dr2.txt', 'Northern')

dr3 = read_tweets('dr3.txt', 'North Midland')

dr4 = read_tweets('dr4.txt', 'South Midland')

dr5 = read_tweets('dr5.txt', 'Southern')

dr6 = read_tweets('dr6.txt', 'New York City')

dr7 = read_tweets('dr7.txt', 'Western')

dr8 = read_tweets('dr8.txt', 'Army Brat (moved around)')


tweets = []
for (words, dialect) in dr1 + dr2 + dr3 + dr4 + dr5 + dr6 + dr7 + dr8:
    words_filtered = [e.lower() for e in nltk.word_tokenize(words) if len(e) >= 3]
    tweets.append((words_filtered, dialect))






def classify_tweet(tweet):
    return \
        classifier.classify(getFeatures(nltk.word_tokenize(tweet)))

    

wordFeatures = wordFeatures(bagOfWords(tweets))
training_set = nltk.classify.apply_features(getFeatures, tweets)
classifier = nltk.NaiveBayesClassifier.train(training_set)



##print(classifier.show_most_informative_features(32))



ConsumerKey = "eNLaoPtYx4OcLKexxibPTECeU"
ConsumerSecret = "SU7QqyjPwCiYmMLcbFA9Kh6c8j4UnHefSbB2kovePQEWaduZWf"
AccessToken = "775195777316614144-FIWbBkr98PzCVjEpApCbbZ59PpvISqQ"
AccessTokenSecret = "vds0ZvdeC9gtXcUdU5XacRjidPOUXTFMk6DfQFTUxssxS"



twitter = Twarc(ConsumerKey,
                  ConsumerSecret,
                  AccessToken,
                  AccessTokenSecret)
				  
#screenname = raw_input("enter a twitter handle: ")
			  
#time = twitter.timeline(screen_name = raw_input("enter a twitter handle: "))
"""
def rate_limit(secs):
    print("going to sleep for %s seconds" % secs)
    while True:
        try:
            time.sleep(0.5)
            yield tweet
        except ValueError as e:
            print "Waiting a few minutes..."
            time.sleep(16 * 60)
        except ValueError as e:
            print "Got a Error->"+ e.reason
            time.sleep(30)
       """
def timeline(self, user_id=None, screen_name=None, max_id=None,
                 since_id=None):
        """
        Returns a collection of the most recent tweets posted
        by the user indicated by the user_id or screen_name parameter.
        Provide a user_id or screen_name.
        """
        # Strip if screen_name is prefixed with '@'
        if screen_name:
            screen_name = screen_name.lstrip('@')
        id = screen_name or user_id
        id_type = "screen_name" if screen_name else "user_id"
        logging.info("starting user timeline for user %s", id)
        url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
        params = {"count": 200, id_type: id}

        while True:
            if since_id:
                params['since_id'] = since_id
            if max_id:
                params['max_id'] = max_id

            try:
                resp = self.get(url, params=params, allow_404=True)
            except requests.exceptions.HTTPError as e:
                if e.response.status_code == 404:
                    logging.info("no timeline available for %s", id)
                    break
                raise e

            statuses = resp.json()

            if len(statuses) == 0:
                logging.info("no new tweets matching %s", params)
                break

            for status in statuses:
                # If you request an invalid user_id, you may still get
                # results so need to check.
                if not user_id or user_id == status.get("user",
                                                        {}).get("id_str"):
                    yield status

            max_id = str(int(status["id_str"]) - 1)

for status in twitter.timeline(screen_name = raw_input("enter a twitter handle: ")):
  #  print(" User: {0} \n Created: {1} \n Text: {2} \n Sentiment: {3} \n ".format(tweet["user"]["name"],tweet["created_at"],tweet["text"])), #classifier.classify(getFeatures( tweet)).encode('utf-8')))



     	print("Tweet: {0} \n Dialect: {1} \n".format( status['full_text'].encode('utf-8'), classifier.classify(getFeatures( status['full_text'].split())).encode('utf-8')))

if classifier.classify(getFeatures(status['full_text'].split())).encode('utf-8') == ['New England']:
		count1 = 0
		with open('NewEnglandtweets.txt', "a") as outfile:
    			json.dump(status, outfile)		
			#f = open('NewEnglandtweets.txt', "a")
			#f.write(status['full_text'].encode('utf-8')+"\n")
			#f.close()
			count1 += 1
        		outfile.write('\n')

if classifier.classify(getFeatures( status['full_text'].split())).encode('utf-8') == ['Northern']:
		count2 = 0
		with open('NewEnglandtweets.txt', "a") as outfile:
    			json.dump(status, outfile)		
			#f = open('Northerntweets.txt', "a")
			#f.write(status['full_text'].encode('utf-8')+"\n")
			#f.close()
			count2 += 1
        		outfile.write('\n')
if classifier.classify(getFeatures( status['full_text'].split())).encode('utf-8') == ['North Midland']:		
		count3 = 0
		with open('NewEnglandtweets.txt', "a") as outfile:
    			json.dump(status, outfile)		
			#f = open('NorthMidlandtweets.txt', "a")
			#f.write(status['full_text'].encode('utf-8')+"\n")
			#f.close()
			count3 += 1
        		outfile.write('\n')
if classifier.classify(getFeatures( status['full_text'].split())).encode('utf-8') == ['South Midland']:
		count4 = 0
		with open('NewEnglandtweets.txt', "a") as outfile:
    			json.dump(status, outfile)		
			#f = open('SouthMidlandtweets.txt', "a")
			#f.write(status['full_text'].encode('utf-8')+"\n")
			#f.close()
			count4 += 1
        		outfile.write('\n')
if classifier.classify(getFeatures( status['full_text'].split())).encode('utf-8') == ['Southern']:
		count5 = 0		
		with open('NewEnglandtweets.txt', "a") as outfile:
    			json.dump(status, outfile)		
			#f = open('Southerntweets.txt', "a")
			#f.write(status['full_text'].encode('utf-8')+"\n")
			#f.close()
			count5 += 1
        		outfile.write('\n')
if classifier.classify(getFeatures( status['full_text'].split())).encode('utf-8') == ['New York City']:
		count6 = 0		
		with open('NewEnglandtweets.txt', "a") as outfile:
    			json.dump(status, outfile)
			#f = open('NewYorkCitytweets.txt', "a")
			#f.write(status['full_text'].encode('utf-8')+"\n")
			#f.close()
			count6 += 1
        		outfile.write('\n')
if classifier.classify(getFeatures( status['full_text'].split())).encode('utf-8') == ['Western']:
		count7 = 0
		with open('NewEnglandtweets.txt', "a") as outfile:
    			json.dump(status, outfile)
			#f = open('Westerntweets.txt', "a")
			#f.write(status['full_text'].encode('utf-8')+"\n")
			#f.close()
			count7 += 1
        		outfile.write('\n')
if classifier.classify(getFeatures( status['full_text'].split())).encode('utf-8') == ['Army Brat(moved around)']:
		count8 = 0
		with open('NewEnglandtweets.txt', "a") as outfile:
    			json.dump(status, outfile)
			#f = open('ArmyBrattweets.txt', "a")
			#f.write(status['full_text'].encode('utf-8')+"\n")
			#f.close()
			count8 += 1
        		outfile.write('\n')

			#total.count = count1+count2+count3+count4+count5+count6+count7+count8
#rate_limit(secs)

#     print(tweet['text'])
#     print(classifier.classify(getFeatures(tweet)).encode('utf-8'))









#test_tweets = read_tweets('happy.txt', 'positive')
#test_tweets.extend(read_tweets('sad.txt', 'negative'))
#total = float(len(tweetlimit))
#total = accuracy = float(len(test_tweets))

#for tweet in test_tweets:
#    if classify_tweet(tweet[0]) != tweet[1]:
#        accuracy -= 1

print 'Number of Tweets Classified  With New England Dialect: %d'  , (count1)  
print 'Number of Tweets Classified  With Northern Dialect: %d' , (count2)
print 'Number of Tweets Classified  With North Midland Dialect: %d' , (count3)
print 'Number of Tweets Classified  With South Midland Dialect: %d'  ,(count4)
print 'Number of Tweets Classified  With Southern Dialect: %d' , (count5)
print 'Number of Tweets Classified  With New York City Dialect: %d' , (count6)
print 'Number of Tweets Classified  With Western Dialect: %d' , (count7)
print 'Number of Tweets Classified With Army Brat (moved around) Dialect: %d' ,  (count8)
print 'Total Number of Tweets Classified: %d'  (total)



print("Training Set Accuracy: {}".format(nltk.classify.accuracy(classifier, training_set) * 100 ) + "%")
raw_input("press enter to exit.")
