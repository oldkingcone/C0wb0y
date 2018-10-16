
#!/usr/bin/python

import twarc
import nltk
import stylometry
import matplotlib
import pandas
import sys
import os
import datetime
from subprocess import call
#import di-alexa-dev.py
print('''

          ..######...#######..##......##.########...#######..##....##
          .##....##.##.....##.##..##..##.##.....##.##.....##..##..##.
          .##.......##.....##.##..##..##.##.....##.##.....##...####..
          .##.......##.....##.##..##..##.########..##.....##....##...
          .##.......##.....##.##..##..##.##.....##.##.....##....##...
          .##....##.##.....##.##..##..##.##.....##.##.....##....##...
          ..######...#######...###..###..########...#######.....##...




''')
username = str(raw_input('[!] Please enter a username [!]\n->'))
out_file_final = str(raw_input('[!] Please enter a name and output file type(csv,txt,json,jsonl,gephi(.gefx))[!]\n->'))
filtered_outfile = username+"-filteredtweets"+".csv" 
stylobot_outfile = username+"-styloanalysis"+".csv" 
out_file = str(username)+".json"



dt_now = datetime.datetime.now()
# place utils  in top directory where dumps is going to be produced. 
try:
    os.makedirs('/home/akrolla/Desktop/dev/cowboyman/dumps/json/')
    os.makedirs('/home/akrolla/Desktop/dev/cowboyman/dumps/txt/')
    os.makedirs('/home/akrolla/Desktop/dev/cowboyman/dumps/txt/csv')
    os.makedirs('/home/akrolla/Desktop/dev/cowboyman/dumps/json/de_dup/')
    os.makedirs('/home/akrolla/Desktop/dev/cowboyman/dumps/json/de_rt/')
except:
    pass

dump_dir = '/home/akrolla/Desktop/dev/cowboyman/dumps/json/'
sylo_dir = '/home/akrolla/Desktop/dev/cowboyman/dumps/txt/'
de_rt = '/home/akrolla/Desktop/dev/cowboyman/dumps/json/de_rt/'
de_dup = '/home/akrolla/Desktop/dev/cowboyman/dumps/json/de_dup/'
os.system('cd %s'% dump_dir)



of = open(out_file,'a')
args = username + ' > ' + out_file




#sets up json to be pased around


try:
    os.system('twarc timeline %s'%args)
    print("Loading")
except:
    raise


#passes json to dedup


try:
  #  args1 =username + str(' --format ')+ str('csv ')
   # args2 = str(' --output ') + out_file_final
   # args3 = args1 + args2
    #out_file1 = str(username)+".csv"
    de_rtd = de_rt + out_file
    args = out_file + ' > ' + de_rtd
    os.system('python /home/akrolla/Desktop/dev/cowboyman/utils/deduplicate.py %s'%args)
    print("Loading")
except:
    raise

#passes json to de rt


try:
    de_dupd = de_dup + out_file
    args = out_file + ' > ' + de_dupd
    os.system('python /home/akrolla/Desktop/dev/cowboyman/utils/noretweets.py %s'%args)
    print("Loading")
except:
    raise



# prints timeline to csv or whatever format



try:
    of = open(out_file,'a')
    args1 =username + str(' --format ')+ str('csv ')
    args2 = str(' --output ') + out_file_final
    args3 = args1 + args2
    print("Loading")
    call('twarc timeline ' + args3, shell=True)
except:
    raise


#try:
#print("would you like a nodal 



#except:
 #   raise



try:
    print("Would you like StyloMetric Analysis Yes or No")
    question = raw_input()
    if question == 'Yes' or 'yes' or 'y' or 'Y':
	data = pandas.read_csv(out_file_final)
	filtered_Data = data['text']
	filtered_Data.to_csv(filtered_outfile,sep='\t', encoding='utf-8')
	print("""\	
            ___                                                 ___    
           /  /\          ___         ___                      /  /\   
          /  /:/_        /  /\       /__/|                    /  /::\   
         /  /:/ /\      /  /:/      |  |:|    ___     ___    /  /:/\:\  
        /  /:/ /::\    /  /:/       |  |:|   /__/\   /  /\  /  /:/  \:\ 
       /__/:/ /:/\:\  /  /::\     __|__|:|   \  \:\ /  /:/ /__/:/ \__\:\\ 
       \  \:\/:/~/:/ /__/:/\:\   /__/::::\    \  \:\  /:/  \  \:\ /  /:/
        \  \::/ /:/  \__\/  \:\      \~~\:\    \  \:\/:/    \  \:\  /:/ 
         \__\/ /:/        \  \:\      \  \:\    \  \::/      \  \:\/:/  
           /__/:/          \__\/       \__\/     \__\/        \  \::/   
           \__\/                                               \__\/    
                                         ___                
                          _____         /  /\          ___   
                         /  /::\       /  /::\        /  /\  
                        /  /:/\:\     /  /:/\:\      /  /:/  
                       /  /:/~/::\   /  /:/  \:\    /  /:/   
                      /__/:/ /:/\:| /__/:/ \__\:\  /  /::\   
                      \  \:\/:/~/:/ \  \:\ /  /:/ /__/:/\:\  
                       \  \::/ /:/   \  \:\  /:/  \__\/  \:\ 
                        \  \:\/:/     \  \:\/:/        \  \:\\
                         \  \::/       \  \::/          \__\/
                          \__\/         \__\/                
By @AKRoLLA47
""")
	from stylometry.extract import *
	import pandas as pd
	StyloInput = username+"-filteredtweets"+".csv"
	StyloOutput = str(sylo_dir+stylobot_outfile)
	StyloCorpus = filtered_outfile
	StyloBot = StyloDocument(filtered_outfile)
	#StyloBot_corpus = StyloCorpus.from_glob_pattern(filtered_outfile)
	#StyloBot_corpus.output_csv(StyloOutput)
	StyloBot.text_output()
	#datas = pandas.read_csv(out_file_final)
	#Filtered_Data = pd.DataFrame(eval(str(StyloBot)))
	#Filtered_Data.to_csv(stylobot_outfile,sep='\t', encoding='utf-8')
	#StyloBot.to_csv(stylobot_outfile,sep='\t', encoding='utf-8')
	#print 'Exporting your file(s) to {}'.format(StyloOutput) 
	#os.system('python stylo_bot.py')
	#os.system('1')
	#os.system(filtered_outfile)
	#os.system(stylobot_outfile)
