## ArticlesOfEase

ArticlesOfEase is a simple python script that primarily takes another great python project, Newspaper, and makes it useful with RSS feeds that only provide URL's to articles and not the actual content.  The result will be all of the articles in the feed displayed in a simple JSON format.

## Example

Running the script is simple, just run the script while passing in the URL to the feed you'd like to collect:

```
python3 articlesofease.py example.com/rss
```

## Motivation

My main motivation was that there was a site I wanted to collect the articles from for offline reading and wanted to also break into some python.  After some research, I found Newspaper, but then realized that the site I wanted to scrape only provided the URL's to their articles and not the content itself.  So, I did some hacking, some more digging, and explored a few more dependencies until I finally got it.  Overall, I got what I was looking for and got to play with python along the way!

## Installation

* You will, of course, need python (I developed in python3 specificaly).
* [Newspaper](https://github.com/codelucas/newspaper) by codelucas
* beautifulsoup4 which you can install using `pip3 install beautifulsoup4`