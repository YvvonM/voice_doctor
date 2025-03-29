#importing the libraries
import os
import subprocess
import platform
import elevenlabs
from gtts import gTTS 
from dotenv import load_dotenv 
from elevenlabs.client import ElevenLabs
import logging

#inititalizing the logger
logging.basicConfig(level = logging.INFO, format= '%(asctime)s - %(levelname)s - %(message)s')

#loading the env file
load_dotenv()

elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY")
#checking if the api key has been corretly loaded
if not elevenlabs_api_key:
    raise ValueError("Api Key not loaded successfully!")

#changinng text to speech using gtts
def text_to_speech_with_gtts_old(text, output_filepath_gtts):
    language = "en"
    audioobj = gTTS(
        text = input_text,
        lang = language,
        slow = False
    )
    audioobj.save(output_filepath_gtts)

input_text="Hi this is Yvvon Majala! I am a Senior AI Engineer at Samsung"
text_to_speech_with_gtts_old(text=input_text, output_filepath_gtts="gtts_testing.mp3")

#changing text to speech using elevenlabs
def text_to_speech_with_eleven_old(input_text, output_filepath_eleven):
    client = ElevenLabs(api_key= elevenlabs_api_key)
    audioobj_eleven = client.generate(
        text = input_text,
        voice = "Mark - ConvoAI",
        output_format= "mp3_22050_32",
        model = "eleven_turbo_v2"
    )
    #saving the audio
    elevenlabs.save(audioobj_eleven, output_filepath_eleven)

text_to_speech_with_eleven_old(input_text= input_text, output_filepath_eleven= "eleven_testing.mp3")

#live audio play with gtts
def text_to_speech_with_gtts_live(input_text, output_filepath_gtts1):
    language = "en"
    audioobj = gTTS(
        text = input_text,
        lang = language,
        slow = False
    )
    audioobj.save(output_filepath_gtts1)

    os_name = platform.system()
    try: 
        if os_name == "Darwin":
            subprocess.run(['afplay', output_filepath_gtts1])
        elif os_name == "Windows":
            subprocess.run(['powershell', 'c', f'(New-Object Media.SoundPlayer "{output_filepath_gtts1}").PlaySync();'])
        elif os_name == "Linux":
            subprocess.run(['afplay', output_filepath_gtts1])
        else:
            raise OSError("Unsupported Operating Sytem")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

#live audioplay with elevenlabs
def text_to_speech_with_eleven_live(input_text, output_filepath_eleven1):
    client = ElevenLabs(api_key= elevenlabs_api_key)
    audioobj_eleven = client.generate(
        text = input_text,
        voice = "Mark - ConvoAI",
        output_format= "mp3_22050_32",
        model = "eleven_turbo_v2"
    )
    #saving the audio
    elevenlabs.save(audioobj_eleven, output_filepath_eleven1)
    os_name = platform.system()
    try: 
        if os_name == "Darwin":
            subprocess.run(['afplay', output_filepath_gtts1])
        elif os_name == "Windows":
            subprocess.run(['powershell', 'c', f'(New-Object Media.SoundPlayer "{output_filepath_gtts1}").PlaySync();'])
        elif os_name == "Linux":
            subprocess.run(['afplay', output_filepath_gtts1])
        else:
            raise OSError("Unsupported Operating Sytem")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


