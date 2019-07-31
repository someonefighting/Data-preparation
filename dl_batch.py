from __future__ import unicode_literals
import youtube_dl


ydl_opts = {
     'format': 'bestaudio/best',
     'postprocessors': [{
         'key': 'FFmpegExtractAudio',
         'preferredcodec': 'mp3',
         'preferredquality': '192',
     }],
}
with open('dalai_videolist') as f:
  for line in f:
    line = line.strip()
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
      ydl.download([line])
