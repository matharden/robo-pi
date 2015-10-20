steps = [
    {
        # 0
        'msg': 'Goodbye',
        'yes': 1,
        'no': 1
    },
    {
        # 1
        'msg': 'Hello, would you like to checkout for messages?',
        'yes': 2,
        'no': 0
    },
    {
        # 2
        'msg': 'I have 5 messages for you. Shall I read them to you?',
        'yes': 3,
        'no': 0
    },
    {
        # 3
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

def question(step):
    global steps
    answer = raw_input(steps[step]['msg'])
    if answer == 'y':
        next_step = steps[step]['yes']
    else:
        next_step = steps[step]['no']
    question(next_step)

question(1)
