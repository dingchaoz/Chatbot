#!/usr/bin/env python

#from jarvis import Jarvis


import logging

logger = logging.getLogger(__name__)


class Jarvis(object):
    
    # Built-in words
    JARVIS_COGNATES = ["jarvis", "gervais", "travis", "tervis", "service"]
    
    STOP_LISTENING_COGNATES = ["go away", "stop listening", "shut down"]
    
    @classmethod
    def is_actionable_command(cls, command):
        return any(cognate in command for cognate in cls.JARVIS_COGNATES)
    
    @classmethod
    def handle_action(cls, command, **kwargs):
        """
            Handles a single text command.
            """
        
        # Use lowercase for processing.
        command = command.lower()
        
        logger.debug("Received command: '%s'", command)
        
        response = kernel.respond(command)
#        print ("Responded back by machine", response)
        es.say(response)
        logger.debug("Responded is: '%s'", response)
        
        # Determine if this is an actionable command.
        if not cls.is_actionable_command(command):
            return
        
        if any(cognate in command for cognate in cls.STOP_LISTENING_COGNATES):
            logger.info("Thank you, enjoy your day, sir.")
        else:
            logger.info("Yes sir?")

#import logging
import speech_recognition as sr
import aiml
import os
import espeak
es = espeak.ESpeak()
es.voice = 'en'
es.speed = 1

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = os.path.abspath("aiml/std-startup.xml"), commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")


# for testing purposes, we're just using the default API key
GOOGLE_SPEECH_RECOGNITION_API_KEY = None

def run_transcription_loop():
    # Most of this code taken from https://github.com/Uberi/speech_recognition/blob/master/examples/microphone_recognition.py.
    r = sr.Recognizer()
    with sr.Microphone() as source:

        while True:
            logger.debug("Awaiting user input.")
            audio = r.listen(source)

            logger.debug("Attempting to transcribe user input.")

            try:
                result = r.recognize_google(audio,
                                            key=GOOGLE_SPEECH_RECOGNITION_API_KEY)
                Jarvis.handle_action(result)
#                response = kernel.respond(result)
#                print ("Responded back by machine", response)
            except sr.UnknownValueError:
                logger.debug("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                logger.warn("Could not request results from Google Speech Recognition service: %s", e)
            except Exception as e:
                logger.error("Could not process text: %s", e)

def main():
    # Set up logger.
    FORMAT = '%(asctime)s %(filename)s:%(lineno)s [%(levelname)s] %(message)s'
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)

    run_transcription_loop()

if __name__ == '__main__':
    main()