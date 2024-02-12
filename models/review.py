#!/usr/bin/python3
"""defines the reviews calass"""

from models.base_model import BaseModel

class Review(BaseModel):
    """deals with reviews"""
    place_id = ""
    user_id = ""
    text = ""
