# 8-9 Messages

# Make a list containing a series of short text messages. Pass the list to a function called 'show_messages()', which prints each text message.

def show_messages(messages):
  """
  Pass a list containing a series of short text messages.
  """
  for message in messages:
    msg = message
    print(msg)
  
text_messages = ('Hey how are you?', 'This is cool.', 'Or is it...')
show_messages(text_messages)
