# Project Title

VOICE ASSISTANT

# Description

This project is a simple voice assistant implemented in Python. It enables users to interact with their computer through spoken commands and receives spoken responses. The assistant listens for commands via the microphone, processes them using speech recognition, and responds using text-to-speech conversion. Users can engage in basic conversations, ask questions, or request information from the assistant. It's a beginner-friendly project that demonstrates the integration of speech recognition and text-to-speech technologies to create a hands-free interaction experience.

# Problem

Create a custom voice assistant using Python to personalize and automate tasks according to your needs. Python's versatility makes it an excellent choice for scripting and development, allowing you to build a voice assistant that can compete with the likes of Siri, Alexa, and Google Assistant.

# Solution

The explanation of the code.
This Python script creates a basic voice assistant that listens for user input via a microphone, processes the input using speech recognition, and responds using text-to-speech capabilities. Here's an explanation of the code:

1. Imports:
   - It imports necessary libraries such as speech_recognition for speech recognition, pyttsx3 for text-to-speech conversion.

2. Initialization:
   - It initializes the speech recognizer (Recognizer) and the text-to-speech engine (pyttsx3.init()).

3. speak() Function:
   - This function takes text input and converts it into speech using the say() method of the text-to-speech engine. Then, it runs the speech using the runAndWait() method.

4. listen() Function:
   - This function listens to the user's voice input via the microphone.
   - It adjusts for ambient noise using adjust_for_ambient_noise().
   - It captures the audio input using listen().
   - It attempts to recognize the speech using Google's Speech Recognition service (recognize_google()).
   - If recognition is successful, it prints the recognized query and returns it in lowercase.
   - If recognition fails due to an unknown value error or a request error, it prints an appropriate error message and returns an empty string.

5. main() Function:
   - This function serves as the main entry point of the script.
   - It starts by greeting the user through the speak() function.
   - It enters a loop where it continuously listens for user input.
   - If the user says "exit", it bids farewell and terminates the loop.
   - Otherwise, it checks the user's input against predefined commands and responds accordingly using the speak() function.
   - If the input doesn't match any predefined commands, it responds with a default "I'm sorry, I didn't understand that command." message.

6. Predefined Commands and Responses:
   - The script contains predefined commands and corresponding responses such as greetings, inquiries about well-being, jokes, and information about the assistant.

7. Error Handling:
   - The script includes error handling for cases where speech recognition fails due to unknown value errors or request errors.

Overall, this code provides a simple framework for building a voice assistant that can engage in basic conversations and perform predefined tasks based on user input. It can be extended with additional commands and functionalities to enhance its capabilities.

# Tech Stack

python Programming.
