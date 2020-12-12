# Web scraper to get news article content

- build a simple web scraper that will return the content of a news article when given a specific URL. Some examples of real products which use similar technologies include price-tracking websites and SEO audit tools which may scrape top search results.

## Requirements

Choose one news website - see article examples below for inspiration. Given a specific article URL from the website of your choice, return the title and content of the article to the user.

Examples article URLs:

https://www.nytimes.com/2020/09/02/opinion/remote-learning-coronavirus.html
https://www.washingtonpost.com/technology/2020/09/25/privacy-check-blacklight/

https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html

https://www.reuters.com/article/us-health-coronavirus-global-deaths/global-coronavirus-deaths-pass-agonizing-milestone-of-1-million-idUSKBN26K08Y

For an extra challenge: Parse out information such as the article title, updated date, and byline to return separately to the user.

### Suggested Implementation

You can use something similar to this service in command line:

```bash
> python scrape_newyorktimes.py news_url
```

We suggest using a HTTP library like **Requests** to get the raw HTML file of the URL. Then use a parsing library like **Beautiful Soup** to parse the content. Alternatively, you can also use a Python scraping tool like **Scrapy.**

#### References

- You can use **xPath** to select elements if there’s no class or div for the element
- Take note of the Python version you have installed! ([reference](https://learntocodewith.me/programming/python/python-2-vs-python-3/#:~:text=Python%203.0%20was%20released%20in,3%20adoption%20is%20growing%20quickly.&text=Notably%2C%20on%20January%201%2C%202018,and%20no%20longer%20be%20maintained.))

## Installation

```bash
# run scrapy 
> scrapy runspider news.py 

# create a csv file 
> scrapy runspider news.py -o nyt.csv
```