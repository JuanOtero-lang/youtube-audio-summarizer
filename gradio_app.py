
import os
from dotenv import load_dotenv
import gradio as gr
import yt_dlp
from transformers import pipeline
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
)


pipe = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-tiny.en",
    chunk_length_s=30,
)

def process_youtube_url_and_summarize(url: str):
    """
    Accepts: a Youtube video URL
    Returns: a summary of the audio from the Youtube video
    """

    if not (url.startswith("http") and ("youtube.com" in url or "youtu.be" in url)):
        return "Please enter a valid YouTube URL."

    try:
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": "%(title)s.%(ext)s",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
            }]
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info).rsplit(".", 1)[0] + ".wav"


    except Exception as e:
        return f"Something went wrong: {str(e)}"


    transcription = pipe(filename, batch_size=8)["text"]

    prompt = f"Please summarize the following text:\n\n{transcription}"

    response = client.responses.create(
        model = "gpt-4o",
        instructions = "You are a helpful assistant that summarizes text.",
        input = prompt,
    )

    summary = response.output_text

    return summary



iface = gr.Interface(
    fn=process_youtube_url_and_summarize,
    inputs=gr.Textbox(label="Enter a YouTube video URL"),
    outputs= gr.Textbox(
        label="Summary",
        lines=10,
    ),
    title="Youtube Audio Summary",
    description="Enter a Youtube video URL and get the summary from its audio."
)

iface.launch()

