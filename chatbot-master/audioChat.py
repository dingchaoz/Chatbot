import aiml
import speech_recognition as sr
import pyttsx
import os
# Create the kernel and learn AIML files
kernel = aiml.Kernel()
if os.path.isfile("bot_brain.brn"):
     kernel.bootstrap(brainFile = "bot_brain.brn")
else:
     kernel.bootstrap(learnFiles = "zoe-startup.xml", commands = "load zoe")
     kernel.saveBrain("bot_brain.brn")
# Start the TTS engine
engine = pyttsx.init('sapi5')
voices = engine.getProperty('voices')
# obtain audio from the microphone
r = sr.Recognizer()
# Press CTRL-C to break this loop
while True:
     # obtain audio from microphone
     with sr.Microphone() as source:
         print("Say something!")
         audio = r.listen(source)
     try:
         myinput = r.recognize_google(audio)
     except sr.UnknownValueError:
         print("Google Speech Recognition could not understand audio")
     except sr.RequestError as e:
         print("Could not request results from Google Speech Recognition service; {0}".format(e))
     print "You said: ", myinput
     if myinput == "exit":
         exit()
     # Get Zoe's response
     zoes_response = kernel.respond(myinput)
     print "Zoe said: ", zoes_response
     engine.setProperty('voice',voices[1].id)
     # have Zoe say the response
     engine.say(zoes_response)
     engine.runAndWait()
