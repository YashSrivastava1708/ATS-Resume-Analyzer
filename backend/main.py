# from fastapi import FastAPI
from pypdf import PdfReader
from fastapi import FastAPI, UploadFile



# skill dataset
SKILLS_DATABASE = [
    "Python",
    "Java",
    "C++",
    "JavaScript",
    "TypeScript",
    "React",
    "Next.js",
    "Node.js",
    "FastAPI",
    "Docker",
    "Kubernetes",
    "AWS",
    "PostgreSQL",
    "MongoDB",
    "Git",
    "GitHub",
    "Linux",
    "HTML",
    "CSS",
    "Tailwind CSS"
]





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


# @app.post("/upload-resume")
# async def upload_resume(file: UploadFile):

#     content = await file.read()

#     return {
#         "filename": file.filename,
#         "content_type": file.content_type,
#         "size_in_bytes": len(content)
#     }



# upload resume api with pdf reading feature

@app.post("/upload-resume")
async def upload_resume(file: UploadFile):

    content = await file.read()

    with open("temp_resume.pdf", "wb") as f:
        f.write(content)

    reader = PdfReader("temp_resume.pdf")

    extracted_text = ""

    for page in reader.pages:
        extracted_text += page.extract_text()

    
    
    found_skills = []

    resume_text_lower = extracted_text.lower()

    for skill in SKILLS_DATABASE:
        if skill.lower() in resume_text_lower:
            found_skills.append(skill)
    # return {
    #     "filename": file.filename,
    #     "text": extracted_text[:1000]
    # }
    
    
    # updated return statements
    
    
    return {
    "filename": file.filename,
    "skills_found": found_skills,
    "total_skills_found": len(found_skills)
}
   