import scrapy


class Ad(scrapy.Item):
    url = scrapy.Field()
    search_phrase = scrapy.Field()


class SkelbiuLt(scrapy.Spider):
    name = 'skelbiu.lt Spider'
    start_urls = ['https://www.skelbiu.lt/']
    ads_page = 'https://www.skelbiu.lt/skelbimai/komunikacijos/mobilus-telefonai/'

    def __init__(self, search_phrase: str) -> None:
        self._search_phrase = search_phrase
        print(self._search_phrase)

    def parse(self, response: scrapy.http.Response) -> None:
        ensure_response_200(response)
        yield scrapy.Request(
            self.ads_page,
            callback=self.parse_ads_page,
        )

    def parse_ads_page(self, resp: scrapy.http.Response) -> None:
        ensure_response_200(resp)
        ad_links = resp.css('.simpleAds a::attr(href)').extract()
        for link in ad_links:
            yield scrapy.Request(resp.urljoin(link),
                                 callback=self.parse_ad_page)

    def parse_ad_page(self, resp: scrapy.http.Response) -> None:
        '''
        Yields Ad objects if search phrase is found in response.
        '''
        ensure_response_200(resp)
        title = resp.xpath('//div[@id = "adTitle"]//text()').extract_first()
        description = ' '.join(
            resp.xpath('//div[@id = "adDescription"]//text()').extract())
        if title and description:
            if self._search_phrase in title or self._search_phrase in description:
                yield Ad(url=resp.url, search_phrase=self._search_phrase)


def ensure_response_200(response: scrapy.http.Response) -> None:
    if response.status != 200:
        raise Exception('Expected HTTP response 200')
