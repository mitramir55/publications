from bs4 import BeautifulSoup
import requests

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
        soup = BeautifulSoup(text, 'html.parser')

        for article_info in soup.select('#gsc_a_b .gsc_a_t'):
            title = article_info.select_one('.gsc_a_at').text
            title_link = f"https://scholar.google.com{article_info.select_one('.gsc_a_at')['href']}"
            authors = article_info.select_one('.gsc_a_at+ .gs_gray').text
            publications = article_info.select_one('.gs_gray+ .gs_gray').text


            articles_dict = {'title':title, 'title_link':title_link,
            'authors': authors, 'publications':publications}
            publications_list.append(articles_dict)

        
        return publications_list



    def scrape_topic(self, phrase):
        
        # search parameters
        topic_name = self.produce_full_names(phrase=phrase)
        params = {"q": phrase, "hl": "en"}
        html = requests.get('https://scholar.google.com/scholar', headers=self.headers, params=params).text
        soup = BeautifulSoup(html, 'lxml')

            
        # the dictionary will be collected here
        dict_ = []

        # Container where all needed dict_ is located
        for result in soup.select('.gs_ri'):
            title = result.select_one('.gs_rt').text
            title_link = result.select_one('.gs_rt a')['href']
            snippet = result.select_one('.gs_rs').text
            #related_articles = result.select_one('a:nth-child(4)')['href']
            #try:
             #   all_article_versions = result.select_one('a~ a+ .gs_nph')['href']
            #except:
             #   all_article_versions = None


            dict_.append({
                'title': title,
                'title_link': title_link,
                'snippet': snippet,
                'topic': topic_name,
                #'related_articles': f'https://scholar.google.com{related_articles}',
            })

        return dict_

    def produce_full_names(self, phrase):
        """
        creates an acronym to be used in the html and css as a class
        """
        if phrase == 'AI':
            return 'Artificial Intelligence'
        elif phrase == 'NLP':
            return 'Natural Language Processing'
        elif phrase == 'RE':
            return 'Requirements engineering'