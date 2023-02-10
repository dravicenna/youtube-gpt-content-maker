# GPT3 TikTok and Youtube Shorts Video Creator
This tool automates the process of creating shorts videos by utilizing GPT3 for content creation. A Python script is used to request the OpenAI API with the configured prompt, which returns 12 historical facts about a specific day. The tool then takes this information and blends it into a background video and applies a music file, both of which are templates stored in a separate folder. Finally, all generated videos are saved in a dedicated folder.

Example [Youtube channel](https://www.youtube.com/channel/UC1CEqxquyFegNANRFQH-YmQ)

Example [Tiktok channel](https://www.tiktok.com/@historyfactstv)

## Motivation
The motivation behind it stems from the desire to save time and effort while still producing high-quality videos that capture the viewer's attention.
## Features
- Automated creation of short videos using GPT3
- Customizable settings (temperature, max_tokens, frequency_penalty, model choice)

## Installation:

To install the necessary packages and dependencies, run the following next steps:
- Clone the repository:

`git clone https://github.com/dravicenna/youtube-gpt-content-maker`

- Create a virtual environment:

`python3.9 -m venv venv`

- Activate the virtual environment:

`source venv/bin/activate`

- Install the required packages:

`python -m pip install -r requirements.txt`

### Moviepy and ImageMagick:
This tool utilizes Moviepy and ImageMagick to generate the final videos. It is important to have ImageMagick installed on your machine in order to run the Python script. You can download ImageMagick from the official website.

With these steps, you should have successfully set up the repository and environment for the youtube-gpt-content-maker script.

## Project Setup:
Before using this tool, there are a few requirements and installations that need to be made.

### Download Video and Music Templates:
Obtain video and music templates to use as the background and soundtrack for your videos. You can setup video and music folders in `config.py`

### API Access:
Rename `.env-example` to `.env` and paste OpenAI API. 

## Usage:
1. Configure the `config.py`
2. Edit `prompts.txt` and paste there some dates line by line. 
3. Run the script: `python main.py`
