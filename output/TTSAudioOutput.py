from output.TTSPlayer import TTSPlayer


class TTSAudioOutput:
    audio_player = TTSPlayer()

    def __init__(self, tts_text):
        self.tts_text = tts_text

    def play_command(self):
        self.audio_player.play_audio(self.tts_text)
