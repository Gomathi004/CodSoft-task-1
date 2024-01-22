import re
import random

def simple_chatbot(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for easier matching
    
    # Define more specific patterns and responses
    greetings = r"hello|hi|hey|greetings"
    farewells = r"bye|goodbye|see you later"
    questions = r"how are you\??|what is your name\??|who created you\??"
    weather_query = r"weather|forecast"
    time_query = r"time|current time|clock"
    
    # Elaborate responses for specific queries
    weather_responses = ["Sure, I can check the weather for you. Where are you located?",
                         "Would you like the weather forecast for a specific location?"]
    time_responses = ["The current time is 10:00 AM.", 
                      "It's currently 2:30 PM."]
    default_response = "I'm sorry, I don't understand that."

    # Check user input against predefined rules using regex pattern matching
    if re.search(greetings, user_input):
        return "Hello! How can I assist you today?"
    elif re.search(farewells, user_input):
        return "Goodbye! Have a wonderful day!"
    elif re.search(questions, user_input):
        if re.search(r"how are you\??", user_input):
            return "I'm just a bot, but I'm here to help!"
        elif re.search(r"what is your name\??", user_input):
            return "I'm a chatbot designed to assist you!"
        elif re.search(r"who created you\??", user_input):
            return "I was created by a team of developers."
    elif re.search(weather_query, user_input):
        return random.choice(weather_responses)
    elif re.search(time_query, user_input):
        return random.choice(time_responses)
    else:
        return default_response

# Example usage:
while True:
    user_text = input("You: ")
    if user_text.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    else:
        response = simple_chatbot(user_text)
        print("Chatbot:", response)