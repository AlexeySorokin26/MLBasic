# Исправленный файл mediafile.py
from datetime import datetime
from abc import ABC, abstractmethod
from typing import Dict

class FileMetaData:  
    def __init__(self,
                 name: str,
                 size: int,
                 created_at: datetime, 
                 owner: str):
        self.name = name
        self.size = size
        self.created_at = created_at 
        self.owner = owner

class MediaFile(ABC):
    def __init__(self, metadata: FileMetaData):  
        self.metadata = metadata 
    
    @abstractmethod
    def get_specific_metadata(self) -> Dict:
        """Возвращает специфичные для типа файла метаданные"""
        pass