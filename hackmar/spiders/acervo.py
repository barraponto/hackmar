# -*- coding: utf-8 -*-
import scrapy


class AcervoSpider(scrapy.Spider):
    name = "acervo"
    allowed_domains = ["192.168.16.12"]
    item_url_template = ('http://192.168.16.12'
                         '/pergamum/biblioteca/index.php'
                         '?rs=ajax_dados_acervo&rsargs[]={}')

    def __init__(self, exploratory=None, *args, **kwargs):
        super(AcervoSpider, self).__init__(*args, **kwargs)
        self.exploratory = bool(exploratory)

    def start_requests(self):
        for number in range(1, 11111):
            yield scrapy.Request(
                self.item_url_template.format(number))

    def parse(self, response):
        response = response.replace(
            body=response.body.decode('string_escape'))

        # if response.xpath('//div[not(strong)]/a'):
            # # i think if there's a link in there.
            # # let's look at it manually
            # self.logger.warning(
                # 'Link found in {}'.format(response.url))

        if self.exploratory:
            # just get the field names, for exploratory looks.
            for field in response.css('table strong::text').extract():
                yield {'field': field.strip()}

        else:
            # get the whole data.
            fields = response.css(
                '.layer_meio strong::text').extract()
            values = (response.css('.layer_meio td:nth-child(2)')
                      .xpath('string(.)')
                      .extract())
            yield dict(zip(fields, values))
