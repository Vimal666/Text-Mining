# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 12:55:08 2020

@author: Vimal PM
"""
#Importing neccesary libraries
import requests  
from bs4 import BeautifulSoup as bs # Beautifulsoup is for web scrapping...used to scrap specific content 
import re # regular expressions 

import nltk
from nltk.corpus import stopwords

import matplotlib.pyplot as plt
from wordcloud import WordCloud

# creating empty reviews list 
protein_reviews =[]

for i in range(1,20):
  protein=[]  
  #url = "https://www.amazon.in/Optimum-Nutrition-Standard-Protein-Powder/product-reviews/B002DYIZH6/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"+str(i)
  url = "https://www.amazon.in/Optimum-Nutrition-Standard-Protein-Powder/product-reviews/B002DYIZH6/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"+str(i)
  response = requests.get(url)
  soup = bs(response.content,"html.parser")# creating soup object to iterate over the extracted content 
  reviews = soup.findAll("span",attrs={"class","a-size-base review-text review-text-content"})
  # Extracting the content under specific tags  
  for i in range(len(reviews)):
    protein.append(reviews[i].text)  
  protein_reviews=protein_reviews+protein
  
  #Next I would like to join all reviews into paragraph
protein_reviews_string=" ".join(protein_reviews)

#Next I'm going to remove unwanted symbols from the reviews
protein_reviews_string=re.sub("[^A-Za-z" "]+"," ",protein_reviews_string).lower()
#spliting every words line by line from the reviews
protein_reviews=protein_reviews_string.split(" ")

#importing the stopwords from nltk
with open("D:\DATA SCIENCE\Data sets\\stopwords.txt","r") as sw:
    stopwords = sw.read()
#splitting the stop words by line
stopwords=stopwords.split("\n")

#applying this stopwords to the protein reviews and removing those stopwords from there
protein_reviews_words=[v for v in protein_reviews if not v in stopwords]

#joinig all reviews in a paragraph
protein_reviews_string=" ".join(protein_reviews_words)

#next I would like to visualize the worldcloud plot to see the most frequent words from the reviews

wordcloud_protein=WordCloud(
                      background_color="black",
                      width=1900,
                      height=1500
                      ).generate(protein_reviews_string)
plt.imshow(wordcloud_protein)

#from the wordcloud plot I can see "product,Protein,Powder,Whey,,Really,Taste" these are the most frequent words from the customer reviewes about whey prtein powder

#Next I'm going to see the postive words from the reviews to perform sentimental analysis
#for that am going to import these positive words
with open("D:\\DATA SCIENCE\\Data sets\\positive-words.txt","r")as pos:
    poswords=pos.read().split("\n")
#Next I want to see the most frequent positive words about this protein powder    
#for that am going to visualize the wordcloud plot again...
protein_positive=" ".join([v for v in protein_reviews_words if v in poswords])    

wordcloud_positive=WordCloud(
                       background_color="black",
                       width=1900,
                       height=1500
                       ).generate(protein_positive)
plt.imshow(wordcloud_positive)
#From the plot I can see "Rich,Genuine,bright,good,golden,gold,amazing" these are the most frequent positive words from this protein powder reviews
#Next I'm going to identify the negative words from the reviews
#imporing the negative words
with open("D:\\DATA SCIENCE\\Data sets\\negative-words.txt","r")as neg:
    negwords=neg.read().split("\n")
#for that am visualizing the wordcloud plot again.
protein_negative=" ".join([v for v in protein_reviews_words if v in negwords])

wordcloud_negative=WordCloud(
                      background_color="black",
                      width=1900,
                      height=1500
                      ).generate(protein_negative)
plt.imshow(wordcloud_negative)
#From the plot I can see "Isolate,Fake,Scratch,Loose,Error,Shocked,Wrong" these are the most frequent negative words from the reviews about protein powder
