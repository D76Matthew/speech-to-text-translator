from translate import Translator
from langdetect import detect

def translate_text(text, target_language):
    source_language = detect(text)
    translator = Translator(from_lang=source_language, to_lang=target_language)
    translation = translator.translate(text)
    return translation

input_text = input("Enter text: ")
target_language = input("Enter language code: ")
translated_text = translate_text(input_text, target_language)
print('original text:', input_text)
print('source language:',detect(input_text))
print("Translated text:", translated_text)
