from dotenv import load_dotenv
from scrapper.scrapper_io.utils.scrapper_io import get_url_html_data, parse_data_from_url, get_next_pagination, sort_data_by_price

headers = {
     "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0"
}

load_dotenv

class WebScrapperIO():
    @staticmethod
    async def scrappe():
        counter: int = 1
        new_url = get_next_pagination(str(counter))
        list_of_laptops = []

        html_data: str = await get_url_html_data(new_url)
        result = parse_data_from_url(html_data, list_of_laptops)

        while True:
            new_url = get_next_pagination(str(counter))
            html_data = await get_url_html_data(new_url)

            if parse_data_from_url(html_data, list_of_laptops) is False:
                list_of_laptops = result
                return sort_data_by_price(result)
            result = parse_data_from_url(html_data, list_of_laptops)
            counter += 1    

     

