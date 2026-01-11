from fastapi import FastAPI
from src.section.router import router as section_router


app = FastAPI(title="Redline")

app.include_router(section_router, prefix="/section", tags=["section"])


@app.get("/")
async def root():
    return {
        "message": "Redline API running"
    }

