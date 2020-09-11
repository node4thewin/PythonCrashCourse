# 8-11

# Start with your work from Exercise 8-10. Call the function 'send_messages()' with a copy of the list of messages. After calling the function, print both of your lists to show that the original list has retained its messages.

# This means you should look through the Chapter above and use [:].

def show_messages(messages):
  """
  Pass a list containing a series of short text messages.
  """
  for message in messages:
    print(message)

def send_messages(messages, sent_messages):
  """Print each message, and then move it sent_messages."""
  print("\nSending all messages:")
  while messages: # while there are messages
    current_message = messages.pop() # pop() out each message to 'current_message'
    print(current_message)
    sent_messages.append(current_message) # then put the messages in 'current_message' into 'sent_messages', this is the list

messages = ["hello there", "how are u?", ":)"]
show_messages(messages)

sent_messages = [] # must have empty list to start with and append/pop
send_messages(messages[:], sent_messages)

print("\nFinal lists:")
print(messages) # THIS SHOULD NOW SHOW THE ORIGINAL LIST vs. Exercise 8-10 which was empty because of .pop()
print(sent_messages)