
from flask import Flask, redirect, url_for, render_template, request, session
from packages import googleScholarScraper
import pickle
import pandas as pd


app = Flask(__name__)

# config------------------------------------------------
app.config['SECRET_KEY'] = '12345'

#------------------------------------------------------


@app.route('/', methods=['GET'])
def index(**kwargs):
    
    topics_acronyms = ['RE', 'NLP', 'AI']
    
    topics_dir_path = r"static\Files\topics_dict.pickle"

    scraper = googleScholarScraper.ArticleScraper()
    topics_dict = {}

    for topic in topics_acronyms:
        dict_ = scraper.scrape_topic(phrase=topic)
        topics_dict[topic] = dict_

    # read the saved file in case the scraping didn't work
    if topics_dict:
        with open(topics_dir_path, 'wb') as f:
            pickle.dump(topics_dict, f)
    else: topics_dict = pd.read_pickle(topics_dir_path)

    return render_template('index.html', topics_dict=topics_dict)


@app.route('/publications', methods=['GET'])
def publications(**kwargs):

    # Ann Barcomb user id 
    user = "1hMBs-8AAAAJ"
    topics_dir_path = r"static\Files\publications_list.pickle"

    scraper = googleScholarScraper.ArticleScraper()
    publications_list = scraper.scrape(user=user)

    # read the saved file in case the scraping didn't work
    if publications_list:
        with open(topics_dir_path, 'wb') as f:
            pickle.dump(publications_list, f)
    else: publications_list = pd.read_pickle(topics_dir_path)
    
    return render_template('publications.html', publications_list=publications_list)


@app.route('/people', methods=['GET'])
def people(**kwargs):
    return render_template('people.html')


@app.route('/teaching', methods=['GET'])
def teaching(**kwargs):
    return render_template('teaching.html')


@app.route('/positions', methods=['GET'])
def positions(**kwargs):
    return render_template('positions.html')

