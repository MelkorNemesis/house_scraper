from pprint import pprint
import asyncio
from config import scrapers


async def main():
    pprint('Running...')

    for scraper in scrapers:
        async for item in scraper.get_items():
            pprint(item)

    pprint('Stopping...')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
