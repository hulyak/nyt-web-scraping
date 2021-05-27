import scrapy


class TruecarSpider(scrapy.Spider):
    name = "truecar"

    def start_requests(self):
        urls = [
            'https://www.truecar.com/used-cars-for-sale/listings/tesla/model-3/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


def parse(self, response):
  # //li[@data-qa="Listings"]
    all_listings = response.xpath(
        '// *[@id="mainContent"]/div/div[4]/div/div/div/div[2]/div[1]/ul/li')

    for tesla in all_listings:
        make_model = tesla.css('div[data-test="cardContent"] > div'
                               )
        year = make_model.css('span.vehicle-card-year::text').get()
        model_raw = make_model.css('span.vehicle-header-make-model').get()
        model = model_raw[model_raw.find('>')+1:-7].replace('<!-- -->', '')

        tesla_data = {
            'url': 'http://truecar.com' + tesla.css('a::attr(href)').get(),
            'model': year + ' ' + model,
            'mileage': tesla.css('div[data-test="cardContent"] > div > div.text-truncate::text').get(),
            'price': tesla.css('div::text').get(),
        }

        yield tesla_data
