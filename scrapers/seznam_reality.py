import unicodedata
import pyppeteer
from scrapers.base import Base
from pyquery import PyQuery as pq
from property import Property


class SeznamReality(Base):
    PROPERTY_LIST_SELECTOR = '.dir-property-list'
    PROPERTY_SELECTOR = '.dir-property-list .property'

    @property
    def host(self):
        return "https://sreality.cz"

    async def get_items(self):
        """ Yield all houses to caller """
        browser = await pyppeteer.launch()
        page = await browser.newPage()
        page.setDefaultNavigationTimeout(60000)
        await page.goto(self.get_url(self.path))

        await page.waitForSelector(self.PROPERTY_LIST_SELECTOR)
        html = await page.content()

        for link in self.get_links_from_html(html):
            async for item in self.get_houses_from_link(page, link):
                yield self.html_to_property(item)

        await browser.close()

    async def get_houses_from_link(self, page, link):
        """ Query houses on the current page and yield them """
        await page.goto(self.get_url(link))
        await page.waitForSelector(self.PROPERTY_LIST_SELECTOR)
        html = await page.content()

        items = pq(html).find(self.PROPERTY_SELECTOR)
        if len(items):
            for item in items:
                yield item

    def get_links_from_html(self, html):
        """ Get all pagination links and return a list """
        pagination = pq(html).find('.paging-small li a:not(.icof)')

        links = [anchor.get('href') for anchor in pagination] if len(pagination) > 0 else [self.path]
        return links

    def html_to_property(self, item):
        name = pq(item).find('h2 a span').text()
        name = unicodedata.normalize('NFKD', name)

        # link
        link = pq(item).find('h2 a').attr('href')
        link = f'{self.host}{link}'

        # locality
        locality = pq(item).find('span.locality').text()

        # price
        price = pq(item).find('span.norm-price').text()
        price = unicodedata.normalize('NFKD', price)

        images = list(map(
            lambda img: img.get('src'),
            pq(item).find('.image-wrap img'))
        )

        return Property(name, link, locality, price, images)
