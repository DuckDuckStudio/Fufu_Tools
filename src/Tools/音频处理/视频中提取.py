from moviepy import VideoFileClip
import os

def extract_audio(video_path, audio_path):
    try:
        # 检查视频文件是否存在
        if not os.path.exists(video_path):
            raise FileNotFoundError("[ERROR] 视频文件不存在")
        
        # 检查输出文件夹是否存在
        
        # 打开视频文件
        video_clip = VideoFileClip(video_path)
        
        # 提取音频
        audio_clip = video_clip.audio

        if audio_clip is None:
            raise ValueError("[ERROR] 视频文件不包含音频轨道")
        
        # 保存音频文件
        audio_clip.write_audiofile(audio_path)
        
        # 关闭视频和音频文件
        video_clip.close()
        audio_clip.close()
        
        input("音频提取完成！按 Enter 键退出...")
    
    except Exception as e:
        print(f"提取过程中出错: {e}")
        input("按 Enter 键退出...")

# 视频文件路径
video_path_input = input("视频文件的完整路径是：")
if video_path_input.startswith(("'", '"')) and video_path_input.endswith(("'", '"')):
    video_path_input = video_path_input[1:-1] # 移除引号

# 获取视频文件名（不带扩展名）
video_name = os.path.splitext(os.path.basename(video_path_input))[0]

# 音频文件路径
audio_path = input("需要将提取后的音频文件输出到哪里：")
if audio_path.startswith(("'", '"')) and audio_path.endswith(("'", '"')):
    audio_path = audio_path[1:-1] # 移除引号

# 如果输出路径是文件夹，则使用视频文件名作为音频文件名
if os.path.isdir(audio_path):
    audio_path = os.path.join(audio_path, f"{video_name}.mp3")

print("[INFO]目前配置信息：\n视频文件路径：", video_path_input, "\n输出音频文件的路径：", audio_path)

# 调用函数提取音频
extract_audio(video_path_input, audio_path)
