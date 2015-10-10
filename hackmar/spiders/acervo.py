# -*- coding: utf-8 -*-
import scrapy


class AcervoSpider(scrapy.Spider):
    name = "acervo"
    allowed_domains = ["192.168.16.12"]
    item_url_template = ('http://192.168.16.12'
                         '/pergamum/biblioteca/index.php'
                         '?rs=ajax_dados_acervo&rsargs[]={}')

    def start_requests(self):
        for number in range(1, 11111):
            yield scrapy.Request(
                self.item_url_template.format(number))

    def parse(self, response):
        response = response.replace(
            body=response.body.decode('string_escape'))

        fields = response.css(
            '.layer_meio strong::text').extract()
        values = (response.css('.layer_meio td:nth-child(2)')
                  .xpath('string(.)')
                  .extract())
        item = dict(zip(fields, values))
        item['pergamus_id'] = response.url.split('=')[-1]
        yield item
