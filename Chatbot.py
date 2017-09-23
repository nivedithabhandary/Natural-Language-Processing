from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"My name is (.*)",
        ['hello %1'],
    ],
    [
        r'hi',
        ['hello', 'namaste', 'namaskara',],
    ],
    [
        r'(.*) (hungry|sleepy|groot)',
        [
            "%1 %2"
        ]
    ],
    [
        r'(.*)(love)(.*)',
        [
            "I always thought Love was a static class until you made an instance of it.",
            "I love user interfaces it's because that's where U and I are always together.",
        ],
    ],
    [
        r'(.*)(relationship)(.*)',
        [
            "Way in which two or more concepts, objects, or people are connected, or the state of being connected.",
        ],
    ],
    [
        r'(does|is there|what) (.*) (forever)(.*)',
        [
            "Loading...",
            "None",
            "while True: pass",
        ],
    ],
    [
        r'(.*)', # default response if no patterns from above is found
        [
            "http://lmgtfy.com/?q=%1",
            "Sorry I don't know what `%1` is?",
        ],
    ],
]

def chatbot():
    print("Hi what's your name?")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
