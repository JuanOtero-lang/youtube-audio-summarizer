# YouTube Audio Summarizer

A Gradio interface that allows users to submit a YouTube video URL and outputs a summarized version of the video’s audio content.  
The app automatically extracts the audio, transcribes it with a Hugging Face Whisper model, and summarizes the transcription using GPT-4o.

---

## Pipeline Overview

```mermaid
flowchart LR
    A[YouTube URL] --> B[yt-dlp: Extract Audio]
    B --> C[OpenAI Whisper ASR: Transcribe Audio]
    C --> D[GPT-4o: Summarize Transcription]
    D --> E[Summarized Text Output]

``` 

## Installation 

  ### 1. Clone the repository
      git clone https://github.com/JuanOtero-lang/youtube-audio-summarizer.git
      cd youtube-audio-summarizer

  ### 2. Install dependencies
      pip install -r requirements.txt

  ### 3. Set up your .env file with your OpenAI API key
      OPENAI_API_KEY=your_openai_api_key

## Usage

  #### Run the Gradio app
    python gradio_app.py

  #### 1. Enter a YouTube URL in the textbox
  #### 2. Wait for the audio to be processed
  #### 3. The summary will appear in the textbox below





