import sounddevice as sd
import wavio

def record_audio(duration, fs, channels):
    print("Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    print("Recording finished.")
    return recording

def save_audio(file_name, recording, fs):
    wavio.write(file_name, recording, fs, sampwidth=2)

def main():
    fs = 44100  # Sample rate
    duration = 5  # Recording duration in seconds
    channels = 2  # Number of audio channels (1 for mono, 2 for stereo)

    recording = record_audio(duration, fs, channels)

    file_name = "recorded_audio.wav"
    save_audio(file_name, recording, fs)

    print(f"Audio saved as {file_name}")

if __name__ == "__main__":
    main()
