import os

from slugify import slugify

import config
from utils.textgenerator import generate_text_list
from utils.videogenerator import VideoGenerator

if __name__ == "__main__":
    vg = VideoGenerator(
        video_folder=config.VIDEO,
        music_folder=config.MUSIC,
        duration=config.DURATION,
        size=config.SIZE
    )
    with open("prompts.txt", "r") as file:
        prompts = file.readlines()
        prompts = [line.strip() for line in prompts]

    for prompt in prompts:
        file_path = f'output/{prompt}'
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        # get list of facts on specific date
        while True:
            facts_list = generate_text_list(prompt)
            print(facts_list)
            answer = input('Generate videos with this text? (y/n) Or Ctrl+c to cancel: ')
            if answer in ['y', 'Y']:
                for text in facts_list:
                    print(f'About the text >> {text}')
                    file_name = slugify(text=text, max_length=60, word_boundary=True) + '.mp4'
                    video = vg.generate_video(text, prompt)
                    video.write_videofile(f'{file_path}/{file_name}', fps=config.FPS, preset="ultrafast", threads=4)
                break
