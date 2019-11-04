from __future__ import unicode_literals
import youtube_dl


ydl_opts = {}
with open('dalai_list') as f:
  for line in f:
    line = line.strip()
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
      ydl.download([line])