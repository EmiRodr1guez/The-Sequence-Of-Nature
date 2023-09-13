import numpy as np
from scipy.fft import *
from scipy.io import wavfile
from flask import request

def freq(start_time, end_time):
    # Check if a file was uploaded
    if 'wav_file' not in request.files:
        return "No file provided"

    uploaded_file = request.files['wav_file']

    # Open the uploaded file and convert to mono
    sr, data = wavfile.read(uploaded_file)
    print(f"Sample rate: {sr}")  # Debugging line
    print(f"Data shape: {data.shape}")  # Debugging line
    if data.ndim > 1:
        data = data[:, 0]

    # Return a slice of the data from start_time to end_time
    dataToRead = data[int(start_time * sr / 1000): int(end_time * sr / 1000) + 1]

    # Debugging lines
    print(f"Data to read length: {len(dataToRead)}")
    print(f"Data to read max value: {np.max(dataToRead)}")

    # Fourier Transform
    N = len(dataToRead)
    yf = rfft(dataToRead)
    xf = rfftfreq(N, 1 / sr)


    print(f"XF shape: {xf.shape}")

    # Uncomment these to see the frequency spectrum as a plot
    # plt.plot(xf, np.abs(yf))
    # plt.show()

    # Get the most dominant frequency and return it
    idx = np.argmax(np.abs(yf)) # type: ignore
    computed_freq = xf[idx]

    # Debugging line
    print(f"Computed frequency: {computed_freq} Hz")

    return computed_freq
