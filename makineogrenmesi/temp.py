# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#kütüphanelerimiz
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

veriler = pd.read_csv('veriler.csv')
print(veriler)
boy = veriler[['boy']]
print(boy)
boykilo = veriler[['boy','kilo']]
print(boykilo)
x=10

# class oluşturarak nesne oluşturmak 
class insan:
    boy =  180
    def kosmak(self,b):
        return b + 10
ali = insan()
print(ali.boy)
print(ali.kosmak(90))

liste = [1,3,5]

