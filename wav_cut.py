import json
import random
import numpy as np
import pprint
from pydub import AudioSegment
import re

path = "0000.mp3"
filename = path.split('.')[0]
wav_audio = AudioSegment.from_mp3(path)
seg_length = 15000
start = 0
end = len(wav_audio)
for index, chunk in enumerate(range(start, end, seg_length)):
    seg_start = chunk
    seg_end = seg_start + seg_length
    if seg_end >= end:
        seg_end = end
    new_segment = wav_audio[seg_start : seg_end]
    output_wavname = "output/" + filename + "_%04d.mp3"%(index)
    new_segment.export(output_wavname, format="mp3")
