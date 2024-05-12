import httpx
import os
from icecream import ic
import asyncio
from typing import List

cookies = {
    'landing': '%2F',
    'PHPSESSID': '0e93255cc6e2e15a19a2c5ead303ffee',
    '_ym_uid': '1715264530591878418',
    '_ym_d': '1715264530',
    '_ym_isad': '1',
    '_theme_products_view_mode': 'compact',
    'products_per_page': '150',
    'balance_viewed': '1355%2C1491%2C1663',
    '_ym_visorc': 'w',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'landing=%2F; PHPSESSID=0e93255cc6e2e15a19a2c5ead303ffee; _ym_uid=1715264530591878418; _ym_d=1715264530; _ym_isad=1; _theme_products_view_mode=compact; products_per_page=150; balance_viewed=1355%2C1491%2C1663; _ym_visorc=w',
    'dnt': '1',
    'priority': 'u=0, i',
    'referer': 'https://grocenberg.online/category/dushevye-sistemy/',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

data = {
    
}

async def connection(client: httpx.AsyncClient, url: str=None):
    count_ = 0
    while count_ != 10:
        try:
            response = await client.get(url, cookies=cookies, headers=headers)
            ic(f'Выполнение конкуренции: {response.status_code}')
            return response
        except httpx.ReadError:
            ic('Соединение было разорвано. Повторная попытка через 5 секунд')
            count_ += 1
            await asyncio.sleep(5)
        except httpx.ReadTimeout:
            ic('Соединение было разорвано. Повторная попытка через 5 секунд')
            count_ += 1
            await asyncio.sleep(5)

            


async def main():
    async with httpx.AsyncClient() as client:
        await connection(client, 'https://grocenberg.online/category/smesiteli/')
        

if __name__ in '__main__':
    asyncio.run(main())