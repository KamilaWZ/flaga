from flask import Flask, render_template
from moje_programy.character_wiki import character
#from moje_programy.open_poem import open_poem
import random

app=Flask(__name__)

@app.route('/')
def index():
    text = open('dane/xd.txt').read()
    return render_template("index.html", text=text)

@app.route('/xd')
def xd():
    return render_template("xd.html")

@app.route('/flaga-dla-ukrainy')
def flaga_dla_ukrainy():
    return render_template("ukraina.html")

#@app.route('/brudnopis')
#def brudnopis():
    #super_heroes = ['Bruce Lee', 'Kubuś Puchatek', 'Kopernik', 'Małysz']
    #chosen_hero = random.choice( super_heroes)
    #description = character( chosen_hero).encode('utf-8').decode()
    #poem_lines = open_poem()
    #return render_template("brudnopis.html", hero=chosen_hero, description=description, poem_lines=poem_lines)

if __name__=="__main__":
    app.run()
