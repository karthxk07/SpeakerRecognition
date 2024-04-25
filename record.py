import os
import pyaudio
import wave

def record_audio(output_filename, duration=2, sample_rate=44100, channels=1, chunk=1024, format=pyaudio.paInt16):
    audio = pyaudio.PyAudio()
    
    stream = audio.open(format=format,
                        channels=channels,
                        rate=sample_rate,
                        input=True,
                        frames_per_buffer=chunk)
    
    frames = []
    
    print("Recording...")
    for _ in range(0, int(sample_rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)
    
    print("Finished recording.")
    
    stream.stop_stream()
    stream.close()
    audio.terminate()
    
    # Save the recorded audio to a WAV file
    wf = wave.open(output_filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(audio.get_sample_size(format))
    wf.setframerate(sample_rate)
    wf.writeframes(b''.join(frames))
    wf.close()

def main():
    # Get user's name
    user_name = input("Please enter your name: ")
    output_folder = f"./audio/{user_name}"
    
    # Create folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Record and save 10 copies of the user's voice
    for i in range(1, 11):
        output_filename = f"{output_folder}/audio_{i}.wav"
        record_audio(output_filename)
        print(f"Audio {i} saved.")
    
    print("All recordings saved.")

if __name__ == "__main__":
    main()
