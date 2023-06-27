import pyttsx3

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

# Example usage
text_to_speech("Hello, how are you?")