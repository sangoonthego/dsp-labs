from pydub import AudioSegment
import os

input_file = "konnichiwa.m4a"
output_file = "konnachiwa.wav"

if not os.path.exists(input_file):
    raise FileNotFoundError(f"File Not Found!!!")

try:
    audio = AudioSegment.from_file(input_file, format="m4a")
    audio.export(output_file, format="wav")
    print(f"Converted Successfully!!!")
except Exception as e:
    print(f"Fail: {e}")