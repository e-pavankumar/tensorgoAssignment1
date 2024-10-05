import speech_recognition as sr
import cohere
import pyttsx3
co = cohere.Client('EyDbyGG26i4ihK0ph4WcV7CHVnNx11anUdawsi4E') 


engine = pyttsx3.init()

def listen_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"User said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Could not request results; check your network connection.")
            return ""
def generate_response(prompt):
    response = co.generate(
        model='command-xlarge-nightly', 
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    )
    message = response.generations[0].text.strip()
    print(f"Bot: {message}")
    return message
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def speech_to_speech_bot():
    while True:
        user_input = listen_speech()
        if user_input.lower() == "exit":
            print("Exiting...")
            break
        if user_input:
            response = generate_response(user_input)
            speak_text(response)

if __name__ == "__main__":
    speech_to_speech_bot()
