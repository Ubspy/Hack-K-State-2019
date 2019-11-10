import re
import nltk
from nltk.corpus import stopwords
import numpy as np
import random
import string 

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

replies = open('reddit.txt').read()

replies.lower()

replies.replace('\n', ' ')
replies = re.sub(r'\[[0-9]*\]', ' ', replies) 
replies = re.sub(r'\s+', ' ', replies)

sentenceList = nltk.sent_tokenize(replies)
replyWords = nltk.sent_tokenize(replies)

lemmantizer = nltk.stem.WordNetLemmatizer()

def lemmatizeWords(words):
    return [lemmantizer.lemmatize(word) for word in words]

removePunctuation= dict((ord(punctuation), None) for punctuation in string.punctuation)

def removePunctuations(text):
    return lemmatizeWords(nltk.word_tokenize(text.lower().translate(removePunctuation)))

def give_reply(userInput):
    chatbot_response=''
    sentenceList.append(userInput)

    stopWords = ""
    for stopWord in stopwords.words('english'):
        stopWords += stopWord + " "

    stopWords = removePunctuations(stopWords)

    wordVectors = TfidfVectorizer(tokenizer=removePunctuations, stop_words=stopWords, lowercase=True)    
    vecrorizedWords = wordVectors.fit_transform(sentenceList)

    similarityValues = cosine_similarity(vecrorizedWords[-1], vecrorizedWords)
    similarSentenceNumber =similarityValues.argsort()[0][-2]
    similarVectors = similarityValues.flatten()
    similarVectors.sort()
    matched_vector = similarVectors[-2]

    if(matched_vector == 0):
        chatbot_response=chatbot_response + "I am sorry! I don't understand you"
        return chatbot_response
    else:
        chatbot_response = chatbot_response + sentenceList[similarSentenceNumber]
        return chatbot_response

continue_discussion=True
print("Hello, thank you for reaching out. What's going on? Why are you contacting us today? ")
userInput = input()
userInput = userInput .lower()
print(give_reply(userInput))
sentenceList.remove(userInput)