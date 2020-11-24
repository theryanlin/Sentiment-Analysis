#!/usr/bin/env python
# coding: utf-8

# 解決 flask 端口:
# * sudo lsof -i:5000
# * sudo kill 769

# In[4]:


from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators

app = Flask(__name__)

class HelloForm(Form):
    sayhello = TextAreaField('', [validators.DataRequired()])

@app.route("/")     
def index():
    form = HelloForm(request.form)
    return render_template('first_app.html', form=form)

@app.route("/hello", methods = ['POST']) 
def hello():       
    form = HelloForm(request.form)
    if request.method == 'POST' and form.validate():
        name = request.form['sayhello']
        return render_template('hello.html', name=name)
    return render_template('first_app.html', form=form)

if __name__ == "__main__":        
    app.run(debug = True)  


# In[ ]:




