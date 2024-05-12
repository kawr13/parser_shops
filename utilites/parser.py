import asyncio
from typing import List
import aiofiles
from icecream import ic
from bs4 import BeautifulSoup as bs
import httpx
from utilites.connections_url import connection
from lxml import html
import json

semafor = asyncio.Semaphore(10)


async def config_load():
    async with aiofiles.open('config.json', 'r+', encoding='utf-8') as file:
        config = await file.read()
        return json.loads(config)
    

async def parsing_url(data: str) -> List[str]:
    url_list = []
    ic('Начало работы парсера')
    async with semafor:
    # https://grocenberg.online/   
        soup = bs(data, 'lxml')
        urls = soup.find_all('div', {'class': 'js-product-list-item item-line-c'})
        for item in urls:
            url = item.find('a', {'class': 'item-line-c__image'}).get('href')
            url_list.append('https://grocenberg.online' + url)
        return url_list


async def parser_data(data: str) -> List[dict]:
    ic('Начало работы парсера 2')
    # https://grocenberg.online/
    config = await config_load()
    product_dict = {}
    async with semafor:
        soup = bs(data, 'lxml')
        product_description_raw = soup.find('div', {'itemprop': 'description'})
        for key, selector in config['selectors'].items():
            element = soup.select_one(selector)
            if element:
                if key == 'images':
                    product_images = 'https://grocenberg.online' + element.get('src')
                    product_dict[key] = product_images
                else:
                    product_dict[key] = element.text
        if product_description_raw:
            product_description = product_description_raw.text
            product_dict['description'] = product_description
        return product_dict

    