from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "ATS Resume Analyzer Backend Running"
    }
    