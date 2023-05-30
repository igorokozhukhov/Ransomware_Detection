import pandas as pd
import numpy as np
import random
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle


def sanitization(web):
    # Приведение URL к нижнему регистру
    web = web.lower()
    token = []
    dot_token_slash = []
    raw_slash = str(web).split('/')
    for i in raw_slash:
        raw1 = str(i).split('-')
        slash_token = []
        for j in range(0, len(raw1)):
            raw2 = str(raw1[j]).split('.')
            slash_token = slash_token + raw2
        dot_token_slash = dot_token_slash + raw1 + slash_token
    token = list(set(dot_token_slash))
    if 'com' in token:
        token.remove('com')
    return token

urls = []
urls.append(input("Input the URL that you want to check (eg. google.com) : "))
# print(urls)

# Использование фильтра белого списка, поскольку модель часто дает ошибки в случае законных URL-адресов,
# поскольку наибольшая проблема заключается не в обнаружении вредоносных URL-адресов, а в их отделении от хороших
whitelist = ['hackthebox.eu', 'root-me.org', 'gmail.com']
s_url = [i for i in urls if i not in whitelist]

# Загрузка модели
file = "Classifier/pickel_model.pkl"
with open(file, 'rb') as f1:
    lgr = pickle.load(f1)
f1.close()
file = "Classifier/pickel_vector.pkl"
with open(file, 'rb') as f2:
    vectorizer = pickle.load(f2)
f2.close()

# Прогнозирование
x = vectorizer.transform(s_url)
y_predict = lgr.predict(x)

for site in whitelist:
    s_url.append(site)
# print(s_url)

predict = list(y_predict)
for j in range(0, len(whitelist)):
    predict.append('good')
print("\nThe entered domain is: ", predict[0])