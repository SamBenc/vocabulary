from numpy import NaN, nan
import pandas as pd
import os

def show_words(sheet_name, topic):
    base_dir = os.getcwd()
    filename = f'vocabulary/app/static/csv/{sheet_name}.csv'
    file_path = os.path.join(base_dir,filename)
    df = pd.read_csv(file_path)
    html = list_to_html(df[topic])
    return html

def show_topic(sheet_name):
    base_dir = os.getcwd()
    filename = f'vocabulary/app/static/csv/{sheet_name}.csv'
    file_path = os.path.join(base_dir,filename)
    df = pd.read_csv(file_path)
    return list_to_href(sheet_name,df.columns)

def list_to_html(mylist):
    html = "<ul class='words_list'>"
    for item in mylist:
        translate = f'https://translate.google.com/?hl=en&sl=en&tl=en&op=translate&text={item}'
        image = f'https://www.google.com/search?q={item}&tbm=isch'
        linguee = f'https://www.linguee.fr/francais-anglais/search?source=anglais&query={item}'
        youtube = f'https://www.youtube.com/results?search_query={item}'
        definition = f'https://www.dictionary.com/browse/{item}'
        if item not in [nan, NaN, 'nan', 'NaN']:
            html += f'''<li class="word">
                            <a href={translate} target="_blank"><i class="fa fa-language"></i></a>&nbsp; &nbsp;
                            <a href={image} target="_blank"><i class="fa fa-image"></i></a>&nbsp; &nbsp;
                            <a href={linguee} target="_blank"><i class="fa fa-quote-right"></i></a>&nbsp; &nbsp;
                            <a href={youtube} target="_blank"><i class="fa fa-youtube"></i></a>&nbsp; &nbsp;
                            <a href={definition} target="_blank"><i class="fa fa-comment"></i></a>&nbsp; &nbsp;
                            {item.capitalize()}
                        </li>'''
    return html + '</ul>'

def list_to_href(link,mylist):
    html = "<ul class='words_list'>"
    for item in mylist:
        html += f"<li><a class='topic' href='/{link}/{item}'><i class='fa fa-arrow-circle-right'></i>&nbsp; &nbsp;{item.capitalize()}</a></li>"
    return html + "</ul>"

def next_topic(sheet_name, topic):
    base_dir = os.getcwd()
    filename = f'vocabulary/app/static/csv/{sheet_name}.csv'
    file_path = os.path.join(base_dir,filename)
    df = pd.read_csv(file_path)
    current_index = df.columns.get_loc(topic)
    if current_index == len(df.columns)-1:
        next = df.columns[0]
    else:
        next = df.columns[current_index+1]
    return str(next).replace(" ","%20")