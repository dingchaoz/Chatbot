from chatterbot import ChatBot

chatbot0 = ChatBot("initBot",
    # storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
    logic_adapters=[
        "chatterbot.logic.BestMatch",
        # "chatterbot.logic.MathematicalEvaluation",
        # "chatterbot.logic.TimeLogicAdapter",
        # {
        #     'import_path': 'chatterbot.logic.SpecificResponseAdapter',
        #     'input_text': 'Can I get a',
        #     'output_text': 'what what'
        # },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.65,
            'default_response': 'I am sorry, but I do not understand.'
        }
    ],
    # input_adapter="chatterbot.input.TerminalAdapter",
    # output_adapter="chatterbot.output.TerminalAdapter",
    database="./database0.db",
    trainer="chatterbot.trainers.ListTrainer"
)

chatbot1 = ChatBot("q1Bot",
    logic_adapters=[
        "chatterbot.logic.BestMatch"],
    database="./database1.db",
    trainer="chatterbot.trainers.ListTrainer"
)
chatbot2 = ChatBot("q2Bot",
    logic_adapters=[
        "chatterbot.logic.BestMatch"],
    database="./database2.db",
    trainer="chatterbot.trainers.ListTrainer"
)
chatbot3 = ChatBot("q3Bot",
    logic_adapters=[
        "chatterbot.logic.BestMatch"],
    database="./database3.db",
    trainer="chatterbot.trainers.ListTrainer"
)
chatbot4 = ChatBot("q4Bot",
    logic_adapters=[
        "chatterbot.logic.BestMatch"],
    database="./database4.db",
    trainer="chatterbot.trainers.ListTrainer"
)
chatbot5 = ChatBot("q5Bot",
    logic_adapters=[
        "chatterbot.logic.BestMatch"],
    database="./database5.db",
    trainer="chatterbot.trainers.ListTrainer"
)
chatbot6 = ChatBot("q6Bot",
    logic_adapters=[
        "chatterbot.logic.BestMatch"],
    database="./database6.db",
    trainer="chatterbot.trainers.ListTrainer"
)
chatbot7 = ChatBot("q7Bot",
    logic_adapters=[
        "chatterbot.logic.BestMatch"],
    database="./database7.db",
    trainer="chatterbot.trainers.ListTrainer"
)
chatbot8 = ChatBot("q8Bot",
    logic_adapters=[
        "chatterbot.logic.BestMatch"],
    database="./database8.db",
    trainer="chatterbot.trainers.ListTrainer"
)
chatbot9 = ChatBot("q9Bot",
    logic_adapters=[
        "chatterbot.logic.BestMatch"],
    database="./database9.db",
    trainer="chatterbot.trainers.ListTrainer"
)
chatbot10 = ChatBot("q10Bot",
    logic_adapters=[
        "chatterbot.logic.BestMatch"],
    database="./database10.db",
    trainer="chatterbot.trainers.ListTrainer"
)
chatbot11 = ChatBot("q11Bot",
    logic_adapters=[
        "chatterbot.logic.BestMatch"],
    database="./database11.db",
    trainer="chatterbot.trainers.ListTrainer"
)
chatbot12 = ChatBot("q12Bot",
    logic_adapters=[
        "chatterbot.logic.BestMatch"],
    database="./database12.db",
    trainer="chatterbot.trainers.ListTrainer"
)
chatbot13 = ChatBot("q13Bot",
    logic_adapters=[
        "chatterbot.logic.BestMatch"],
    database="./database13.db",
    trainer="chatterbot.trainers.ListTrainer"
)
chatbot14 = ChatBot("q14Bot",
    logic_adapters=[
        "chatterbot.logic.BestMatch"],
    database="./database14.db",
    trainer="chatterbot.trainers.ListTrainer"
)
chatbot15 = ChatBot("q15Bot",
    logic_adapters=[
        "chatterbot.logic.BestMatch"],
    database="./database15.db",
    trainer="chatterbot.trainers.ListTrainer"
)
chatbot16 = ChatBot("q16Bot",
    logic_adapters=[
        "chatterbot.logic.BestMatch"],
    database="./database16.db",
    trainer="chatterbot.trainers.ListTrainer"
)
chatbot17 = ChatBot("q17Bot",
    logic_adapters=[
        "chatterbot.logic.BestMatch"],
    database="./database17.db",
    trainer="chatterbot.trainers.ListTrainer"
)
chatbot18 = ChatBot("q18Bot",
    logic_adapters=[
        "chatterbot.logic.BestMatch"],
    database="./database18.db",
    trainer="chatterbot.trainers.ListTrainer"
)
########################################################################################################################


