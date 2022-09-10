# AVC
Voice activated audio commands

## Prerequisites:
- Some Virtual Audio Cable Program (VBCable, Virtual Audio Cable Lite, etc)
- FFMpeg installed (preferably set to PATH)

**CURRENTY A WORK IN PROGRESS. THIS IS ABSOLUTELY A MVC.**    

- Currenty relative pathing does not work so this deals entirely in absolute paths (i.e. you can't write ../folder/audio.mp3 you must write C:/Users/Name/folder/audio.mp3)

- All audio files must be .mp3 files
- ~~Also while I have added some tts command support it does not work.~~ TTS NOW WORKS
- Currently program is only known to work on windows

Commands must be .json files of the following format:
```
{
  "command_phrases":[
     "these are phrases that",
     "the program will recognize",
     "to activate the audio",
     "you can have virtually any number of these"
  ],
  "outputs" : [
     {
        "command_type": "audio",
        "audio_file": <Absolute path to file>
     },
     {
	"command_type" "tts",
	"text": "some text for tts"
     }
  ]
}
```

You can have multiple outputs with multiple audio files, these will be played one at a time.
