import os
import concurrent.futures


video_urls = [
    "https://www.youtube.com/watch?v=hxsJvKYyVyg"
]


def download_video(video_url):
    os.system(f"yt-dlp -x --audio-format mp3 {video_url}")
    title = os.popen(f"yt-dlp --get-title {video_url}").read().strip()
    print(f"{title}下载完成！")


with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for url in video_urls:
        futures.append(executor.submit(download_video, url))
    for future in concurrent.futures.as_completed(futures):
        try:
            _ = future.result()
        except Exception as e:
            print(f"An error occurred: {e}")

