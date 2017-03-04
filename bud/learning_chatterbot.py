from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Anya")

conversation = [
    "Hello",
    "How can i help you?",
    "I need get access to a table in FDW",
    "I can help you with that! What is the table name?",
    "Auto prem table",
    "Thank you, why do you need access to it?",
    "I just need it.",
    "Please give more specific business reason"
]

chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)

response = chatbot.get_response('Hello')
print response