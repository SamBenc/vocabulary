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

def list_to_html(mylist):
    html = "<ul class='words_list'>"
    for item in mylist:
        item = str(item).capitalize()
        search_item = str(item).replace(" ","%20").replace("/","%20")
        try:
            word_def = get_def(search_item)
        except Exception as e:
            word_def = e
            continue
        translate = f'https://translate.google.com/?hl=en&sl=en&tl=en&op=translate&text={search_item}'
        image = f'https://www.google.com/search?q={search_item}&tbm=isch'
        linguee = f'https://www.linguee.fr/francais-anglais/search?source=anglais&query={search_item}'
        youtube = f'https://www.youtube.com/results?search_query={search_item}'
        definition = f'https://www.dictionary.com/browse/{search_item}'
        if item not in [nan, NaN, 'nan', 'NaN']:
            html += f"""
            <!-- Button trigger modal -->
            <li type="button" class="word" data-toggle="modal" data-target="#{search_item}">{item}</li>

            <!-- Modal -->
            <div class="modal fade" id="{search_item}" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog modal-dialog-centered" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="exampleModalLabel">{item}</h5>
                            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                            </button>
                        </div>
                        <div class="modal-body">
                                        <p class="word d-flex justify-content-center">
                                            <a href={translate} target="_blank"><i class="fa fa-language"></i></a>&nbsp; &nbsp;
                                            <a href={image} target="_blank"><i class="fa fa-image"></i></a>&nbsp; &nbsp;
                                            <a href={linguee} target="_blank"><i class="fa fa-quote-right"></i></a>&nbsp; &nbsp;
                                            <a href={youtube} target="_blank"><i class="fa fa-youtube"></i></a>&nbsp; &nbsp;
                                            <a href={definition} target="_blank"><i class="fa fa-comment"></i></a>&nbsp; &nbsp;
                                        </p>
                                        {word_def}
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                        </div>
                    </div>
                </div>
            </div>
            """
    html += '</ul>'
    return html

"""
def getMeaning(word, lang):
    try:
        return GoogleTranslator(source='en', target=lang).translate(word)
    except Exception as e:
        return "Not Found"

def show_words(sheet_name, topic):
    filename = f'app/static/csv/{sheet_name}.csv'
    df = pd.read_csv(filename)
    html = list_to_html(df[topic])
    return html

def show_topic(sheet_name):
    filename = f'app/static/csv/{sheet_name}.csv'
    df = pd.read_csv(filename)
    return list_to_href(sheet_name,df.columns)

def list_to_html(mylist):
    html = "<ul class='words_list'>"
    for item in mylist:
        item = str(item).capitalize()
        search_item = str(item).replace(" ","%20").replace("/","%20")
        try:
            word_def = get_def(search_item)
        except Exception as e:
            word_def = e
            continue
        translate = f'https://translate.google.com/?hl=en&sl=en&tl=en&op=translate&text={search_item}'
        image = f'https://www.google.com/search?q={search_item}&tbm=isch'
        linguee = f'https://www.linguee.fr/francais-anglais/search?source=anglais&query={search_item}'
        youtube = f'https://www.youtube.com/results?search_query={search_item}'
        definition = f'https://www.dictionary.com/browse/{search_item}'
        if item not in [nan, NaN, 'nan', 'NaN']:
            html += f
            <!-- Button trigger modal -->
            <li type="button" class="word" data-toggle="modal" data-target="#{search_item}">{item}</li>

            <!-- Modal -->
            <div class="modal fade" id="{search_item}" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog modal-dialog-centered" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="exampleModalLabel">{item}</h5>
                            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                            </button>
                        </div>
                        <div class="modal-body">
                                        <p class="word d-flex justify-content-center">
                                            <a href={translate} target="_blank"><i class="fa fa-language"></i></a>&nbsp; &nbsp;
                                            <a href={image} target="_blank"><i class="fa fa-image"></i></a>&nbsp; &nbsp;
                                            <a href={linguee} target="_blank"><i class="fa fa-quote-right"></i></a>&nbsp; &nbsp;
                                            <a href={youtube} target="_blank"><i class="fa fa-youtube"></i></a>&nbsp; &nbsp;
                                            <a href={definition} target="_blank"><i class="fa fa-comment"></i></a>&nbsp; &nbsp;
                                        </p>
                                        {word_def}
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                        </div>
                    </div>
                </div>
            </div>
            
    html += '</ul>'
    return html

def showMenu(item):
    translate = f'https://translate.google.com/?hl=en&sl=en&tl=en&op=translate&text={item}'
    image = f'https://www.google.com/search?q={item}&tbm=isch'
    linguee = f'https://www.linguee.fr/francais-anglais/search?source=anglais&query={item}'
    youtube = f'https://www.youtube.com/results?search_query={item}'
    definition = f'https://www.dictionary.com/browse/{item}'
    html = f'''<table class="menuList hide">
                    <tr>
                        <td class='padding'><a href={translate} target="_blank"><i class="fa fa-language"></i></a></td>
                        <td class='padding'><a href={image} target="_blank"><i class="fa fa-image"></i></a></td>
                        <td class='padding'><a href={linguee} target="_blank"><i class="fa fa-quote-right"></i></a></td>
                        <td class='padding'><a href={youtube} target="_blank"><i class="fa fa-youtube"></i></a></td>
                        <td class='padding'><a href={definition} target="_blank"><i class="fa fa-comment"></i></a></td>
                    </tr>
                </table>'''
    return html

def list_to_html(mylist):
    html = "<ul class='words_list'>"
    for item in mylist:
        if item not in [nan, NaN, 'nan', 'NaN']:
            html += f'<li class="word"><i class="fa fa-globe" aria-hidden="true"></i>&nbsp;&nbsp;<i class="fa fa-external-link" aria-hidden="true" onclick="showList()"></i>&nbsp;&nbsp;{item.capitalize()}</li>'
    return html + '</ul>'

def list_to_href(link, mylist):
    html = ""
    for item in mylist:
        html += f"<a class='topic' href='/{link}/{item}'><i class='fa fa-arrow-right'></i> {item.capitalize()} </a><br>"
    return html

def next_topic(sheet_name, topic):
    filename = f'app/static/csv/{sheet_name}.csv'
    df = pd.read_csv(filename)
    current_index = df.columns.get_loc(topic)
    if current_index == len(df.columns)-1:
        next = df.columns[0]
    else:
        next = df.columns[current_index+1]
    return str(next).replace(" ","%20")

"""