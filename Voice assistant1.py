#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install wolframalpha


# In[2]:


pip install wikipedia


# In[3]:


pip install SpeechRecognition


# In[4]:


pip install ecapture


# In[5]:


pip install twilio


# In[6]:


import speech_recognition as sr
import pyttsx3

# Initialize the speech recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print(f"You said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return ""

def main():
    speak("Hello! I'm your voice assistant. How can I help you today?")

    while True:
        query = listen()
        
        if "exit" in query:
            speak("Goodbye!")
            break
        
        # Add your own commands and responses here
        if "hello" in query:
            speak("Hi there!")
        elif "how are you" in query:
            speak("I'm doing well, thank you for asking!")
        elif "tell me a joke" in query:
            speak("Why don't scientists trust atoms? Because they make up everything!")
        elif "tell me about yourself" in query:
            speak(" I'm an AI created to assist you with various tasks and have conversations.")
        elif "what's your favorite food" in query:
            speak("I don't eat, but I've heard good things about data bytes!")
        elif "thank you" in query:
            speak("you are welcome!")
        elif "sorry" in query:
            speak("be considerate next time if you know it!")
        else:
            speak("I'm sorry, I didn't understand that command.")
            
if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




