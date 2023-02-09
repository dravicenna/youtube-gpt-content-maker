import os
import random
from typing import Tuple

import moviepy.editor as me
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip


class VideoGenerator:

    def __init__(
        self,
        video_folder: str = 'video',
        music_folder: str = 'music',
        duration: int = 8,
        size: Tuple[int, int] = (1080, 1920),
        channel_name: str = 'historyfactstv'

    ) -> None:
        self.video_folder = video_folder
        self.music_folder = music_folder
        self.video_list = os.listdir(video_folder)
        self.music_list = os.listdir(music_folder)
        self.duration = duration
        self.size = size
        self.channel_name = channel_name

    def _pick_random_file(self, file_list: list[str]) -> str:
        return random.choice(file_list)

    def make_audio(self):
        # Load the music file and set duration
        return me.AudioFileClip(f"./{self.music_folder}/{self._pick_random_file(self.music_list)}").set_duration(self.duration)  # NOQA

    def header(self, header_text):
        return me.TextClip(
            f'Facts about\n{header_text}',
            font='Helvetica-Bold',
            fontsize=85,
            color='white',
            method='label',
            stroke_color='black',
            stroke_width=1
        ).set_duration(self.duration).set_position(("center", 150))

    def content(self, text):
        return me.TextClip(
            text,
            font='Helvetica-Bold',
            fontsize=70,
            color='white',
            bg_color='black',
            method='caption',
            size=(self.size[0]*0.8, None),
            # stroke_color='black',
            # stroke_width=1
        ).set_duration(self.duration).set_position("center")

    def footer(self):
        return me.TextClip(
            f'@{self.channel_name}',
            font='Helvetica-Bold',
            fontsize=50,
            color='white',
            bg_color='black',
            method='label',
            # stroke_color='black',
            # stroke_width=1
        ).set_duration(self.duration).set_position(("center", self.size[1]*0.9))

    def make_video(self):
        # Load the video file
        return me.VideoFileClip(f"./{self.video_folder}/{self._pick_random_file(self.video_list)}").subclip(0, self.duration)  # NOQA

    def _make_main_clip(self, text, header_text) -> CompositeVideoClip:
        video = self.make_video()
        # Overlay the music on the video
        video = video.set_audio(self.make_audio())
        # Resize
        video = video.resize(self.size)
        # Create content text clips
        header = self.header(header_text)
        main_text = self.content(text)
        footer = self.footer()
        # Composing
        return me.CompositeVideoClip([video, header, main_text, footer]).set_duration(self.duration)

    def generate_video(self, text: str, header_text: str) -> CompositeVideoClip:
        return self._make_main_clip(text, header_text)
        # finalclip.write_videofile(f"1.mp4", temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac") # NOQA
