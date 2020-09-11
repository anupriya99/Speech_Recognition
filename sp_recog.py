import speech_recognition as src
import time

store = src.Recognizer()
with src.Microphone() as s:

    print("Please speak")

    audio_input=store.record(s,duration=7)
    print("Recording time",time.strftime("&I:%M:%S"))

    try:
        text_output= store.recognize_google(audio_input)
        print("Text coverted from audio:\n")
        print(text_output)
        print("Finished!")

        print("Execution time",time.strftime("%I:%M:%S"))
    except:
        print("Couldn't process the audio input")

