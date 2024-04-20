import numpy as np 
import pandas as pd 
#pandas ---> xử lý dữ liệu 
# import os
# for dirname, _, filenames in os.walk('/kaggle/input'):
#     for filename in filenames:
#         print(os.path.join(dirname, filename))


import json
with open('./datachat.json', 'r') as f:
    data = json.load(f)
df = pd.DataFrame(data['intents'])

dic = {"tag":[], "patterns":[], "responses":[]}
for i in range(len(df)):
    ptrns = df[df.index == i]['patterns'].values[0]
    rspns = df[df.index == i]['responses'].values[0]
    tag = df[df.index == i]['tag'].values[0]

    for j in range(len(ptrns)):
        dic['tag'].append(tag)
        dic['patterns'].append(ptrns[j])
        dic['responses'].append(rspns)
        
df = pd.DataFrame.from_dict(dic)
# data frame đã hoàn chỉnh ---> chỉnh bị tiến hành train

# 


from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import classification_report



# Chia dữ liệu train và test
X = df['patterns']
y = df['tag']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Mã hóa dữ liệu 
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# SVC là một mô hình train ai
model = SVC()
model.fit(X_train_vec, y_train)

y_pred = model.predict(X_test_vec)


def predict_intent(user_input):

    #Mã hóa dữ liệu user_input 
    user_input_vec = vectorizer.transform([user_input])
    intent = model.predict(user_input_vec)[0]
    response = df.loc[df['tag'] == intent, 'responses'].values[0][0]
    
    return response

