## Parser Shops

This is a Python async web scraper that extracts product information from the [grocenberg.online](https://grocenberg.online/) website.

### Features
- Asynchronous parsing of multiple product URLs
- Configuration loading from a JSON file for flexible selector handling
- Concurrent parsing using asyncio Semaphores
- Utilizes BeautifulSoup for HTML parsing and HTTPX for HTTP requests

### Prerequisites
- Python 3.7+
- aiofiles
- icecream
- BeautifulSoup4
- httpx

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your_username/parser_shops.git
   cd parser_shops
   ```
2. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Usage
1. Ensure your `config.json` file is properly configured with selectors for the desired product information.
2. Run the scraper using the provided scripts or integrate it into your own application.

### Example
```python
import asyncio
from parser_shops import parsing_url, parser_data

async def main():
    # Fetch URLs to parse
    urls = [
        'https://grocenberg.online/category/product-1',
        'https://grocenberg.online/category/product-2',
        'https://grocenberg.online/category/product-3',
    ]

    # Parse product URLs concurrently
    tasks = [parsing_url(url) for url in urls]
    parsed_urls = await asyncio.gather(*tasks)

    # Fetch and parse product data
    data_tasks = [parser_data(data) for data in parsed_urls]
    parsed_data = await asyncio.gather(*data_tasks)

    # Process parsed product data
    for product in parsed_data:
        print(product)

asyncio.run(main())
```

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgments
- Thank you to the developers of BeautifulSoup, httpx, aiofiles, and icecream for their excellent libraries.
- Special thanks to the contributors of this project.

### Contributions
Contributions are welcome! Please feel free to submit a pull request or open an issue with any improvements or suggestions.
