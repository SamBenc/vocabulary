from app import app
from app import tools
from flask import render_template

@app.route("/")
def home():
    flowers = [    ('Flowers', 'Fleurs', 'الزهور'),    ('Roses', 'Roses', 'الورد'),    ('Violets', 'Violettes', 'البنفسج'),    ('Poppies', 'Coquelicots', 'الأقحوان'),    ('Lavenders', 'Lavandes', 'الخزامى'),    ('Candlesticks', 'Oenothères', 'الشمعدان'),    ('Jasmines', 'Jasmins', 'الفل'),    ('Lilies', 'Lys', 'الزنبق'),    ('Marigolds', 'Soucis', 'العبادة'),    ('Carnations', 'Œillets', 'القرنفل'),    ('Narcissus', 'Narcisses', 'النرجس'),    ('Amber', 'Ambre', 'العنبر'),    ('Camellias', 'Camélias', 'الكاميليا'),    ('Purple', 'Violet', 'الأرجواني'),    ('Desert rose', 'Rose du désert', 'الوردة'),    ('Jasmine', 'Jasmin', 'الياسمين'),    ('Daisies', 'Marguerites', 'الحماسة'),    ('Susans', 'Lilas', 'السوسن'),    ('Spring flowers', 'Fleurs de printemps', 'الربيع'),    ('Red poppies', 'Coquelicots rouges', 'الشقائق')]
    birds = [("Bald Eagle", "Pygargue à tête blanche", "نسر أمريكي"),           ("Robin", "Merle", "بلدق الأرض"),           ("Blue Jay", "Geai bleu", "غراب الزرقاء"),           ("Sparrow", "Moineau", "عصفور"),           ("Cardinal", "Cardinal", "الهدهد الأحمر"),           ("Hawk", "Faucon", "صقر"),           ("Pelican", "Pélican", "البجع"),           ("Penguin", "Manchot", "بطريق"),           ("Flamingo", "Flamant", "فلامنغو"),           ("Seagull", "Mouette", "نورس"),           ("Woodpecker", "Pic", "ببغاء"),           ("Owl", "Hibou", "بومة"),           ("Duck", "Canard", "بطة"),           ("Swan", "Cygne", "البجعة"),           ("Parrot", "Perroquet", "ببغاء"),           ("Canary", "Canari", "كناري"),           ("Hummingbird", "Colibri", "عصفور الزهور"),           ("Pigeon", "Pigeon", "حمام"),           ("Kiwi", "Kiwi", "كيوي"),           ("Emu", "Émeu", "نعامة")]
    gemstones = [    ("Diamond", "Diamant", "الماس"),    ("Pearl", "Perle", "لؤلؤ"),    ("Emerald", "Émeraude", "زمرد"),    ("Sapphire", "Saphir", "ياقوت"),    ("Turquoise", "Turquoise", "فيروز"),    ("Ruby", "Rubis", "عقيق"),    ("Lapis Lazuli", "Lapis-Lazuli", "اللازورد"),    ("Jade", "Jade", "اليشم"),    ("Amethyst", "Améthyste", "الأمثيلست"),    ("Aquamarine", "Aigue-marine", "بلور الماء"),    ("Garnet", "Grenat", "العقيق"),    ("Opal", "Opale", "أوبال"),    ("Topaz", "Topaze", "توباز"),    ("Peridot", "Péridot", "زبرجد"),    ("Tourmaline", "Tourmaline", "الطورمالين"),    ("Citrine", "Citrine", "الزبرجد"),    ("Alexandrite", "Alexandrite", "الألكسندريت"),    ("Tanzanite", "Tanzanite", "التنزانيت"),    ("Moonstone", "Pierre de lune", "حجر القمر"),    ("Onyx", "Onyx", "العقيق"),    ("Coral", "Corail", "مرجان")]

    return render_template("index.html", title = "Vocabulary", flowers = flowers, birds=birds, gemstones=gemstones)

@app.route("/<csv>", defaults={'topic' : 'vocabulary'})
@app.route("/<csv>/<topic>", methods=["GET", "POST"])
def theme(csv, topic):
    if topic != "vocabulary":
        return render_template("index.html", title = f"{csv.capitalize()} > {topic.capitalize()}", content1 = tools.show_words(csv,topic), footer = f'/{csv}/{tools.next_topic(csv,topic)}')
    else:
        return render_template("index.html", title = csv.capitalize(), content1 = tools.show_topic(csv))