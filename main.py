import asyncio
import time
from typing import List
from icecream import ic
from bs4 import BeautifulSoup as bs
import httpx
from utilites.connections_url import connection
from utilites.parser import config_load, parser_data, parsing_url
import aiofiles
import json


semafor = asyncio.Semaphore(5)

timeout = httpx.Timeout(10.0, read=30.0)


async def search_url(client: httpx.AsyncClient, url: str):
    async with semafor:
        response = await connection(client, url)
        await asyncio.sleep(0.5)
        return response.text


async def write(data: List[dict]):
    async with aiofiles.open('data.json', 'w', encoding='utf-8') as file:
        await file.write(json.dumps(data, ensure_ascii=False))


async def command_post(client: httpx.AsyncClient, categories: list[str]):
    task = [asyncio.create_task(search_url(client, 'https://grocenberg.online/category/' + category + '/')) for category in categories]
    result = await asyncio.gather(*task, return_exceptions=False)
    tasks = [asyncio.create_task(parsing_url(res)) for res in result]
    urls = await asyncio.gather(*tasks, return_exceptions=False)
    tasks2 = [asyncio.create_task(search_url(client, url)) for items in urls for url in items]
    data_sites = await asyncio.gather(*tasks2, return_exceptions=False)
    tasks3 = [asyncio.create_task(parser_data(res)) for res in data_sites]
    product_data = await asyncio.gather(*tasks3, return_exceptions=False)
    await write(product_data)


async def main():
    
    category_lst = await config_load()
    async with httpx.AsyncClient(timeout=timeout) as client:
        await command_post(client, category_lst['categoryes'])



if __name__ in '__main__':
    asyncio.run(main())
    
    
