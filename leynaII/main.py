from flask import Flask, render_template, request, jsonify
# import aiml
import os
from chatterbot import ChatBot
# make separate chatbots for each question, to isolate Q/A conversations
from chatterbot.trainers import ListTrainer

chatbot = [ChatBot("initBot",
                  storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
                  logic_adapters=[
                      "chatterbot.logic.BestMatch",
                      {
                          'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                          'threshold': 0.4,
                          'default_response': 'I am sorry, but I do not understand.'
                      }
                  ],
                  database="./database0.db",
                  ), ChatBot("q1Bot",
                  storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
                  logic_adapters=[
                      "chatterbot.logic.BestMatch",
                      {
                          'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                          'threshold': 0.4,
                          'default_response': 'I am sorry, but I do not understand.'
                      }
                  ],
                  database="./database1.db",
                  ), ChatBot("q2Bot",
                  storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
                  logic_adapters=[
                      "chatterbot.logic.BestMatch",
                      {
                          'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                          'input_text': 'What do you call a cat at the beach?',
                          'output_text': 'Sandy Claws'
                      },
                      {
                          'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                          'threshold': 0.4,
                          'default_response': 'Okay. Next question -'
                      }
                  ],
                  database="./database2.db",
                  ), ChatBot("q3Bot",
                  storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
                  logic_adapters=[
                      "chatterbot.logic.BestMatch",
                      {
                          'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                          'input_text': 'What do you call a cat at the beach?',
                          'output_text': 'Sandy Claws'
                      },
                      {
                          'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                          'threshold': 0.4,
                          'default_response': 'Okay. Next question -'
                      }
                  ],
                  database="./database3.db",
                  ), ChatBot("q4Bot",
                  storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
                  logic_adapters=[
                      "chatterbot.logic.BestMatch",
                      {
                          'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                          'input_text': 'What do you call a cat at the beach?',
                          'output_text': 'Sandy Claws'
                      },
                      {
                          'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                          'threshold': 0.4,
                          'default_response': 'Okay. Next question -'
                      }
                  ],
                  database="./database4.db",
                  ), ChatBot("q5Bot",
                  storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
                  logic_adapters=[
                      "chatterbot.logic.BestMatch",
                      {
                          'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                          'input_text': 'What do you call a cat at the beach?',
                          'output_text': 'Sandy Claws'
                      },
                      {
                          'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                          'threshold': 0.4,
                          'default_response': 'Okay. Next question -'
                      }
                  ],
                  database="./database5.db",
                  ), ChatBot("q6Bot",
                  storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
                  logic_adapters=[
                      "chatterbot.logic.BestMatch",
                      {
                          'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                          'input_text': 'What do you call a cat at the beach?',
                          'output_text': 'Sandy Claws'
                      },
                      {
                          'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                          'threshold': 0.4,
                          'default_response': 'Okay. Next question -'
                      }
                  ],
                  database="./database6.db",
                  ), ChatBot("q7Bot",
                  storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
                  logic_adapters=[
                      "chatterbot.logic.BestMatch",
                      {
                          'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                          'input_text': 'What do you call a cat at the beach?',
                          'output_text': 'Sandy Claws'
                      },
                      {
                          'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                          'threshold': 0.4,
                          'default_response': 'Okay. Next question -'
                      }
                  ],
                  database="./database7.db",
                  ), ChatBot("q8Bot",
                  storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
                  logic_adapters=[
                      "chatterbot.logic.BestMatch",
                      {
                          'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                          'input_text': 'What do you call a cat at the beach?',
                          'output_text': 'Sandy Claws'
                      },
                      {
                          'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                          'threshold': 0.4,
                          'default_response': 'Okay. Next question -'
                      }
                  ],
                  database="./database8.db",
                  ), ChatBot("q9Bot",
                  storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
                  logic_adapters=[
                      "chatterbot.logic.BestMatch",
                      {
                          'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                          'input_text': 'What do you call a cat at the beach?',
                          'output_text': 'Sandy Claws'
                      },
                      {
                          'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                          'threshold': 0.4,
                          'default_response': 'Okay. Next question -'
                      }
                  ],
                  database="./database9.db",
                  ), ChatBot("q10Bot",
                  storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
                  logic_adapters=[
                      "chatterbot.logic.BestMatch",
                      {
                          'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                          'input_text': 'What do you call a cat at the beach?',
                          'output_text': 'Sandy Claws'
                      },
                      {
                          'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                          'threshold': 0.4,
                          'default_response': 'Okay. Next question -'
                      }
                  ],
                  database="./database10.db",
                  ), ChatBot("q11Bot",
                  storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
                  logic_adapters=[
                      "chatterbot.logic.BestMatch",
                      {
                          'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                          'input_text': 'What do you call a cat at the beach?',
                          'output_text': 'Sandy Claws'
                      },
                      {
                          'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                          'threshold': 0.4,
                          'default_response': 'Okay. Next question -'
                      }
                  ],
                  database="./database11.db",
                  ), ChatBot("q12Bot",
                  storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
                  logic_adapters=[
                      "chatterbot.logic.BestMatch",
                      {
                          'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                          'input_text': 'What do you call a cat at the beach?',
                          'output_text': 'Sandy Claws'
                      },
                      {
                          'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                          'threshold': 0.4,
                          'default_response': 'Okay. Next question -'
                      }
                  ],
                  database="./database12.db",
                  ), ChatBot("q13Bot",
                  storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
                  logic_adapters=[
                      "chatterbot.logic.BestMatch",
                      {
                          'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                          'input_text': 'What do you call a cat at the beach?',
                          'output_text': 'Sandy Claws'
                      },
                      {
                          'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                          'threshold': 0.4,
                          'default_response': 'Okay. Next question -'
                      }
                  ],
                  database="./database13.db",
                  ), ChatBot("q14Bot",
                  storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
                  logic_adapters=[
                      "chatterbot.logic.BestMatch",
                      {
                          'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                          'input_text': 'What do you call a cat at the beach?',
                          'output_text': 'Sandy Claws'
                      },
                      {
                          'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                          'threshold': 0.4,
                          'default_response': 'Okay. Next question -'
                      }
                  ],
                  database="./database14.db",
                  ), ChatBot("q15Bot",
                  storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
                  logic_adapters=[
                      "chatterbot.logic.BestMatch",
                      {
                          'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                          'input_text': 'What do you call a cat at the beach?',
                          'output_text': 'Sandy Claws'
                      },
                      {
                          'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                          'threshold': 0.4,
                          'default_response': 'Okay. Next question -'
                      }
                  ],
                  database="./database15.db",
                  ), ChatBot("q16Bot",
                  storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
                  logic_adapters=[
                      "chatterbot.logic.BestMatch",
                      {
                          'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                          'input_text': 'What do you call a cat at the beach?',
                          'output_text': 'Sandy Claws'
                      },
                      {
                          'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                          'threshold': 0.4,
                          'default_response': 'Okay. Next question -'
                      }
                  ],
                  database="./database16.db",
                  ), ChatBot("q17Bot",
                  storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
                  logic_adapters=[
                      "chatterbot.logic.BestMatch",
                      {
                          'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                          'input_text': 'What do you call a cat at the beach?',
                          'output_text': 'Sandy Claws'
                      },
                      {
                          'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                          'threshold': 0.4,
                          'default_response': 'Okay. Next question -'
                      }
                  ],
                  database="./database17.db",
                  ), ChatBot("q18Bot",
                  storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
                  logic_adapters=[
                      "chatterbot.logic.BestMatch",
                      {
                          'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                          'input_text': 'What do you call a cat at the beach?',
                          'output_text': 'Sandy Claws'
                      },
                      {
                          'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                          'threshold': 0.4,
                          'default_response': 'Okay. Next question -'
                      }
                  ],
                  database="./database18.db",
                  )]

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

