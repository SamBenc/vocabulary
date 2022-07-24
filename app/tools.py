from numpy import NaN, nan
import pandas as pd
from bs4 import BeautifulSoup
import requests

def get_def(word):
    url = "https://www.merriam-webster.com/dictionary/"+str(word)
    doc = requests.get(url)
    html = BeautifulSoup(doc.text, "html.parser")
    result = html.find("div", {"id":"dictionary-entry-1"})
    return result

def show_words(sheet_name, topic):
    filename = f'app/static/csv/{sheet_name}.csv'
    df_raw = pd.read_csv(filename)
    df = df_raw[topic].fillna("")
    df = df.drop_duplicates()
    html = list_to_html(df)
    return html

def show_topic(sheet_name):
    filename = f'app/static/csv/{sheet_name}.csv'
    df = pd.read_csv(filename)
    return list_to_href(sheet_name,df.columns)

def list_to_html(mylist):
    html = "<ul class='words_list'>"
    for item in mylist:
        if item not in [nan, NaN, 'nan', 'NaN']:
            html += f'<li type="button" class="word" data-toggle="modal" data-target="#modal1" onclick="defpopup(this)">{str(item).capitalize()}</li>'
    html += '</ul>'
    return html

def list_to_href(link,mylist):
    html = "<ul class='words_list'>"
    for item in mylist:
        html += f"<li><a class='topic' href='/{link}/{item}'><i class='fa fa-arrow-circle-right'></i>&nbsp; &nbsp;{str(item).capitalize()}</a></li>"
    return html + "</ul>"

def next_topic(sheet_name, topic):
    filename = f'app/static/csv/{sheet_name}.csv'
    df = pd.read_csv(filename)
    current_index = df.columns.get_loc(topic)
    if current_index == len(df.columns)-1:
        next = df.columns[0]
    else:
        next = df.columns[current_index+1]
    return str(next).replace(" ","%20")

def show_home():
    return "<h3>Look up a word, learn it forever.</h3>"