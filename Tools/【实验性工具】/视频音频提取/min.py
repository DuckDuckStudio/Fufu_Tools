from moviepy.editor import VideoFileClip
import os

def extract_audio(video_path, audio_path):
    try:
        # 检查视频文件是否存在
        if not os.path.exists(video_path):
            raise FileNotFoundError("视频文件不存在")
        
        # 检查输出文件夹是否存在
        
        # 打开视频文件
        video_clip = VideoFileClip(video_path)
        
        # 提取音频
        audio_clip = video_clip.audio
        
        # 保存音频文件
        audio_clip.write_audiofile(audio_path)
        
        # 关闭视频和音频文件
        video_clip.close()
        audio_clip.close()
        
        print("音频提取完成！")
    
    except FileNotFoundError as e:
        print(f"错误：{e}")

# 视频文件路径
video_path_input = input("视频文件的完整路径是：")
video_path = video_path_input.strip('\"')

# 获取视频文件名（不带扩展名）
video_name = os.path.splitext(os.path.basename(video_path))[0]

# 音频文件路径
audio_path_input = input("需要将提取后的音频文件输出到哪里：")
audio_path = audio_path_input.strip('\"')

# 如果输出路径是文件夹，则使用视频文件名作为音频文件名
if os.path.isdir(audio_path):
    audio_path = os.path.join(audio_path, f"{video_name}.mp3")

print("[INFO]目前配置信息：\n视频文件路径：", video_path_input, "\n输出音频文件的路径：", audio_path)

# 调用函数提取音频
extract_audio(video_path, audio_path)

