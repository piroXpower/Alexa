import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty(voices)
engine.setProperty('voice',voices[1].id)
def talk(text):
engine.say(text)
engine.runandWait()


def take_command():
try:
   with sr.Microphone() as source:
       print("Listening...")
       voice = listener.listen(source)
   command = listener.recognize_google(voice)
   command = command.lower()
   if 'alexa' in command:
       command = command.replace('alexa','')
      print(command)
except:
    pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
    song = command.replace('play','')
    talk('playing'+song)
    pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M:%S %p')
        print(time)
        talk('Current time is' +time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is','')
        info = wikipedia.summary(person,10)
        print(info)
        talk(info)
        elif 'date' in command:
            talk('I am having headache today')
            elif 'are you single' in command:
                talk('I am in relationship with wifi')
                elif 'joke' in command:
                    talk(pyjokes.get_joke())
                    else:
                        talk("Please tell the command again")
                    
        
while True:
   run_alexa()
