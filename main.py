# from transformers import *
# import torch
# from transformers import AutoTokenizer, AutoModelWithLMHead
import requests
from bs4 import BeautifulSoup
import newspaper
import json
import pytz
import image


#fetching news data from api
url = ('https://newsapi.org/v2/top-headlines?'
       'country=in&'
       'apiKey=57aea496d9a3441dbaef71384e28c804')
response = requests.get(url)
# print (response.json())

data=response.json()
articles = data['articles']
# Extract URLs for each article
urls = [article['url'] for article in articles]

articles_summary=[]
# Print the extracted URLs
timezone = pytz.timezone('Asia/Kolkata')


#setup summarizer
# tokenizer = AutoTokenizer.from_pretrained('t5-base')
# model = AutoModelWithLMHead.from_pretrained('t5-base', return_dict=False)



for url in urls:
    # print(url)
    article = newspaper.Article(url=url, language='en')
    article.download()
    article.parse()
    # print(article.title)
    # inputs = tokenizer.encode("summarize: " + article.text, return_tensors='pt',max_length=10000,truncation=True)
    # summary_ids = model.generate(inputs, max_length=150, min_length=80, length_penalty=5., num_beams=2)
    # summary = tokenizer.decode(summary_ids[0])

    article ={
    "title": str(article.title),
    "text": str(article.text),
    "authors": article.authors,
    "published_date": str(article.publish_date),
    "top_image": str(article.top_image),
    "videos": article.movies,
    "keywords": article.keywords,
    "summary": str(article.summary)
    }
    articles_summary.append(article)

print(len(articles_summary))


#take only one article for demostration
# for article in articles_summary:
#     image.process_articles(article["summary"])

article={
    "summary":"the social media giant is carrying out its last batch of a three-part round of layoffs. the company's shares closed marginally up in a broadly weaker market. the cuts are likely to impact around 490 employees at its international headquarters in Dublin. the social media giant is the first big tech company to announce a second round of mass layoffs."
}
image.process_articles(article["summary"])