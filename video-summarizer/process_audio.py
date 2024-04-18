import yt_dlp

def get_audio(video_url: str) -> str:
    video_id = video_url.split("=")[1]
    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'paths': {'home': 'audio/'},
        'outtmpl': {'default': '%(id)s.%(ext)s'},
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
        }]
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download([video_url])
        if error_code != 0:
            raise Exception('Failed to download video')

    return f'audio/{video_id}.m4a'
