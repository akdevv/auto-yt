import os
import datetime
from utils.video_creator import create_video


def main():
    audio_path = "data/audio/react-hooks-tutorial.wav"
    video_path = "data/video/bg-video.mp4"

    try:
        video = create_video(audio_path, video_path)
        print(f"Video created successfully: {video}")
    except Exception as e:
        print(f"Error creating video: {e}")


if __name__ == "__main__":
    main()
