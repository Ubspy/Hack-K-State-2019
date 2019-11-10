import re
import nltk
from nltk.corpus import stopwords
import numpy as np
import random
import string 

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class NLPResponse:
    def __init__(self):
        replies = open('reddit.txt').read()

        replies.lower()

        replies.replace('\n', ' ')
        replies = re.sub(r'\[[0-9]*\]', ' ', replies) 
        replies = re.sub(r'\s+', ' ', replies)

        self.sentenceList = nltk.sent_tokenize(replies)
        replyWords = nltk.sent_tokenize(replies)

        self.lemmantizer = nltk.stem.WordNetLemmatizer()

        self.removePunctuation= dict((ord(punctuation), None) for punctuation in string.punctuation)


    def lemmatizeWords(self, words):
        return [self.lemmantizer.lemmatize(word) for word in words]

    def removePunctuations(self, text):
        return self.lemmatizeWords(nltk.word_tokenize(text.lower().translate(self.removePunctuation)))

    def give_reply(self, userInput):
        chatbot_response=''
        self.sentenceList.append(userInput)

        stopWords = ""
        for stopWord in stopwords.words('english'):
            stopWords += stopWord + " "

        stopWords = self.removePunctuations(stopWords)

        wordVectors = TfidfVectorizer(tokenizer=self.removePunctuations, stop_words=stopWords, lowercase=True)    
        vecrorizedWords = wordVectors.fit_transform(self.sentenceList)

        similarityValues = cosine_similarity(vecrorizedWords[-1], vecrorizedWords)
        similarSentenceNumber =similarityValues.argsort()[0][-2]
        similarVectors = similarityValues.flatten()
        similarVectors.sort()
        matched_vector = similarVectors[-2]

        if(matched_vector == 0):
            chatbot_response = chatbot_response + "I'm really sorry to hear that, that's terrible, you shouldn't have to suffer through that."
            return chatbot_response
        else:
            chatbot_response = chatbot_response + self.sentenceList[similarSentenceNumber]
            return chatbot_response
