import sounddevice as sd
from scipy.io.wavfile import write

freq = 44100
second = 5

print("Starting to Record...")

recording = sd.rec(int(second * freq), samplerate=freq, channels=1, dtype="int16")
sd.wait()
write("test2.m4a", freq, recording)
print("Recorded Successfully!!!")