import google.generativeai as genai
import pyttsx3


genai.configure(api_key='AIzaSyAIjeC0pQeaVQi6d-DilfvpOnDC1hsQv8I')

models=[ m for m in genai.list_models() if 'generateText' in m.supported_generation_methods]

model = models[0].name

user_promt=input("Enter your promt:")

completion = genai.generate_text(
    model=model,
    prompt= user_promt,
    max_output_tokens=2024
)
tts_engine= pyttsx3.init()

spoken_response = completion.result.replace('*','')


print(spoken_response)

tts_engine.say(spoken_response)

tts_engine.runAndWait()