import os
from datetime import datetime
from moviepy.editor import AudioFileClip, VideoFileClip, concatenate_videoclips

def generate_filename():
    now = datetime.now()
    return f"VID-{now.strftime('%d%m%Y-%H%M%S')}.mp4"


def create_video(audio_path, video_path, output_dir="output"):
    try:
        audio = AudioFileClip(audio_path)
        video = VideoFileClip(video_path)

        audio_duration = audio.duration
        video_duration = video.duration

        if video_duration > audio_duration:
            # Trim the video to the audio duration
            final_video = video.subclip(0, audio_duration)
        else:
            # Loop the video to match the audio duration
            loop_times = int(audio_duration // video_duration) + 1
            video_clips = [video] * loop_times

            # Concatenate the video clips
            concatenated_video = concatenate_videoclips(video_clips)
            final_video = concatenated_video.subclip(0, audio_duration)

        # Add audio to the video
        final_video = final_video.set_audio(audio)

        output_filename = generate_filename()
        output_path = os.path.join(output_dir, output_filename)

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        final_video.write_videofile(
            output_path, codec="libx264", audio_codec="aac")

        video.close()
        audio.close()
        final_video.close()

        return output_path
    except Exception as e:
        print(f"Error creating video: {e}")
        return None
