from flask import Flask
import urllib2
import os
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser


app = Flask(__name__)


page = urllib2.urlopen("http://www.espn.com/nhl/team/_/name/stl/st-louis-blues")
soup = BeautifulSoup(page.read(), "lxml")
soup= soup.find_all("div", class_="results")
score = str(soup[0])
outcome = "W"
if "W" not in score:
    outcome = "L"


@app.route('/')
def hello_world():
    return outcome

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    