import openai

# Replace with your OpenAI API key
api_key = "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"


# Function to get a response from the chatbot
def get_chatbot_response(prompt):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50  # Adjust the response length as needed
    )
    return response.choices[0].text.strip()


# Main loop for the chatbot
print("Chatbot: Hello! How can I help you today? (Type 'exit' to end)")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = get_chatbot_response("User:" + user_input)
    print("Chatbot:", response)
