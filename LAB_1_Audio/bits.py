import wave

file_path = "konnachiwa.wav"

with wave.open(file_path, "rb") as file:
    samples = file.getsampwidth()
    # exchange to bit
    bits = samples * 8
    print(f"Count of Bits: {bits} bits")