# flags to mark progress through form, but allowing for intermittent conversation
qCount = 19
state = [False for _ in range(qCount)]
bud = [None for _ in range(qCount)]
proceed = ["Great. Let's begin",
           "Okay. Next question -",
           "Okay. Next question -",
           "Okay. Next question -",
           "Okay. Next question -",
           "Okay. Next question -",
           "Okay. Next question -",
           "Okay. Next question -",
           "Okay. Next question -",
           "Okay. Next question -",
           "Okay. Next question -",
           "Okay. Next question -",
           "Okay. Next question -",
           "Okay. Next question -",
           "Okay. Next question -",
           "Okay. Next question -",
           "Okay. Next question -",
           "Okay. Next question -",
           "Okay. Next question -",
           ]
# bot = ["chatbot%i" % i for i in range(qCount)]
question = [None,
            "Will this request ever be used to give Desjardin employees access to data?",
            "What data set (schema) are you requesting access to?",
            "Who is the primary contact?",
            "Who is the secondary contact?",
            "What is your business case?",
            "Please list the schemas and tables you are requesting access for.",
            "Are all the fields in the tables or schema required?",
            "Please describe in detail how this data will be used. -- How will the data be consumed?",
            "What are the downstream uses of the data, and who will have access?",
            "Will a vendor be provided data downstream?",
            "Please enter the Primary Data Owner's alias.",
            "If SPI is included, will it be masked or truncated (i.e. only the last 4 digits available)?",
            "If PHI (Protected Health Information) is included, have those who will have access to the information taken HIPAA training?",
            "If PHI is included, will anyone in Marketing have access to the information?",
            "Is any information coming directly from Client?  If so, will Marketing have access to the information?",
            "Have 'protected person' and 'do not share' individuals been properly accounted for and scrubbed from the information provided?",
            "How many data owners are there?",
			"Have you completed the metadata worksheet?"]



