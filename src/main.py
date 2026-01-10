from fastapi import FastAPI
from src.section.router import router as section_router


app = FastAPI(title="Redline V1")

app.include_router(section_router, prefix="/section")


@app.get("/")
async def root():
    return {
        "message": "Redline API running"
    }

