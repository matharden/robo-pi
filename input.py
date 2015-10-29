import subprocess

steps = [
  {
    # 0 Check for unread messeges.
    'no': 0
  },
  {
    # 1 Some unread messages
    'msg': 'I have 5 messages for you. Shall I read them to you?',
    'yes': 2,
    'no': 0,
    'timeout': 0
  },
  {
    # 2
    'msg': 'Nanny says: Happy Birthday! Would you like to hear that again?',
    'yes': 3,
    'no': 4
  },
  {
    # 4
    'msg': 'Would you like to delete that message from Nanny?',
    'yes': 5,
    'no': 5
  },
  {
    # 5
    'msg': 'There are 4 more messages. Press "No" if you want me to stop',
    'yes': 3,
    'no': 0
  },
]

pointer = 0

def assignYes(action, args):
  pass
  # while True:
  #   input_state = GPIO.input(18)
  #   if input_state == False:
  #     # Button pressed
  #     action(args)
  #     # break

def assignNo(action, args):
  pass
  # while True:
  #   input_state = GPIO.input(25)
  #   if input_state == False:
  #     # Button pressed
  #     action(args)
  #     # break

# Get from Twitter and save them to messeges.txt.
def fetchMessages():
  pass

# Find Unread messages in messages.txt.
# "You have n messages. Shall I read them to you?"
def checkMessages():
  pass
  # messageId = getNextUnreadMessage()
  # if messageId
    # assignYes(readMessage, messageId)
  # else
    # assignNo(stop)

# Return message ID/line or zero/false
def getNextUnreadMessage():
  pass

# Return details and form sentence
# eg. "Daddy says good night, see you in the morning."
def getMessage(id):
  pass

# Read message id
def readMessage(id):
  pass
  # message = getMessage(id)
  # say(message, readMessage, next, id)

def say(message, yesAction, noAction, yesArgs):
  pass
  # espeak(message)
  # assignYes(yesAction, yesArgs)
  # assignNo(noAction)

# eg. markMessage('R')
def markMessageRead():
  pass

# readMessage(1)


# End any flow. Say goodbye.
def stop():
  pass

def question(step):
  global steps
  answer = raw_input(steps[step]['msg'])
  if answer == 'y':
    next_step = steps[step]['yes']
  else:
    next_step = steps[step]['no']
  question(next_step)

# question(1)

f = open('messages.txt', 'r')
messages = f.readlines()
f.close()

c = 0
def read():
  global c
  a = raw_input('read next?')
  if a == 'y':
    print messages[c]
    subprocess.call('espeak ' + messages[c] + ' 2>/dev/null', shell=True)
    c+= 1
    read()

read()
