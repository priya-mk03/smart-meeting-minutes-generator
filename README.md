# AI Meeting Minutes Generator

AI Meeting Minutes Generator is a Streamlit-based web application that uses speech-to-text and natural language processing to automatically generate clear, concise meeting summaries. It supports audio uploads (MP3/WAV) and produces structured minutes that can be directly emailed to your team.

## Features

- Upload and process meeting audio in `.mp3` or `.wav` formats.
- Automatic transcription of speech to text using Whisper.
- Clean, filler-free transcripts.
- Summarized meeting minutes using BART Large CNN.
- Impact metrics to show productivity gains:
  - Estimated hours saved
  - Cost savings
- One-click option to send minutes via email.
- User-friendly Streamlit interface.

## How It Works

1. Upload a meeting recording.
2. The audio is transcribed into text using Whisper.
3. The transcript is cleaned and summarized with BART.
4. Minutes and metrics are displayed in the Streamlit UI.
5. Optionally, send the generated minutes directly to your team by email.

## Setup

1. Clone the repository:
 ```bash
 git clone https://github.com/your-username/ai-meeting-minutes-generator.git
 cd ai-meeting-minutes-generator

2.  Create a virtual environment
 ```bash
 python -m venv venv
 ```

Activate the environment:
  
  **Windows (PowerShell):**
  ```bash
  venv\Scripts\activate
  ```
  **Mac/Linux:**
  ```bash
  source venv/bin/activate
  ```

3. Install dependencies
```bash
 pip install -r requirements.txt
 ```

4. Configure your email credentials in environment variables or a `.env` file:
 ```bash
 EMAIL_ADDRESS=your_email@example.com
 EMAIL_PASSWORD=your_app_password
 ```

5. Run the app:
 ```bash
 streamlit run app.py
 ```

## Privacy & Security

- Uploaded audio files are processed temporarily and deleted after use.
- No files are stored or shared outside the application.
- Email integration requires secure app passwords (recommended for Gmail).
- Sensitive information should not be shared in uploaded audio files.

## Tech Stack

- Frontend/UI: Streamlit
- Backend: Python
- ASR (Automatic Speech Recognition): Whisper
- Summarization: BART Large CNN (Hugging Face Transformers)

## File Structure
```bash
ai-meeting-minutes-generator/
├── app.py                # Main Streamlit app
├── requirements.txt      # Python dependencies
├── .gitignore            # Git ignore file
├── .env                  # Email credentials (excluded from Git)
└── README.md             # Project documentation
```

## License
This project is open source and available under the MIT License.

## Author
Ambika Narayanan






    

