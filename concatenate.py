import os
import subprocess


def concatenate_videos(video_paths, output_path):
    # Create a temporary file to list all the video paths
    with open("temp.txt", "w") as f:
        for path in video_paths:
            f.write(f"file '{path}'\n")

    # Use ffmpeg to concatenate the videos
    command = [
        "ffmpeg",
        "-f", "concat",
        "-safe", "0",
        "-i", "temp.txt",
        "-c", "copy",
        output_path
    ]
    subprocess.run(command)

    # Remove the temporary file
    os.remove("temp.txt")


def extract_and_combine_videos(root_directory):
    # Define the path to the subdirectory
    video_subdir = os.path.join(root_directory, "/Users/alexwang/men-be-nice/GPT3.5Trial1/videos")

    # Recursively get a list of all mp4 files in the subdirectory
    videos = [os.path.join(dirpath, filename)
              for dirpath, dirnames, filenames in os.walk(video_subdir)
              for filename in filenames if filename.endswith('.mp4')]

    # Define the output directory and create it if it doesn't exist
    output_dir = os.path.join(root_directory, "Final Video")
    os.makedirs(output_dir, exist_ok=True)

    # Define the path to the output video
    output_video = os.path.join(output_dir, "combined.mp4")

    # Concatenate the videos
    concatenate_videos(videos, output_video)


if __name__ == "__main__":
    root_dir = "Output"
    extract_and_combine_videos(root_dir)
