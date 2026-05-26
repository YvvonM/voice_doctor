# Voice Doctor

An AI-powered virtual doctor that you can **speak to** and that **talks back**. Describe your symptoms out loud, optionally share an image, and receive a spoken medical response — all through a simple browser interface.

> **Disclaimer:** This project is built for educational and learning purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for medical concerns.

---

## Features

- **Voice input** — speak your symptoms directly into your microphone
- **Image analysis** — upload a photo (e.g. a rash, wound, or scan) for visual diagnosis support
- **Voice output** — the doctor responds in a natural spoken voice via ElevenLabs TTS
- **AI-powered reasoning** — uses Groq's LLM API and vision capabilities for fast inference
- **Gradio web UI** — runs locally in your browser, no frontend setup needed

---

## How It Works

The app is composed of three main modules:

| Module | Description |
|---|---|
| `voice_of_the_patient.py` | Records audio from the microphone and transcribes it using Groq's Whisper API |
| `Brain_of_doc.py` | Encodes the uploaded image and sends it along with the transcribed query to the vision LLM for analysis |
| `voice_of_the_doc.py` | Converts the doctor's text response to speech using the ElevenLabs API |
| `app.py` | Ties everything together in a Gradio interface |

---

## Prerequisites

- Python 3.8+
- A [Groq API key](https://console.groq.com/)
- An [ElevenLabs API key](https://elevenlabs.io/)

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/YvvonM/voice_doctor.git
cd voice_doctor
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

> You may also need to install `gradio` separately if it's not already in your environment:
> ```bash
> pip install gradio
> ```

3. **Set up environment variables**

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
```

---

## Usage

Run the app with:

```bash
python app.py
```

This will launch a Gradio interface in your browser. From there:

1. Click the microphone icon and describe your symptoms
2. Optionally upload an image for visual analysis
3. Submit and receive the doctor's spoken and written response

---

## Project Structure

```
voice_doctor/
├── app.py                    # Main Gradio app
├── Brain_of_doc.py           # Image encoding and LLM vision analysis
├── voice_of_the_doc.py       # Text-to-speech via ElevenLabs
├── voice_of_the_patient.py   # Audio recording and speech-to-text via Groq
├── requirements.txt          # Python dependencies
└── .gitignore
```

---

## Dependencies

| Package | Purpose |
|---|---|
| `groq` | LLM and Whisper speech-to-text API |
| `elevenlabs` | Text-to-speech voice output |
| `gTTS` | Fallback text-to-speech (Google TTS) |
| `SpeechRecognition` | Audio input handling |
| `pydub` | Audio file processing |
| `python-dotenv` | Environment variable management |
| `gradio` | Web UI framework |

---

## License

This project is open source. Feel free to fork and build on it for learning purposes.
