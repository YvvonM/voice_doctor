#importing libraries
import os
import base64
from groq import Groq
from dotenv import load_dotenv
import logging

#Initializing the logger 
logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)

#loaing the env file
load_dotenv()
#loading the groq key
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("Groq Api Key not loaded successfully")

#loading the image
def decode_image(image_path):
    image_file = open(image_path, "rb")
    print(f"image {image_path} has been loaded successfully")
    return base64.b64encode(image_file.read()).decode("utf-8")

#loading the model
def analyze_image_with_query(query,encoded_image):
    model = "llama-3.2-90b-vision-preview"
    client = Groq()
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }
        ]

    chat_completion = client.chat.completions.create(
        messages = messages,
        model = model
    )

    return chat_completion.choices[0].message.content

encoded_image = decode_image("/workspace/voice_doctor/data/acne.jpg")
query = "What can I use to solve this problem on my face"
response = analyze_image_with_query(query, encoded_image)
print(response)

