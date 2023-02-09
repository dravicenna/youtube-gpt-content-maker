import os

import config
from textgenerator import generate_text_list
from videogenerator import VideoGenerator

if __name__ == "__main__":
    vg = VideoGenerator(
        video_folder=config.VIDEO,
        music_folder=config.MUSIC,
        duration=config.DURATION,
        size=config.SIZE
    )
    with open("prompts.txt", "r") as file:
        dates = file.readlines()
        dates = [line.strip() for line in dates]

    for date in dates:
        file_path = f'output/{date}'
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        # get list of facts on specific date
        facts_list = generate_text_list(date)
        for index, text in enumerate(facts_list):
            print(f'About the text >> {text}')
            file_name = f"{date}_{str(index+1)}.mp4"
            video = vg.generate_video(text, date)
            video.write_videofile(f'{file_path}/{file_name}', fps=config.FPS, preset="ultrafast")
