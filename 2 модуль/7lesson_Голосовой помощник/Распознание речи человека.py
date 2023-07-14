import speech_recognition as sr
import pyttsx3
import pyaudio
import random
import datetime

r = sr.Recognizer()   # инициализирую
voice = pyttsx3.init()
voice.say("Привет, меня зовут Товарищ.")
voice.runAndWait()

print(str(sr.Microphone.list_microphone_names()))

list_hi = ["привет", "здравствуйте", "доброго времени суток", "hello", "hi"]
films = ["film1", "film2", "film3", "film5", "film6"]
while True:
    with sr.Microphone(device_index=1) as mf:   #с помощью микрофона с индексом 1 (тот, который используется в системе автоматически)
        print("Скажите что-нибудь...")   # напечатать ...
        audio = r.listen(mf) # аудио = прослушай то, что слышно в микрофоне

    speech = r.recognize_google(audio, language="ru_RU").lower()   # speech = преобразуй речь с помощью (сейчас гугл, но вариантов много), из аудио, язык = русский(Такое обозначение - ru_RU) и сохрани в нижнем регистре
    print("Вы сказали: " + str(speech))

    if speech.find("привет") >= 0:
        voice.say(random.choice(list_hi))
        voice.runAndWait()

    elif speech.find("время") >= 0:
        voice.say(f"{datetime.datetime.today():%h%m}")
        voice.runAndWait()

    elif speech.find("пока") >=0 or speech.find("До встречи") >= 0:
        voice.say("До свидания!")
        voice.runAndWait()
        break
    elif speech.find("фильм") >= 0:
        voice.say(random.choice(films))
        voice.runAndWait()
    else:
        voice.say("я вас не понимаю")
        voice.runAndWait()