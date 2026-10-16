
print("🤖 Welcome to Basic Chatbot!")
print("Type 'bye' to exit.")

while True:
    user = input("You: ").lower().strip()

    if user in ["hello", "hi", "hey"]:
        print("Bot: Hello! How are you?")

    elif user in ["fine", "i am fine", "i'm fine", "good", "i am good"]:
        print("Bot: That's great to hear!")

    elif user in ["how are you", "how are you doing"]:
        print("Bot: I'm doing great! Thanks for asking.")

    elif user in ["your name", "what is your name", "what's your name"]:
        print("Bot: I'm your Basic Chatbot.")

    elif user in ["who are you", "what are you"]:
        print("Bot: I'm a simple chatbot made using Python.")

    elif user in ["good morning", "good afternoon", "good evening"]:
        print("Bot: Hello! Hope you have a wonderful day!")

    elif user in ["thank you", "thanks", "thankyou"]:
        print("Bot: You're welcome!")

    elif user in ["what can you do", "help"]:
        print("Bot: I can chat with you and answer simple questions.")

    elif user in ["what is python", "what's python"]:
        print("Bot: Python is a programming language.")

    elif user in ["who created you", "who made you"]:
        print("Bot: I was created using Python!")

    elif user in ["bye", "goodbye", "exit"]:
        print("Bot: Goodbye! Have a nice day!")
        break

    else:
        print("Bot: Sorry, I don't understand that yet.")
