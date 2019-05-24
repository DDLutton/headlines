#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 20:28:56 2019

@author: l
"""

import feedparser
from flask import Flask


app = Flask(__name__)
RSS_FEEDS = {'anxiety':'https://www.psychiatryadvisor.com/home/topics/anxiety/feed',
             'mood':'https://www.psychiatryadvisor.com/home/topics/mood-disorders/feed',
                 'depression':'https://www.nature.com/subjects/depression.rss',
                 'dwarves':'http://www.bay12games.com/dwarves/dev_now.rss',
                 'obitOne':'https://www.nytimes.com/services/xml/rss/nyt/Obituaries.xml',
                 'obitTwo':'https://www.bucktroutfuneralhome.net/obituary/feed/',
                 'leprosy':'http://www.wpro.who.int/feeds/entity/laos/en/rss.xml',
                 'death':'http://rawdataserver.com/CDB/rss'
                 }

@app.route("/")
@app.route("/anxiety")
def anxiety():
    return get_news('anxiety')
@app.route("/mood")
def mood():
    return get_news('mood')
@app.route("/depression")
def depression():
    return get_news('depression')
@app.route("/dwarves")
def dwarves():
    return get_news('dwarves')
@app.route("/obitOne")
def obitOne():
    return get_news('obitOne')
@app.route("/obitTwo")
def obitTwo():
    return get_news('obitTwo')
@app.route("/leprosy")
def leprosy():
    return get_news('leprosy')
@app.route("/death")
def death():
    return get_news('death')

def get_news(publication):
    feed = feedparser.parse(RSS_FEEDS[publication])
    first_article = feed['entries'][0]
    return """<html>
    <body>
        <h1>Headlines </h1>
        <b>{0}</b> <br/>
        <i>{1}</i> <br/>
        <p>{2}</p> <br/>
    </body>
</html>""".format(first_article.get("title"),
 first_article.get("published"),
 first_article.get("summary"))

if __name__ == '__main__':
  app.run(port=5000, debug=True)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  