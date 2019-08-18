import asyncio
from pyppeteer.errors import TimeoutError

from scraper.helpers import log, elog
from scraper.config import scrapers
from scraper.handlers import handle_mongodb
from scraper import new_estates


async def scrape():
    log('Starting...')

    '''Scrape houses from various servers'''
    try:
        for scraper in scrapers:
            async for item in scraper.get_items():
                handle_mongodb(item, on_new_estate=new_estates.new_estates_add)
    except TimeoutError as e:
        elog("Caught exception: {}".format(str(e)))

    '''Process any newly discovered estates.'''
    new_estates.new_estates_handle()

    log('Finishing...')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(scrape())
