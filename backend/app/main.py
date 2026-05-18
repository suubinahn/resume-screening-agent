from fastapi import FastAPI, UploadFile, File, Form
from pydantic import BaseModel

from app.services.ai_service import analyze_resume
from app.services.pdf_service import extract_text_from_pdf

app = FastAPI()


class ResumeRequest(BaseModel):
    jd: str
    resume: str


@app.post("/analyze")
def analyze(data: ResumeRequest):

    result = analyze_resume(
        data.jd,
        data.resume
    )

    return result


@app.post("/analyze-pdf")
async def analyze_pdf(
    jd: str = Form(...),
    file: UploadFile = File(...)
):

    resume_text = extract_text_from_pdf(file.file)

    result = analyze_resume(
        jd,
        resume_text
    )

    return result