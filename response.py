import google.generativeai as genai
import pyttsx3
import speech_recognition as sr


genai.configure(api_key='AIzaSyAIjeC0pQeaVQi6d-DilfvpOnDC1hsQv8I')

models=[ m for m in genai.list_models() if 'generateText' in m.supported_generation_methods]

model = models[0].name

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("listening...")
    audio = recognizer.listen(source)

try:
    user_prompt = recognizer.recognize_google(audio)
    print(f"you said: {user_prompt}")
except sr.UnknownValueError:
    print("I Cloudn't understand what u said.")
    exit()
except sr.RequestError as e:
    print("Cloud not able to connect google speech")
    exit()


completion = genai.generate_text(
    model=model,
    prompt=user_prompt,
    max_output_tokens=2024
)
tts_engine= pyttsx3.init()

spoken_response = completion.result.replace('*','')


print(spoken_response)

tts_engine.say(spoken_response)

tts_engine.runAndWait()