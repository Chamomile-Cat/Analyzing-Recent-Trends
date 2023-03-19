# import additional modules

from bs4 import BeautifulSoup
import requests


# import selenium

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# get html as BS object using Selenium

def get_html(main_url):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    browser = webdriver.Chrome(options=options)

    browser.get(main_url)
    raw_html = browser.page_source

    raw_html = BeautifulSoup(raw_html, 'html.parser')
    
    browser.close()

    return raw_html


# get html using BS

def get_html2(main_url):
    result = requests.get(main_url)
    raw_html = BeautifulSoup(result.text, 'html.parser')
    
    return raw_html


# get links to each page

def get_links_each_page(raw_html):
    list_html_containing_links = raw_html.find_all(name='a', class_='rounded-0 page-link')
    list_html_containing_links = list_html_containing_links[:-1]

    pages_links_list=[]
    for i in list_html_containing_links:
        link = 'https://www.degruyter.com' + i.get('href')
        pages_links_list.append(link)
    return pages_links_list


# get links  to each article

def get_links_to_articles_degruyter(pages_links_list):

    articles_links_list=[]

    for link in pages_links_list:
        pages_raw_html = get_html(link)
        list_html_to_articles = pages_raw_html.find_all(name='a', class_='linkHoverDark')    
        for i in list_html_to_articles:
            link = 'https://www.degruyter.com' + i.get('href')
            articles_links_list.append(link)

    return articles_links_list


# get titles from Degruyter

def get_titles_degruyter(pages_links_list):
    each_titles_strings = []

    for i in pages_links_list:
        html_each_article = get_html(i)
        list_html_containing_titles = html_each_article.find_all(class_='titleSearchPageResult mb-0')
        for i in list_html_containing_titles:
            if i.string != None:
                each_titles_strings.append(i.string.replace('\n','').strip())
            if i.string == None:
                each_titles_strings.append(i.text.replace('\n','').strip())            

    return each_titles_strings


# get abstract from Degruyter

def get_abstract_degruyter(articles_links_list):
    abstract_list = []
    
    for i in articles_links_list:
        html_each_article = get_html(i)
        html_abstract = html_each_article.find(name='div', class_='abstract')
        abstract_text = html_abstract.find(name='p').text
        abstract_list.append(abstract_text)
        return abstract_list


# get keywords from Degruyter

def get_keywords_degruyter(articles_links_list):
    total_keyword_list = [] # keyword list of all articles with each article's keywords in a list of their own

    for i in articles_links_list:
        html_each_article = get_html(i)
        keyword_html_list = html_each_article.find_all(name='a', class_='ga_keyword') # keyword_list is a list of keywords for each individual article
        keyword_list = [i.text for i in keyword_html_list] 
        total_keyword_list.append(keyword_list) 
        return total_keyword_list
