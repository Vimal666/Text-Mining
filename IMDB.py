# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 23:17:26 2020

@author: Vimal PM
"""

#importing neccesary libraries
import requests
from bs4 import BeautifulSoup as bs
import re
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from wordcloud import WordCloud
#creating empty reviews list
#Here am taking the reviews of movie "Interstellar"
movie_review_interstellar=[]
for i in range(1,50):
    movie=[]
    url="https://www.imdb.com/title/tt0816692/reviews?ref_=tt_urv"+str(i)
    response=requests.get(url)
    soup=bs(response.content,"html.parser")#creating soup object to iterative over the extracted content
    reviews=soup.find_all("div",attrs={"class","text show-more__control"})
    #extracting the contents
    for i in range(len(reviews)):
        movie.append(reviews[i].text)
        movie_reviews=movie_review_interstellar+movie
        
#Next am joining all reviws in a paragraph         
Movie_review_string=" ".join(movie_reviews)
#removing the unwanted symbols from reviews
Movie_review_string=re.sub("[^A-Za-z" "]+"," ",Movie_review_string).lower()
#spliting every words line by line
movie_reviews=Movie_review_string.split(" ")
#Loading the stopwords
with open("D:\\DATA SCIENCE\\Data sets\\positive-words.txt","r")as sw:
    stopwords=sw.read().split("\n")
#appling the stop words to  reviews and removing those stopwords from there    
Movie_review_words=[v for v in movie_reviews if not v in stopwords]
#joining all reviews in a paragraph
Movie_review_string=" ".join(movie_reviews)
#going to see the most frequent words from the reviews
#for that I would like to visualize the wordcloud plot
wordcloud_movie=WordCloud(
        background_color="black",
        width=1900,
        height=1500
        ).generate(Movie_review_string)
plt.imshow(wordcloud_movie)
#from the plot I can see "Movie,Interstellar,Film,Nolan,story,time,see,visual,best" these are the most freuquent words from the reviews
#next am going to perform the sentimental analysis on the reviews 
#first I would like to identify the negative words
with open("D:\\DATA SCIENCE\\Data sets\\negative-words.txt","r")as neg:
    negwords=neg.read().split("\n")
#for that am visualizing the wordcloud plot again.
Movie_negative=" ".join([v for v in Movie_review_words if v in negwords])
#visualizing the negative wordcloud
wordcloud_negative=WordCloud(
        background_color="black",
        width=1900,
        height=1500
        ).generate(Movie_negative)
plt.imshow(wordcloud_negative)
#from the plot I can see "dark,plot,hard,unknown,doubt,critic,lost" these are the most frequent negative words from the review
