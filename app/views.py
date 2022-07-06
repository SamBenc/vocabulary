from app import app
from app import tools
from flask import render_template

@app.route("/")
def home():
    return render_template("index.html", extension = "typical", title = "Vocabulary", content1 = tools.show_home())

@app.route("/<csv>")
def csv(csv):
    return render_template("index.html", extension = "typical", title = csv.capitalize(), content1 = tools.show_topic(csv))

@app.route("/<csv>/<topic>", methods=["GET", "POST"])
def theme(csv, topic):
    return render_template("index.html", extension = "typical", title = f"{csv.capitalize()} > {topic.capitalize()}", content1 = tools.show_words(csv,topic), footer = f'/{csv}/{tools.next_topic(csv,topic)}')