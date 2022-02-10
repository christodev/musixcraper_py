import flask
from flask import request, jsonify
# from os import system
import musixcraper;

app = flask.Flask(__name__);
app.config['DEBUG'] = True;

#Create some test data to test api

people = [
    {
        'name':'Christian',
        'age': '21'
    },
    {
        'name':'Melissa',
        'age': '16'
    }

];

@app.route('/', methods=['GET'])
def Index():
    return "Hello all!";

@app.route('/lyrics', methods=['GET'])
def GetLyrics():
    # system('python3 ../musixcraper2.py');
    lyrics = musixcraper.SearchForLyrics()
    return f"Here is your lyrics: {lyrics}";

app.run();