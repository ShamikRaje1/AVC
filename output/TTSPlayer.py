import pyttsx3


class TTSPlayer:

    def __init__(self):
        self.engine = pyttsx3.init()
        rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', rate-50)

    def play_audio(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
