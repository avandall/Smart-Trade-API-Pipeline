from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from app.core.processing import process_file

router = APIRouter()


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    result = process_file(content)
    return JSONResponse({"status": "ok", "result": result})
