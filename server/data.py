
questions = [
    {
        'content': 'What does Wi-Fi allow computers to do?',
        'choices': [
            {'A': 'Print documents'},
            {'B': 'Connect to the internet wirelessly'},
            {'C': 'Play music'},
            {'D': 'Charge the battery'}
        ],
        'answer': 'B'
    },
    {
        'content': 'What is the main function of a router?',
        'choices': [
            {'A': 'Store data'},
            {'B': 'Display images'},
            {'C': 'Connect different networks together'},
            {'D': 'Run applications'}
        ],
        'answer': 'C'
    },
    {
        'content': 'Which one of these is a valid IP address?',
        'choices': [
            {'A': '192.168.1.1'},
            {'B': '999.999.999.999'},
            {'C': 'abc.def.ghi.jkl'},
            {'D': '256.256.256.256'}
        ],
        'answer': 'A'
    },
    {
        'content': 'What does LAN stand for?',
        'choices': [
            {'A': 'Local Area Network'},
            {'B': 'Large Application Network'},
            {'C': 'Long Access Node'},
            {'D': 'Light Access Network'}
        ],
        'answer': 'A'
    },
    {
        'content': 'Which device do we usually use at home to connect to the internet?',
        'choices': [
            {'A': 'Printer'},
            {'B': 'Router'},
            {'C': 'Mouse'},
            {'D': 'Monitor'}
        ],
        'answer': 'B'
    },
    {
        'content': 'Which of the following is a network cable?',
        'choices': [
            {'A': 'HDMI'},
            {'B': 'Ethernet'},
            {'C': 'USB'},
            {'D': 'VGA'}
        ],
        'answer': 'B'
    },
    {
        'content': 'What does the internet allow people to do?',
        'choices': [
            {'A': 'Wash dishes'},
            {'B': 'Fly airplanes'},
            {'C': 'Share and access information globally'},
            {'D': 'Cook food'}
        ],
        'answer': 'C'
    },
    {
        'content': 'What is the name of the unique number given to every device on a network?',
        'choices': [
            {'A': 'MAC address'},
            {'B': 'File name'},
            {'C': 'Password'},
            {'D': 'Folder name'}
        ],
        'answer': 'A'
    },
    {
        'content': 'Which one is a common use of the internet?',
        'choices': [
            {'A': 'Sending letters'},
            {'B': 'Using a calculator'},
            {'C': 'Sending emails'},
            {'D': 'Writing books'}
        ],
        'answer': 'C'
    },
    {
        'content': 'What does a web browser do?',
        'choices': [
            {'A': 'Plays games'},
            {'B': 'Prints documents'},
            {'C': 'Opens websites'},
            {'D': 'Draws pictures'}
        ],
        'answer': 'C'
    }
]

def get_next_question():
    for q in questions:
        yield q

question_next = get_next_question()
