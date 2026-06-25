
import re
import random

# -----------------------------
# Chat Templates
# -----------------------------
BOT_TEMPLATE = " {}"
USER_TEMPLATE = " {}"

# -----------------------------
# Rules and Responses
# -----------------------------
rules = {
    r"do you think (.*)": [
        "Why do you think {0}?",
        "What makes you think {0}?",
        "If {0}, what does that mean to you?"
    ],

    r"do you remember (.*)": [
        "Did you think I would forget {0}?",
        "Why haven't you been able to forget {0}?",
        "What about {0}?"
    ],

    r"i want (.*)": [
        "Why do you want {0}?",
        "What would it mean if you got {0}?",
        "What's stopping you from getting {0}?"
    ],

    r"if (.*)": [
        "Do you really think it's likely that {0}?",
        "What would happen if {0}?",
        "Why are you concerned that {0}?"
    ],
    r"can you (.*)": [
        "What makes you think I can't {0}?",
        "If I could {0}, what would you do?",
        "Why do you ask if I can {0}?"
    ],
    r"i am (.*)": [
        "How long have you been {0}?",
        "Do you believe it is normal to be {0}?",
        "What does being {0} mean to you?"
    ],
    r"my name is (.*)": [
        "Hello {0}, how can I help you today?"
    ],
    r"^(hello|hi|hey)$": [
        "Hello! How can I assist you today?",
        "what's your name?",
        "what's up?"
    ],
    r"^no$": [
        "Why not?",
        "Alright, I understand. Can you tell me more?",
        "What makes you say no?"
    ],
    r"are you (.*)": [
        "Why do you ask if I am {0}?",
        "What makes you think I am {0}?",
        "Do you believe I am {0}?"
    ],
    r"do you (.*)": [
        "Why do you ask if I {0}?",
        "What makes you think I {0}?",
        "Do you believe I {0}?"
    ],
    r"I can (.*)": [
        "How do you know you can {0}?",
        "Teach me {0}?",
        "Why do you think you can {0}?"
    ],
    r"would you (.*)": [
        "Why do you ask if I would {0}?",
        "Yes, If I was a Human, I would {0}.",
        "What makes you think I would {0}?"
    ],
    r"who (made|created) you(.*)": [
        "Aman created me. He is a great programmer and a good friend of mine.",
    ],
    r"^you are (?!bot|a bot$)(.*)": [
        "No, you are {0}!",
        "Why do you think I am {0}?"
    ]

}

# -----------------------------
# Pronoun Reflection
# -----------------------------
def replace_pronouns(message):
    message = message.lower()
    
    if "you are" in message:
        return message.replace("you are", "I am", 1)
    else:   
        reflections = {
            "i": "you",
            "me": "you",
            "my": "your",
            "am": "are",
            "you": "me",
            "your": "my"
        }

    words = message.split()

    reflected_words = [
        reflections.get(word, word)
        for word in words
    ]

    return " ".join(reflected_words)


# -----------------------------
# Pattern Matching
# -----------------------------
def match_rule(rules, message):

    response = random.choice([
        "I'm not sure I understand. Can you tell me more?",
        "How can I help you with that?",
        "why do you say that?",
        "okay, ask me something else."

    ])

    phrase = None

    for pattern, responses in rules.items():

        match = re.search(pattern, message.lower())

        if match:

            response = random.choice(responses)

            if "{0}" in response:
                phrase = match.group(1)

            return response, phrase

    return response, phrase


# -----------------------------
# Generate Response
# -----------------------------
def respond(message):

    message = message.rstrip("?.!")

    response, phrase = match_rule(rules, message)

    if phrase:

        phrase = replace_pronouns(phrase)

        response = response.format(phrase)

    return response


# -----------------------------
# Send Message
# -----------------------------
def send_message(message):

    print(USER_TEMPLATE.format(message))

    bot_response = respond(message)

    print(BOT_TEMPLATE.format(bot_response))
    print()


# -----------------------------
# Chat Loop
# -----------------------------
def chatbot():

    print("=" * 40)
    print("Chillbot")
    print("Type 'quit' to exit")
    print("=" * 40)

    while True:

        user_input = input("You: ")

        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Goodbye!")
            break

        print(BOT_TEMPLATE.format(
            respond(user_input)
        ))
        print()


# -----------------------------
# Run Program
# -----------------------------
if __name__ == "__main__":
    chatbot()

