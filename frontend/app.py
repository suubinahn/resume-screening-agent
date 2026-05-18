import streamlit as st
import requests

st.title("AI Resume Screening Agent")

jd = st.text_area("채용 공고 입력")

uploaded_files = st.file_uploader(
    "이력서 PDF 업로드",
    type=["pdf"],
    accept_multiple_files=True
)

if st.button("분석 시작"):

    if uploaded_files:

        results = []

        for file in uploaded_files:

            files = {
                "file": file
            }

            data = {
                "jd": jd
            }

            response = requests.post(
                "https://resume-screening-agent-7d9z.onrender.com/analyze-pdf",
                files=files,
                data=data
            )

            result = response.json()

            if "score" in result:

                result["name"] = file.name

                results.append(result)

        # 점수 높은 순 정렬
        results.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        st.subheader("지원자 순위")

        for idx, result in enumerate(results):

            st.write(
                f"{idx+1}위 - {result['name']} ({result['score']}점)"
            )

            st.subheader("강점")
            for item in result["strengths"]:
                st.write("- ", item)

            st.subheader("보완점")
            for item in result["weaknesses"]:
                st.write("- ", item)

            st.subheader("이력서 기반 면접 질문")
            for q in result["questions"]:
                st.write("- ", q)

            st.divider()

    else:
        st.warning("PDF 파일을 업로드해주세요.")