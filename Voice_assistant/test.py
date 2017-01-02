
#https://pypi.python.org/pypi/gTTS/1.0.2
from gtts import gTTS
import os
tts = gTTS(text='Hello World', lang='en')
tts.save("hello.mp3")
os.system("mpg321 hello.mp3")
