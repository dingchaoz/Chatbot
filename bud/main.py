from flask import Flask, render_template, request, jsonify
#import aiml
import os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


chatbot = ChatBot("Leyna2")


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/ask", methods=['POST'])
def ask():
	message = str(request.form['messageText'])

	# kernel = aiml.Kernel()

	# if os.path.isfile("bot_brain.brn"):
	#     kernel.bootstrap(brainFile = "bot_brain.brn")
	# else:
	#     kernel.bootstrap(learnFiles = os.path.abspath("aiml/std-startup.xml"), commands = "load aiml b")
	#     #kernel.bootstrap(learnFiles = os.path.abspath("aiml/mr-startup.xml"), commands = "load aiml b")
	#     kernel.saveBrain("bot_brain.brn")

	# kernel now ready for use
	while True:
	    if message == "quit":
	        exit()
	    elif message == "give me a response":
	        kernel.saveBrain("bot_brain.brn")
	    else:
	        bot_response = str(chatbot.get_response(message))
	        # print bot_response
	        return jsonify({'status':'OK','answer':bot_response})
	# text_file = open("Output.txt", "a")
	# mArray = []
	# mArray.append(message,bot_response)
	# text_file.write("\n")
	# text_file.write("\n".join(mArray))
	# text_file.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0',port = 9080,debug=True)