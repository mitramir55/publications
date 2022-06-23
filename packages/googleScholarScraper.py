from bs4 import BeautifulSoup
import requests, lxml, os

class ArticleScraper:
    """
    creates an html link to find and scrape data for author's name
    """

    def __init__(self):
        self.headers = {
            'User-agent':
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
            }
        
    def scrape(self, user):

        """
        creates a list of dictionaries with the publication info
        input: name of author
        output: [{title, title_link, authors, publication}, {...}]
        """
        params = {"user": user, "sortby": "pubdate", "hl":"en"}
        publications_list = []

        html = requests.get('https://scholar.google.com/citations', params=params, headers=self.headers, timeout=5)
        text = html.text
        soup = BeautifulSoup(text, 'lxml')

        for article_info in soup.select('#gsc_a_b .gsc_a_t'):
            title = article_info.select_one('.gsc_a_at').text
            title_link = f"https://scholar.google.com{article_info.select_one('.gsc_a_at')['href']}"
            authors = article_info.select_one('.gsc_a_at+ .gs_gray').text
            publications = article_info.select_one('.gs_gray+ .gs_gray').text


            articles_dict = {'title':title, 'title_link':title_link,
            'authors': authors, 'publications':publications}
            publications_list.append(articles_dict)

        
        return publications_list