initialQA = ["I am",
             "Great. Let's begin",
             "Okay",
             "Great. Let's begin",
             "Yes",
             "Great. Let's begin",
             "Sure",
             "Great. Let's begin",
             "Yep",
             "Great. Let's begin",
             "Sounds good",
             "Great. Let's begin",
             "I'm ready",
             "Great. Let's begin",
             "Not yet",
             "Okay.  What can I answer for you?",
             "How long does the process take?",
             "It varies based on the complexity of the request and sensitivity of the requested data. Most requests are approved within 7 days.",
             "submit the form?",
             "I do not submit the form yet, but hope to be able to as I learn more",
             "What do you do?",
             "I will walk you through the process, answer questions along the way, and give you a preliminary approval estimate when we are finished",
             "What role do you play?",
             "I will walk you through the process, answer questions along the way, and give you a preliminary approval estimate when we are finished",
             "How many questions can you answer?",
             "I'm constantly learning",
             "How many questions are in the BUD form?",
             "578",
             "How many questions are there?",
             "578",
             "What if I don't know an answer?",
             "We can save our progress and resume when you are ready",
             "Are you the final approver?",
             "I do not make any final approvals",
             "Who makes the final approval?",
             "I do not make any final approvals",
             "What's your name?",
             "It's at the top of the screen, foolish mortal",
             "What's my name?",
             "Amanda Hug-n-kiss",
             ]

# "Will this request ever be used to give Desjardin employees access to data?"
q1 = ["No",
      "Okay. Next question -",
      "Nope",
      "Okay. Next question -",
      "Negative",
      "Okay. Next question -",
      "Don't think so",
      "Okay. Next question -",
      "Probably not",
      "Okay. Next question -",
      "Yes",
      "Okay. Next question -",
      "Yep",
      "Okay. Next question -",
      "Probably",
      "Okay. Next question -",
      "Possibly",
      "Please confirm.",
      "Maybe",
      "Please confirm.",
      "I'm not sure",
      "Please confirm.",
      "Desjardin",
      "On January 1, 2015, Desjardins Group purchased State Farm's Canadian businesses in property and casualty " + \
      "and life insurance, as well as Canadian mutual funds, loan and living benefits companies.",
      "Okay",
      "Please answer whenever you are ready.",
      ]

# "What data set (schema) is being requested?"
q2 = ["I don't know",
      "You will need this information before proceeding",
      "I'm not sure",
      "You will need this information before proceeding",
      "Do you know",
      "I do not have that information.",
      "Can you help?",
      "I can only record your responses at this time.",
      "Okay",
      "Please answer whenever you are ready.",
      ]

# "Who is the primary contact for this request?"
q3 = ["I don't know",
      "You will need this information before proceeding",
      "I'm not sure",
      "You will need this information before proceeding",
      "Do you know",
      "I do not have that information.",
      "Can you help?",
      "I can only record your responses at this time.",
      "Okay",
      "Please answer whenever you are ready.",
      ]

# "Who is the secondary contact for this request?"
q4 = ["I don't know",
      "You will need this information before proceeding",
      "I'm not sure",
      "You will need this information before proceeding",
      "Do you know",
      "I do not have that information.",
      "Can you help?",
      "I can only record your responses at this time.",
      "Okay",
      "Please answer whenever you are ready.",
      ]

# "What is your business case?"
q5 = ["I don't know",
      "You will need this information before proceeding",
      "I'm not sure",
      "You will need this information before proceeding",
      "I don't have a business case",
      "You will need this information before proceeding",
      "Okay",
      "Please answer whenever you are ready.",
      ]

