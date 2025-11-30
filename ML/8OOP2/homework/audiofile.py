from mediafile import FileMetaData  
from mediafile import MediaFile  
from typing import Dict

class AudioFile(MediaFile):
    def get_specific_metadata(self) -> Dict:
        return {
            "duration": "00:03:45",
            "bitrate": "320 kbps",
            "codec": "MP3"
        }

if __name__ == "__main__":
    from datetime import datetime
    meta = FileMetaData("test.mp3", 1024, datetime.now(), "user")
    audio = AudioFile(meta)
    print(audio.get_specific_metadata())