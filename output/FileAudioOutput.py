from output.AudioPlayer import AudioPlayer


class FileAudioOutput:
    audio_player = AudioPlayer()

    def __init__(self, audio_file):
        self.audio_file = audio_file

    def play_command(self):
        self.audio_player.play_audio(self.audio_file)
