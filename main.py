
from flask import Flask, redirect, url_for, render_template, request, session
from packages import googleScholarScraper


app = Flask(__name__)

# config------------------------------------------------
app.config['SECRET_KEY'] = '12345'

#------------------------------------------------------
@app.route('/', methods=['GET'])
def index(**kwargs):

    # Ann Barcomb user id 
    user = "1hMBs-8AAAAJ"

    scraper = googleScholarScraper.ArticleScraper()
    publications_list = scraper.scrape(user=user)
    
    return render_template('index.html', publications_list=publications_list)

@app.route('/people', methods=['GET'])
def people(**kwargs):
    return render_template('people.html')