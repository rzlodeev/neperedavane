from fastapi import FastAPI

from api.v1.homepage import router as homepage_router

app = FastAPI()
app.include_router(homepage_router, prefix="/api/v1/homepage", tags=["homepage"])

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
