from app import app
from app import tools
from flask import render_template

@app.route("/")
def home():
    return render_template("index.html", extension = "typical", title = "Vocabulary", content1 = tools.show_home())

@app.route("/<csv>", defaults={'topic' : 'vocabulary'})
@app.route("/<csv>/<topic>", methods=["GET", "POST"])
def theme(csv, topic):
    if topic != "vocabulary":
        return render_template("index.html", extension = "typical", title = f"{csv.capitalize()} > {topic.capitalize()}", content1 = tools.show_words(csv,topic), footer = f'/{csv}/{tools.next_topic(csv,topic)}')
    else:
        return render_template("index.html", extension = "typical", title = csv.capitalize(), content1 = tools.show_topic(csv))