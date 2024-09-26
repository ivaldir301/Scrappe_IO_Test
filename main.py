from utils.logger import Logger
from scrapper.scrapper_io.main import WebScrapperIO
import asyncio

async def main():
    Logger.info_logging("Project is being runned.")
    print(await WebScrapperIO.scrappe())

if __name__ == "__main__":
    asyncio.run(main())