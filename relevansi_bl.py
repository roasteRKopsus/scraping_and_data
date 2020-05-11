import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import numpy as np
pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 5000)
pd.set_option('display.width', 100000)
pd.set_option('display.precision', 0)
pd.option_context('display.colheader_justify','left')

site = "https://www.bukalapak.com/products?utf8=%E2%9C%93&source=navbar&from=omnisearch&search_source=omnisearch_organic&from_keyword_history=false&search%5Bkeywords%5D=kopi+arabika"
hdr = {'user-agent' : 'GoogleChrome'}

req = Request(site, headers=hdr)
page = urlopen(req)
page_soup = BeautifulSoup(page, 'html.parser')
#print(page_soup.find_all('a'))

product_raw = page_soup.find(class_ = 'basic-products basic-products--grid' )
product_row = product_raw.find_all(class_ = 'col-12--2')

productname = [productname.find(class_='product__name line-clamp--2 js-tracker-product-link qa-list').get_text() for productname in product_row]
productprice_relevansi = [productprice.find(class_='amount positive').get_text() for productprice in product_row]
#productprice2 = [float(productprice2) for productprice2 in productprice ]
productrating = [productrating.find(class_='product__rating').get_text() for productrating in product_row]
#print(productrating)
#print(productrating)

#print(product_row)
productname2 = [x.replace("\n, ' '" , '') for x in productname]
productrating2 = [x.replace('\n', '') for x in productrating]
