#kütüphanelerimiz
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

eksik = pd.read_csv('eksikveriler.csv')

print(eksik)

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy= 'mean')
yas = eksik.iloc[:,1:4].values
print(yas)
imputer = imputer.fit(yas[:,1:4])
yas[:,1:4]= imputer.transform(yas[:,1:4])
print(yas)