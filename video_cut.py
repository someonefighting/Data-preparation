f=open('wav_cut','w')
for i in range(20):
    for t in range(2,36):
        f.write("ffmpeg -ss 00:"+"%02d:00 -i "%(t)+ "%04d.mp4 -t 60 -strict -2 "%(i) + "output/%04d_%04d"%(i,t) + ".mp4\n")
f.close()
