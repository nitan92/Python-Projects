import speech_recognition as sr
import pyttsx3, pywhatkit, datetime
import wikipedia,pyjokes



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
coco_voice = voices[1]
engine.setProperty('voice', coco_voice.id)
# Test the coco voice
engine.say("Hello, I am Coco, Your assistant. How i can help you today?")
engine.runAndWait()
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Coco' in command:
                command = command.replace('Coco', '')
                print(command)
    except:
        pass
    return command

def run_coco():
    command = take_command()
    if "play" in command:
        song = command.replace('play', '')
        talk("Playing"+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = command.replace('time', '')
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk("Current time is "+time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please repeat it again!!')

while True:
    run_coco()