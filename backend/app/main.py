
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.routers import crops, markets, prices, predictions

app = FastAPI(
    title="AgriTrade API",
    description="Backend API for the AgriTrade project",
    version="1.0.0"
)

# Allow requests from the Vue + Vite frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Existing API routers
app.include_router(crops.router)
app.include_router(markets.router)
app.include_router(prices.router)
app.include_router(predictions.router)


@app.get("/")
def root():
    return {
        "message": "AgriTrade API is running"
    }
