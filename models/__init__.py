#!/usr/bin/python3

from .base_model import BaseModel
from .engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
