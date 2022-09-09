config_list = ['ffmpeg', 'commands', 'output', 'input']

config_types = {
    'ffmpeg': 'file',
    'commands': 'dir',
    'output': 'output',
    'input': 'input'
}

config_prompts = {
    'ffmpeg': 'Enter the absolute path to your FFMpeg executable: ',
    'commands': 'Enter the path to the commands folder: ',
    'output': 'Enter the number of the output sound device',
    'input': 'Enter the number of the mic used for voice recognition'
}

config_values = {
    'ffmpeg': '',
    'commands': '',
    'output': '',
    'input': ''
}
