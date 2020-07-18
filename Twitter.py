# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 12:37:37 2020

@author: Vimal PM
"""
#importing the libraries
import pandas as pd
import tweepy
#Applying my twitter consumer keys and secret keys
Consumer_key='kwBrATHHoCSOdkyiya8Y89fdl'
Consumer_secret='ru4zYgSfEtpj7WdlRw3SFRcEPICgGSSKjlCPlSqIVXUlfipmuu'
Access_key='813308482342490112-NUbSbpN0s0kinoCAA8WEBlUkdOI5D2s'
Access_secret='bOKmq9tnlUcnG7HS66WNoDnfd1qvBPHEXyzgYPpsowxSo'
#creating an empty list called "Alltweets"
alltweets = []	
def get_all_tweets(screen_name):
    auth = tweepy.OAuthHandler(Consumer_key,Consumer_secret)
    auth.set_access_token(Access_key,Access_secret)
    api = tweepy.API(auth)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    alltweets.extend(new_tweets)
    
    oldest = alltweets[-1].id - 1
    while len(new_tweets)>0:
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest) #save most recent tweets
        alltweets.extend(new_tweets) #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        print ("...%s tweets downloaded so far" % (len(alltweets)))
        
    outtweets = [[tweet.created_at,tweet.entities["hashtags"],tweet.entities["user_mentions"],tweet.favorite_count,
                  tweet.geo,tweet.id_str,tweet.lang,tweet.place,tweet.retweet_count,tweet.retweeted,tweet.source,tweet.text,
                  tweet._json["user"]["location"],tweet._json["user"]["name"],tweet._json["user"]["time_zone"],
                  tweet._json["user"]["utc_offset"]] for tweet in alltweets]
    
    
    tweets_df = pd.DataFrame(columns = ["time","hashtags","user_mentions","favorite_count",
                                    "geo","id_str","lang","place","retweet_count","retweeted","source",
                                    "text","location","name","time_zone","utc_offset"])
    tweets_df["time"]  = pd.Series([str(i[0]) for i in outtweets])
    tweets_df["hashtags"] = pd.Series([str(i[1]) for i in outtweets])
    tweets_df["user_mentions"] = pd.Series([str(i[2]) for i in outtweets])
    tweets_df["favorite_count"] = pd.Series([str(i[3]) for i in outtweets])
    tweets_df["geo"] = pd.Series([str(i[4]) for i in outtweets])
    tweets_df["id_str"] = pd.Series([str(i[5]) for i in outtweets])
    tweets_df["lang"] = pd.Series([str(i[6]) for i in outtweets])
    tweets_df["place"] = pd.Series([str(i[7]) for i in outtweets])
    tweets_df["retweet_count"] = pd.Series([str(i[8]) for i in outtweets])
    tweets_df["retweeted"] = pd.Series([str(i[9]) for i in outtweets])
    tweets_df["source"] = pd.Series([str(i[10]) for i in outtweets])
    tweets_df["text"] = pd.Series([str(i[11]) for i in outtweets])
    tweets_df["location"] = pd.Series([str(i[12]) for i in outtweets])
    tweets_df["name"] = pd.Series([str(i[13]) for i in outtweets])
    tweets_df["time_zone"] = pd.Series([str(i[14]) for i in outtweets])
    tweets_df["utc_offset"] = pd.Series([str(i[15]) for i in outtweets])
    tweets_df.to_csv(screen_name+"_tweets.csv")
    return tweets_df
#here am geting the information of actor "@TomCrusie"
tweet = get_all_tweets("TomCruise")
#Next i would like to data frame all texts got from tweets
Text=pd.DataFrame(tweet.text)
Text.head

<bound method NDFrame.head of                                                                                                                                                   text
0         I know many of you have waited 34 years. Unfortunately, it will be a little longer. Top Gun: Maverick will fly this… https://t.co/C7TjmMgGJM
1                                                                                                         Summer 2020. #TopGun https://t.co/4AABKxnEDv
2                                                              Warning: Real flying. Real g-forces. May make you puke. #TopGun https://t.co/CRjROgOvwd
3                                                                                                  See you in the sky. #TopGun https://t.co/vdhTtXb0io
4                                                                                     Feel the need. Trailer tomorrow. #TopGun https://t.co/rWHfKdkmGF
                                                                                                                                               ...
3020           "I feel the need, the need for speed" http://t.co/BeKwGsEw4j #F1 @redbullracing #Racing #LoopingHelicoptersWhat? http://t.co/X3EBi6LKFP
3021                                                         TU, we responded! -TeamC @casiopea1027 Hi dude ^^Cograts ~!!\nVK☞☞ send 4 massage 4 u^^;;
3022  http://t.co/4oBuw7x45h is a European social network w/100mil users &amp; we JUST launched a profile Увидимся там! -TeamTC http://t.co/QzETDkNNhe
3023  TU! You &amp; everyone here ARE TeamTC and YES, U ALL ROCK! @Rainnne It is getting closer to the release date of Oblivion!! \o/ #TeamCruiseRocks
3024   That is awesome! Thank you! -TeamTC @mmny_1314 @TomCruise -TeamTC Anime &amp; collaboration. \nI made again.:D #Oblivion http://t.co/ZqkD5pishv

[3025 rows x 1 columns]>

#Above shows the first and last five tweets of  Tom cruise
#creating a string object of all texts from tweets
Text=tweet["text"]
#next I want to join all texts into paragraph
Tweet_text_strings=" ".join(Text)
#removing the unwanted symbols from the texts
#for that importing the re
import re
Tweet_text_strings=re.sub("[^A-Za-z" "]+"," ",Tweet_text_strings).lower()
#spliting every words line by line
Tweet_text=Tweet_text_strings.split(" ")
#loading other libraries to perform sentimental analysis 
import nltk
from nltk.corpus import stopwords

import matplotlib.pyplot as plt
from wordcloud import WordCloud
##importing the stopwords from nltk
with open("D:\DATA SCIENCE\Data sets\\stopwords.txt","r") as sw:
    stopwords = sw.read()
    #splitting the stop words by line
stopwords=stopwords.split("\n")
#applying the stopwords to  all tweet texts and removing those stop words from there
Tweet_text_words=[v for v in Tweet_text if not v in stopwords]
#joining all texts in a paragraph
Tweet_text_strings=" ".join(Tweet_text_words)

#next am going to visualize the wordcloud plot to identify most frequent words from tweets
wordcloud_tweet=WordCloud(
        background_color="black",
        width=1900,
        height=1500
        ).generate(Tweet_text_strings)
plt.imshow(wordcloud_tweet)
#from the plot I can see "Tom cruise,Co,Cruise,Teamtc,Movie,oblivion" these are the most frequent words from the tweet texts they mentioned.....

#Next I would like to see the positve words from the tweets
#for that am going to load the postive words dataset
with open("D:\\DATA SCIENCE\\Data sets\\positive-words.txt","r")as pos:
    poswords=pos.read().split("\n")
#Appling the positive words to all tweet texts
Tweet_positive=" ".join([v for v  in Tweet_text_words if v in poswords])    
#here am going to plot the positve wordcloud    
wordcloud_positive=WordCloud(
        background_color="black",
        width=1900,
        height=1500
        ).generate(Tweet_positive)
plt.imshow(wordcloud_positive)
#From the plot I can see "Love,Awesome,good,great,amazing,fans,best" these are the most frequent positive words from the users tweets..... 

#Next I'm going to see the negative words from the tweets
#For that am opening the negative datasets
with open("D:\\DATA SCIENCE\\Data sets\\negative-words.txt","r")as neg:
    negwords=neg.read().split("\n")
#applying these negative words to tweets    
Tweet_negative=" ".join([v for v in Tweet_text_words if v in negwords])
#Next am going to see the negative wordcloud plot to identify most frequent negative words
wordcloud_negative=WordCloud(
        background_color="black",
        width=1900,
        height=1500
        ).generate(Tweet_negative)
plt.imshow(wordcloud_negative)
#from the plot I  can see "Impossible,risky,stunt,miss,kill,hard,blunt" these are the most frequent negative words from the tweet texts...
