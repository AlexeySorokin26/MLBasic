from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional, Dict

class FileMetadata:
    """Общие метаданные для всех файлов"""
    def __init__(self, 
                 name: str, 
                 size: int, 
                 created_at: datetime,
                 owner: str):
        self.name = name
        self.size = size  # в байтах
        self.created_at = created_at
        self.owner = owner

class MediaFile(ABC):
    """Абстрактный базовый класс для медиа-файлов"""
    def __init__(self, metadata: FileMetadata):
        self.metadata = metadata
    
    @abstractmethod
    def get_specific_metadata(self) -> Dict:
        """Возвращает специфичные для типа файла метаданные"""
        pass

class AudioFile(MediaFile):
    def get_specific_metadata(self) -> Dict:
        return {
            "duration": "00:03:45",
            "bitrate": "320 kbps",
            "codec": "MP3"
        }

class VideoFile(MediaFile):
    def get_specific_metadata(self) -> Dict:
        return {
            "resolution": "1920x1080",
            "fps": 30,
            "has_audio": True
        }

class PhotoFile(MediaFile):
    def get_specific_metadata(self) -> Dict:
        return {
            "resolution": "4000x3000",
            "camera_model": "Canon EOS 5D"
        }
    
    def apply_filter(self, filter_name: str) -> None:
        # Логика применения фильтра
        pass

class Storage(ABC):
    """Абстрактное хранилище"""
    @abstractmethod
    def save(self, file: MediaFile) -> None:
        pass
    
    @abstractmethod
    def delete(self, file_name: str) -> None:
        pass

class LocalStorage(Storage):
    """Локальное хранилище"""
    def save(self, file: MediaFile) -> None:
        print(f"Сохранение {file.metadata.name} на диск")
    
    def delete(self, file_name: str) -> None:
        print(f"Удаление {file_name} с диска")

class CloudStorage(Storage):
    """Облачное хранилище (S3-подобное)"""
    def __init__(self, bucket_name: str):
        self.bucket = bucket_name
    
    def save(self, file: MediaFile) -> None:
        print(f"Загрузка {file.metadata.name} в облако {self.bucket}")
    
    def delete(self, file_name: str) -> None:
        print(f"Удаление {file_name} из облака {self.bucket}")

class MediaManager:
    """Упрощенный интерфейс для работы с медиа"""
    def __init__(self, storage: Storage):
        self.storage = storage
    
    def upload(self, file: MediaFile) -> None:
        self.storage.save(file)
    
    def process_file(self, file: MediaFile) -> None:
        print(f"Обработка {file.metadata.name}")
        # Вызов методов конвертации/фильтрации

if __name__ == "__main__":
    # Создаем файлы
    audio_meta = FileMetadata("song.mp3", 1024*1024*5, datetime.now(), "user1")
    audio = AudioFile(audio_meta)
    
    video_meta = FileMetadata("movie.mp4", 1024*1024*50, datetime.now(), "user2")
    video = VideoFile(video_meta)
    
    # Выбираем хранилище
    cloud = CloudStorage("my-media-bucket")
    local = LocalStorage()
    
    manager = MediaManager(cloud)
    manager.upload(audio)
    manager.upload(video)
    