
from flask import Flask, redirect, url_for, render_template, request, session
from googleScholarScraper import ArticleScraper


app = Flask(__name__)

# config------------------------------------------------
VOCAB_FILE = 'Vocabulary.xlsx'
ALLOWED_EXTENSIONS = {'txt'}

app.config['SECRET_KEY'] = '12345'

#------------------------------------------------------
@app.route('/', methods=['GET'])
def index(**kwargs):

    # Ann Barcomb user id 
    user = "1hMBs-8AAAAJ"

    scraper = ArticleScraper()
    publications_list = scraper.scrape(user=user)
    
    return render_template('papers.html', publications_list=publications_list)

