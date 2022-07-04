For creating a scraper for relevant topic on the main page:

```

@app.route('/', methods=['GET'])
def index(**kwargs):

    try:
        # Ann Barcomb user id 
        user = "1hMBs-8AAAAJ"

        scraper = googleScholarScraper.ArticleScraper()
        publications_list = scraper.scrape(user=user)
        
    except:
        return render_template('index.html', papers=False)

    return render_template('index.html', papers=True)


```