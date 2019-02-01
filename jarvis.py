from gtts import gTTS
import speech_recognition as sr
import os
import RPi.GPIO as GPIO

# led setup
red = 17
blue = 22
yello = 27

r = 2
g = 3
b = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(yello, GPIO.OUT)
GPIO.setup(r, GPIO.OUT)
GPIO.setup(g, GPIO.OUT)
GPIO.setup(b, GPIO.OUT)

def setColor(red, green, blue):
    GPIO.output(r, red)
    GPIO.output(g, green)
    GPIO.output(b, blue)

def turnOff(red=0, green=0, blue=0):
    GPIO.output(r, red)
    GPIO.output(g, green)
    GPIO.output(b, blue)

# gtts 하이퍼 마라미터
language = 'en'
done = False

def speak(command):
    jarvis = gTTS(text=command, lang='en', slow=False)
    jarvis.save('jarvis.mp3')
    os.system("mpg321 jarvis.mp3")

def command(text):
    if 'turn on the red light ' in text:
        command = 'yes bose, turn on the red light'
        GPIO.output(red, True)
    elif 'turn on the blue light' in text:
        command = 'yes bose, turn on the blue light'
        GPIO.output(blue, True)
    elif 'turn on the yello light' in text:
        command = 'yes bose, turn on the yello light'
        GPIO.output(yello, True)
    elif 'turn off the red light ' in text:
        command = 'yes bose, turn off the red light'
        GPIO.output(red, False)
    elif 'turn off the blue light' in text:
        command = 'yes bose, turn off the blue light'
        GPIO.output(blue, False)
    elif 'turn off the yello light' in text:
        command = 'yes bose, turn off the yello light'
        GPIO.output(yello, False)
    elif 'turn on the pupple light' in text:
        command = 'yes bose, turn on the pupple light'
        setColor(80, 0, 80)
    elif 'turn off the pupple light' in text:
        command = 'yes bose, turn off the pupple light'
        turnOff()
    elif 'turn on the pink light' in text:
        command = 'yes bose, turn on the pink light'
        setColor(255, 51, 153)
    elif 'turn off the pink light' in text:
        command = 'yes bose, turn off the pink light'
        turnOff()
    elif 'thank you jarvis' in text:
        command = "you are welcome, sir"
    elif 'bye jarvis' in text:
        command = 'yes sir, Please call me again next time. bye'
    else:
        command = "i can't understand, what you said. please again command to me"
    return command

def jarvis(done1=False):
    rs = sr.Recognizer()
    while not done1:
        with sr.Microphone() as source:
            print("Speak Anything : ")
            audio = rs.listen(source)
            try:
                text = rs.recognize_google(audio)
                print("You said:")
                command = command(text)
                if command == 'yes sir, Please call me again next time. bye':
                    speak(command)
                speak(command)
            except:
                print("Sorry could not recognize what you said!!!")
            
r = sr.Recognizer()
while not done:
    with sr.Microphone() as source1:
        audio = r.listen(source1)
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
        
            # jarvis 호출
            if 'jarvis' in text:
                jarvis = gTTS(text="hello everyone my name is jarvis, I am an assistant to Yungyo.\
                what can i help you?", lang=language, slow=False)
                jarvis.save("jarvis.mp3")
                os.system("mpg321 jarvis.mp3")
                jarvis()
                done=True
        except:
            print("Sorry could not recognize what you said")
        

