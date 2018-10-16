# C0wb0y

This is still very much a work in progress


C0wb0y: a suite of AI driven heuristics to determine characteristics of users of social media




#### di-alexa: 

A  model derived from DARPA's TIMIT corpus of the 8 dialectal regions of the United States.
this can determine where in the country a user likely is.

#### NLPtimelinez & NLPtweetz:

A sentiment analysis model based on Robert Plutchik's theory of the Range of emotions it contains a model (in progress) of 12 different emotions ranging from the least to most extreme of emotions.
this can be used to determine various things , like emotions to certain topics in avarying range, it can also be used to find people whom might be prone to violence about certain topics.

#### StyloBot: 
A stylometric analysis model that builds a corpus and determines different lexical and syntactical values to determine authorship of the author.

This is still very much in development, some of the sentiment models are not complete , i was trying to put around 1,000,000 tweets into the model as a whole. (to handpick a million tweets takes a lot of time, and to reduce biasing I would like to crowdsource this part.)  



### Roadmap:


change all the models over to the same api

#### neural net :
I would like to build a neural net to relate all of the analytics into a profile of said user

#### graphing: 
I would also like to see various graphs and analytics applied so we can take these and add them to the profile made from the analytics into the neural net, for future comparisons. 


#### usage:

this program creates hardcoded directories , in which it stores the different processes of deduplication, changing from json to csv. So you might need to change the filepaths.actually you will have to..

you only have to enter the username of the user and the name of the file and type of file you want.


#### install:
- ```pip install -r requirements.txt```

nltk       <-------requires 'punkt' NLTK  libary 
(open interpreter ) 
To install the needed templates for dialectical analysis, from inside of a python shell, run these commands:

- ```import nltk```

- ```nltk.download('punkt')```

- ```quit()```


