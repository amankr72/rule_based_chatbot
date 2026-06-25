# Rule-Based Chatbot

## Overview

This project is a rule-based conversational chatbot developed using **Python**, **Flask**, **HTML**, **CSS**, and **JavaScript**. The chatbot uses **Regular Expressions (Regex)** for intent matching and **pronoun reflection** to generate context-aware responses. Inspired by the ELIZA chatbot, it demonstrates the fundamentals of Natural Language Processing (NLP) without relying on machine learning or external AI models.

The chatbot is integrated with a responsive web interface, allowing users to interact with it through a browser in real time.

---

## Features

* Rule-based conversational system
* Regular Expression (Regex) pattern matching
* Pronoun reflection for contextual responses
* Dynamic response generation using predefined rules
* Randomized responses for more natural conversations
* Interactive web interface built with HTML, CSS, and JavaScript
* Flask backend for request handling
* Responsive chatbot UI
* Easily extendable rule and response database

---

## Technologies Used

* Python
* Flask
* HTML5
* CSS3
* JavaScript
* Regular Expressions (Regex)
* Git
* GitHub
* Render

---

## Project Structure

```text
Rule-Based-Chatbot/
│
├── app.py                  # Flask application
├── chatbot.py              # Chatbot logic and response generation
├── requirements.txt        # Project dependencies
├── README.md
│
├── templates/
│   └── index.html          # Frontend interface
│
└── static/
    ├── style.css           # Styling
    └── script.js           # Client-side functionality
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/your-username/Rule-Based-Chatbot.git
```

### Navigate to the project directory

```bash
cd Rule-Based-Chatbot
```

### Install the required dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## How It Works

1. The user enters a message in the web interface.
2. JavaScript sends the message to the Flask backend using the Fetch API.
3. Flask forwards the input to the chatbot engine.
4. The chatbot compares the input against predefined Regex rules.
5. If a matching pattern is found, the captured phrase undergoes pronoun reflection.
6. A suitable response is selected randomly from the available responses.
7. The generated response is returned and displayed in the chat interface.

---

## Sample Conversation

**User**

```
Hello
```

**Bot**

```
Hello! How can I assist you today?
```

**User**

```
I want to learn Python.
```

**Bot**

```
Why do you want to learn Python?
```

**User**

```
Do you remember my birthday?
```

**Bot**

```
Did you think I would forget your birthday?
```

---

## Future Enhancements

* Intent classification using NLP
* Machine Learning-based response generation
* Conversation history
* User authentication
* Database integration
* Voice input and speech synthesis
* Sentiment analysis
* Integration with Large Language Models (LLMs)

---

## Author

**Aman Kumar**

B.Tech in Internet of Things (IoT)

---

## License

This project is developed for educational and learning purposes.
