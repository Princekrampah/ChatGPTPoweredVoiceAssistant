import speech_recognition as sr

#################################################################

# Install pyaudio for us to record mic

# Linux
# sudo apt-get install python-pyaudio python3-pyaudio

# Mac OS
# brew install portaudio
# pip install pyaudio

# Window
# pip install pyaudio

# Testing the installation
# python -m speech_recognition

#################################################################

# initialize the Recognizer object
r = sr.Recognizer()

# get list of available mics
for mic_index, mic_name in enumerate(sr.Microphone.list_microphone_names()):
    print(
        f"Microphone with name {mic_name} found for Microphone(device_index={mic_index})")

# initialize the Microphone object
# start device_index with 0 for system default if you
# do not have an external mic connected
mic = sr.Microphone(device_index=6)

# capture mic input
with mic as source:
    print("Listening....")
    # incase your program does not return
    # theres probably too much ambient noise
    # use this to handle the ambient noise
    r.adjust_for_ambient_noise(source)
    print("Adjusted to ambient noise")
    audio = r.listen(source)
    
    # recognize audio
    text = r.recognize_google(audio, show_all=True)
    print(text.get("alternative")[0])
    