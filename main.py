import nltk
from nltk.corpus import wordnet as wn

nltk.download('wordnet')


def greeting():
    print("Hello! I'm Tob - a simple chatbot.")
    name = input("What's your name? ")
    print(f"Nice to meet you, {name}!")

def weather_response():
    # Respond to weather-related questions
    print("The weather is sunny with a slight chance of rain. Stay prepared!")

def end_chat():
    print("Goodbye! Have a great day!")

#end_chat corpus
end_chat_corpus = ['bye', 'goodbye', 'exit', 'quit', 'done', 'stop', 'end', 'thanks', 'thank you']

def chatbot():
    # Greet the user
    greeting()
    # Ask the user for their input
    while True:
        user_input = input("How can I help you? ")
        if "weather" in user_input:
            weather_response()
        elif user_input.lower() in end_chat_corpus: 
            end_chat()
            break  # End the conversation
        else:
            print("I'm sorry, this is out of my scope. Please ask another question.")

# Run the chatbot
if __name__ == "__main__":
    chatbot()