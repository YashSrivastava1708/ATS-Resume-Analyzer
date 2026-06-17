# from fastapi import FastAPI
from pypdf import PdfReader
from fastapi import FastAPI, UploadFile, File, Form

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


# for comparing against any job profile
#as of now, manually made, but will be extracted from the user when he uploads the JD


# JOB_SKILLS = [
#     "Python",
#     "React",
#     "FastAPI",
#     "Git",
#     "Docker",
#     "PostgreSQL",
#     "AWS"
# ]

#we will use helper function instead:::
def extract_skills_from_text(text: str):
    
    found = []

    text_lower = text.lower()

    for skill in SKILLS_DATABASE:

        if skill.lower() in text_lower:
            found.append(skill)

    return found



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

# @app.post("/upload-resume")
# async def upload_resume(file: UploadFile):

# more sturctured format with the help of forms:


@app.post("/upload-resume")
async def upload_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):

    content = await file.read()

    with open("temp_resume.pdf", "wb") as f:
        f.write(content)

    reader = PdfReader("temp_resume.pdf")

    extracted_text = ""

    for page in reader.pages:
        extracted_text += page.extract_text()

    
    # GOT REMOVED BECAUSE  NOW WE WILL COMPARE THE KEYWORDS FROM THE JD:
#     found_skills = []

#     resume_text_lower = extracted_text.lower()

#     for skill in SKILLS_DATABASE:
#         if skill.lower() in resume_text_lower:
#             found_skills.append(skill)
    
    
#     #comparision against a specific profile
#     matched_skills = []

#     for skill in JOB_SKILLS:

#         if skill in found_skills:
#             matched_skills.append(skill)
    
#     #missing skills:
#     missing_skills = []
#     for skill in JOB_SKILLS:
#         if skill not in found_skills:
#             missing_skills.append(skill)
#     # return {
#     #     "filename": file.filename,
#     #     "text": extracted_text[:1000]
#     # }
    
    
#     # calculations of new parameters with thus arrived values
    
#     ats_score = int(
#     (len(matched_skills) / len(JOB_SKILLS))
#     * 100
# )
    
    resume_skills = extract_skills_from_text(
        extracted_text
    )

    job_skills = extract_skills_from_text(
        job_description
    )

    matched_skills = []

    for skill in job_skills:

        if skill in resume_skills:
            matched_skills.append(skill)


    missing_skills = []

    for skill in job_skills:

        if skill not in resume_skills:
            missing_skills.append(skill)
            
    if len(job_skills) == 0:
        ats_score = 0
    else:
        ats_score = int(
            len(matched_skills)
            / len(job_skills)
            * 100
        )
        # updated return statements
    #     return {
    #     "filename": file.filename,
    #     "skills_found": found_skills,
    #     "total_skills_found": len(found_skills)
    # }
    
    
    
    #more updated statements:
    
    #     return {
    #     "filename": file.filename,
    #     "ats_score": ats_score,
    #     "matched_skills": matched_skills,
    #     "missing_skills": missing_skills
    # }

    # MUCH MORE UPDATED AND RICHER OUTPUT

    return {
        "filename": file.filename,
        "ats_score": ats_score,
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }