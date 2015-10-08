# -*- coding: utf-8 -*-
import scrapy


class AcervoSpider(scrapy.Spider):
    name = "acervo"
    allowed_domains = ["192.168.16.12"]
    item_url_template = 'http://192.168.16.12/pergamum/biblioteca/index.php?rs=ajax_dados_acervo&rsargs[]={}'

    def __init__(self, exploratory=None, *args, **kwargs):
        super(AcervoSpider, self).__init__(*args, **kwargs)
        self.exploratory = bool(exploratory)

    def start_requests(self):
        for number in range(1, 11111):
            yield scrapy.Request(self.item_url_template.format(number))

    def parse(self, response):
        response = response.replace(body=response.body.decode('string_escape'))
        if self.exploratory:
            for field in response.css('table strong::text').extract():
                yield {'field': field.strip()}
        else:
            fields = response.css('table strong::text')
            values = response.xpath('//div[not(strong)]/text()')[1:len(fields)+1]
            yield dict(zip(fields, values))
