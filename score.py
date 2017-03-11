from flask import Flask
import urllib2
import re
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser


app = Flask(__name__)


page = urllib2.urlopen("http://www.espn.com/nhl/team/_/name/stl/st-louis-blues")
soup = BeautifulSoup(page.read(), "lxml")
soup= soup.find_all("div", class_="results")
score = str(soup[0])
outcome = "Win!"
if "W" not in score:
    outcome = "Loss!"


@app.route('/')
def hello_world():
    return outcome
    