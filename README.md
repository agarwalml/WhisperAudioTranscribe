# Audio-transcriber
Simple Python audio transcriber using OpenAI's Whisper speech recognition model

Table of Contents
=================
* [Installation Instructions](#Installation-Instructions)

# Installation Instructions

1. Python version needs to be below 3.11

2. Install required packages with pip

`pip install -r requirements.txt`

2. Run a program with Python3

`python3 transcriber.py -u, --url <URL>`

3. pytube requires pip installation 

4. ffmpeg needs to be pip installed if not already present

5. in "LOCAL_PATH_TO/pytube/cipher.py",
Change this line:
411:     transform_plan_raw = find_object_from_startpoint(raw_code, match.span()[1] - 1)
to this:
152: transform_plan_raw = js

