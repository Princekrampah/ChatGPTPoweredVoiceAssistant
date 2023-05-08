import speech_recognition as sr


def speech_recog_from_mic(recognizer, mic):
    '''
        This function will take the recognizer and mic objects.
        Pick sound from mic and try to recognize the audio
    '''

    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("Recognizer argument must be of type Recognizer class")

    if not isinstance(mic, sr.Microphone):
        raise TypeError("Mic needs to be of type Microphone class")

    # adjust to ambient noise and begin to record
    with mic as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        audio = recognizer.listen(source)

    try:
        transcript = recognizer.recognize_google(audio)
    except:
        transcript = None

    return transcript


if __name__ == "__main__":
    r = sr.Recognizer()
    m = sr.Microphone(device_index=6)
    transcript = speech_recog_from_mic(r, m)
    print(transcript)
