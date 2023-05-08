import speech_recognition as sr
import pyttsx3 as tts
import sys
import openai
import os
import webbrowser
from dotenv import load_dotenv


from generate_file_name import generate_random_file_name
from write_program import write_program
from image_generation import generate_image
from generals import general_questions

# load env
load_dotenv() 

# get the API key from the environment variables
openai.api_key = os.getenv("GPT_API_KEY")
print(os.getenv("GPT_API_KEY"))
# ChartGPT bot
def GPT_bot(recognizer: sr.Recognizer, mic: sr.Microphone):
    '''
        This function is what controls the bot itself. It controls
        the wake up word, speaking and making requests to the ChartGPT
        API
    '''

    # instantiate the speaker
    speaker = tts.init()
    # st speaker rate
    speaker.setProperty("rate", 150)

    # check if the argument passed to the function is of sr.Recognizer instance
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("Recognizer argument is not of the sr.Recognizer")

    # check if the argument passed to the function is of sr.Microphone instance
    if not isinstance(mic, sr.Microphone):
        raise TypeError("Mic argument is not of type sr.Microphone")

    # start an infinite while loop
    while True:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source)

            try:
                # convert audio to text using Google speech API
                text: str = recognizer.recognize_google(audio)
                # print(text)

                # check for wake up work
                if "hello james" in text.lower():
                    # create user
                    speaker.say("Hello Prince, how can I help you")
                    speaker.runAndWait()

                    # Once we recognize the wake up word, we convert it
                    # text           
                    audio = recognizer.listen(source)
                    text = recognizer.recognize_google(audio)

                    # call function to generate code
                    if "write a program" in text.lower():
                        response_text: str = write_program(openai=openai, text=text)
                        file_name: str = generate_random_file_name()

                        with open(file_name, "w") as f:
                            print(file_name)
                            f.write(response_text)

                            cwd = os.getcwd()

                            os.popen(f"cd {cwd} && code {file_name}")
                        
                    if "generate" in text.lower() and "image" in text.lower():
                        # function to generate images from ChatGPT
                        image_url: str = generate_image(openai=openai, text=text)
                        # open image in new browser
                        webbrowser.open_new(image_url)

                    if "exit" in text.lower():
                        speaker.say("Bye Prince")
                        speaker.runAndWait()
                        sys.exit(0)

                    else:
                        # general questions to ChatGPT function call
                        response_text: str = general_questions(openai=openai, text=text)
                        speaker.say(response_text)
                        speaker.runAndWait()
            except sr.UnknownValueError:
                print("Google Speech Recogniition could not understand")
            except sr.RequestError as e:
                print(f"Cound not request results from Google Speeck Recognizer {e}")


if __name__ == "__main__":
    # create a recognizer
    r = sr.Recognizer()
    # usually 14
    m = sr.Microphone(device_index=14)
    # start the bot
    GPT_bot(r, m)