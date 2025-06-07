
# 🧠 Agent Assist – Real-Time AI Sales Assistant

Agent Assist is an AI-driven real-time support tool designed for sales agents during live calls. By analyzing ongoing call audio and referencing a customizable knowledge base, the assistant provides concise, high-impact suggestions to boost sales effectiveness and pitch quality.

## 🚀 Features

- 🔊 Upload sales call recordings (MP3/M4A/WAV)
- ⏱️ Automatically splits audio into timed segments (with overlap)
- 🧠 Uses Google Gemini API (2.5 Flash) to:
  - Summarize recent conversation
  - Suggest contextual pitch ideas and objection handlers
- 📚 Accepts custom knowledge bases or provides a sample
- 🌊 Stylish live suggestion display with animated UI
- 📈 Designed for real-time refresh and seamless user experience

---

## 🛠️ Project Structure

```
.
├── streamlit_app.py          # Main Streamlit frontend
├── audioManipulations.py     # Audio splitting, duration calc, and encoding
├── getSuggestions.py         # Gemini API call and prompt management
├── getWaves.py               # UI: Wave animation + suggestion rendering
├── samples.py                # Sample knowledge base + sample audio download
├── requirements.txt          # Python dependencies
├── packages.txt              # System-level requirements
└── AUDIO-2025-03-02.mp3      # Sample audio (used in samples.py)
```

---

## 🔧 Installation

### 1. Clone the repository

```bash
git clone https://your-repo-url
cd your-repo
```

### 2. Set up a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Install system dependencies

```bash
# FFmpeg is required for audio processing
sudo apt-get install ffmpeg   # For Linux
brew install ffmpeg           # For macOS
```

---

## 🔐 Setup Environment Variables

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_api_key_1
GEMINI_API_KEY_2=your_api_key_2
...
GEMINI_API_KEY_8=your_api_key_8
```

---

## ▶️ Running the App

```bash
streamlit run streamlit_app.py
```

---

## 🧪 Try With a Sample

If you don’t have a call/audio file, just select **“No, I need a sample”** on the sidebar to use demo data and knowledge base.

---

## 📚 Custom Knowledge Base Format

Your knowledge base should include:

- Plan details
- Eligibility criteria
- Objection handling tactics
- Unique selling points
- Claims process
- FAQs or regional information

The AI uses this knowledge to generate contextual pitch ideas.

---

## 🧠 How it Works

1. Upload a call audio.
2. Enter the product/company knowledge base.
3. App splits the audio every 45 seconds with overlap.
4. AI listens to the latest segment + entire transcript + KB.
5. Returns a **summary of the latest segment** and new **one-liner sales suggestions**.
6. Suggestions display as blocks in real-time.

---

## 📦 Dependencies

From `requirements.txt`:
- `streamlit`
- `pydub`
- `requests`
- `dotenv`

From `packages.txt`:
- `ffmpeg`

---
