import speech_recognition as sr
from langdetect import detect

r = sr.Recognizer()
language_code = input('language code:') #need to specify source language since google speech recognition auto detect isn't accurate

def speech_to_text():
    with sr.Microphone() as source:
        print("Speak something...")
        audio = r.listen(source)
    try:
        v_text = r.recognize_google(audio, language=language_code)  # Use Google Speech Recognition API
        source_language = detect(v_text)
        print('detect language:', source_language)
        print("You said:", v_text)
        return v_text, source_language
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Error: {0}".format(e))

speech_to_text()