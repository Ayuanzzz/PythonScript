# coding: utf-8
import os
import subprocess

# # 导航到文件位置
# os.chdir(r'C:\Users\admin\Downloads')
#
# # 查找以 "audio" 或 "video" 开头的 MP4 文件
# for root, dirs, files in os.walk('.'):
#     for file in files:
#         if file.endswith('.mp4'):
#             if file.startswith('audio'):
#                 dest_name = 'audio.mp4'
#             elif file.startswith('video'):
#                 dest_name = 'video.mp4'
#             else:
#                 continue  # 忽略其他文件
#
#             # 构造源文件和目标文件路径
#             source_path = os.path.join(root, file)
#             dest_path = os.path.join(root, dest_name)
#
#             # 重命名文件
#             os.rename(source_path, dest_path)


# 定义要合成的音频和视频文件路径
video_file = r"C:\Users\admin\Downloads\video_第22讲、osgDB(2)写文件.mp4_哔哩哔哩_bilibili.mp4"
audio_file = video_file.replace("video","audio")


# 定义输出文件路径和名称
output_file = video_file.replace("video","merge")

# 构造 FFmpeg 命令
ffmpeg_cmd = ['ffmpeg', '-i', video_file, '-i', audio_file, '-c', 'copy', output_file]

# 运行 FFmpeg 命令
subprocess.run(ffmpeg_cmd)
