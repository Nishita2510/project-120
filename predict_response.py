#Text Data Preprocessing Lib
import nltk
nltk.download('punkt')
nltk.download('wordnet')

# words to be igonred/omitted while framing the dataset
ignore_words = ['?', '!',',','.', "'s", "'m"]

import json
import pickle

import numpy as np
import random

# Model Load Lib
import tensorflow
from data_preprocessing import get_stem_words

from sklearn.feature_extraction.text import CountVectorizer

# load the model
model = tensorflow.keras.models.load_model('./chatbot_model.h5')

# Load data files
intents = json.loads(open('./intents.json').read())
words = pickle.load(open('./words.pkl','rb'))
classes = pickle.load(open('./classes.pkl','rb'))


def preprocess_user_input(user_input):

    bag=[]
    bag_of_words = []

    # tokenize the user_input
    user_input = input('type your message here: ')

    response = bot_response(user_input)
    print('Bot Response', response)

    # convert the user input into its root words : stemming
    stemmed_words = [ps.stem(word) for word in words]

    stemmed_sentence = " ".join(stemmed_words)
    print("Stemmed sentence:", stemmed_sentence)

    # Remove duplicacy and sort the user_input
    items = user_input.split()

    # Remove duplicates and sort
    unique_sorted_items = sorted(set(items))

    # Print the result
    print("Unique and sorted items:", unique_sorted_items)
   
    # Input data encoding : Create BOW for user_input
    vectorizer = CountVectorizer()

    # Fit and transform the input
    bow = vectorizer.fit_transform([user_input])

    # Print the Bag-of-Words representation
    print(bow.toarray())
    
    return np.array(bag)
    
def bot_class_prediction(user_input):
    inp = preprocess_user_input(user_input)
  
    prediction = model.predict(inp)
   
    predicted_class_label = np.argmax(prediction[0])
    
    return predicted_class_label


def bot_response(user_input):

   predicted_class_label =  bot_class_prediction(user_input)
 
   # extract the class from the predicted_class_label
   predicted_class = ""

   # now we have the predicted tag, select a random response

   for intent in intents['intents']:
    if intent['tag']==predicted_class:
       
       # choose a random bot response
        bot_response = ""
    
        return bot_response
    

print("Hi I am Stella, How Can I help you?")

while True:

    # take input from the user
    user_input = input('Type you message here : ')

    response = bot_response(user_input)
    print("Bot Response: ", response)