#still need to figure out how to get this to a file
except:
    raise


try:
    print("Would you like Sentiment Analysis Yes or No")
    question = raw_input()
    if question == 'Yes' or 'yes' or 'y' or 'Y':
	from twarc import Twarc
	import twython
	print("""\
                     
	o    o o      .oPYo. 
	8b   8 8      8    8 
	8`b  8 8     o8YooP' 
	8 `b 8 8      8      
	8  `b8 8      8      
	8   `8 8oooo  8      
	..:::........:..:::::
	:::::::::::::::::::::
	:::::::::::::::::::::
                                                    
	ooooo o o     o .oPYo. o     o o    o .oPYo. oooooo 
	  8   8 8b   d8 8.     8     8 8b   8 8.         d' 
	  8   8 8`b d'8 `boo   8     8 8`b  8 `boo      d'  
 	  8   8 8 `o' 8 .P     8     8 8 `b 8 .P       d'   
	  8   8 8     8 8      8     8 8  `b8 8       d'    
	  8   8 8     8 `YooP' 8oooo 8 8   `8 `YooP' dooooo 
	::..::....::::..:.....:..........:::..:.....:.......
	::::::::::::::::::::::::::::::::::::::::::::::::::::
	::::::::::::::::::::::::::::::::::::::::::::::::::::
	By @AKRoLLA47
	""")



	def bagOfWords(tweets):
	    wordsList = []
	    for (words, sentiment) in tweets:
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



	positiveTweets = read_tweets('happy.txt', 'positive')
	negativeTweets = read_tweets('sad.txt', 'negative')
#placeholder model






	tweets = []
	for (words, sentiment) in positiveTweets + negativeTweets:
	    words_filtered = [e.lower() for e in nltk.word_tokenize(words) if len(e) >= 3]
	    tweets.append((words_filtered, sentiment))






	def classify_tweet(tweet):
	    return \
	        classifier.classify(getFeatures(nltk.word_tokenize(tweet)))

    

	wordFeatures = wordFeatures(bagOfWords(tweets))

	training_set = nltk.classify.apply_features(getFeatures, tweets)
##print training_set
	classifier = nltk.NaiveBayesClassifier.train(training_set)

##print(classifier.show_most_informative_features(32))

	#ConsumerKey = ""
	#ConsumerSecret = ""
	#AccessToken = ""
	#AccessTokenSecret = ""

#this section is for twarc

	#twitter = Twarc(ConsumerKey,
                  #ConsumerSecret,
                  #AccessToken,
                  #AccessTokenSecret)
	def nlptimelinez():				  
		#screenname = raw_input("enter a twitter handle: ")
		#tweetlimit = raw_input("enter a limit of tweets(max 150): ")				  



		#time = twitter.get_user_timeline(screen_name = screenname, count = tweetlimit)
		#twarc call below
		#time = twitter.timeline(username)
		time = out_file_final


		for tweet in time:
	    		print("Tweet: {0} \n Sentiment: {1} \n".format( tweet["full_text"].encode('utf-8'),
			classifier.classify(getFeatures( tweet["full_text"].split())).encode	('utf-8')))
			test_tweets = read_tweets('happy.txt', 'positive')
			test_tweets.extend(read_tweets('sad.txt', 'negative'))

		for tweet in time:
			if classifier.classify(getFeatures(tweet["full_text"].split())).encode('utf-8') != 'negative':

				f = open('happy.txt', "a")
				f.write(tweet["full_text"].encode('utf-8')+"\n")
				f.close()
	
	
			if classifier.classify(getFeatures( tweet["full_text"].split())).encode('utf-8') != 'positive':
				f = open('sad.txt', "a")
				f.write(tweet["full_text"].encode('utf-8')+"\n")
				f.close()

	nlptimelinez()


#total = accuracy = float(len(test_tweets))
#for tweet in test_tweets:
#    if classify_tweet(tweet[0]) != tweet[1]:
#        accuracy -= 1
#print('Total accuracy: %f%% (%d/20).' % (accuracy / total * 100, accuracy))
	print("Training Set Accuracy: {}".format(nltk.classify.accuracy(classifier, training_set) * 100 ) + "%")
	raw_input("press enter to exit.")



except:
    raise
