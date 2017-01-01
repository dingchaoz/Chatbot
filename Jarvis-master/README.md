# Project Jarvis

by [AJ Minich](http://ajminich.com/projects)

Jarvis is a personal assistant that uses natural language processing and a database 
of pre-programmed functionality to respond to user requests. Jarvis is driven by a 
Java-based backend that performs core operations, and can be used through various 
interfaces.

Jarvis is named after Tony Stark's automated assistant in the *[Ironman](http://en.wikipedia.org/wiki/Edwin_Jarvis#Film)* series.

## Overview

Here are some examples of anticipated behavior::

```bash
> jarvis
Yes sir?

> jarvis remind me to set a timer for 5 minutes
Timer set for 3:04:32 PM.

> jarvis stop listening
Yes sir, I will be offline until the next time you type "jarvis".
```

## Setup
To set up this project on a local machine, perform the following steps.

### Prerequisites
- git
- Unix-based machine
- pip

### Clone
First, clone this repository to the local machine or server.

### Virtualenv
If you haven't already, install the virtualenv package:
 
    $ pip install virtualenv
    
Then create a virtualenv:

    $ virtualenv venv
    
Load the new environment:

    $ source venv/bin/activate

### Install PyAudio
Follow the directions at https://people.csail.mit.edu/hubert/pyaudio/ to install PyAudio.

Note that portaudio.h may not link correctly on Mac OSX machines; in this case
run:

    $ pip install --global-option='build_ext' --global-option='-I/usr/local/include' --global-option='-L/usr/local/lib' pyaudio
    
### Dependencies
Install dependencies using pip:

    $ pip install -r requirements.txt

## Running
To run a basic example, start the included listener:

    $ python listen.py

## Plans

### To Do
- Remove dependency on top-level SpeechRecognition package. 
- Console
  - run as a background daemon
  - incorporate Jarvis into the login and logout functions
  - have Jarvis warn if any of the directories are getting full (df -h)
  - make it possible to tell Jarvis to shut up
- Store things like API keys in a configuration file
- Add REST API support
- Engine
  - bring in the NLP software from http://nlp.stanford.edu/software/index.shtml
  - allow basic commands to be parsed and responded to
  - consider using data from Freebase Quad Dump (http://aws.amazon.com/datasets/2052645406658757)
- voice interface
  - consider bringing in soundbites from http://www.wavsource.com/movies/iron_man.htm
  
### Complete
- Rewrite project in Python using the SpeechRecognition package.

### Abandoned
*None yet*

## Disclaimer
The Jarvis and Ironman names are trademark of Marvel Entertainment, LLC. I do
not own the rights to these.
