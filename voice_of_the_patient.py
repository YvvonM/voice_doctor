#importing libraries
import os
from dotenv import load_dotenv
from groq import Groq 
import logging
import speech_recognition as sr 
from pydub import AudioSegment
from io import BytesIO

#setting up the logging
logging.basicConfig(level = logging.INFO, format= '%(asctime)s - %(levelname)s - %(message)s')

#loading the dotenv file
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

#Checking if the file is correctly loaded
if not groq_api_key:
    raise ValueError("Groq Api Key not loaded successfully")


#recording the audio
def record_audio(file_path, timeout = 20, phrase_time_limit = None):

    """
    Simplified function to record audio from the microphone and save it as an MP3 file.

    Args:
    file_path (str): Path to save the recorded audio file.
    timeout (int): Maximum time to wait for a phrase to start (in seconds).
    phrase_time_lfimit (int): Maximum time for the phrase to be recorded (in seconds).
    """
    #checking for sound
    recongizer = sr.Recognizer()
    #recording
    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise")
            #adjusting microphone to get clear audio
            recongizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Start speaking now")

            #recording the audio
            audio_data = recongizer.listen(source, timeout = timeout, phrase_time_limit = phrase_time_limit)
            logging.info("Recording complete")

            #Converting the recording into wav format
            wav_data = audio_data.get_wav_data()
            #reading the wav file
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            #exporting thefile in mp3 format
            audio_segment.export(file_path, format = "mp3", bitrate = "128k")
            logging.info(f"Audio saved to {file_path}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
audio_filepath="patient_voice_test_for_patient.mp3"
# record_audio(file_path=audio_filepath)

#transcribing the audio output
def transcribe_with_groq(audio_filepath):
    #setting the model
    sst_model = "whisper_large_v3"
    client = Groq(api_key= groq_api_key)
    audio_file = open(audio_filepath, "rb")
    transcription = client.audio.transcriptions.create(
        model = sst_model,
        file= audio_file,
        language = "en"
    )
    return transcription.text

