import os
import re
import streamlit as st
from transformers import pipeline
from datetime import datetime
import urllib.parse

# ---------------------------------------------------------
# Load Hugging Face Models (cached locally after first run)
# ---------------------------------------------------------
asr = pipeline("automatic-speech-recognition", model="openai/whisper-base")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# -------------------------------------------
#      Convert audio file to text (ASR)
# -------------------------------------------
def audio_to_text(audio_file):
    result = asr(audio_file)
    return result["text"]

# ----------------------------------------------
#       Clean filler words from transcript
# ----------------------------------------------
def clean_transcript(text):
    text = re.sub(r"\b(um+|ah+|like)\b", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

# -------------------------------------------------
#     Summarize transcript into concise minutes
# -------------------------------------------------
def summarize_transcript(text):
    summary = summarizer(text, max_length=200, min_length=50, do_sample=False)
    return summary[0]["summary_text"]

# ----------------------------------
#           Streamlit UI
# ----------------------------------
st.set_page_config(page_title="AI Meeting Minutes Generator")
st.title("AI Meeting Minutes Generator")
st.write("Upload a meeting audio file to get transcript + summarized minutes.")

#  Privacy & Disclaimer
with st.expander("Privacy & Security Notice"):
    st.markdown("""
    - Your meeting audio and transcripts are **not stored**.
    - Hugging Face models run locally after first download.
    """)

# Upload audio file
uploaded_file = st.file_uploader("Upload a meeting recording (MP3/WAV)", type=["mp3", "wav"])

if uploaded_file is not None:
    st.info("Processing with AI, please wait...")

    # Save uploaded file temporarily
    with open("temp_audio.mp3", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Step 1: Transcribe
    transcript = audio_to_text("temp_audio.mp3")
    clean_text = clean_transcript(transcript)

    # Step 2: Summarize
    summary = summarize_transcript(clean_text)

    # Step 3: Display Results
    st.subheader("Meeting Summary")
    st.write(summary)

    st.subheader("Full Transcript")
    st.write(clean_text)

    # Step 4: Email link (Full minutes in email body with bold headings)
    date_str = datetime.now().strftime("%Y-%m-%d")
    email_body = f"""Hi Team,%0D%0A%0D%0A
    Here are the meeting minutes from {date_str}:%0D%0A%0D%0A
    **Summary:**%0D%0A{summary}%0D%0A%0D%0A
    **Full Transcript:**%0D%0A{clean_text}%0D%0A%0D%0A
    Best,%0D%0AYour AI Assistant
    """
    email_body_encoded = urllib.parse.quote(email_body)

    st.markdown(
        f"[📧 Send via Email](mailto:?subject=Meeting Minutes {date_str}&body={email_body_encoded})"
    )

    # Step 5: Impact Metrics (ROI shown in UI only)
    st.subheader("📊 Impact Metrics (Estimated ROI)")
    st.write("""
    - **Estimated hours saved per meeting:** 2 hours  
    - **Cost savings per meeting:** $100  
    - **Productivity boost:** Faster note-taking and better follow-ups  
    """)

    st.success("Meeting Minutes generated successfully!")

# Cleanup temp files
if os.path.exists("temp_audio.mp3"):
    os.remove("temp_audio.mp3")
