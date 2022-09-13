from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
df=pd.read_csv("Q_A_Lexicon.csv")
questions=df['Question'].values.tolist()
labels=df['S.No'].values.tolist()
answers=df['Answers'].values.tolist()
nb = GaussianNB()
d=df[['Question','Answers']].values.tolist()
class ChatBot:
  exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later", "stop")
  w=("hi","hello","whatsup")
  def start_chat(self):
    i=True
    while True:
        user_response = input("Hi, I'm a chatbot,How can i help you?\n")
        if user_response not in self.w:
            for i in range(len(d)):
                if user_response in d[i][0]:
                    print(d[i][1])
                    break
        if user_response in self.exit_commands:
            print("Ok, have a great day!")
            break
    
        if user_response  in self.w and user_response not in questions:
            print("Sorry, I didnot understand,Please try agian:")
            i=True
        
    
    
    
  def generate_response(self, sentence):
    input_vector = nb.transform([sentence])
    predict = classifier.predict(input_vector)
    #print(predict)
    index = int(predict[0])
    return answers[index-1]
etcetera = ChatBot()
etcetera.start_chat()
