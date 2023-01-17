from fastapi import FastAPI
from scraper import Scraper

app = FastAPI()
data = Scraper()


@app.get("/{laptops}")
async def read_item(laptops):
    return data.web_scraper_data(laptops)
