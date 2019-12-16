from pydub import AudioSegment
from pydub.silence import split_on_silence
 
sound = AudioSegment.from_file("filePath")
loudness = sound.dBFS
#print(loudness)
 
chunks = split_on_silence(sound,
    # must be silent for at least half a second
    min_silence_len=430,
 
    # consider it silent if quieter than -16 dBFS
    silence_thresh=-45,
    keep_silence=400
 
)
print('total chunks：', len(chunks))
 

'''
for x in range(0,int(len(sound)/1000)):
    print(x,sound[x*1000:(x+1)*1000].max_dBFS)
'''
 
for i, chunk in enumerate(chunks):
    chunk.export("chunk{0}.mp3".format(i), format="mp3")
