# Audio Input Module: Processes speech input and converts to text
import speech_recognition as sr

def read_audio_input():
    """
    Captures speech input and converts it to text using Google Speech API.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now:")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Audio not recognized."
