import sounddevice as sd

from config_code import config_values


class AudioPlayer:

    def __init__(self):
        sd.default.device = config_values['output']

    def play_audio(self, audio_array):
        print(config_values['output'])
        sd.default.device = config_values['output']
        sd.play(audio_array, 44100)
        sd.wait()
