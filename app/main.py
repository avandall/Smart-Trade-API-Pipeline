from fastapi import FastAPI, UploadFile, File, HTTPException, BackgroundTasks
from app.api import upload, report
import shutil
import os
from app.core.processing import DataProcessor


app = FastAPI(title="Smart Trade API")

os.makedirs("data", exist_ok=True)
async def run_data_pipeline(file_path: str):
    
    try:
        processor = DataProcessor(file_path)
        result = processor.process()
        msg = f"✅ Xử lý xong! \nTổng thu: {result['summary']['total_income']} \nTổng chi: {result['summary']['total_expense']}"
        print(msg) # Log tạm thời
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if os.path.exists(file_path):  #xoa file sau khi xong
            os.remove(file_path)
    
@app.post("/upload-transaction/")
async def upload_csv(background_task : BackgroundTasks,file: UploadFile = File()):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a CSV file.")
    temp_path = f"data/raw_{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    background_task.add_task(run_data_pipeline, temp_path)
    return {
        "message": "File uploaded successfully. Processing will be done in the background.",
        "file_name": file.filename,
        "status": "Processing"
    }

@app.get("/")
def health_check():
    return {"message": "API is running!"}