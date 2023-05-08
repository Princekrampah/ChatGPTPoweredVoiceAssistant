import speech_recognition as sr


def wake_up_word(recognizer: sr.Recognizer, mic: sr.Microphone):
    '''
        This function takes the user input from the mic and
        listens for wake up wordk and says hello when its the wake up word
    '''

    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("Recognizer argument is not of the sr.Recognizer")

    if not isinstance(mic, sr.Microphone):
        raise TypeError("Mic argument is not of type sr.Microphone")

    
    while True:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.2)
            audio = recognizer.listen(source)

            try:
                text = recognizer.recognize_google(audio)
                if "hello james" in text.lower():
                    print("woken up")
            except sr.UnknownValueError:
                print("Google Speech Recogniition could not understand")
            except sr.RequestError as e:
                print(f"Cound not request results from Google Speeck Recognizer {e}")


if __name__ == "__main__":
    r = sr.Recognizer()
    m = sr.Microphone(device_index=14)
    wake_up_word(r, m)