# "Please list the schemas and tables you are requesting access for."
q6 = ["I don't know",
      "You will need this information before proceeding",
      "I'm not sure",
      "You will need this information before proceeding",
      "Okay",
      "Please answer whenever you are ready.",
      ]

# "Are all the fields in the tables or schema required?"
q7 = ["I don't know",
      "You will need this information before proceeding",
      "I'm not sure",
      "You will need this information before proceeding",
      "No",
      "Okay. Next question -",
      "Nope",
      "Okay. Next question -",
      "Negative",
      "Okay. Next question -",
      "Don't think so",
      "Okay. Next question -",
      "Probably not",
      "Okay. Next question -",
      "Yes",
      "Okay. Next question -",
      "Yep",
      "Okay. Next question -",
      "Probably",
      "Okay. Next question -",
      "Possibly",
      "Please confirm.",
      "Maybe",
      "Please confirm.",
      "Okay",
      "Please answer whenever you are ready.",
      ]

# "Please describe in detail how this data will be used. -"
q8 = ["I don't know",
      "You will need this information before proceeding",
      "I'm not sure",
      "You will need this information before proceeding",
      "Okay",
      "Please answer whenever you are ready.",
      ]

# "What are the downstream uses of the data, and who will have access?",
q9 = ["I don't know",
      "You will need this information before proceeding",
      "I'm not sure",
      "You will need this information before proceeding",
      "Okay",
      "Please answer whenever you are ready.",
      ]

# "Will a vendor be provided data downstream?",
q10 = ["I don't know",
      "You will need this information before proceeding",
      "I'm not sure",
      "You will need this information before proceeding",
       "No",
       "Okay. Next question -",
       "Nope",
       "Okay. Next question -",
       "Negative",
       "Okay. Next question -",
       "Don't think so",
       "Okay. Next question -",
       "Probably not",
       "Okay. Next question -",
       "Yes",
       "Okay. Next question -",
       "Yep",
       "Okay. Next question -",
       "Probably",
       "Okay. Next question -",
       "Possibly",
       "Please confirm.",
       "Maybe",
       "Please confirm.",
      "Okay",
      "Please answer whenever you are ready.",
      ]

# "Please enter the Primary Data Owner's alias.",
q11 = ["I don't know",
      "You will need this information before proceeding",
      "I'm not sure",
      "You will need this information before proceeding",
      "Okay",
      "Please answer whenever you are ready.",
      ]

# "If SPI is included, will it be masked or truncated (i.e. only the last 4 digits available)?",
q12 = ["I don't know",
       "You will need this information before proceeding",
       "I'm not sure",
       "You will need this information before proceeding",
       "No",
       "Okay. Next question -",
       "Nope",
       "Okay. Next question -",
       "Negative",
       "Okay. Next question -",
       "Don't think so",
       "Okay. Next question -",
       "Probably not",
       "Okay. Next question -",
       "Yes",
       "Okay. Next question -",
       "Yep",
       "Okay. Next question -",
       "Probably",
       "Okay. Next question -",
       "Possibly",
       "Please confirm.",
       "Maybe",
       "Please confirm.",
       "na",
       "Okay. Next question -",
       "n/a",
       "Okay. Next question -",
       "Okay",
       "Please answer whenever you are ready.",
       ]

# "If PHI (Protected Health Information) is included, have those who will have access to the information taken HIPAA training?",
q13 = ["I don't know",
       "You will need this information before proceeding",
       "I'm not sure",
       "You will need this information before proceeding",
       "No",
       "Okay. Next question -",
       "Nope",
       "Okay. Next question -",
       "Negative",
       "Okay. Next question -",
       "Don't think so",
       "Okay. Next question -",
       "Probably not",
       "Okay. Next question -",
       "Yes",
       "Okay. Next question -",
       "Yep",
       "Okay. Next question -",
       "Probably",
       "Okay. Next question -",
       "Possibly",
       "Please confirm.",
       "Maybe",
       "Please confirm.",
       "na",
       "Okay. Next question -",
       "n/a",
       "Okay. Next question -",
       "Okay",
       "Please answer whenever you are ready.",
       ]

