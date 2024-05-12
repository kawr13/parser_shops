import asyncio
import aiofiles
import json
import yaml


async def json_to_yml():
    async with aiofiles.open('data.json', 'r') as f:
        content = await f.read()
        data = json.loads(content)
        return yaml.dump(data, allow_unicode=True)
    

async def writeble_yml(data: yaml):
    async with aiofiles.open('data.yml', 'w', encoding='utf-8') as file:
        await file.write(data)
        
        
async def main():
    data: yaml = await json_to_yml()
    await writeble_yml(data)
    

if __name__ == '__main__':
    asyncio.run(main())