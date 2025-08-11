import numpy as np
import librosa

file_path = "test.wav"

# read file
y, sr = librosa.load(file_path, sr=None, mono=True)

# calcu freq by pyin
freq0, voiced_flag, voiced_probs = librosa.pyin(
    y,
    fmin = librosa.note_to_hz("C2"),  # ~65.41 Hz
    fmax = librosa.note_to_hz("C7"),
    sr=sr
)

# calcu mean freq
freq0_mean = np.nanmean(freq0)
print(f"Frequence = {freq0_mean}")