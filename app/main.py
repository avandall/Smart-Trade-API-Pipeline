from fastapi import FastAPI
from app.api import upload, report

app = FastAPI(title="Smart Trade API")

app.include_router(upload.router, prefix="/api")
app.include_router(report.router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Smart Trade API"}
