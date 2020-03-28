import csv
import aiohttp
import asyncio
import aiofiles
import nest_asyncio

from src.sources import data_sources
from src.utils import LOG, clean_text
from src.config import *

nest_asyncio.apply()


class SemaphoreController:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not SemaphoreController._instance:
            SemaphoreController._instance = super(SemaphoreController, cls).__new__(cls, *args, **kwargs)
        return SemaphoreController._instance

    def __init__(self):
        self._semaphore = asyncio.Semaphore(value=SEMAPHORE_LIMIT)

    async def get_semaphore(self):
        await self._semaphore.acquire()

    def release_semaphore(self):
        self._semaphore.release()


async def fetch(entry, session, semaphore, verbose=VERBOSE):
    # Get semaphore
    await semaphore.get_semaphore()

    if verbose > 2:
        LOG.info("Successfully acquired the semaphore")

    counter = 0
    while counter < QUERY_RETRY_LIMIT:
        try:
            async with session.get(entry['url'], timeout=10, headers=HEADERS) as response:
                data = await response.text()
            if data:
                semaphore.release_semaphore()
                return data
            else:
                await asyncio.sleep(SEMAPHORE_WAIT)

        except Exception as e:
            LOG.error(f"Error retrieving {entry['url']}: {e}")
            await asyncio.sleep(SEMAPHORE_WAIT)

    semaphore.release_semaphore()
    return None


async def write_file(data, name, clean=False):
    file_ref = DATA_FOLDER.joinpath(name)

    async with aiofiles.open(file_ref.as_posix(), mode="w") as file_obj:
        if isinstance(data, list):
            with csv.writer(file_obj, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL) as writer:
                for r in data:
                    await writer.writerow(r)
        elif isinstance(data, str):
            if clean:
                data = clean_text(data)
            await file_obj.write(data)


async def update_sources(semaphore):
    async with aiohttp.ClientSession() as session:
        for country, array in data_sources.items():
            LOG.info(f"Processing country: {country}")
            for val in array:
                if val['type'] == 'csv':
                    res = await fetch(val, session, semaphore)
                    if res:
                        await write_file(res, f"{val['output']}.csv", clean=not val['isClean'])


def update_data_sources():
    semaphore = SemaphoreController()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(update_sources(semaphore))


if __name__ == '__main__':
    update_data_sources()
