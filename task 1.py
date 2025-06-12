# Simple Rule-Based Chatbot
# Inputs: "Hello", "How are you", "Bye"
# Responses: "Hi!", "I'm fine, thanks!", "Goodbye!"

# Define the response rules
responses = {
    "hello": "Hi!",
    "hi": "Hi!",
    "hey": "Hi!",
    "how are you": "I'm fine, thanks!",
    "what's up": "I'm fine, thanks!",
    "bye": "Goodbye!",
    "goodbye": "Goodbye!",
    "see you": "Goodbye!"
}

def get_response(user_input):
    # Clean the input by making it lowercase and removing punctuation
    cleaned_input = user_input.lower().strip(",.?!")
    
    # Check if the cleaned input matches any predefined responses
    if cleaned_input in responses:
        return responses[cleaned_input]
    else:
        return "I don't understand that. Try saying 'Hello', 'How are you', or 'Bye'."

def chat():
    print("Chatbot: Hi! I'm a simple chatbot. Type 'bye' to exit.")
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Get and print the response
        response = get_response(user_input)
        print(f"Chatbot: {response}")
        
        # Exit if the user says bye
        if user_input.lower().strip(",.?!") in ["bye", "goodbye", "see you"]:
            break

# Start the chatbot
if __name__ == "__main__":
    chat()