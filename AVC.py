import json
import os.path
import time

import sounddevice
import speech_recognition as sr
import config_code
from controller.CommandController import CommandController
from commandparser import CommandParser
import speechRecognition.SpeechRecog as sp


def get_valid_path(prompt, file_or_dir):
    while True:
        usr_in = input(prompt)
        if file_or_dir:
            if os.path.isfile(usr_in):
                return usr_in
        else:
            if os.path.isdir(usr_in):
                return usr_in
        print('invalid ', "file" if file_or_dir else "dir")


def get_item_in_list(prompt, item_list, ret_name):
    print('HERE')
    while True:
        print(prompt)
        for i, mic in enumerate(item_list):
            if ret_name:
                print(i, mic['name'], mic['max_input_channels'])
            else:
                print(i, mic)
        usr_in = int(input())
        if usr_in > len(item_list) or usr_in < 0:
            print("Invalid Index")
        else:
            if ret_name:
                print(item_list[usr_in]['name'])
                return item_list[usr_in]['name'] + ', MME'
            else:
                return usr_in


def load_or_create_config():
    if os.path.exists('config.json'):
        print("IT EXISTS")
        with open('config.json', 'r') as c:
            configs = json.load(c)
            for line in configs:
                config_code.config_values[line] = configs[line]
    else:
        print('IT DOES NOT EXIT')
        for line in config_code.config_list:
            print(line)
            print(config_code.config_types[line])
            if config_code.config_types[line] == 'file' or config_code.config_types[line] == 'dir':
                print('EVAL TRUE!!!!')
                file_or_dir = config_code.config_types[line] == 'file'
                config_code.config_values[line] = get_valid_path(config_code.config_prompts[line],
                                                                 file_or_dir)
            elif config_code.config_types[line] == 'input':
                mic_list = sr.Microphone.list_microphone_names()
                config_code.config_values[line] = get_item_in_list(config_code.config_prompts[line],
                                                                   mic_list,
                                                                   False)
            elif config_code.config_types[line] == 'output':
                print('HERE OUTPUT')
                devices = sounddevice.query_devices()
                config_code.config_values[line] = get_item_in_list(config_code.config_prompts[line], devices, True)

        with open('config.json', 'w+') as config_file:
            json.dump(config_code.config_values, config_file)


if __name__ == '__main__':
    load_or_create_config()
    command_dict = CommandParser.parse_commands()
    ctrl = CommandController(command_dict)
    is_exit = False
    continuous_record = False
    sp.recognize_and_run_cmds(ctrl)
    while not is_exit:
        try:
            print('Working!')
            time.sleep(1)
        except Exception as e:
            print('Error! ', e)
            print(e.with_traceback())
            input()
