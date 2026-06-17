# from fastapi import FastAPI
from fastapi import FastAPI, UploadFile
app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "ATS Resume Analyzer Backend Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/version")
def version():
    return {
        "version": "1.0.0"
    }

# @app.post("/upload-resume")
# async def upload_resume(file: UploadFile):

#     return {
#         "filename": file.filename,
#         "content_type": file.content_type
#     }

#more ehanced upload API:
@app.post("/upload-resume")
async def upload_resume(file: UploadFile):

    content = await file.read()

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size_in_bytes": len(content)
    }