from scrapers.base import Base
import asyncio


class SReality(Base):
    async def get_items(self):
        for i in range(3):
            await asyncio.sleep(0.5)
            yield i * 2
