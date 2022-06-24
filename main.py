
from flask import Flask, redirect, url_for, render_template, request, session
from packages import googleScholarScraper


app = Flask(__name__)

# config------------------------------------------------
app.config['SECRET_KEY'] = '12345'

#------------------------------------------------------

@app.route('/index', methods=['GET'])
def index(**kwargs):

    try:
        # Ann Barcomb user id 
        user = "1hMBs-8AAAAJ"

        scraper = googleScholarScraper.ArticleScraper()
        publications_list = scraper.scrape(user=user)
        
    except:
        return render_template('index.html', papers=False)

    return render_template('index.html', papers=True)


@app.route('/', methods=['GET'])
def publications(**kwargs):

    # Ann Barcomb user id 
    user = "1hMBs-8AAAAJ"

    scraper = googleScholarScraper.ArticleScraper()
    publications_list = scraper.scrape(user=user)
    
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
