import scrapy
from sample.items import SampleItem


class SampleSpiderSpider(scrapy.Spider):
    name = "sample_spider"
    allowed_domains = ["ja.wikipedia.org"]
    start_urls = ["https://ja.wikipedia.org/"]

    def parse(self, response):
        items = response.xpath('//*[@id="on_this_day"]//li')
        for i in items:
            text = [t.get() for t in i.xpath('.//text()')]
            item = SampleItem()
            item['today'] = "".join(text)
            yield item