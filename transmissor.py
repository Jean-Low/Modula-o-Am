import scipy.io.wavfile as wav
import soundfile as sf
import sounddevice as sd

m1 = wav.read("Wavs/Saved Game.wav");
print(m1[0])
print(m1[1])

print("IIIIIIIIIIIIIIIIIIIIIIIII RAAAAAAAAAAA")
m1, fs = sf.read("Wavs/Saved Game.wav");
print(m1)
print(len(m1))
print(m1[0])
print(m1[1])
print(m1[:,1])


def playSound(sound,looping = False):
    print("playing audio")
    sd.play(sound, fs,loop = looping)
    sd.wait()
