from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import pathlib

from app.api.v1.homepage import router as homepage_router

app = FastAPI()
app.include_router(homepage_router, prefix="/api/v1/homepage", tags=["homepage"])

# Connect React.js frontend
build_path = pathlib.Path(__file__).parent.parent / "build"

app.mount("/static", StaticFiles(directory=build_path / "static", html=True), name="static")
app.mount("/", StaticFiles(directory=build_path, html=True), name="root_static")

@app.get("/", response_class=HTMLResponse)
async def root():
    index_file = build_path / "index.html"
    return index_file.read_text(encoding="utf-8")

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)