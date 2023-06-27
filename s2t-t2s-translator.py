import speech_recognition as sr
from translate import Translator
from langdetect import detect
import pyttsx3

r = sr.Recognizer()
language_code = input('source language code:') #need to specify source language since google speech recognition auto detect isn't accurate
target_language = input('translated language code:')

def speech_to_text():
    with sr.Microphone() as source:
        print("Speak something...")
        audio = r.listen(source)
    try:
        v_text = r.recognize_google(audio, language=language_code)  # Use Google Speech Recognition API
        source_language = detect(v_text)
        return v_text, source_language
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Error: {0}".format(e))

def translate_text(texttrans, target_language):
    source_language = detect(texttrans)
    translator = Translator(from_lang=source_language, to_lang=target_language)
    translation = translator.translate(texttrans)
    return translation

def text_to_speech(text):
    engine = pyttsx3.init()  # Initialize the TTS engine
    voices = engine.getProperty('voices')
    for voice in voices:
        if voice.name == 'Microsoft Zira Desktop - English (United States)':
            engine.setProperty('voice', voice.id)
            break
    engine.setProperty('rate', 150)  # Set speech rate to 150 words per minute
    engine.setProperty('volume', 1)  # Set volume to 100% of the maximum
    engine.say(text)  # Convert the text to speech
    engine.runAndWait()  # Wait for the speech to complete

input_text, source_language = speech_to_text()
translated_text = translate_text(input_text, target_language)

print('original text:', input_text)
print('source language:',detect(input_text))
print("Translated text:", translated_text)
print('translated language:',detect(translated_text))
text_to_speech(translated_text)