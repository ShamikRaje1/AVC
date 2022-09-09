import speech_recognition
from config_code import config_values

command_list = ''


def callback(recognizer, audio):
    try:
        word = recognizer.recognize_google(audio)
        print(word)
        command_list.play_if_command_exists(word)
    except speech_recognition.UnknownValueError:
        print("Debug: Unknown value")


def recognize_and_run_cmds(command_ctrl):
    global command_list
    command_list = command_ctrl
    mic = speech_recognition.Microphone(device_index=config_values['input'])
    r = speech_recognition.Recognizer()
    with mic as source:
        r.adjust_for_ambient_noise(source)
    r.listen_in_background(mic, callback)