@app.route("/ask", methods=['POST'])
def ask():
    global state, bud, proceed, question
    message = str(request.form['messageText'])

    while True:
        if message == "quit":
            exit()
        else:
            i = 0
            # determine current state
            while state[i]:
                i += 1

            # ask question appropriate for state
            if i < qCount-1:
                bot_response = str(chatbot[i].get_response(message))
                # will remain in current state until bot_response signifies acceptable user response
                if bot_response == proceed[i]:
                    state[i] = True
                    i += 1
                    bud[i] = message
                    # ask next BUD form question
                    bot_response += "</p><p>" + question[i]
                return jsonify({'status': 'OK', 'answer': bot_response})
            # state implies all BUD questions have acceptable user responses
            else:
                bot_response = "Here is what I've recorded for you:"
                for i, user_response in enumerate(bud[1:]):
                    bot_response += "</p></p>Q" + str(i+1) + ": " + str(user_response)

                bot_response += "</p></p></p></p>Are you ready to submit?"
                return jsonify({'status': 'OK', 'answer': bot_response})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9080, debug=True)







# chatbot0 = ChatBot("initBot",
#                   storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
#                   logic_adapters=[
#                       "chatterbot.logic.BestMatch",
#                       # "chatterbot.logic.MathematicalEvaluation",
#                       # "chatterbot.logic.TimeLogicAdapter",
#                       {
#                           'import_path': 'chatterbot.logic.SpecificResponseAdapter',
#                           'input_text': 'What do you call a cat at the beach?',
#                           'output_text': 'Sandy Claws'
#                       },
#                       {
#                           'import_path': 'chatterbot.logic.LowConfidenceAdapter',
#                           'threshold': 0.25,
#                           'default_response': 'I am sorry, but I do not understand.'
#                       }
#                   ],
#                   # input_adapter="chatterbot.input.TerminalAdapter",
#                   # output_adapter="chatterbot.output.TerminalAdapter",
#                   database="./database0.db",
#                   # trainer="chatterbot.trainers.ListTrainer"
#                   )




# chatbot0 = ChatBot("initBot",
#                   storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
#                   logic_adapters=[
#                       "chatterbot.logic.BestMatch",
#                       {
#                           'import_path': 'chatterbot.logic.LowConfidenceAdapter',
#                           'threshold': 0.5,
#                           'default_response': 'I am sorry, but I do not understand.'
#                       }
#                   ],
#                   database="./database0.db",
#                   )
# chatbot1 = ChatBot("q1Bot",
#                   storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
#                   logic_adapters=[
#                       "chatterbot.logic.BestMatch",
#                       {
#                           'import_path': 'chatterbot.logic.LowConfidenceAdapter',
#                           'threshold': 0.5,
#                           'default_response': 'I am sorry, but I do not understand.'
#                       }
#                   ],
#                   database="./database1.db",
#                   )
# chatbot2 = ChatBot("q2Bot",
#                   storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
#                   logic_adapters=[
#                       "chatterbot.logic.BestMatch",
#                       {
#                           'import_path': 'chatterbot.logic.SpecificResponseAdapter',
#                           'input_text': 'What do you call a cat at the beach?',
#                           'output_text': 'Sandy Claws'
#                       },
#                       {
#                           'import_path': 'chatterbot.logic.LowConfidenceAdapter',
#                           'threshold': 0.5,
#                           'default_response': 'Okay. Next question -'
#                       }
#                   ],
#                   database="./database1.db",
#                   )



# if i == 1:
#     bot_response = str(chatbot1.get_response(message))
#     if bot_response == proceed[i]:
#         state[i] = True
#         i += 1
#         bud[i] = message
#         bot_response += "</p><p>" + question[i]
#     return jsonify({'status': 'OK', 'answer': bot_response})
#
# if i == 2:
#     bot_response = str(chatbot2.get_response(message))
#     if bot_response == proceed[i]:
#         state[i] = True
#         i += 1
#         bud[i] = message
#         bot_response += "</p><p>" + question[i]
#     return jsonify({'status': 'OK', 'answer': bot_response})
# if i == 3:
#     return jsonify({'status': 'OK', 'answer': bud})