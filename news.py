# Web scraper to get news article content
import scrapy
from bs4 import BeautifulSoup

class NYTScraper(scrapy.Spider):
    name = "NYTScraper"
    start_urls = [
        "https://www.nytimes.com/"
    ]
    
    def parse(self, response):
        titles = response.css('.e1voiwgp0').extract()
        links = response.css('.css-1ee8y2t a::attr(href)').extract()
        content = response.css('.css-1hmipqs').extract()
        
        for item in zip(titles, links, content):
            all_items = {
                'title': BeautifulSoup(item[0]).text,
                'link' : item[1],
                'content': BeautifulSoup(item[2]).text
            }
            
            yield all_items
