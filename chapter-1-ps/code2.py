# 3. Install an external module and use it to perform an operation of your interest. 



import pyttsx3  # Importing the 'pyttsx3' module, which is used for text-to-speech conversion

engine = pyttsx3.init()  # Initializing the text-to-speech engine

# Setting the text that will be converted to speech
engine.say("I will speak this text")  # The 'say' method queues the text for speech synthesis

engine.runAndWait()  # The 'runAndWait' method processes the voice command and waits for it to finish speaking
