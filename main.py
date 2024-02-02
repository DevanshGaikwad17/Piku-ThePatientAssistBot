import openai
import pywhatkit
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
openai.api_key = "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"


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = .5
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception:
        return "None"
    return query


if __name__ == '__main__':
    while True:
        query = takeCommand().lower()

        if 'eco' in query:
            print(query)
            query = query.replace("eco", "")
            completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=[{"role": "user", "content": query }])
