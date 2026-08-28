from fastapi import FastAPI

from backend.app.routers import crops, markets, prices


app = FastAPI(
    title="AgriTrade API",
    description="Backend API for the AgriTrade project",
    version="1.0.0"
)


app.include_router(crops.router)
app.include_router(markets.router)
app.include_router(prices.router)

@app.get("/")
def root():
    return {
        "message": "AgriTrade API is running"
    }