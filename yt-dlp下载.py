import yt_dlp

# 创建yt-dlp实例并设置输出路径
ydl_opts = {
    'outtmpl': 'D:/movies/%(title)s.%(ext)s',  # 指定输出路径和文件名格式
}

ydl = yt_dlp.YoutubeDL(ydl_opts)


# 指定要下载的视频URL
base_url = "https://www.bilibili.com/video/BV11h4y1L7ce/?"

# 循环生成不同的URL
for page_number in range(38, 62):  # 从p=2到p=4
    # 构建完整的URL
    url = base_url + f"p={page_number}&vd_source=ddfdb2b3b3b380c6629deff6cd46520f"

    # 输出生成的URL
    print(url)
    # 下载视频
    ydl.download([url])

print("下载完成")

