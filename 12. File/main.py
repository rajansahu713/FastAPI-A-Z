from fastapi import FastAPI, File, UploadFile, Form
from pathlib import Path
from typing import Union

app = FastAPI()


async def save_upload_file(upload_file: UploadFile, destination: Union[str, Path]) -> bool:
    try:
        destination_path = Path(destination)
        destination_path.parent.mkdir(parents=True, exist_ok=True)
        
        with destination_path.open("wb") as buffer:
            buffer.write(upload_file.file.read())
        
        return True
    except Exception as e:
        return False


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...), name: str = Form(...)):
    upload_folder = "upload"  # Replace this with your desired folder path
    file_saved = await save_upload_file(file, destination=f"{upload_folder}/{file.filename}")
    return {
        "filename": file.filename,
        "File Upload": file_saved
        }