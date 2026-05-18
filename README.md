# Resume Screening Agent

본 프로젝트는 개인적으로 수행한 생성형 AI 기반 이력서 분석 및 면접 보조 미니 프로젝트입니다.

채용 공고(JD)와 지원자의 이력서를 기반으로 적합도를 분석하고, 강점/보완점 및 예상 면접 질문을 자동 생성하는 AI Resume Screening Agent를 구현하였습니다.

사용자는 여러 지원자의 PDF 이력서를 업로드할 수 있으며, 시스템은 OpenAI API를 활용하여 지원자별 적합도를 분석하고 점수 기반 순위를 제공합니다.

---

## 프로젝트 소개

본 프로젝트는 이력서 검토 및 면접 준비 과정을 보조하기 위해 제작한 생성형 AI 기반 Resume Screening Agent입니다.

채용 공고와 지원자의 이력서를 비교 분석하여 적합도를 평가하고, 강점/보완점 및 예상 면접 질문을 자동 생성할 수 있도록 구현하였습니다.

또한 PDF 이력서 업로드 기능과 다중 지원자 비교 기능을 통해 실제 채용 프로세스와 유사한 흐름으로 구성하였습니다.

---

## 주요 기능

### AI 기반 이력서 분석
- 채용 공고(JD)와 이력서 간 적합도 분석
- 100점 기준 적합도 점수 생성
- 강점 및 보완점 자동 추출

### 예상 면접 질문 생성
- 지원자의 경험 및 부족한 부분 기반 면접 질문 자동 생성

### PDF 이력서 업로드
- PDF 파일 업로드 및 텍스트 자동 추출
- 다중 지원자 이력서 처리 가능

### 지원자 비교 및 순위화
- 여러 지원자의 분석 결과 비교
- 점수 기반 자동 정렬 및 순위 제공

### 구조화된 평가 기준
- 기술 스택
- 프로젝트 경험
- 협업 경험
- 우대사항 충족 여부

기준으로 세부 점수 계산

---

## 기술 스택

### Backend
- FastAPI
- OpenAI API
- Python
- Pydantic
- PyPDF

### Frontend
- Streamlit

### Deployment
- Render
- Streamlit Community Cloud

### Collaboration
- GitHub

---

## 프로젝트 구조

```text
agent/
├── backend/
│   ├── app/
│   │   ├── services/
│   │   │   ├── ai_service.py
│   │   │   └── pdf_service.py
│   │   ├── prompts.py
│   │   └── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── app.py
│   └── requirements.txt
│
└── .gitignore
```

---

## 시스템 아키텍처

```text
사용자
   ↓
Streamlit UI
   ↓
FastAPI Server
   ↓
OpenAI API
```

---

## 실행 방법

### Backend 실행

```bash
cd backend

.\venv\Scripts\Activate

uvicorn app.main:app --reload --port 8001
```

---

### Frontend 실행

```bash
cd frontend

streamlit run app.py
```

---

## 배포 링크
https://resume-screening-agent-kwncyukmstsnbf7eygtx9w.streamlit.app/

---

## 주요 구현 포인트

- FastAPI 기반 AI API 서버 구현
- Streamlit 기반 채용 운영 UI 개발
- OpenAI API 활용 생성형 AI 분석 기능 구현
- PDF 이력서 자동 처리 기능 구현
- 다중 지원자 비교 및 점수 기반 순위화 구현
- JSON 기반 응답 구조 설계
- Prompt Engineering 기반 평가 기준 구조화

---

## 트러블슈팅

### FastAPI 포트 충돌 문제
기존 로컬 서버와 포트 충돌이 발생하여 FastAPI 서버 포트를 변경하여 해결하였습니다.

### OpenAI 응답 JSON 파싱 문제
응답 형식을 JSON으로 제한하고 response_format을 적용하여 해결하였습니다.

### Render 배포 오류
requirements.txt 누락으로 uvicorn 설치 실패 문제가 발생하였으며, pip freeze를 통해 해결하였습니다.

---

## 향후 개선 사항

- 면접 답변 평가 기능 추가
- RAG 기반 사내 질문 데이터 연동
- 벡터DB 기반 검색 기능 추가
- 관리자 대시보드 구현
- 지원자 히스토리 저장 기능 추가
