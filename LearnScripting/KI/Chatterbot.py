from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a chatbot instance
chatbot = ChatBot('MyChatBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot with the English corpus data
trainer.train("chatterbot.corpus.english")

while True:
    user_input = input("You: ")

    # Get a response from the chatbot
    response = chatbot.get_response(user_input)

    print("ChatBot:", response)
