import re

fout = open('video_cut', 'w')
with open('video_info') as f:
    for line in f:
        line = line.strip()
        video_index, video_type, duration, _ = re.split('[. ]', line)
        for start_time in range(0, int(duration)-15, 15):
            fout.write("ffmpeg -ss "+"%d -i "%(start_time) + video_index + "." + video_type + " -t 15 -strict -2 -c copy " + "/mnt/cephfs_hl/speech/home/liruyun/Dalai/%s_%04d_%s"%(video_index, start_time, video_type) + "." + video_type + "\n")

