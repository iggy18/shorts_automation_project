from src.download_video import download_video
from src.stitch import stitch
from src.add_text import add_text
from src.generate_text import generate_text
from src.generate_topics import generate_topics

def main():
    topics = generate_topics(4)
    for search_term, topic in topics.items():
        generate_text(topic['value'])
        video_info = download_video(topic['summary'])
        # file_name = stitch(video_info)
        # add_text(video_info, file_name)

if __name__ == "__main__":
    main()