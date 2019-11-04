import scrapy

class BlogSpider(scrapy.Spider):
    name = 'radio'
    start_urls = ['https://doc.ubuntu-fr.org/liste_radio_france']

    def parse(self, response):
        # for title in response.css('.post-header>h2'):
        #     yield {'title': title.css('a ::text').get()}

        # for next_page in response.css('a.next-posts-link'):
        #     yield response.follow(next_page, self.parse)
        body = "<html><body></body></html>"
        # print(response.selector.xpath('//body/text()').get())
        scrapy.Selector(text=body)