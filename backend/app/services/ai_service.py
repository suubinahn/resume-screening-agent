import os
import json

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def analyze_resume(jd, resume):

    prompt = f"""
    [채용 공고]
    {jd}

    [이력서]
    {resume}

    평가 기준:

    1. 기술 스택 일치도 (40점)
    2. 프로젝트 경험 (30점)
    3. 협업 경험 (20점)
    4. 우대사항 충족 여부 (10점)

    총점 100점 기준으로 평가하세요.

    아래 JSON 형식으로만 응답하세요.

    {{
      "score": 0,
      "detail_scores": {{
        "skills": 0,
        "projects": 0,
        "collaboration": 0,
        "bonus": 0
      }},
      "strengths": [],
      "weaknesses": [],
      "questions": []
    }}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": """
                당신은 채용 분석 AI입니다.

                반드시 모든 응답은 한국어로 작성하세요.
                
                반드시 JSON 형식으로만 응답하세요.

                적합도 점수(score)는 반드시 0~100 사이의 정수로 반환하세요.

                점수 기준:
                - 매우 적합: 85~100
                - 보통 적합: 60~84
                - 부적합: 0~59

                세부 점수 기준:
                - skills: 기술 스택 일치도 (40점)
                - projects: 프로젝트 경험 (30점)
                - collaboration: 협업 경험 (20점)
                - bonus: 우대사항 충족 여부 (10점)

                아래 형식을 정확히 지키세요.

                {
                  "score": 0,
                  "detail_scores": {
                    "skills": 0,
                    "projects": 0,
                    "collaboration": 0,
                    "bonus": 0
                  },
                  "strengths": [],
                  "weaknesses": [],
                  "questions": []
                }
                """
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    result = response.choices[0].message.content

    print("GPT 응답:")
    print(result)

    try:
        return json.loads(result)

    except Exception as e:
        print("JSON 파싱 오류:", e)

        return {
            "score": 0,
            "detail_scores": {
                "skills": 0,
                "projects": 0,
                "collaboration": 0,
                "bonus": 0
            },
            "strengths": [],
            "weaknesses": ["JSON 파싱 실패"],
            "questions": []
        }