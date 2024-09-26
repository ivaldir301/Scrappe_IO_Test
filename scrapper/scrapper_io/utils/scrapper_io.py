import httpx
from utils.logger import Logger
from selectolax.parser import HTMLParser    
from scrapper.models.laptop import Laptop
import os
from dotenv import load_dotenv

load_dotenv()

# Adding the headers and user-agent in the request so the website does not present suspesious behaviour
headers = {
     "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0"
}

async def get_url_html_data(target_url: str) -> str:
    Logger.info_logging(f"going to: {target_url}")

    async with httpx.AsyncClient():
        response = httpx.get(target_url, headers=headers)
        if response.status_code == 200:
            return response.text
    Logger.error_logging("was not possible no get website html data")
    return False

def get_next_pagination(next_pagination: str) -> str:
    url: str = os.getenv("WEBSCRAPPER_IO_BASE_URL")
    return url + next_pagination

def parse_data_from_url(data: str, list: Laptop) -> bool:
    html = HTMLParser(data)
    result_container = html.css("div.col-lg-9 div.row div.col-md-4")

    if result_container == []:
        return False    
    
    try:
        for product in result_container:
            laptop_data: Laptop = Laptop()

            try:
                laptop_data.price = product.css_first(".caption h4").text()
            except Exception as e:
                Logger.warning_logging(f"Coudn't find the price element: {e}")
                laptop_data.price = None

            try:
                laptop_data.name = product.css_first(".title").text()
            except Exception as e:
                Logger.warning_logging(f"Coudn't find name element: {e}")
                laptop_data.name = None

            try:
                attribut = product.css_first("a[href]")
                if attribut:
                    laptop_data.url = "webscraper.io" + attribut.attributes.get("href")
            except Exception as e:
                Logger.warning_logging(f"Coudn't get the link element: {e}")
                laptop_data.url = None

            try:
                laptop_data.description = product.css_first("p.description").text()
            except Exception as e:
                Logger.warning_logging(f"Coudn't find description element: {e}")
                laptop_data.description = None

            try:
                laptop_data.number_of_reviews = product.css_first("div.ratings p.review-count").text()
            except Exception as e:
                Logger.warning_logging(f"Coudn't find the reviews element: {e}")
                laptop_data.number_of_reviews = None

            list.append(laptop_data.to_dict())
    except Exception as e:
        Logger.error_logging(f"There was an issue pulling data from website: {e}")
        return list, False
    
    return list
    
def sort_data_by_price():
    pass