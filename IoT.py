from gtts import gTTS
import os

mytext = 'ha ha'

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("jarvis.mp3")
os.system("mpg321 jarvis.mp3")