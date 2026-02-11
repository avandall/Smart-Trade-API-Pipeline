from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from app.core.processing import DataProcessor

router = APIRouter()


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    processor = DataProcessor(file.filename)
    result = processor.process()
    return JSONResponse({"status": "ok", "result": result})
