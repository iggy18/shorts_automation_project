from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import VideoFileClip, ImageClip


def add_text(video_info, file_name):
    width, height = video_info.width, video_info.height
    background = Image.new('RGBA', (width, height), (255, 255, 255, 0))
    font = ImageFont.truetype('Roboto-Bold.ttf', 72)  # Choose your font and size
    draw = ImageDraw.Draw(background)
    text = "This is your text"
    textwidth, textheight = draw.textsize(text, font)
    x = (width - textwidth) / 2
    y = (height - textheight) / 2
    draw.text((x, y), text, font=font, fill=(255, 255, 255, 128))
    background.save('text.png')

    # Now use MoviePy to overlay this image on your video
    video = VideoFileClip(file_name)
    text_clip = ImageClip('text.png').set_duration(video.duration)  # Make sure the text image lasts as long as the video
    final = CompositeVideoClip([video, text_clip])

    final.write_videofile('src/edited_{}'.format(file_name), codec='libx264')
    print('progress: video edited')