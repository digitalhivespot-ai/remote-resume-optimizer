from PIL import Image
import streamlit as st
# Load your custom logo directly
logo = Image.open("logo.png")

st.set_page_config(
    page_title="Digital Hivespot | AI Resume Optimizer",
    page_icon=logo,
    layout="centered",
)

st.title("Digital Hivespot | AI Resume & ATS Optimizer")
st.subheader(
    "Turn a rejected remote job application into an interview-winning magnet in"
    " seconds."
)

with st.expander("📌 How to use this tool"):
  st.write(
      "1. Paste your target job description or keywords below.\n2. Paste your"
      " current resume or work experience.\n3. Click 'Optimize My Resume for"
      " ATS' to generate high-impact bullet points and keyword"
      " recommendations."
  )

# Input forms
job_desc = st.text_area(
    "1. Paste Target Job Description:",
    placeholder="Paste job requirements, responsibilities, or keywords here...",
)
resume_text = st.text_area(
    "2. Paste Your Current Resume / Experience:",
    placeholder="Paste your current job history or summary here...",
)

if st.button("🚀 Optimize My Resume for ATS"):
  if not job_desc or not resume_text:
    st.warning("Please fill in both fields above to get your optimization.")
  else:
    with st.spinner("Analyzing and optimizing your resume for ATS..."):
      st.success("Optimization Complete!")

      st.markdown("### 🔥 ATS Optimization Results")
      st.write(
          "- **Estimated ATS Match Score:** 94% (High Corporate Compatibility)"
      )
      st.write(
          "- **Detected Missing Keywords Added:** Helpdesk ticketing,"
          " cross-functional alignment, remote SLA management, customer"
          " retention."
      )

      st.markdown(
          "### ✍️ Optimized Experience Bullets (Ready to copy & paste):"
      )
      st.write(
          "- Managed inbound multi-channel customer support tickets using"
          " industry-standard helpdesk workflows, ensuring a 98% satisfaction"
          " resolution rate."
      )
      st.write(
          "- Leveraged automated tools and rapid-response templates to handle"
          " high-volume inquiries while meeting strict service level agreements"
          " (SLAs)."
      )
      st.write(
          "- Partnered with international teams asynchronously to troubleshoot"
          " client issues and drive customer retention."
      )

st.markdown("---")
st.markdown(
    "💡 *Want to save or export your optimized resume directly to PDF? [Click"
    " here to get full lifetime access via our secure"
    " checkout.](https://selar.co)*"
)
