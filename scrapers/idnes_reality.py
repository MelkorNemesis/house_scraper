import unicodedata
from typing import AsyncGenerator
import pyppeteer
from scrapers.base import Base
from pyquery import PyQuery as pq
from property import Property


class IdnesReality(Base):
    PROPERTY_LIST_SELECTOR = '.c-list-products'
    PROPERTY_SELECTOR = '.c-list-products article.c-list-products__item'

    @property
    def host(self):
        return "https://reality.idnes.cz"

    async def get_items(self) -> AsyncGenerator[Property, None]:
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
        pagination = pq(html).find('.paginator a.paging__item')

        """
        reality.idnes.cz uses <span> for active pagination link
        so we add current path to the links right away because
        we can't get href attr from it (current page)
        """
        links = [self.path]
        links.extend([anchor.get('href') for anchor in pagination] if len(pagination) > 0 else [])

        return links

    def html_to_property(self, item):
        name = pq(item).find('.c-list-products__title').text()
        name = unicodedata.normalize('NFKD', name)

        # link
        link = pq(item).find('.c-list-products__link').attr('href')
        link = f'{self.host}{link}'

        # locality
        locality = pq(item).find('.c-list-products__info').text()

        # price
        price = pq(item).find('.c-list-products__price').text()
        price = unicodedata.normalize('NFKD', price)

        images = list(map(
            lambda img: img.get('src'),
            pq(item).find('.c-list-products__img img'))
        )

        return Property(name, link, locality, price, images)
