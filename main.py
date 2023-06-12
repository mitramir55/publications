
from flask import Flask, redirect, url_for, render_template, request, session
from packages import googleScholarScraper
import pickle
import pandas as pd


app = Flask(__name__)
app.debug = True


# config------------------------------------------------
app.config['SECRET_KEY'] = '12345'

#------------------------------------------------------

def check_scraped_content(dictionary):
    """
    checks all the topics and makes sure they have been searched
    if not, returns False
    """
    scraped_bool = True
    for topic, content_list in dictionary.items(): 
        try: assert len(content_list)>0
        except: scraped_bool = False

    return scraped_bool

def save_or_read_file(path, file):

    """
    saves the scraped content if it's been completely searched and collected
    reads the previously saved file in case the scraping hasn't worked
    """
    scraped_bool = check_scraped_content(file)
    
    if scraped_bool:
        with open(path, 'wb') as f:
            pickle.dump(file, f)
    else: file = pd.read_pickle(path)

    return file


@app.route('/', methods=['GET'])
def index(**kwargs):

    topics_acronyms = ['RE', 'NLP', 'AI']
    
    topics_dir_path = r"static\\files\\topics_dict.pickle"

    scraper = googleScholarScraper.ArticleScraper()
    topics_dict = scraper.scrape_topics(topics_acronyms)
    topics_dict = save_or_read_file(path=topics_dir_path, file=topics_dict)

    return render_template('index.html', topics_dict=topics_dict)


@app.route('/publications', methods=['GET'])
def publications(**kwargs):

    """
    This function scrapes the publications of Dr. Barcomb
    """
    # Ann Barcomb user id 
    user = "1hMBs-8AAAAJ"
    topics_dir_path = r"static\\files\\publications_list.pickle"

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

