from numpy import NaN, nan
import pandas as pd

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
    filename = f'app/static/csv/{sheet_name}.csv'
    df = pd.read_csv(filename)
    current_index = df.columns.get_loc(topic)
    if current_index == len(df.columns)-1:
        next = df.columns[0]
    else:
        next = df.columns[current_index+1]
    return str(next).replace(" ","%20")

def show_home():
    html='''
        <table>
            <tr><h4>Labyrinth<h4></tr>
            <tr><p>Do you ever find yourself working on a tedious task with many twists and turns? If you're stuck doing something that's extremely complex, you can call it a labyrinth. Additionally, any maze or place with "intricate passageways" can be described by this word.</p></tr>
            <tr><h4>Ineffable<h4></tr>
            <tr><p>Sometimes, almost every word fails. When that happens, you can turn to the word "ineffable," which means "unspeakable" or "indescribable." For example, if your feelings about someone are almost impossible to accurately pin down, you can say they're ineffable.</p></tr>
            <tr><h4>Incendiary<h4></tr>
            <tr><p>Meaning extremely hot or inflammatory, anything that causes a fire is incendiary. However, when used in contexts that aren't related to fire, this word can also describe someone who likes to start quarrels.</p></tr>
            <tr><h4>Ephemeral<h4></tr>
            <tr><p>Things that don't last forever are ephemeral. From conversations to arguments, some things just tend to be short-lived, which isn't necessarily a bad thing.</p></tr>
            <tr><h4>Cynosure<h4></tr>
            <tr><p>Back in the 17th century, the word cynosure was used to describe the northern constellation, Ursa Minor. And while this is still the case now, Merriam-Webster additionally notes that anyone who is the "center of attention" or "serves to guide" is cynosure.</p></tr>
            <tr><h4>Propinquity<h4></tr>
            <tr><p>Similar to the term proximity, the word "propinquity" is another way to talk about someone who lives near you. Aside from your next-door neighbors and roommates, it can also refer to "nearness of relation," in terms of kinship.</p></tr>
            <tr><h4>Infatuation<h4></tr>
            <tr><p>Do you have a really strong desire to be near or know more about someone, you may have an infatuation. You can also use the term to describe your non-human obsession of the moment, whether it's a TV show or your new puppy.</p></tr>
            <tr><h4>Incandescent<h4></tr>
            <tr><p>While the word "incandescent" is one way to talk about the electric lamps in your living room, it can also be used in reference to the brightness or someone's intellect or personality.</p></tr>
            <tr><h4>Eudaemonia<h4></tr>
            <tr><p>Originated from the Greek word "eudaimon," the word "eudaemonia" means the state of being lucky or happy. If you're in a state of general well-being or feeling great joy, this is one way to express it.</p></tr>
            <tr><h4>Raconteur<h4></tr>
            <tr><p>Are you good at telling a story? Then you can start telling your friends that you're a raconteur. Even if you're not the best storyteller, it's still a fun word to say.</p></tr>
            <tr><h4>Petrichor<h4></tr>
            <tr><p>The Greek words for "stone" and the "ethereal blood of the gods" combine to give us a perfectly beautiful term for the way the earth smells after it rains. Scientists have spent decades trying to determine exactly why that smell is so pleasing; in fact, two are credited for coining "petrichor" in a 1964 Nature article.</p></tr>
            <tr><h4>Sumptuous<h4></tr>
            <tr><p>Meaning "extremely costly, rich, luxurious, or magnificent," the word "sumptuous" can be used to describe anything from a five-star vacation to your favorite fluffy blanket.</p></tr>
            <tr><h4>Angst<h4></tr>
            <tr><p>If you've woken up with a prevailing sense of anxiety about how the day will go, you could say you're experiencing some angst. It's not a pleasant feeling, but the word for it, which dates back to the eighth century, does have a certain soothing sound.</p></tr>
            <tr><h4>Aesthete<h4></tr>
            <tr><p>An aesthete, according to Merriam-Webster, is "one having or affecting sensitivity to the beautiful especially in art." You might be one if you're frequently moved by sculptures and paintings…or if you pretend to be for the sake of other people. Either way, the word is a joy to say.</p></tr>
            </tr><tr><h4>Nadir<h4></tr>
            <tr><p>An astronomical term that's been co-opted for colloquial usage, nadir means the lowest point, as in the "nadir of her popularity." Its opposite term, zenith, has a similar appeal.</p></tr>
            <tr><h4>Miraculous<h4></tr>
            <tr><p>That which seemed impossible or at least incredibly unlikely without the influence of some supernatural force can be described as "miraculous." Maybe that's the birth of a child or being able to carry on a morning conversation before a cup of coffee.</p></tr>
            </tr><tr><h4>Lassitude<h4></tr>
            <tr><p>Suffering from a lack of energy? Describe your tiredness—whether it's in your body, your mind, or both—with this term, and at least it will sound prettier.</p></tr>
            </tr><tr><h4>Gossamer<h4></tr>
            </tr><tr>One of several definitions of this word, per Dictionary.com, is "a fine, filmy cobweb seen on grass or bushes or floating in the air in calm weather, especially in autumn." It's thought to have come from the Middle English term gosesummer, "possibly first used as name for late, mild autumn, a time when goose was a favorite dish." But it can also be used to refer to anything thin and airy, from a summer shawl to the wings of a butterfly.
            </tr><tr><h4>Bungalow<h4></tr>
            </tr><tr>Bungalow is a cozy word for a specific type of house: usually one that's either a single story or two stories with a sloping roof. Though there may be additional criteria depending on where in the world you're using the term.
            </tr><tr><h4>Scintilla<h4></tr>
            </tr><tr>Not to be confused with those furry crepuscular rodents, scintilla means a spark or a trace of something. Perhaps you feel a scintilla of guilt after eating the last cookie, or experience a scintilla of attraction to someone you just met.
            </tr><tr><h4>Aurora<h4></tr>
            </tr><tr>Originally the name of the Roman goddess of sunrise, the word aurora is now used to describe the dawn, as well as the stunning luminous phenomenon that takes place in the upper atmosphere of a planet's magnetic polar regions. For example, you may have a trip to see the Aurora Borealis as an item on your bucket list.
            </tr><tr><h4>Inure<h4></tr>
            </tr><tr>Not all beautiful words have beautiful meanings. The word inure means to accept or grow accustomed to something undesirable. For example, your family's constant criticism could inure you to toxic behavior from loved ones.
            </tr><tr><h4>Mellifluous<h4></tr>
            </tr><tr>This lyrical word refers to something that is sweet and enjoyable, especially when it comes to sound. You might find the early spring sounds of chirping birds to be quite mellifluous.
            </tr><tr><h4>Euphoria<h4></tr>
            </tr><tr>Derived from the Greek word for healthy, the word euphoria is now used to describe an intense feeling of happiness or elation. A sense of euphoria may be the result of a fortunate turn of events or an indescribable personal high.
            </tr><tr><h4>Serendipity<h4></tr>
            </tr><tr>You've probably experienced this phenomenon more than you realize—remember that time you went on a coffee run and stumbled upon the best chocolate cake your city has to offer? Or when you were cleaning your home and found those earrings you thought were gone years ago? Those happy coincidences are all cases of serendipity.
            </tr><tr><h4>Cherish<h4></tr>
            </tr><tr>The word cherish means to hold dear or cultivate with care and affection. Whether that's your family, your home, or your most prized possession (or all three!), everyone has someone or something that they cherish.
            </tr><tr><h4>Demure<h4></tr>
            </tr><tr>One of our favorite beautiful words, demure is used to describe any modest and reserved behavior. Etymologists believe it may have been derived from the Anglo-French verb demorer or demourer, which means "to linger."
            </tr><tr><h4>Elixir<h4></tr>
            </tr><tr>If you're well-versed in the world of Harry Potter, you probably associate this word with the elixir of life derived from the Sorcerer's Stone. In the 17th century, alchemists believed it was possible to create an elixir that would turn base metals to stone and allow people to live forever. Today, the word is used to identify a substance that's capable of changing base metals into gold. You might also use it to describe that cocktail you just whipped up at your home bar.
            </tr><tr><h4>Eternity<h4></tr>
            </tr><tr>Forever; always; a limitless time. These are just some ways to describe the endless and sometimes frightening idea of eternity.
            </tr><tr><h4>Felicity<h4></tr>
            </tr><tr>This one's just another word for a state of happiness. For example, you might find yourself in a state of felicity the next time you're surrounded by people you love.
            </tr><tr><h4>Languor<h4></tr>
            </tr><tr>Another beautiful word with a not-so-beautiful definition, languor refers to lethargy or weakness in body and mind. You might experience this phenomenon when you've been working too many hours and are starting to hit burnout. All that means is it's time to use that PTO!
            </tr><tr><h4>Love<h4></tr>
            </tr><tr>There's way more than one definition for this feeling, action, phenomenon (etc, etc). But we can all agree that the word love is as beautiful as everything it describes.
            </tr><tr><h4>Solitude<h4></tr>
            </tr><tr>If you're an extrovert, then solitude may not be ideal. But if you're an introvert, you'll probably enjoy and seek out solitude, or the act of being alone and away from society.
            </tr><tr><h4>Epiphany<h4></tr>
            </tr><tr>While there are several meanings of this word, most people associate an epiphany with a life-changing realization. You'll find examples of these in your favorite books and movies, such as the classic scene in Clueless when Cher realizes she's "majorly, totally, butt-crazy in love" with her stepbrother Josh.
            </tr><tr><h4>Quintessential<h4></tr>
            </tr><tr>Have you ever met someone who embodies all of the characteristics of the city they're from or the career path they've chosen? Then you might have come across someone who is perfectly typical, otherwise known as quintessential. Snacking on strawberries and cream while sipping a Pimm's Cup at Wimbledon? That's so quintessentially British!
            </tr><tr><h4>Plethora<h4></tr>
            </tr><tr>This word has two definitions—one beautiful and one not so beautiful. While plethora is most commonly associated with having an abundance of something (close your eyes and picture a plethora of disposable income!), it's also a medical word that's used to describe increased blood in a specific area.
            </tr><tr><h4>Nemesis<h4></tr>
            </tr><tr>As beautifully as this word rolls off of the tongue, it is associated with a rival or arch-enemy and can be used to describe inflicting an act of vengeance. That friend-of-a-friend who grinds your gears every time he comes to Friday night drinks? He might be your nemesis.
            </tr><tr><h4>Lithe<h4></tr>
            </tr><tr>One syllable and full of grace, the word lithe is used to characterize flexibility and a slim figure. For example, you may have noticed the lithe ballerinas when you attended a performance of The Nutcracker at Christmastime.
            </tr><tr><h4>Tranquility<h4></tr>
            </tr><tr>Hopefully, you'll achieve a state of tranquility on your next beach vacation. This is just another word for being free from agitation of mind or spirit.
            </tr><tr><h4>Elegance<h4></tr>
            </tr><tr>Another word that sounds exactly the way it's defined, elegance is a quality of style and grace.
            </tr> <tr><h4>Renaissance<h4></tr>
            </tr><tr>Whether you're referring to your own personal revival in life or the transitional period between the 14th and 17th centuries, the word renaissance will roll off the tongue and fulfill all of your aesthetically pleasing linguistic needs.
            </tr><tr><h4>Eloquence<h4></tr>
            </tr><tr>A quality found in the most skillful politicians, this word refers to persuasive expressiveness. Look out for eloquence in the 2020 presidential debates—which candidate's eloquence will win your vote?
            </tr><tr><h4>Sequoia<h4></tr>
            </tr><tr>These larger than life trees can be found throughout California, particularly in their namesake national park in the southern Sierra Nevada Mountains. Having a hard time differentiating between a sequoia and a redwood (or the Sequoia National Park and the Redwood National and State Parks)? Here's an easy way to differentiate: if you're on the coast, then you're probably looking up at a redwood; if you're inland, then you've definitely found yourself in the presence of a sequoia.
            </tr><tr><h4>Peace<h4></tr>
            </tr><tr>Ever versatile, the word peace can refer to a state of mind, freedom from civil disturbances, or a time without war.
            </tr><tr><h4>Lullaby<h4></tr>
            </tr><tr>There isn't a better word to describe a soothing melody to get your child to sleep. But this word isn't reserved for babies—it can also be used as a verb meaning to quiet with or as with a lullaby.
            </tr><tr><h4>Paradox<h4></tr>
            </tr><tr>The beginning of the end. Youth is wasted on the young. These are both examples of paradox, or a statement that seemingly contradicts itself.
            </tr><tr><h4>Pristine<h4></tr>
            </tr><tr>This beautiful word seems to sparkle—and that's fitting, since pristine means "fresh and clean or as if new."
            </tr><tr><h4>Effervescent<h4></tr>
            </tr><tr>Here's a clever new way to describe the bubbly can-do person around your office. Instead of merely calling them fun to be around, you could take things up a notch and say they have an effervescent personality. That simply means they have an appealingly lively quality.
            </tr><tr><h4>Opulence<h4></tr>
            </tr><tr>Do you dream of owning a mansion in Beverly Hills with a Maserati in the driveway and regular shopping trips on Rodeo Drive? Then you might be pining for a life of opulence. Keep on grinding!
            </tr><tr><h4>Ethereal<h4></tr>
            </tr><tr>This light and airy word might remind you of celestial bodies. Ethereal can refer to the upper regions of space as well as anything that is heavenly and unworldly seeming.
            </tr><tr><h4>Sanguine<h4></tr>
            </tr><tr>A complicated and beautiful word, sanguine comes with several meanings. It's typically used as a synonym for optimism, but it can also describe a blood-red hue or something relating to blood.
            </tr><tr><h4>Panacea<h4></tr>
            </tr><tr>Panacea means all-healing in Greek and, fittingly, Panacea was the Greek goddess of healing. Today, the word is used to refer to something that could fix everything. Imagine a remedy for all of the problems you face on a daily basis—that would be a panacea.
            </tr><tr><h4>Bodacious<h4></tr>
            </tr><tr>While this word is often used to describe a body's curves, bodacious can also be used to describe something that is remarkable or admirable. For example, a person might have a bodacious energy or a home might have bodacious decor.
            </tr><tr><h4>Axiom<h4></tr>
            </tr><tr>An axiom is a statement that is widely accepted as true. For example, from the Declaration of Independence—"we hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty, and the Pursuit of Happiness." These "truths" could also be described as axioms.
            </tr><tr><h4>Silhouette<h4></tr>
            </tr><tr>Depending on the situation, seeing a silhouette—or the outline of a figure—may be beautiful or spooky. For example, seeing the silhouette of a young couple on a park bench is lovely, but if you see a shadowy silhouette in a house you thought was empty, then you might want to run away.
            </tr><tr><h4>Surreptitious<h4></tr>
            </tr><tr>This word means to act clandestinely or to do or acquire something by stealth. For example, that person at your job who always seems to be working on a secret project might be considered surreptitious.
            </tr><tr><h4>Ingenue<h4></tr>
            </tr><tr>You'll find examples of this word in classic literature, film, and television. Naive and innocent female characters such as Sandy at the start of Grease and Ophelia from Hamlet are examples of ingenues.
            </tr><tr><h4>Dulcet<h4></tr>
            </tr><tr>This dainty word is another one that seems to describe exactly what it sounds like—which is anything that is generally pleasing. For example, you may have recently listened to particularly dulcet music or indulged in a dulcet chocolate cake.
            </tr><tr><h4>Tryst<h4></tr>
             <tr>This crisp word is usually used to describe a somewhat discreet meeting between two lovers. While technically defined as any sort of meeting or appointment (not necessarily with romantic motivations), you probably don't want to refer to the next meeting at your office as a "tryst".
            </tr><tr><h4>Ebullience<h4></tr>
            <tr>A beautiful word that's probably best used to describe a litter of golden retriever puppies, ebullience is the quality of excitement and enthusiasm./tr>
        </table>'''
    return html