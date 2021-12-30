from app import app
from app import tools
from flask import render_template

@app.route("/")
def home():
    print(tools.next_topic("nouns","classroom"))
    return render_template("index.html", extension = "typical", title = "Vocabulary", content1 = "<h4>You can't build up a vocabulary if you never meet any new words. And to meet them you must read. The more you read the better.</h4>")

@app.route("/<csv>", defaults={'topic' : 'vocabulary'})
@app.route("/<csv>/<topic>", methods=["GET", "POST"])
def theme(csv, topic):
    if topic != "vocabulary":
        return render_template("index.html", extension = "typical", title = f"{csv.capitalize()} > {topic.capitalize()}", content1 = tools.show_words(csv,topic), footer = f'/{csv}/{tools.next_topic(csv,topic)}')
    else:
        return render_template("index.html", extension = "typical", title = csv.capitalize(), content1 = tools.show_topic(csv))