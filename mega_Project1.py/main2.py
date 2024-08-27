import speech_recognition as sr
import pyttsx3
import webbrowser
import requests
import openai
import datetime

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set properties for the voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Try 1 for female, 0 for male
engine.setProperty('rate', 150)  # Slower rate for clearer voice
engine.setProperty('volume', 1.0)  # Max volume

# Initialize OpenAI
openai.api_key = "YOUR_OPENAI_API_KEY"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not catch that.")
        return ""
    except sr.RequestError:
        print("Request error; check your internet connection.")
        return ""

def process_command(command):
    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")
    elif "open facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://linkedin.com")
    elif "play" in command:
        # Example: play a song if musicLibrary is defined
        song = command.split("play ")[-1]
        # Replace musicLibrary.music[song] with the actual URL
        link = "https://example.com/" + song
        speak(f"Playing {song}")
        webbrowser.open(link)
    elif "news" in command:
        get_news()
    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {now}")
    elif "date" in command:
        today = datetime.datetime.today().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")
    elif "exit" in command:
        speak("Goodbye!")
        exit()
    else:
        openai_response(command)

def get_news():
    api_key = "YOUR_NEWS_API_KEY"
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        if articles:
            speak("Here are the top news headlines:")
            for article in articles[:5]:
                speak(article['title'])
        else:
            speak("No news found.")
    else:
        speak("Failed to fetch news.")

def openai_response(command):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=command,
        max_tokens=50
    )
    answer = response.choices[0].text.strip()
    speak(answer)

if __name__ == "__main__":
    speak("Hello, I am your assistant. How can I help you today?")
    while True:
        command = listen()
        if command:
            process_command(command)
