#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
import joblib


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():

    #Alternative Usage of Saved Model
    joblib.dump(clf, 'NB_spam_model.pkl')
    movie_review_model = open(r'Desktop/Sentiment Analysis/movie_review/movie_review_model.pkl','rb')
    lr_tfidf = joblib.load(movie_review_model) # reuse this model

    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        my_prediction = lr_tfidf.predict(data)
    return render_template('result.html', prediction = my_prediction)

if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




