# import basic modules

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import scipy.special as special
import time as time
import datetime as dt
import os


# import additional modules

from bs4 import BeautifulSoup
import requests

# import module I created for webscrapping

import html_operations


# get raw html using my module

main_url = 'https://www.degruyter.com/search?query=journalKey%3A%28COGL%29+AND+%28collocation%29&startItem=0&pageSize=10&sortBy=relevance&documentVisibility=all&pubDateFacet=last5years'

raw_html = html_operations.get_html(main_url=main_url)


# get links for each page

# scrape url for each

pages_links_list = html_operations.get_links_each_page(raw_html=raw_html)
articles_links_list = html_operations.get_links_to_articles_degruyter(pages_links_list=pages_links_list)


titles = html_operations.get_titles_degruyter(pages_links_list=pages_links_list)
abstracts = html_operations.get_abstract_degruyter(articles_links_list=articles_links_list)
keywords = html_operations. get_keywords_degruyter(articles_links_list=articles_links_list)

print(titles) # complete
print(abstracts)
print(keywords)
print('hello')



# data = {'Title': titles, 'Abstract': abstracts, 'Keywords': keywords}
# articles_df = pd.DataFrame(data)

# print(articles_df)