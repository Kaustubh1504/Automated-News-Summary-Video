import newspaper
import json

url = 'https://www.thehealthsite.com/diseases-conditions/world-thyroid-day-2023-untreated-thyroid-problems-in-the-elderly-can-lead-to-cardiovascular-diseases-980614/'
  
article = newspaper.Article(url=url, language='en')
article.download()
article.parse()

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


print(article["title"] \
     + "\n\t\t" + article["published_date"] \
     + "\n\n"\
     + "\n" + article["text"]\
     + "\n\n")