from fastapi import FastAPI, HTTPException
from scrapper.scrapper_io.main import WebScrapperIO
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/test", status_code=201)
def test():
    return "HELLO WORLD"

@app.get("/laptops", status_code=201)
async def get_laptops_sorted_by_price():
    result = await WebScrapperIO.scrappe()
    if result is not None or result is not []:
        return result
    else:
        raise HTTPException(status_code=500, detail="There was an error while processing the data") 