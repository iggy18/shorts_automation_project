import os
from moviepy.editor import *

def stitch(video_info):
    # Specify the directory containing your video files
    video_dir = "src/source_video"

    # Get a list of all files in the directory
    all_files = os.listdir(video_dir)
    
    clips = []
    
    for file in all_files:
        full_path = os.path.join(video_dir, file)
        clips.append(VideoFileClip(full_path))

    # Concatenate the video clips
    final_clip = concatenate_videoclips(clips, method='compose')
    
    file_name = "src/stitched_{}".format(video_info.file_name)

    # Write the result to a file
    final_clip.write_videofile(file_name, fps=30)
    print('progress: videos concatenated')
    
    return file_name
