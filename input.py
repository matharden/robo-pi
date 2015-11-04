import subprocess
import time

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

def assignYesNo(yes, no):
    i = raw_input()
    # Test for no first, so enter does 'yes'.
    if no is not None and i.lower() == 'n':
        no()
    else:
        if yes is not None:
            yes()

# Get from Twitter and save them to messeges.txt.
def fetchMessages():
    pass

# Open file and return contents.
def getMessages():
    f = open('messages.txt', 'r')
    messages = f.readlines()
    f.close()
    return messages

# Get all unread messages from messages.txt.
def checkMessages():
    global number_of_messages, messages
    if number_of_messages:
        message = 'You have ' + str(number_of_messages) + ' messages. Shall I read them?'
        say(message, readMessage, stop, stop)
    else:
        say('You have no messages.', None, None, stop)

# Return details and form a sentence
# eg. "Daddy says good night, see you in the morning."
def getMessageFromList():
    global messages, pointer
    return messages[pointer]

# Read message id
def readMessage():
    message = getMessageFromList()
    say(message, None, None, repeatMessage)

def repeatMessage():
    print 'repeatMessage'
    say('Would you like to hear that again?', readMessage, deleteMessage, stop)

def deleteMessage():
    pass
    # say('Shall I delete this message?', markMessageAsRead, remainingMessages, stop)

def goToNextMessage():
    pass
    # pointer += 1
    # readMessage()

def say(message, yesAction, noAction, timeout):
    # espeak(message)
    print message
    # print yesAction
    # assignYes(yesAction)
    # assignNo(noAction)
    assignYesNo(yesAction, noAction)
    print 'sleep for 1 second'
    time.sleep(1)
    print 'sleep done, now run timeout method'
    timeout()
    print 'timeout done'

def markMessageAsRead():
    pass
    # mark with 'R'
    # write to file using ID
    # remainingMessages

def remainingMessages():
    pass
    # if number_of_messages > pointer:
    #   say('There are n messages', null, null, goToNextMessage)
    # else:
    #   say('You have no more messages.', null, null, stop)

# End any flow. Say goodbye.
def stop():
    print 'STOP'
    # reset
    # say(randomMessage('goodbye'))

# def question(step):
#     global steps
#     answer = raw_input(steps[step]['msg'])
#     if answer == 'y':
#         next_step = steps[step]['yes']
#     else:
#         next_step = steps[step]['no']
#     question(next_step)

# question(1)

# c = 0
# def read():
#     global c, messages
#     a = raw_input('read next?')
#     if a == 'y':
#         print messages[c]
#         subprocess.call('espeak ' + messages[c] + ' 2>/dev/null', shell=True)
#         c+= 1
#         read()

messages = getMessages()

number_of_messages = len(messages)
pointer = 0

checkMessages()
