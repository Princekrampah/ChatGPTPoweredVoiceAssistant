import speech_recognition as sr

r = sr.Recognizer()

# get list of all available microphones and speakers
for mic_index, mic_name in enumerate(sr.Microphone.list_microphone_names()):
    print(str(mic_index) + " " + mic_name)

mic = sr.Microphone(device_index=14)

with mic as source:
    r.adjust_for_ambient_noise(source)

    audio = r.listen(source)

    text = r.recognize_google(audio)
    print(text)

