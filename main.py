import Pygame
import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from openai import OpenAI
from gtts import gTTS
# import os


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "56f44b6481f749dbb0eb2a8f0d595e3d"

def speak(text):


   
    engine.say(text)
    engine.runAndWait()
   

# # Initialize the mixer module
#    pygame.mixer.init()

# # Load the MP3 file
#    pygame.mixer.music.load(r"C:\python tutorial\jarvis\hello.mp3")

# # Play the MP3 file
#    pygame.mixer.music.play()

# # Keep the program running until the music finishes playing
#    while pygame.mixer.music.get_busy():
#     pygame.time.Clock().tick(10)
#    # os.remove("hello.mp3")
#    # os.remove

   
def aiProcess(command):
   client = OpenAI(api_key="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",)
   completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant. give short responses"},
        {
            "role": "user",
            "content": command
        }
    ]
    )
   return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
       webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
       webbrowser.open("https://faceebook.com")
    elif "open youtube" in c.lower():
       webbrowser.open("https://youtube.com")
    elif "open instagram" in c.lower():
       webbrowser.open("https://instagram.com")
    elif "open linkedin" in c.lower():
       webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
       song = c.lower().split(" ")[1]
       link = musiclibrary.music[song]
       webbrowser.open(link)

    elif "news" in c.lower():
     r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
     if r.status_code == 200:
    # Parse the JSON data
      data = r.json()
    
    # Initialize an empty list to store the headlines
    headlines = []
    
    # Extract the articles from the JSON response
    articles = data.get('articles', [])
    
    # Loop through each article and extract the title (headline)
    for article in articles:
        headline = article.get('title')
        if headline:  # Ensure there's a title
            headlines.append(headline)
    
    # Print the list of headlines
    print("List of Headlines:")
    for idx, headline in enumerate(headlines, 1):
        speak(f"{idx}. {headline}")

    else:
    #let openAI handle the request
      output = aiProcess(c)
      speak(output)
       
if __name__ == "__main__":
    speak("Initializing Jarvis")
while True:
    #listen for the wake word "jarvis"
    # obtain audio from the microphone
    r = sr.Recognizer()

    print("recognizing")
    try:
       with sr.Microphone() as source:
         print("Listening...")
         audio = r.listen(source, timeout=5, phrase_time_limit=3)
       word = r.recognize_google(audio)
       if(word.lower() == "jarvis"):
          speak("HELLO!")
          #listen for command
          with sr.Microphone() as source:
            print("Jarvis Active...")
            audio = r.listen(source)
            command = r.recognize_google(audio)

            processCommand(command)
    except Exception as e:
      print("Error; {0}".format(e))