# "If PHI is included, will anyone in Marketing have access to the information?",
q14 = ["I don't know",
       "You will need this information before proceeding",
       "I'm not sure",
       "You will need this information before proceeding",
       "No",
       "Okay. Next question -",
       "Nope",
       "Okay. Next question -",
       "Negative",
       "Okay. Next question -",
       "Don't think so",
       "Okay. Next question -",
       "Probably not",
       "Okay. Next question -",
       "Yes",
       "Okay. Next question -",
       "Yep",
       "Okay. Next question -",
       "Probably",
       "Okay. Next question -",
       "Possibly",
       "Please confirm.",
       "Maybe",
       "Please confirm.",
       "na",
       "Okay. Next question -",
       "n/a",
       "Okay. Next question -",
       "Okay",
       "Please answer whenever you are ready.",
       ]

# "Is any information coming directly from Client?  If so, will Marketing have access to the information?",
q15 = ["I don't know",
       "You will need this information before proceeding",
       "I'm not sure",
       "You will need this information before proceeding",
       "No",
       "Okay. Next question -",
       "Nope",
       "Okay. Next question -",
       "Negative",
       "Okay. Next question -",
       "Don't think so",
       "Okay. Next question -",
       "Probably not",
       "Okay. Next question -",
       "Yes",
       "Okay. Next question -",
       "Yep",
       "Okay. Next question -",
       "Probably",
       "Okay. Next question -",
       "Possibly",
       "Please confirm.",
       "Maybe",
       "Please confirm.",
       "Okay",
       "Please answer whenever you are ready.",
       ]

# "Have "protected person" and "do not share" individuals been properly accounted for and scrubbed from the information provided?",
q16 = ["I don't know",
       "You will need this information before proceeding",
       "I'm not sure",
       "You will need this information before proceeding",
       "No",
       "Okay. Next question -",
       "Nope",
       "Okay. Next question -",
       "Negative",
       "Okay. Next question -",
       "Don't think so",
       "Okay. Next question -",
       "Probably not",
       "Okay. Next question -",
       "Yes",
       "Okay. Next question -",
       "Yep",
       "Okay. Next question -",
       "Probably",
       "Okay. Next question -",
       "Possibly",
       "Please confirm.",
       "Maybe",
       "Please confirm.",
       "na",
       "Okay. Next question -",
       "n/a",
       "Okay. Next question -",
       "Okay",
       "Please answer whenever you are ready.",
       ]

# "How many data owners are there?",
q17 = ["I don't know",
       "You will need this information before proceeding",
       "I'm not sure",
       "You will need this information before proceeding",
       "Okay",
       "Please answer whenever you are ready.",
       ]

# "Have you completed the metadata worksheet?"]
q18 = ["I don't know",
       "You will need this information before proceeding",
       "I'm not sure",
       "You will need this information before proceeding",
       "Okay",
       "Please answer whenever you are ready.",
       ]



chatbot0.train(initialQA)
chatbot1.train(q1)
chatbot2.train(q2)
chatbot3.train(q3)
chatbot4.train(q4)
chatbot5.train(q5)
chatbot6.train(q6)
chatbot7.train(q7)
chatbot8.train(q8)
chatbot9.train(q9)
chatbot10.train(q10)
chatbot11.train(q11)
chatbot12.train(q12)
chatbot13.train(q13)
chatbot14.train(q14)
chatbot15.train(q15)
chatbot16.train(q16)
chatbot17.train(q17)
chatbot18.train(q18)




# response = chatbot.get_response("How's it going?")
#
# print(response)

# print("Hello friend!")
# # The following loop will execute each time the user enters input
# while True:
#     try:
#         # We pass None to this method because the parameter
#         # is not used by the TerminalAdapter
#         bot_input = chatbot.get_response(None)
#
#     # Press ctrl-c or ctrl-d on the keyboard to exit
#     except (KeyboardInterrupt, EOFError, SystemExit):
#         break