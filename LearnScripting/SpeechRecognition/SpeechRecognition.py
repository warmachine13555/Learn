import speech_recognition as sr

def transcribe_speech():
    # Create a recognizer instance
    r = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Speak something...")
        audio = r.listen(source)

    try:
        # Perform speech recognition
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from the speech recognition service: {e}")

    return ""


def save_transcription(transcription):
    filename = "transcription.txt"
    with open(filename, "w") as file:
        file.write(transcription)
    print(f"Transcription saved to '{filename}'")


# Main script
if __name__ == "__main__":
    transcription = transcribe_speech()
    print("Transcription:", transcription)
    save_transcription(transcription)