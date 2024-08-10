import scrapy

domain = "https://kubernetes.io"

class K8sDocSpider(scrapy.Spider):
    name = "K8sDocSpider"
    start_urls = ['https://kubernetes.io/docs/home/']

    def parse_doc(self, response):
        yield{
            "Title": response.xpath('//title/text()').get(),
            "Para": response.xpath('//div[@id="maindoc"]//p').get()
            # "Para": [p for p in response.xpath('//div[@id="maindoc"]//p').getall()]
        }


    def parse(self, response):
        for url in response.xpath('//a[has-class("align-left")]//@href').getall():
            # yield {'URL': url}
            next_page = response.urljoin(url)
            if next_page:
                yield response.follow(next_page, self.parse_doc)
