import speech_recognition as sr

# create an instance of the recognizer class
r = sr.Recognizer()

# second till listner will stop listing
sec = 5

# use the microphone as source of audio input
with sr.Microphone() as source:
    print("Speak anything: ")
    # adjust for ambient noise
    r.adjust_for_ambient_noise(source)

    # continuously listen for audio until there is 5 seconds of silence
    audio_data = r.listen(source, phrase_time_limit=sec)

    try:
        # recognize speech using Google Speech Recognition
        text = r.recognize_google(audio_data, language="en-US")

        # print the recognized text
        words = text.split() if isinstance(text, str) else []
        text_without_silence = " ".join(word for word in words if isinstance(word, str))
        print("You said: ", text_without_silence)

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
