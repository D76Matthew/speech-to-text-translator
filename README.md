# speech-to-text-translator
 creating speech-to-text with a translator using google speech recognition API

## Library

you could install it in Python using the `pip` command

### speech_recognition
`pip install SpeechRecognition`

### pyaudio
`pip install pyaudio`

### translator
`pip install translate`

### langdetect : language detection
`pip install langdetect`

### pyttsx3
`pip install pyttsx3`

## Codes

the code consists of:

- translator: translate sentences into the desired language
- s2t: speech to text
- s2t-trans: combine s2t with translator
- t2s: text to speech
- s2t-t2s-translator: combine s2t, translate it, then t2s the translated text

## Future Update

- Create speech command for controlling IOT (ESP32) by connecting it to HTTP protocol or MQTT protocol
- Implement with AI to create basic conversation
