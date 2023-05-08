import speech_recognition as sr
import pyttsx3 as tts
import sys
import openai
import datetime
import os
import webbrowser
from dotenv import load_dotenv

load_dotenv(dotenv_path="../env") 

# get the API key from the environment variables
openai.api_key = os.getenv("GPT_API_KEY")

# used to generate file names
def generate_random_file_name() -> str:
    basename = "gpt_code_file"
    suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    file_name = "_".join([basename, suffix])
    return file_name

# ChartGPT bot
def GPT_bot(recognizer: sr.Recognizer, mic: sr.Microphone):
    '''
        This function is what controls the bot itself. It controls
        the wake up word, speaking and making requests to the ChartGPT
        API.
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
                text = recognizer.recognize_google(audio)
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

                    if "write a program" in text.lower():
                        response = openai.Completion.create(
                            engine="text-davinci-003",
                            prompt= text,
                            temperature=0,
                            max_tokens=1500,
                            top_p=1,
                            frequency_penalty=0,
                            presence_penalty=0)

                        if 'choices' in response:
                            x = response['choices']

                            if len(x) > 0:
                                response_text = x[0]['text']

                            else:
                                response_text = ""

                            print(response_text)
                      
                            if "python" in text.lower():
                                file_name = generate_random_file_name()
                                file_name = file_name + ".py"

                            if "javascript" in text.lower():
                                file_name = generate_random_file_name()
                                print(file_name)
                                file_name = file_name + ".js"

                            if "java" in text.lower():
                                file_name = generate_random_file_name()
                                print(file_name)
                                file_name = file_name + ".java"

                            if "c plus plus" in text.lower():
                                file_name = generate_random_file_name()
                                file_name = file_name + ".cpp"

                            if "golang" in text.lower() or "in go" in text.lower():
                                file_name = generate_random_file_name()
                                file_name = file_name + ".go"


                        with open(file_name, "w") as f:
                            print(file_name)
                            f.write(response_text)

                        cwd = os.getcwd()

                        os.popen(f"cd {cwd} && code {file_name}")
                        
                    if "generate" in text.lower() and "image" in text.lower():
                        response = openai.Image.create(
                            prompt=text,
                            n=1,
                            size="1024x1024"
                        )
                        image_url = response['data'][0]['url']

                        # open image in new browser
                        webbrowser.open_new(image_url)

                    if "exit" in text.lower():
                        speaker.say("Bye Prince")
                        speaker.runAndWait()
                        sys.exit(0)

                    else:
                        openai_response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                                {"role": "system", "content": text},
                            ]
                        )

                        response_text = openai_response.get("choices")[0].get("message").get("content")
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