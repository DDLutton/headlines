#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 20:28:56 2019

@author: l
"""

import feedparser
from flask import Flask
from flask import render_template

app = Flask(__name__)
RSS_FEEDS = {'anxiety':'https://www.psychiatryadvisor.com/home/topics/anxiety/feed',
             'mood':'https://www.psychiatryadvisor.com/home/topics/mood-disorders/feed',
                 'depression':'https://www.nature.com/subjects/depression.rss',
                 'dwarves':'http://www.bay12games.com/dwarves/dev_now.rss',
                 'obitOne':'https://www.nytimes.com/services/xml/rss/nyt/Obituaries.xml',
                 'emergencies':'https://afro.who.int/rss/emergencies.xml',
                 'death':'http://rawdataserver.com/CDB/rss'
                 }



@app.route("/")
@app.route("</publication>")
def get_news(publication="anxiety"):
    feed = feedparser.parse(RSS_FEEDS[publication])
    first_article = feed['entries'][0]
    return render_template("home.html")

if __name__ == '__main__':
  app.run(port=5000, debug=True)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  