print("You said: " + r.recognize_google(audio))
        if "tor" in r.recognize_google(audio):
            speak("Opening tor")
            webbrowser.open("https://www.torproject.org/")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
