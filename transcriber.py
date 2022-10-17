#!/usr/bin/env python3

from googletrans import Translator
import youtube_dl
import subprocess
import whisper
import getopt
import torch
import sys

audiofile = "audio.mp3" # Save audio file as audio.mp3

# Download mp3 audio of a Youtube video. Credit to Stokry
# https://dev.to/stokry/download-youtube-video-to-mp3-with-python-26p
def audio():
    url = None
    argv = sys.argv[1:]
    try:
        opts,args = getopt.getopt(argv, "u:",["url="])
    except :
        print("Usage: python3 transcriber.py -u <url>")

    for opt, arg in opts:
        if opt in ['-u', '--url']:
            url = arg

    video_info = youtube_dl.YoutubeDL().extract_info(url=url,download=False)
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':audiofile,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

# Check wether CUDA is available or not
def checkDevice():
    if (torch.cuda.is_available() == 1):
        DEVICE = "cuda"
    else:
        DEVICE = "cpu"
    return DEVICE

def main():
    audio() # Download an mp3 audio file to transcribe to text

	# Select speech recognition model
    name = input("Select speech recognition model name (tiny, base, small, medium, large): ")
    model = whisper.load_model(name,device=checkDevice())

    choice = input("Do you want to translate audio transcription to English? (Yes/No)")
    if (choice == "Yes"):
        # Save transcribed text to file
        result = model.transcribe(audiofile)
        with open('transcription.txt', 'a') as file:
            file.write(result["text"])
            file.write("\n")
    elif (choice == "No"):
        # Translate transcribed text. Credit to Harsh Jain at educative.io
        # https://www.educative.io/answers/how-do-you-translate-text-using-python
        transaltor = Translator() # Create an instance of Translator() class
        # Transcribe text from audio file, translate it to English and write it to translation.txt
        result = model.transcribe(audiofile)
        translation = translator.translate(result["text"])
        with open('translation.txt', 'a') as file:
            file.write(translation)
            file.write("\n")

if __name__ == "__main__":
    main()
