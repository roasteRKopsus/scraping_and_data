import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import numpy as np
import matplotlib.pyplot as plt

from terlaris_bl import productprice_terlaris
from terbaru_bl import  productprice_terbaru
from relevansi_bl import productprice_relevansi
from terlaris_bl import value_count
harga_df = pd.DataFrame({
    'terlaris' : productprice_terlaris,
    'terbaru' : productprice_terbaru,
    'relevansi' : productprice_relevansi
})

count1= harga_df['terlaris'].value_counts()
count2= harga_df['terbaru'].value_counts()
count3= harga_df['relevansi'].value_counts()
harga_count = pd.DataFrame({
    'terlaris' : count1,
    'terbaru' :count2,
    'relevansi' :count3
})
harga_count['total'] = harga_count.sum(axis=1)

print(harga_df)
print(harga_df.describe())
print('x'*100)
count1= harga_df['terlaris'].value_counts()
count2= harga_df['terbaru'].value_counts()
count3= harga_df['relevansi'].value_counts()
print(harga_count.fillna(0))
print(harga_df.describe())
harga_count.plot()