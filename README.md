# GPT3 Youtube Short Creator
This tool automates the process of creating short videos by utilizing GPT3 for content creation. A Python script is used to request the OpenAI API with the configured prompt, which returns 12 historical facts about a specific day. The tool then takes this information and blends it into a background video and applies a music file, both of which are templates stored in a separate folder. Finally, all generated videos are saved in a dedicated folder.

Example [Youtube channel](https://www.youtube.com/channel/UC1CEqxquyFegNANRFQH-YmQ)
Example [Tiktok channel](https://www.tiktok.com/@historyfactstv)
## Motivation
The motivation behind it stems from the desire to save time and effort while still producing high-quality videos that capture the viewer's attention.
## Features
- Automated creation of short videos using GPT3
- Customizable settings (temperature, max_tokens, frequency_penalty, model choice)

## Installation:
To install the necessary packages and dependencies, run the following command in your terminal:

`pip install -r requirements.txt`
## Setup:
Before using this tool, there are a few requirements and installations that need to be made.
### Download Video and Music Templates:
Obtain video and music templates to use as the background and soundtrack for your videos. You can setup video and music folders in `config.py`
### API Access:
Rename `.env-example` to `.env` and paste OpenAI API. 

### ImageMagick:
This tool utilizes ImageMagick to generate the final videos. It is important to have ImageMagick installed on your machine in order to run the Python script. You can download ImageMagick from the official website.

### Python 3.10:
This tool is written in Python 3.10, so it is important to have the latest version of Python installed on your machine. You can download Python 3.10 from the official Python website.

## Usage:
1. Configure the `config.py`
2. Edit `prompts.txt` and paste there some dates line by line. 
3. Run the script: `python main.py`

## Generated Videos:
The script will send the prompt to the OpenAI API and receive a response with 12 history facts
The script will then generate a video by pasting the text onto a background video and applying a music file