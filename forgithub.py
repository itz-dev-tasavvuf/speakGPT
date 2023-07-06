import openai
from gtts import gTTS
import pygame
import tempfile
import os
import keyboard

# Set up OpenAI API credentials
openai.api_key = 'yourapikey'

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_file:
        temp_filename = temp_file.name
        tts.save(temp_filename)
    pygame.mixer.init()
    pygame.mixer.music.load(temp_filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        if keyboard.is_pressed('tab'):
            break
    pygame.mixer.music.stop()
    os.remove(temp_filename)

# Example usage of ChatGPT API and text-to-speech conversion
def generate_chat_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    chat_response = response.choices[0].message.content
    return chat_response

# Continuous conversation loop
while True:
    # Get user input
    user_input = input("You: ")

    # Check if user wants to exit
    if user_input.lower() == "exit":
        break

    # Generate chat response
    response = generate_chat_response(user_input)

    # Convert response to speech
    text_to_speech(response)





