import feedparser
from newspaper import Article
import nltk
import time
from bs4 import BeautifulSoup
from xml.etree  import ElementTree
import json
import pprint
import sys

feed = feedparser.parse(str(sys.argv[1]))
print(feed.feed.title)
print(repr(len(feed.entries)) + " articles compiled on " + time.strftime("%m/%d/%Y %H:%M:%S") + "\n\n")

for entry in feed.entries:
	article = Article(entry.link)
	article.download()
	article.parse()

	try:
	  html_string = ElementTree.tostring(article.clean_top_node)
	except:
	  html_string = "Error converting html to string."

	soup = BeautifulSoup(html_string, 'html.parser')
	a = {
         'authors': str(', '.join(article.authors)), 
         'title': article.title,
         'text': soup.get_text(),
         'top_image': article.top_image
         }

	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(a)