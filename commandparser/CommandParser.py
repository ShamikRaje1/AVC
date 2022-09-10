import os
import pyttsx3
import numpy as np
import pydub
import json
from config_code import config_values
from output.FileAudioOutput import FileAudioOutput


def tts_to_numpy(text):
    engine = pyttsx3.init()
    engine.save_to_file(text, 'temp.wav')
    engine.runAndWait()
    sr, x = mp3_to_numpy('temp.wav', 'wav')
    os.remove('temp.wav')
    return sr, x


def mp3_to_numpy(f, file_format, normalized=False):
    input_file = os.path.normpath(f)
    #pydub.AudioSegment.converter = config_values['ffmpeg']
    a = pydub.AudioSegment.from_file(input_file, file_format)
    y = np.array(a.get_array_of_samples())
    if a.channels == 2:
        y = y.reshape((-1, 2))
    if normalized:
        return a.frame_rate, np.float32(y) / 2 ** 15
    else:
        return a.frame_rate, y


def parse_commands():
    command_dict = {}

    all_commands = [os.path.join(config_values['commands'], f) for f in os.listdir(config_values['commands'])
                    if os.path.isfile(os.path.join(config_values['commands'], f))]
    for cfile in all_commands:
        print(cfile)
        os.path.normpath(cfile)
        with open(cfile, 'r') as com_file:
            command = json.load(com_file)
            output_seq = []
            for output in command["outputs"]:
                output_obj = ''
                if output['command_type'] == 'audio':
                    sr, x = mp3_to_numpy(output['audio_file'], 'mp3')
                    output_obj = FileAudioOutput(x)
                elif output['command_type'] == 'tts':
                    sr, x = tts_to_numpy(output['text'])
                    output_obj = FileAudioOutput(x, rate=sr)
                output_seq.append(output_obj)

            for phrase in command['command_phrases']:
                command_dict[phrase] = output_seq

    return command_dict
