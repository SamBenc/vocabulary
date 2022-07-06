from app import app
from app import tools
from flask import render_template

@app.route("/")
def home():
    try:
        return render_template("index.html", extension = "typical", title = "Vocabulary", content1 = tools.show_home())
    except Exception as e:
        return render_template("index.html", extension = "typical", title = "Error", content1 = e)

@app.route("/<csv>")
def csv(csv):
    try:
        return render_template("index.html", extension = "typical", title = csv.capitalize(), content1 = tools.show_topic(csv))
    except Exception as e:
        return render_template("index.html", extension = "typical", title = "Error", content1 = e)

@app.route("/<csv>/<topic>", methods=["GET", "POST"])
def theme(csv, topic):
    try:
        return render_template("index.html", extension = "typical", title = f"{csv.capitalize()} > {topic.capitalize()}", content1 = tools.show_words(csv,topic), footer = f'/{csv}/{tools.next_topic(csv,topic)}')
    except Exception as e:
        return render_template("index.html", extension = "typical", title = "Error", content1 = e)