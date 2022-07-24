from app import app
from app import tools
from flask import render_template
from bs4 import BeautifulSoup
import requests

@app.route("/")
def home():
    try:
        return render_template("index.html", extension = "typical", title = "Vocabulary", content1 = tools.show_home())
    except Exception as e:
        return render_template("index.html", extension = "typical", title = "Maintenance Required", content1 = e)

@app.route("/<csv>")
def csv(csv):
    try:
        return render_template("index.html", extension = "typical", title = csv.capitalize(), content1 = tools.show_topic(csv))
    except Exception as e:
        return render_template("index.html", extension = "typical", title = "Maintenance Required", content1 = e)

@app.route("/<csv>/<topic>", methods=["GET", "POST"])
def theme(csv, topic):
    try:
        return render_template("index.html", extension = "typical", title = f"{csv.capitalize()} > {topic.capitalize()}", content1 = tools.show_words(csv,topic), footer = f'/{csv}/{tools.next_topic(csv,topic)}')
    except Exception as e:
        return render_template("index.html", extension = "typical", title = "Maintenance Required", content1 = e)

@app.route("/get/<word>", methods=["GET", "POST"])
def getdef(word):
    try:
        url = "https://www.wordhippo.com/what-is/the-noun-for/"+str(word)+".html"
        doc = requests.get(url)
        html = BeautifulSoup(doc.text, "html.parser")
        wordtype = html.find_all("div", {"class":"defv2wordtype"})
        relatedwords = html.find_all("div", {"class":"defv2relatedwords"})
        result= ""
        for i in range(0,len(wordtype)):
            result += str(wordtype[i])
            result += str(relatedwords[i])
        return result
    except Exception as e:
        return e