#1.kütüphaneler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#2.veri onisleme
#2.1verionyukleme
veriler = pd.read_csv('eksikveriler.csv')

print(veriler)
#veri on isleme
boy = veriler[['boy']]
print(boy)
boykilo = veriler[['boy','kilo']]
print(boykilo)
x=10

#eksik veriler
#sci-kit learn
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy= 'mean')
#iloc veri kümesinden veri almak için kullanılır
yas = veriler.iloc[:,1:4].values
print(yas)
imputer = imputer.fit(yas[:,1:4])
yas[:,1:4]= imputer.transform(yas[:,1:4])
print(yas)

#encoder: Kategorik-> numeric
ulke = veriler.iloc[:,0:1].values
print(ulke)
from sklearn import preprocessing

le = preprocessing.LabelEncoder()

ulke[:,0] = le.fit_transform((veriler.iloc[:,0]))

print(ulke)


ohe = preprocessing.OneHotEncoder()
ulke = ohe.fit_transform(ulke).toarray()
print(ulke)
#numpy dizilerinin data frame dönüşümü
#sonucu tek bir dataframede toplayacağız
sonuc = pd.DataFrame(data=ulke, index = range(22), columns = ['fr','tr','us'])
print(sonuc)

sonuc2 = pd.DataFrame(data = yas, index = range(22), columns = ['boy','kilo','yas'])
print(sonuc2)

cinsiyet = veriler.iloc[:,-1].values
print(cinsiyet)
sonuc3 = pd.DataFrame(data = cinsiyet, index = range(22), columns=['cinsiyet'])
print(sonuc3)

#data frame birleştimek için
s = pd.concat([sonuc, sonuc2], axis=1) #axis sona kolon olarak eklemesini istiyoruz
print(s)

s2=pd.concat([s,sonuc3], axis=1)
print(s2)


#eğitim ve test kümeleri oluşturmak
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(s,sonuc3,test_size=0.33,random_state=0)



#verilerin ölçeklenmesi
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

X_train =sc.fit_transform(x_train)
X_test =sc.fit_transform(x_test)




















