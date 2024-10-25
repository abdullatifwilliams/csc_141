def send_messages(messages):
    sent_messages = []
    while messages:
        current_message = messages.pop(0)  # Remove the first message from the list
        print(current_message)
        sent_messages.append(current_message)  # Add the message to sent_messages
    return sent_messages

# List of short text messages
text_messages = [
    "Hello, how are you?",
    "Don't forget the meeting at 3 PM.",
    "Happy birthday to you!",
    "Are you coming to the party tonight?",
    "Let me know when you get home safely."
]

# Call the function with a copy of the messages list
sent_messages = send_messages(text_messages.copy())

# Print both lists to verify that the original list has retained its messages
print("\nOriginal Messages:", text_messages)  # Should contain all original messages
print("Sent Messages:", sent_messages)  # Should contain all sent messages