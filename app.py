import streamlit as st
import requests
import PyPDF2

st.set_page_config(
    page_title="AI Job Application Assistant",
    page_icon="💼",
    layout="centered"
)

st.title("💼 AI Job Application Assistant")
st.caption("AI-powered Resume & Job Matching System")

st.subheader("📄 Upload Resume")

resume = st.file_uploader(
    "Choose your resume PDF",
    type=["pdf"]
)


st.subheader("💼 Job Description")

job_description = st.text_area(
    "Paste the job description below",
    height=250,
    placeholder="Paste the complete job description here..."
)

if st.button("🔍 Analyze Job", use_container_width=True):
    if resume is None:
        st.warning("Please upload your resume.")

    elif not job_description:
        st.warning("Please enter the job description.")

    else:
        # Read PDF
        pdf_reader = PyPDF2.PdfReader(resume)

        resume_text = ""

        for page in pdf_reader.pages:
            text = page.extract_text()

            if text:
                resume_text += text + "\n"

        # n8n Webhook
        webhook_url = "https://yadavritu7022.app.n8n.cloud/webhook/5de969cb-703e-4e14-9d0d-f0a27a658968"

        # Send TEXT instead of PDF binary
        data = {
            "resume_text": resume_text,
            "job_description": job_description
        }

        response = requests.post(
            webhook_url,
            json=data
        )

        st.write("Status:", response.status_code)

        if response.status_code == 200:
            result = response.json()

            if "output" in result:
                st.markdown(result["output"])
            else:
                st.json(result)
        else:
            st.error(f"Error {response.status_code}")
            st.write(response.text)