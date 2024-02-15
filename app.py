# Import the necessary library for using ChatGPT
import openai

# Set up your API key for authentication
api_key = 'apy_key'
openai.api_key = api_key

# Define a function to interact with ChatGPT
def chat_with_gpt(prompt):
    # Use the chat completions endpoint for chat models
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    # Return the generated response
    return response.choices[0].message.content

# Example prompt to start a conversation
user_input = "What is the OpenAI mission?"

# Get a response from ChatGPT
agent_response = chat_with_gpt(user_input)

# Print the response
print(agent_response)
